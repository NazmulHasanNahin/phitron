
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import *
from .import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.home,name="homepage"),
    path("author/",include("author.urls")),
    path("catagory/<slug:catagory_slug>",views.home,name="catagory_wise_post"),
    path("catagory/",include("catagories.urls")),
    path("post/",include("posts.urls")),
]
urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)