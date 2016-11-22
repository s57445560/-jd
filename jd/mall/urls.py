#!/usr/bin/env python
# coding:utf-8
# Author: Sun Yang

from django.conf.urls import url, include
from django.contrib import admin

from mall import views

urlpatterns = [
    url(r'^login', views.login),
    url(r'^register/', views.register),
    url(r'^cart/', views.cart),
    url(r'', views.home),


]