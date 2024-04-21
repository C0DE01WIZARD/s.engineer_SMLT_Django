from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from systems.views import page_not_found

urlpatterns = [
    # url HTML page
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),

    path('', include('systems.urls')),
    path('', include('blog_app.urls')),
    path('', include('users.urls')),
    path('', include('feedback.urls')),
    path('', include('dispatching_app.urls')),
    path('', include('incidents.urls')),
    path('', include('documentation.urls')),
    path('', include('service_app.urls')),
    path('', include('purchase_app.urls')),

    # url django_debug_toolbar
    path("__debug__/", include("debug_toolbar.urls")),
]

handler404 = page_not_found  # exception 404 Not found
admin.site.site_header = 'Управление сервисом s.engineer'
admin.site.index_title = 'S.ENGINEER'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
