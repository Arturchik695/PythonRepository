from django.contrib import admin
from .models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms


class BlogAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Blog
        fields = '__all__'


class BlogAdmin(admin.ModelAdmin):
    form = BlogAdminForm
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('id', 'title', 'time_created', 'time_update', 'photo', 'is_published')
    list_display_links = ('id', 'title')
    readonly_fields = ('time_created', 'time_update')
    list_editable = ('is_published',)


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name',)}


admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)


