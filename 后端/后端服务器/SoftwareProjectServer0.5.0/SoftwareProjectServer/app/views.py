from django.shortcuts import render, HttpResponse
from django.core.exceptions import ValidationError
from app import models
from app.utils.encrypt import md5
from django import forms
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response


class RegisterModelForm(forms.ModelForm):
    class Meta:
        model = models.UserProfile
        fields = ["user_name", "phone_number", "password", "user_email"]

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


class UserProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.UserProfile
        fields = ["id", "user_name", "phone_number", "user_email", "user_picture"]


class UserProfilePictureSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.UserProfile
        fields = ["user_picture"]


class QuestionModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Question
        fields = "__all__"


class Mistakes(serializers.ModelSerializer):
    class Meta:
        model = models.Mistakes
        fields = "__all__"

    def create(self, validated_data):
        mistake = models.Mistakes.objects.create(**self.validated_data)
        return mistake


class Errors(serializers.ModelSerializer):
    class Meta:
        model = models.Errors
        fields = "__all__"

    def create(self, validated_data):
        error = models.Errors.objects.create(**self.validated_data)
        return error


# CBV
class LoginView(APIView):
    def post(self, request):
        data = request.data
        # 检测手机号表中账号是否存在
        if models.UserProfile.objects.filter(phone_number=data['phone_number']).exists():
            account = models.UserProfile.objects.filter(phone_number=data['phone_number']).first()
            if account.password == md5(data['password']):
                user_info = models.UserProfile.objects.filter(phone_number=data['phone_number'])
                serializer = UserProfileSerializers(instance=user_info, many=True)
                serializer.data[0]["success"] = True
                return Response(serializer.data)
            else:
                return Response([{"success": False, "info": "密码错误"}])
        # 检测用户昵称是否存在
        elif models.UserProfile.objects.filter(user_name=data['phone_number']).exists():
            account = models.UserProfile.objects.filter(user_name=data['phone_number']).first()
            if account.password == md5(data['password']):
                user_info = models.UserProfile.objects.filter(user_name=data['phone_number'])
                serializer = UserProfileSerializers(instance=user_info, many=True)
                serializer.data[0]["success"] = True
                return Response(serializer.data)
            else:
                return Response([{"success": False, "info": "密码错误"}])
        else:
            return Response([{"success": False, "info": "账号不存在"}])


class RegisterView(APIView):
    def post(self, request):
        form = RegisterModelForm(data=request.data)
        if form.is_valid():
            form.save()
            return Response([{'success': True}])
        else:
            res = form.errors
            res["success"] = False
            return Response([res])


class EditView(APIView):
    def post(self, request):
        instance = models.UserProfile.objects.get(pk=request.data["user_id"])
        serializer = UserProfileSerializers(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class EditPictureView(APIView):
    def post(self, request):
        instance = models.UserProfile.objects.get(pk=request.data["user_id"])
        instance.user_picture = request.FILES['file'].read()
        instance.save()
        return Response("OK")


class QuestionView(APIView):
    def get(self, request):
        question_list = models.Question.objects.filter(question_type=request.GET["type"]).order_by('?')[:25]
        serializer = QuestionModelSerializers(instance=question_list, many=True)
        return Response(serializer.data)

    def put(self, request):
        serializer = Mistakes(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response("OK")
        else:
            return Response(serializer.errors)


class MistakesView(APIView):
    def get(self, request):
        data = request.GET

        question_id = models.Mistakes.objects.filter(user_id=data["user_id"]).values("question_id")

        mistake_list = models.Question.objects.filter(id__in=question_id, question_type=data["question_type"])

        serializer = QuestionModelSerializers(instance=mistake_list, many=True)

        return Response(serializer.data)

    def delete(self, request):
        models.Mistakes.objects.get(question_id=request.data["question_id"], user_id=request.data["user_id"]).delete()
        return Response("OK")


class ErrorView(APIView):
    def put(self, request):
        serializer = Errors(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response("OK")
        else:
            return Response(serializer.errors)
