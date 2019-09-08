from django.contrib import admin
from django.urls import path,include

urlpatterns = [path('Quizz/',include('Quizz.urls')),
    path('admin/', admin.site.urls),
]
