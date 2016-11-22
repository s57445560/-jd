#!/usr/bin/env python
# coding:utf-8
# Author: Sun Yang

from django import template
from django.utils.safestring import mark_safe
from django.template.base import Node, TemplateSyntaxError


register = template.Library()

@register.simple_tag
def yang_1(all, money):
    return int(all) * int(money)