from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static 


urlpatterns = [
    path('',views.home, name='home'),
    path('logout_view/',views.logout_view,name='logout_view'),
    path('service-requests/',views.service_requests,name='service_requests'),
    path('track-request/',views.track_requests,name='track_requests'),
    path("handle-requests/",views.handle_requests,name="handle_requests"),
]

if settings.DEBUG:  
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
