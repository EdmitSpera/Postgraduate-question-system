"""
URL configuration for SoftwareProjectServer project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    # 定义路径
    # 这个列表中每个元素是调用 path() 函数，函数中有两个参数，第一个是路径字符串；第二个表示在访问该路径时，绑定到views模块中特定的类中
    # 并且根据访问这个路径时的方法，调用类中相应的函数（即 get、post、delete、put等）
    path('login/', views.LoginView.as_view()),
    path('register/', views.RegisterView.as_view()),
    path('edit/', views.EditView.as_view()),
    path('picture/', views.EditPictureView.as_view()),
    path('question/', views.QuestionView.as_view()),
    path('mistake/', views.MistakesView.as_view()),
    path('error/', views.ErrorView.as_view())
]
