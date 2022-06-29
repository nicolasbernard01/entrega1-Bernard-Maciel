from django import forms


class Nueva_Gorra(forms.Form):

    bordado = forms.CharField(max_length=30, label='Bordado')
    color = forms.CharField(max_length=30, label='Color')
    precio = forms.IntegerField(label='Precio')



class Nueva_Remera(forms.Form):

    color = forms.CharField(max_length=30, label='Color')
    estampado = forms.CharField(max_length=30, label='Estampado')
    talle = forms.IntegerField(label='Talle' )
    precio = forms.IntegerField(label='Precio')


class Nuevo_Cliente(forms.Form):

    nombre = forms.CharField(max_length=30, label='Nombre')
    apellido = forms.CharField(max_length=30, label='Apellido')
    edad = forms.IntegerField(label='Edad')
    email = forms.EmailField(label='Email')