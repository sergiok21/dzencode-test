from django.conf import settings
from django.shortcuts import redirect
from django.urls import path, include

urlpatterns = [
    path('', lambda req: redirect('1/')),
    path('', include('comments.urls', namespace='comments')),
]


if settings.DEBUG:
    urlpatterns.append(path('__debug__/', include('debug_toolbar.urls')),)
    urlpatterns += [
        path('captcha/', include('captcha.urls')),
    ]
