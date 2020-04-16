from django import forms
from django.forms import ModelForm
from . import models
 
class TaskForm(ModelForm):
    title = forms.CharField(widget = forms.TextInput(attrs={'placeholder':'Add new task'}))

    class Meta:
        model = models.Task
        fields = '__all__'

