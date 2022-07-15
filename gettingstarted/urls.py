from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static


admin.autodiscover()

import hello.views
import ascii_art.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
   # path("", hello.views.index, name="index"),
    # path("db/", hello.views.db, name="db"),
    # path("admin/", admin.site.urls),

    
    path('do_ascii_art/',ascii_art.views.do_ascii_art,name = 'do_ascii_art'),
    path('do_ascii_art_web/',ascii_art.views.do_ascii_art_web,name = 'do_ascii_art_web'),
    path('do_animated_ascii_art/',ascii_art.views.do_animated_ascii_art,name = 'do_animated_ascii_art'),
    path("",ascii_art.views.ascii,name= "ascii"),
    path("ascii/",ascii_art.views.ascii,name= "ascii"),
    path("animated_ascii/",ascii_art.views.animated_ascii,name= "animated_ascii"),
        
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += staticfiles_urlpatterns()
