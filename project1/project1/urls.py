"""project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from myapp import views
from messagesalert import views
from Registration import views
from crud import views
from django.contrib.auth import views as au

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.Home),
    # path('Home/', views.Home1)
    # path('',views.Home),
    # path('Home/', views.Home1),
    # path('',views.Form),
    # path('product',views.product)
    # path('',views.Form1),
    # path('OutputF1',views.OutputF1)
    # path ('',views.static)
    # path('',views.bootstrap)
    # path('',views.mvt, name='mvt'),
    # path('dataadd', views.dataadd,name='dataadd'),
    # path('update/<int:id>', views.update,name='update'),
    # path('delete/<int:id>', views.delete,name='delete'),
    
    # path('',views.message,name="message"),
    # path('success/',views.success,name="success"),
    # path('info/',views.info,name="info"),
    # path('warning/',views.warning,name="warning"),
    # path('danger/',views.danger,name="danger")
    # path('',views.home,name='ho'),
    # # path('login/',views.login,name='lo'),
    # path('login/',au.LoginView.as_view(template_name='login.html'),name='lo'),
    # path('logout/',au.LogoutView.as_view(template_name='logout.html'),name='logout'),
    # path('register/',views.register, name='re'),
    # path('profile/',views.profile, name='pr'),
    path('',views.homecrud, name='home'),
    path('insert/',views.insertcrud, name='insert'),
    path('update/<int:id>',views.updatecrud),
    path('delete/<int:id>',views.deletecrud),
]
