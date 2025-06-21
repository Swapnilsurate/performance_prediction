# predictor/views.py
from django.shortcuts import render
from .forms import StudentForm
from .predict_model import predict_pass_status

def index(request):
    result = None
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            math = form.cleaned_data["math"]
            science = form.cleaned_data["science"]
            english = form.cleaned_data["english"]
            result = predict_pass_status(math, science, english)
    else:
        form = StudentForm()
    return render(request, "predictor/index.html", {"form": form, "result": result})
