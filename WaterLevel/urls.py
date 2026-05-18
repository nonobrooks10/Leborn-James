"""WaterLevel URL Configuration"""
from django.urls import path
from app01.views import user, account

urlpatterns = [
    # 核心页面/认证
    path('index/', account.index),
    path('login/', account.login),
    path('logout/', account.logout),
    path('image/code/', account.image_code),
    
    # 水位检测核心功能
    path('user/identity/', user.user_identity),
    path('user/detection/', user.user_detection),
    path('user/startDetect/', user.user_start_detect),
    
    # 基础用户管理（保留核心CRUD）
    path('user/list/', user.user_list),
    path('user/add/', user.user_add),
    path('user/<int:nid>/edit/', user.user_edit),
    path('user/<int:nid>/delete/', user.user_delete),
    
    # 数据统计（核心展示）
    path('chart/list/', account.chart_list),
    path('chart/bar/', account.chart_bar),
]