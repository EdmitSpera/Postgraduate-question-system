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


class UserProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.UserProfile
        fields = ["id", "user_name", "phone_number", "user_email", "profile_picture"]


class QuestionModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Question
        fields = "__all__"


class QuestionModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Question
        exclude = ["question_picture"]


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


class Errors(serializers.ModelSerializer):
    class Meta:
        model = models.Errors
        fields = "__all__"

    def create(self, validated_data):
        error = models.Errors.objects.create(**self.validated_data)
        return error


# CBV
class LoginView(APIView):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        data = request.data
        if models.UserProfile.objects.filter(phone_number=data['phone_number']).exists():
            account = models.UserProfile.objects.filter(phone_number=data['phone_number']).first()
            if account.password == md5(data['password']):
                # question_type_list = models.Question.objects.values('question_type').distinct()
                user_info = models.UserProfile.objects.filter(phone_number=data['phone_number'])
                # serializer = QuestionTypeModelSerializers(instance=question_type_list, many=True)
                serializer = UserProfileSerializers(instance=user_info, many=True)
                serializer.data[0]["success"] = True
                return Response(serializer.data)
            else:
                return Response([{"success": False, "info": "密码错误"}])
        else:
            return Response([{"success": False, "info": "账号不存在"}])


class RegisterView(APIView):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        form = RegisterModelForm(data=request.data)
        if form.is_valid():
            form.save()
            return Response([{'success': True}])
        else:
            res = form.errors
            res["success"] = False
            return Response([res])


class questionView(APIView):
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


class ErrorView(APIView):
    def put(self, request):
        serializer = Errors(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response("OK")
        else:
            return Response(serializer.errors)
