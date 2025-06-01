from django.urls import path

from .views import *

urlpatterns = [
    path('blog', blog),
    path('posts', posts),
    path('categories', categories),
    path('mediafiles', MediaFiles),
    path('themes', themes),
    path('blogthemes', blogthemes),
]