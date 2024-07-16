from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from portfolio import settings
from siteweb.views import home, projet, cv, contact




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='index'),
    path('projet/', projet, name='projet'),
    path('cv/', cv, name='cv'),
    path('contact/', contact, name='contact')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)