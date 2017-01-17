# -*- coding: utf-8 -*-
from django.contrib import admin

from articles.models import Article
# Register your models here.


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'creation_date')