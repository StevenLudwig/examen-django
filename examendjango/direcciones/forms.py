# -*- coding: utf-8 -*-
from django.forms import ModelForm, TextInput, CharField, Select, EmailField
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.forms import UserCreationForm

from .models import Direccion


def CreateGroup(name_grupo, *args):
    new_group, created = Group.objects.get_or_create(name=name_grupo)
    if created:
        for i in range(len(args)):
            ct = ContentType.objects.get_for_model(args[i][1])
            change = Permission.objects.create(codename='change_' + args[i][0],
                name='Can change ' + args[i][0], content_type=ct)
            new_group.permissions.add(change)
    return new_group


class UserForm(UserCreationForm):
    """ Clase para crear un nuevo usuario de Admin """
    #Campo nombre ------------------------------------
    first_name = CharField(
        widget=TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre'
                }),
        required=True,
        max_length=30,
        help_text='A valid email address, please.')
    #Campo apellido ----------------------------------
    last_name = CharField(
        widget=TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Apellido'
                }),
        required=True,
        max_length=30)
    #Campo email -------------------------------------
    email = EmailField(
        widget=TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email',
                'type': 'email'
                }),
        required=True)

    # Meta -------------------------------------------
    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "is_staff",
            "password1",
            "password2"
            )
        widgets = {
            'username': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Usuario'
                }),
            'password1': TextInput(attrs={'class': 'form-control'}),
            'password2': TextInput(attrs={'class': 'form-control'})
            }

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()

        #Agregamos un Grupo----------------------------------------------------
        modelos = [
            ('Direccion', Direccion)
        ]
        grupo = CreateGroup('custom', modelos)
        grupo.user_set.add(user)

        return user


class UserChangeForm(ModelForm):
    """ Clase para actualizar datos del usuario de Admin."""

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',)
        widgets = {
            'username': TextInput(attrs={
                'class': 'form-control'
                }),
            'first_name': TextInput(attrs={
                'class': 'form-control'
                }),
            'last_name': TextInput(attrs={
                'class': 'form-control'
                }),
            'email': TextInput(attrs={
                'class': 'form-control'
                })
            }


class DireccionForm(ModelForm):
    class Meta:
        model = Direccion
        fields = [
            'user',
            'calle',
            'num_calle',
            'num_int',
            'estado',
            'municipio',
            'colonia',
            'pais'
            ]
        widgets = {
            'calle': TextInput(attrs={
                'placeholder': 'Nombre de la calle',
                'required': 'on',
                'class': 'form-control'
                }),
            'num_calle': TextInput(attrs={
                'placeholder': '23',
                'type': 'number',
                'min': '0',
                'step': '1',
                'required': 'on',
                'class': 'form-control'
                }),
            'num_int': TextInput(attrs={
                'placeholder': '#2',
                'class': 'form-control'
                }),
            'municipio': TextInput(attrs={
                'required': 'on',
                'class': 'form-control'}),
            'colonia': TextInput(attrs={
                'required': 'on',
                'class': 'form-control'}),
            'estado': Select(attrs={
                'required': 'on',
                'class': 'form-control'
                }),
            'pais': Select(attrs={
                'required': 'on',
                'class': 'form-control'
                })
            }