from django.shortcuts import render, HttpResponse
from django.core.exceptions import ValidationError
from app import models
from app.utils.encrypt import md5
from django import forms
import secrets
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response


class RegisterModelForm(forms.ModelForm):
    class Meta:
        model = models.UserProfile
        fields = ["phone_number", "password", "user_email"]

    def clean_phone_number(self):
        phone = self.cleaned_data['phone_number']

        if models.UserProfile.objects.filter(phone_number=phone).exists():
            raise ValidationError("手机号已存在")

        return phone

    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password) < 8:
            raise ValidationError("密码长度不能少于8个字符")

        return md5(password)


# Create your views here.
# FBV
# def register(request):
#     if request.method == 'GET':
#         return render(request, 'register.html')
#
#     form = RegisterModelForm(data=request.POST)
#     print(request.POST)
#     if form.is_valid():
#         form.save()
#         return HttpResponse('注册成功')
#     else:
#         print(form.errors)
#         return HttpResponse(form.errors)
#
#
# def login(request):
#     if request.method == 'GET':
#         return render(request, 'login.html')
#
#     data = request.POST
#     print(data)
#     if models.UserProfile.objects.filter(phone_number=data['phone_number']).exists():
#         account = models.UserProfile.objects.filter(phone_number=data['phone_number']).first()
#         if account.password == md5(data['password']):
#             random_string = secrets.token_urlsafe(32)
#             response = HttpResponse('登录成功')
#             response.set_cookie('Cookie', random_string)
#             return response
#         else:
#             return HttpResponse('密码错误')
#     else:
#         return HttpResponse('账号不存在')


class UserProfileSerializers(serializers.Serializer):
    user_name = serializers.CharField(max_length=20)
    phone_number = serializers.CharField(max_length=11)
    password = serializers.CharField(max_length=32)
    user_email = serializers.EmailField()
    profile_picture = serializers.ImageField()


# class QuestionSerializers(serializers.Serializer):
#     id = serializers.IntegerField(max_value=20)
#     question_description = serializers.CharField(max_length=1024)
#     question_picture = serializers.SerializerMethodField()
#     answer = serializers.CharField(max_length=1)
#     question_type = serializers.CharField(max_length=32)
#
#     def get_question_picture(self, obj):
#         return obj.question_picture.decode('ASCII')


class QuestionModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Question
        fields = "__all__"


class QuestionTypeModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Question
        fields = ["question_type"]


class Mistakes(serializers.ModelSerializer):
    class Meta:
        model = models.Mistakes
        fields = "__all__"

    def create(self, validated_data):
        mistake = models.Mistakes.objects.create(**self.validated_data)
        return mistake


# CBV
class LoginView(APIView):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        data = request.POST
        if models.UserProfile.objects.filter(phone_number=data['phone_number']).exists():
            account = models.UserProfile.objects.filter(phone_number=data['phone_number']).first()
            if account.password == md5(data['password']):
                question_type_list = models.Question.objects.values('question_type').distinct()
                print(question_type_list)
                serializer = QuestionTypeModelSerializers(instance=question_type_list, many=True)
                # random_string = secrets.token_urlsafe(32)
                response = HttpResponse('登录成功')
                # response.set_cookie('Cookie', random_string)
                # return response
                return Response(serializer.data)
            else:
                return HttpResponse('密码错误')
        else:
            return HttpResponse('账号不存在')


class RegisterView(APIView):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        form = RegisterModelForm(data=request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('注册成功')
        else:
            print(form.errors)
            return HttpResponse(form.errors)


class LogoutView(APIView):
    def post(self, request):
        pass


class TestView(APIView):
    def get(self, request):
        # 获取数据
        user_list = models.UserProfile.objects.all()

        # 构建序列化器对象
        serializer = UserProfileSerializers(instance=user_list, many=True)

        return Response(serializer.data)

    def post(self, request):
        print(request.data)

        serializer = UserProfileSerializers(data=request.data)
        # 检验数据
        serializer.is_valid()

        return Response()


class questionView(APIView):
    def get(self, request):
        question_list = models.Question.objects.filter(question_type=request.GET["type"]).order_by('?')[:25]
        serializer = QuestionModelSerializers(instance=question_list, many=True)
        # print(type(Response(serializer.data)))
        return Response(serializer.data)

    def put(self, request):
        serializer = Mistakes(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response("OK")
        else:
            return Response(serializer.errors)
