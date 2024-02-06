from django import forms
from home.models import BmiMeasurement

class BmiForm(forms.ModelForm):
    class Meta:
        model = BmiMeasurement
        fields = "__all__"
        exclude = ("bmi", "message", "user", )

class UpdateBmiForm(forms.ModelForm):
    class Meta:
        model = BmiMeasurement
        fields = "__all__"
        exclude = ("message", "user", )



