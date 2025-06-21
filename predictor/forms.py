# predictor/forms.py
from django import forms

class StudentForm(forms.Form):
    math = forms.IntegerField(label="Math Marks")
    science = forms.IntegerField(label="Science Marks")
    english = forms.IntegerField(label="English Marks")
