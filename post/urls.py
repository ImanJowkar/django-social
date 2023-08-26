"""
URL configuration for socialmedia project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.post, name='post')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='post')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from post import views

app_name = 'post'
urlpatterns = [
    path('', views.PostView.as_view(), name='all-post'),
    path('<int:post_id>/<slug:post_slug>/', views.PostDetailView.as_view(), name='post-detail'),
    path('delete/<int:post_id>/', views.PostDeleteView.as_view(), name='post-delete'),
    path('update/<int:post_id>/', views.PostUpdateView.as_view(), name='post-update')
]