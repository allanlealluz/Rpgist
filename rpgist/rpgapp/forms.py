from django.forms import ModelForm
from django import forms
from .models import Personagem,Habs,User

class CharacterForm(ModelForm):
    class Meta:
        model = Personagem
        fields = ['name','life','str','defense','agi','mag','sab','int','chak','perm']
class LogUser(ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        password = forms.PasswordInput()
        name = forms.CharField(max_length=50)
class CreateHabForm(ModelForm):
    class Meta:
        model = Habs
        fields = ['habname','habdesc','fk','cust']