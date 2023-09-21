from django.contrib import admin
from django.urls import path
from app.views import home,second,Third,Message
from OCP import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home,name="home"),
    path("second/",second,name="second"),
    path("Third/",Third,name="Third"),
    path("Message/",Message,name="Message")
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
