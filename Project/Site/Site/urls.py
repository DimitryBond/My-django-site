from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('demand/', include('demand.urls')),
    path('geography/', include('geography.urls')),
    path('skills/', include('skills.urls')),
    path('vacancies/', include('vacancies.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
