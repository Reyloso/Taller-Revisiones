from django import forms
from .models import Auto, Cliente, Consecionario, Revision


class forms_auto(forms.ModelForm):

    class Meta:
        model = Auto

        fields = ['marca','tipo','modelo','color','consecionario','matricula']


class forms_cliente(forms.ModelForm):

    class Meta:
        model = Cliente

        fields = ['nid','nombre','primer_apellido','segundo_apellido','telefono','auto']


class forms_consecionario(forms.ModelForm):

    class Meta:
        model = Consecionario

        fields = ['nit','nombre','telefono']

class forms_revision(forms.ModelForm):

    class Meta:
        model = Revision

        fields = ['id','auto','filtro','aceite','frenos','motor']
