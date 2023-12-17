from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import ImportFile, AdminLogin
from .forms import FileForm
from django.shortcuts import get_object_or_404
from django.http import FileResponse
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.urls import reverse
import os


def pdf_files(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())

def display_admin(request):
  pdf_list = ImportFile.objects.all().values() 
  file_count = len(pdf_list)
  template = loader.get_template('admin_landing.html')
  context = {
        'pdf_list': pdf_list,
        'file_count':file_count,
  }
  return HttpResponse(template.render(context, request))

def go_back(request):
    url = reverse('main_pdfs')
    return HttpResponseRedirect(url)

def go_index(request):
    url = reverse('pdfs')
    return HttpResponseRedirect(url)

def login_admin(request):
    if request.method == 'POST':
        user_name = 'admin'
        password = request.POST['user_pass']
        admin  = AdminLogin.objects.filter(user_name=user_name).first()
        if admin.user_name == user_name and admin.user_pass == password:
            return redirect('admin')
        else:
            return render(request, 'admin_login.html',{'error_message': 'Invalid Credentials!'})
    return render(request, 'admin_login.html')

def logout_view(request):
    logout(request)
    return redirect('admin_landing')

def index(request):
    template = loader.get_template('pdf_list.html'); 
    return HttpResponse(template.render())

def about_us(request):
    template = loader.get_template('about.html');
    return HttpResponse(template.render())

def pdf_gallery(request):
    pdf_files = ImportFile.objects.all()
    template = loader.get_template('pdfs.html'); 
    file_count = len(pdf_files)
    context = {
        'pdf_files': pdf_files,
        'file_count':file_count,
    }
    return HttpResponse(template.render(context, request))

def download_file(request, pk):
    instance = get_object_or_404(ImportFile, pk=pk)
    pdf_file = instance.file_pdf

    if pdf_file:
        try:
            # Serve the PDF file as a downloadable response
            response = FileResponse(pdf_file, as_attachment=True)
            response['Content-Disposition'] = f'attachment; filename="{instance.file_pdf.name}"'
            return response
        except FileNotFoundError:
            return HttpResponse("PDF not found.")
    else:
        return HttpResponse("PDF path not available.")
    
def add_object(request):
    if request.method == 'POST':
        file_image = request.FILES.get('file_image')
        file_name = request.POST.get('file_name')
        file_abstract = request.POST.get('file_abstract')
        file_pdf = request.FILES.get('file_pdf')

        ImportFile.objects.create(
            file_image=file_image,
            file_name=file_name,
            file_abstract=file_abstract,
            file_pdf=file_pdf
        )
        return redirect('admin')  # Replace 'object_list' with your actual list view URL

    return render(request, 'add_file.html')

def update_object(request, pk):
    obj = get_object_or_404(ImportFile, pk=pk)

    if request.method == 'POST':
        obj.file_image = request.FILES.get('file_image')
        obj.file_name = request.POST.get('file_name')
        obj.file_abstract = request.POST.get('file_abstract')
        obj.file_pdf = request.FILES.get('file_pdf')

        obj.save()
        return redirect('admin')  # Replace 'object_list' with your actual list view URL

    return render(request, 'update_file.html', {'obj': obj})

def delete_object(request, pk):
    obj = get_object_or_404(ImportFile, pk=pk)

    if request.method == 'POST':
        # Delete associated files
        if obj.file_image:
            # Remove image file
            image_path = obj.file_image.path
            os.remove(image_path)

            # Remove image file entry from database
            obj.file_image.delete()

        if obj.file_pdf:
            # Remove pdf file
            pdf_path = obj.file_pdf.path
            os.remove(pdf_path)

            # Remove pdf file entry from database
            obj.file_pdf.delete()

        # Delete the object itself
        obj.delete()
        return redirect('admin')  # Replace 'admin' with your actual list view URL

    return render(request, 'delete_file.html', {'obj': obj})
    

