from django.urls import path
from template_url_app import views

app_name = 'template_url_app'

urlpatterns = [ 
    path('relative_url_template/',views.relative_url_template,name='relative'),
    path('other/',views.other,name='other'),
]
