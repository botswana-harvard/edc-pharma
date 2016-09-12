from django.conf.urls import url, include
from django.contrib import admin

from edc_base.views import LoginView, LogoutView
from edc_pharma.admin_site import edc_pharma_admin
from edc_pharma.views import HomeView

urlpatterns = [
    url(r'login', LoginView.as_view(), name='login_url'),
    url(r'logout', LogoutView.as_view(pattern_name='login_url'), name='logout_url'),
    url(r'^admin/', edc_pharma_admin.urls),
    url(r'^admin/', admin.site.urls),
    url(r'^edc_label/', include('edc_label.urls', namespace='edc-label')),
    url(r'^edc/', include('edc_base.urls', namespace='edc-base')),
    url(r'^', HomeView.as_view(), name='home_url'),
]
