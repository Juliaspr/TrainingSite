import string

from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordContextMixin
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic import TemplateView, FormView
from django.utils.translation import gettext_lazy as _
from .forms import EnrollForm
from .forms import EnrollGroup

import fitness.models as mod


def test_link(request):
    return render(request, 'test.html')


@csrf_exempt
def signUp_link(request):
    if request.method == "GET":
        return render(request, 'signUp.html')
    elif request.method == "POST":
        username = request.POST["name"]
        email = request.POST["email"]
        password = request.POST["pass"]
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return redirect('signIn')


@csrf_exempt
def signIn_link(request):
    if request.method == "GET":
        return render(request, "signIn.html", {"sucess": 1})
    if request.method == "POST":
        email = request.POST["your_email"]
        username = User.objects.get(email=email).username
        password = request.POST["your_pass"]
        user = authenticate(username=username, password=password)
        if user is None:
            return render(request, "signUp.html", {"sucess": 0})
        else:
            login(request, user)
            return redirect('/')


def enrollForm(request):
    form = EnrollForm()
    return render(request, 'enrollForm.html', {"form": form})


@login_required
def personalTraining(request):
    if request.method == "POST":
        form = EnrollForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.username = User.objects.get(username=request.user.username)
            form.save()
            return redirect('/')
        return render(request, "enrollForm.html", {'form': form})


def enrollGroup(request):
    form = EnrollGroup()
    return render(request, 'enrollForm.html', {"form": form})


@login_required
def groupTraining(request):
    if request.method == "POST":
        form = EnrollGroup(request.POST, request.FILES)
        if form.is_valid():
            obj1 = form.save(commit=False)
            obj1.username = User.objects.get(username=request.user.username)
            obj1.email = User.objects.get(email=request.user.email)
            form.save()
            return redirect('/')
        return render(request, "groupEnroll.html", {'form': form})


class PasswordChangeView(PasswordContextMixin, FormView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('password_change_done')
    template_name = 'password.html'
    title = _('Password change')

    @method_decorator(sensitive_post_parameters())
    @method_decorator(csrf_protect)
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        # Updating the password logs out all other sessions for the user
        # except the current one.
        update_session_auth_hash(self.request, form.user)
        return super().form_valid(form)


class PasswordChangeDoneView(PasswordContextMixin, TemplateView):
    template_name = 'password.html'
    title = _('Password change successful')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


def logoutUser(request):
    logout(request)
    return redirect('/')


def index(request, string="all"):
    categories_list = mod.GroupPrograms.objects.all()
    print(string)
    name = "Categories"
    if string == "index":
        name = string
    elif string == "Растяжка":
        categories_list = mod.GroupPrograms.objects.filter(description=mod.GroupPrograms.objects.get(description=string))
        name = string
    elif string == "Силовая":
        categories_list = mod.GroupPrograms.objects.filter(description=mod.GroupPrograms.objects.get(description=string))
        name = string
    elif string == "Работа на пресс":
        categories_list = mod.GroupPrograms.objects.filter(description=mod.GroupPrograms.objects.get(description=string))
        name = string
    return render(request, 'index.html', {"nameHead": name, "CList": categories_list})


def index2(request):
    trainer_list = mod.Trainers.objects.all()
    return render(request, 'Index2.html', {"tr_l": trainer_list})


def checkmail(request):
    result = {'code': 1, "content": ""}
    email = request.GET.get("email")
    print(email)
    user = User.objects.filter(email__exact=email).first()
    if user:
        result = {'code': -1, "content": "Пользователь с такой почтой существует"}
    else:
        result = {'code': 1, "content": "Пользователь с такой почтой не существует"}
    return JsonResponse(result)
