from django.urls import path
from django.conf import settings 
from django.conf.urls.static import static 
from . import views 

urlpatterns = [
	path('<slug:slug>', views.BlogDetailView.as_view(), name='blog_detail'),
	path('', views.HomeListView.as_view(), name='home'),


] 

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)