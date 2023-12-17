from django.contrib import admin
from .models import ImportFile
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

class ImportFileModel(admin.ModelAdmin):
    list_display = ('file_id', 'file_image', 'file_name','file_abstract','file_pdf') 
    actions = ['custom_update_action']

    def custom_update_action(self, request, queryset):
        # Check if only one object is selected
        if queryset.count() == 1:
            obj = queryset.first()
            return redirect(f'/admin/pdfs/importfile/{obj.file_id}/change/')
        else:
            self.message_user(request, 'Please select only one object to update.')

    custom_update_action.short_description = 'Custom Update Selected Object'
admin.site.register(ImportFile, ImportFileModel)