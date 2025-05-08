
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.inicio,name='inicio'),
    path('tienda/',include('tienda.urls')),
    path('carrito/', include('carrito.urls')),
    path('auths/', include('auths.urls')),

    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
