from django.urls import path
from . import views

urlpatterns = [
    path('', views.pdf_files, name='pdfs'),
    path('admin_page/add/', views.add_object, name='add_object'),
    path('admin_page/update/<int:pk>/', views.update_object, name='update_object'),
    path('admin_page/delete/<int:pk>/', views.delete_object, name='delete_object'),
    path('admin_page', views.display_admin, name='admin'),
    path('admin_landing', views.login_admin, name='admin_landing'),
    path('logout/', views.logout_view, name='logout'),
    
    path('museum_pdfs/pdf_list', views.index, name='main_pdfs'),
    path('museum_pdfs/pdf_list/studies', views.pdf_gallery, name='pdf_gallery'),
    path('download/<int:pk>/', views.download_file, name='download_file'),
    path('museum_pdfs/pdf_list', views.go_back, name='back'),
    path('museum_pdfs/pdf_list/about_us', views.about_us, name='about_us'),
    path('', views.go_index, name='back_index'),
    
    
]