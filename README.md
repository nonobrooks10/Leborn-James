# Leborn-James
水库的水位监测与异常报警系统
项目简介
Django+MySQL 开发的水库的水位监测与异常报警系统[测试文件.docx](https://github.com/user-attachments/files/28658789/default.docx)
，当前为第一周基础版，完成架构、用户模块与系统骨架。

环境
Python 3.9+
Django 3.2
MySQL 8.0


1. 安装依赖
```bash
pip install django mysqlclient
```
2. 创建数据库
```sql
CREATE DATABASE syj DEFAULT CHARSET utf8mb4;
```
3. 初始化表
```bash
python manage.py makemigrations
python manage.py migrate
```
4. 运行
```bash
python manage.py runserver
```
访问：http://127.0.0.1:8000/login/

已实现（第一周）
用户登录/注册/验证码
MySQL 三张核心表
登录权限拦截
系统首页与导航骨架

下周计划
OpenCV 水尺识别
视频流接入
图片识别页面
