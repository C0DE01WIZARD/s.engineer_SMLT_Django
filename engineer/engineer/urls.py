from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from systems.views import page_not_found

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('systems.urls')),
    path('', include('users.urls')),
    path('', include('feedback.urls')),
    path('', include('dispatching.urls')),
    path('', include('forum_incidents.urls')),
    path('', include('documentation.urls')),
    # path('', include('emergency.urls'))

]

handler404 = page_not_found  # 404 Not found

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
