from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .predict_model import predict_pass_status

@csrf_exempt  # only for development, remove in production
def predict_api(request):
    if request.method == "POST":
        print("Received POST") 
        data = json.loads(request.body)
        print("Data received:", data)
        math = data.get("math")
        science = data.get("science")
        english = data.get("english")
        if math is None or science is None or english is None:
            return JsonResponse({"error": "All fields are required"}, status=400)
        result = predict_pass_status(math, science, english)
        return JsonResponse({"result": result})
    return JsonResponse({"error": "Only POST method allowed"}, status=405)
