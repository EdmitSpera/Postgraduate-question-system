from django.db import models
from django.core.validators import RegexValidator


# 这个文件是定义数据库中的表
# 一个类对应数据库中的一张表， 类中的属性对应表中的一个字段
# 另外在下面表中，没用明确定义出每个表中的主键（主码），这是因为django框架会默认给每张表定义默认的id整型主键，并且根据插入的数据，从1开始自增
# 用户数据表
class UserProfile(models.Model):
    # 用户昵称（不允许重复、可为null、可为空串）
    user_name = models.CharField(
        unique=True,
        null=True,
        blank=True,
        max_length=20,
        error_messages={
            'unique': '昵称已存在',
        }
    )

    # 电话号码
    phone_number = models.CharField(
        # 定义长度
        max_length=11,
        unique=True,
        null=True,
        blank=True,
        # 使用正则表达式验证手机号格式
        validators=[
            RegexValidator(
                regex=r'^(13[0-9]|14[01456879]|15[0-35-9]|16[2567]|17[0-8]|18[0-9]|19[0-35-9])\d{8}$',
                message='手机号格式不正确'
            ),
        ],
        verbose_name='手机号',
        # 定义返回错误信息
        error_messages={
            # 重复时返回一下信息
            'unique': '手机号已存在',
        }
    )

    # 用户密码
    password = models.CharField(
        max_length=32,
        null=True,
        verbose_name='密码'
    )

    # 邮箱
    user_email = models.EmailField(
        verbose_name='邮箱',
        unique=True,
        null=True,
        blank=True,
        # 使用正则表达式验证邮箱格式，不正确时返回对应信息
        validators=[
            RegexValidator(
                regex=r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$',
                message='邮箱格式不正确'
            ),
        ],
        # 同样定义错误信息
        error_messages={
            # 出现相同邮箱时返回一下错误信息
            'unique': '邮箱已存在',
        }
    )

    # 用户头像
    user_picture = models.BinaryField(verbose_name='头像', blank=True, null=True)

    def __str__(self):
        return self.phone_number


# 问题表
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


# 错题表
class Mistakes(models.Model):
    user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="用户ID")
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name="问题ID")

    # 这是该类内的一个配置类
    # 用来定义更为复杂的逻辑
    class Meta:
        # 这里两个属性合起来的唯一性
        unique_together = ("user_id", "question_id")


# 报错表
class Errors(models.Model):
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name="问题ID")
