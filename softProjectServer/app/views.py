from django.shortcuts import render, HttpResponse
from django.core.exceptions import ValidationError
from app import models
from django import forms

class UserProfileModelForm(forms.ModelForm):
    class Meta:
        model = models.UserProfile
        fields = ["phone_number", "password"]

    def clean_phone_number(self):
        phone = self.cleaned_data['phone_number']

        if models.UserProfile.objects.filter(phone_number=phone).exists():
            raise ValidationError("手机号已存在")

        return phone

    # def clean_password(self):
    #     password = self.cleaned_data['password']
    #
    #     if len(password) < 8:
    #         raise ValidationError("密码长度不能少于8个字符")
    #
    #     return password

# Create your views here.
def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')

    form = UserProfileModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return HttpResponse('注册成功')
    else:
        print(form.errors)
        return HttpResponse(form.errors)


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    form = UserProfileModelForm()


    data = request.POST
    if models.UserProfile.objects.filter(phone_number=data['account']).exists():
        account = models.UserProfile.objects.filter(phone_number=data['account']).first()
        if account.password == data['password']:
            return HttpResponse('登录成功')
        else:
            return HttpResponse('密码错误')
    else:
        return HttpResponse('账号不存在')


