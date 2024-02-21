"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404, handler400, handler403, handler500
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("__debug__/", include("debug_toolbar.urls")),
    path('accounts/', include('django.contrib.auth.urls')),
    path("", include("moto.urls")),
    path('api/v1/', include('moto.api_urls')),
    #path('api/v2/', include('moto.api_urls_v2')),
    path('automatic-crud/', include('automatic_crud.urls')),
    #permisos de api
    path('oauth2/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('accounts/', include('allauth.urls')),

    
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = "moto.views.mi_error_404"
handler400 = "moto.views.mi_error_400"
handler403 = "moto.views.mi_error_403"
handler500 = "moto.views.mi_error_500"

