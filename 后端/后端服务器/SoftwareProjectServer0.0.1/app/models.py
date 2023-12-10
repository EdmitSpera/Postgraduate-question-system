from django.db import models
from django.core.validators import RegexValidator
from django.core.validators import MinLengthValidator

class UserProfile(models.Model):
    user_name = models.CharField(
        unique=True,
        null=True,
        blank=True,
        max_length=20,
    )

    phone_number = models.CharField(
        max_length=11,
        unique=True,
        null=True,
        blank=True,
        validators=[
            RegexValidator(
                regex=r'^(13[0-9]|14[01456879]|15[0-35-9]|16[2567]|17[0-8]|18[0-9]|19[0-35-9])\d{8}$',
                message='手机号格式不正确'
            ),
        ],
        verbose_name='手机号'
    )

    password = models.CharField(
        max_length=15,
        null=True,
        validators=[
            MinLengthValidator(limit_value=8, message='密码长度不能少于8个字符'),
        ],
        verbose_name='密码'
    )

    user_email = models.EmailField(
        verbose_name='邮箱',
        unique=True,
        null=True,
        blank=True,
    )

    profile_picture = models.ImageField(verbose_name='头像', upload_to='profile_pics/', blank=True, null=True)

    def __str__(self):
        return self.phone_number
