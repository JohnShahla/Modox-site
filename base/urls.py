from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.sitemaps.views import sitemap
from main.sitemaps import ProjectSitemap

sitemaps = {
    'project': ProjectSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls', namespace='main')),

    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = "main.views.error_404_view"