from django.db import models
from django.core.validators import RegexValidator


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
        max_length=32,
        null=True,
        verbose_name='密码'
    )

    user_email = models.EmailField(
        verbose_name='邮箱',
        unique=True,
        null=True,
        blank=True,
        validators=[
            RegexValidator(
                regex=r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$',
                message='邮箱格式不正确'
            ),
        ],
    )

    profile_picture = models.ImageField(verbose_name='头像', upload_to='profile_pics/', blank=True, null=True)

    def __str__(self):
        return self.phone_number


class Question(models.Model):
    question_description = models.CharField(
        verbose_name='题干',
        max_length=1024,
        null=True,
        blank=True,
    )
    question_picture = models.BinaryField(
        verbose_name='题目图片',
        null=True,
        blank=True,
    )
    option_1 = models.CharField(
        verbose_name="选项1",
        null=True,
        blank=True,
        max_length=256
    )
    option_2 = models.CharField(
        verbose_name="选项2",
        null=True,
        blank=True,
        max_length=256
    )
    option_3 = models.CharField(
        verbose_name="选项3",
        null=True,
        blank=True,
        max_length=256
    )
    option_4 = models.CharField(
        verbose_name="选项4",
        null=True,
        blank=True,
        max_length=256
    )
    option_5 = models.CharField(
        verbose_name="选项5",
        null=True,
        blank=True,
        max_length=256
    )
    answer = models.CharField(
        verbose_name="答案",
        null=True,
        blank=True,
        max_length=1,
    )
    question_type = models.CharField(
        verbose_name="题型",
        null=True,
        blank=True,
        max_length=32,
    )


class Mistakes(models.Model):
    user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="用户ID")
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name="问题ID")

    class Meta:
        unique_together = ("user_id", "question_id")


class Errors(models.Model):
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name="问题ID")