from django import forms
from .models import Addname

class NameForm(forms.ModelForm):

  class Meta:
    model = Addname
    fields = ('name',)
    