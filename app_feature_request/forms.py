from django import forms
from .models import Clients,FeatureReq

class CreateFeatureReq(forms.ModelForm):


    class Meta:
        model = FeatureReq
        fields=['clients','title','description','clientpriority','target_date','productarea']

