from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from portfolio import settings
from siteweb.views import home, projet, cv, contact
from accounts.views import login_user, logout_user, signup




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='index'),
    path('projet/', projet, name='projet'),
    path('cv/', cv, name='cv'),
    # path('cv/<int:pk>/', cv_detail, name='detail'),
    path('contact/', contact, name='contact'),
    path('signup/', signup, name='signup'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)