from django.forms import ModelForm
from .models import Tareas

class Tareasform(ModelForm):
    class Meta:
        model = Tareas
        fields = ['title', 'description', 'estado' ]
