from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from dashboard import views

#Django Apps URL Configuration
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('accounts/', include('allauth.urls')),
    path('accounts/profile/', views.profile, name="profile")

]   + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)\
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
