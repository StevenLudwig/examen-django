# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import auth
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import update_session_auth_hash

from .forms import UserForm, UserChangeForm, DireccionForm

from .models import Direccion


#Usuario ======================================================================
@method_decorator(login_required(login_url='/'), name='dispatch')
class Usuarios(View):

    plantilla = "users.html"

    def get(self, request, *args, **kwargs):
        contexto = {'usuarios': User.objects.all()}
        return render(request, self.plantilla, contexto)


@method_decorator(login_required(login_url='/'), name='dispatch')
class CreateUsuarios(View):

    plantilla = "add_user.html"

    def get(self, request, *args, **kwargs):
        contexto = {'form': UserForm()}
        return render(request, self.plantilla, contexto)

    def post(self, request, *args, **kwargs):  # *********** Post *************
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('us')
        else:
            return render(request, self.plantilla, {'form': form})


@method_decorator(login_required(login_url='/'), name='dispatch')
class UpdateUsuarios(View):

    plantilla = "update_user.html"

    def get(self, request, *args, **kwargs):
        contexto = {'id': request.GET['id'],
            'form': UserChangeForm(
                instance=User.objects.get(id=request.GET['id']))}
        return render(request, self.plantilla, contexto)

    def post(self, request, *args, **kwargs):  # *********** Post *************
        form = UserChangeForm(
            request.POST, instance=User.objects.get(id=request.POST['id']))
        if form.is_valid():
            form.save()
            return redirect('us')
        else:
            return render(request, self.plantilla, {'form': form})


@method_decorator(login_required(login_url='/'), name='dispatch')
class DeleteUsuarios(View):
    def post(self, request, *args, **kwargs):  # *********** Post *************
        User.objects.get(id=request.POST['id']).delete()
        return redirect('us')


@method_decorator(login_required(login_url='/'), name='dispatch')
class UpdatePassword(View):

    plantilla = "pass.html"

    def get(self, request, *args, **kwargs):
        contexto = {'form': PasswordChangeForm(user=request.user)}
        return render(request, self.plantilla, contexto)

    def post(self, request, *args, **kwargs):  # *********** Post *************
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('logout')
        else:
            return render(request, self.plantilla, {'form': form})



#Direcciones ==================================================================
@method_decorator(login_required(login_url='/'), name='dispatch')
class Direcciones(View):

    plantilla = "direccion.html"

    def get(self, request, *args, **kwargs):
        contexto = {'direcciones': Direccion.objects.all()}
        return render(request, self.plantilla, contexto)


@method_decorator(login_required(login_url='/'), name='dispatch')
class CreateDireccion(View):

    plantilla = "add_address.html"

    def get(self, request, *args, **kwargs):
        contexto = {'form': DireccionForm()}
        return render(request, self.plantilla, contexto)

    def post(self, request, *args, **kwargs):  # *********** Post *************
        form = DireccionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ad')
        else:
            return render(request, self.plantilla, {'form': form})


@method_decorator(login_required(login_url='/'), name='dispatch')
class UpdateDireccion(View):

    plantilla = "update_address.html"

    def get(self, request, *args, **kwargs):
        contexto = {'id': request.GET['id'],
            'form': DireccionForm(
                instance=Direccion.objects.get(id=request.GET['id']))}
        return render(request, self.plantilla, contexto)

    def post(self, request, *args, **kwargs):  # *********** Post *************
        form = DireccionForm(request.POST,
            instance=Direccion.objects.get(id=request.POST['id']))
        if form.is_valid():
            form.save()
            return redirect('ad')
        else:
            return render(request, self.plantilla, {'form': form})


@method_decorator(login_required(login_url='/'), name='dispatch')
class DeleteDireccion(View):
    def post(self, request, *args, **kwargs):  # *********** Post *************
        Direccion.objects.get(id=request.POST['id']).delete()
        return redirect('ad')


def salir(request):
    auth.logout(request)
    # Redireccciona a una página de entrada correcta.
    return redirect('index')