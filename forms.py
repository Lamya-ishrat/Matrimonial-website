from django import forms
from . import models


class CreateBiodata(forms.ModelForm):
    class Meta:
        model = models.BiodataModel
        fields = ['name', 'gender', 'nationality', 'dob',
                  'division', 'city', 'education', 'occupation', 'mobile', 'email',
                  'father_name', 'mother_name', 'siblings', 'profile_image', 'my_file']
