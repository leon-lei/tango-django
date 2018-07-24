from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from registration.backends.simple.views import RegistrationView

from . import views

# Create a new class that redirects the user to the index page, if successful at logging
class MyRegistrationView(RegistrationView):
    def get_success_url(self, user):
        return '/rango/'


urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('rango/', include('rango.urls')),
    path('accounts/register/', MyRegistrationView.as_view(), name='registration_register'),
    path('accounts/', include('registration.backends.simple.urls')),
]

if not settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)