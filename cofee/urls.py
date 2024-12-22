from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('',views.about,name='about'),
    path('location/',views.location,name='location'),
    path('contact/',views.contact,name='contact'),
    path('Aboutus/',views.aboutus,name='aboutus'), 
    path('Register/',views.Registration,name='Registration'),
    path('login/',views.login_view, name='login'),
    path('home/',views.home, name='home'),
    path('order/',views.order,name='order'),
    path('end/',views.end, name='end')
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

