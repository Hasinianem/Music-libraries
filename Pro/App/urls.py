from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import spotify_callback

urlpatterns = [
    path('', views.dashboard),
    path('dashboard/', views.dashboard),
    path('home/', views.home),
    path('register/', views.user_register, name='register'),
    path('login/', views.user_login, name='user_login'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path("", views.home, name="home"),
    path("play/<str:song_id>/", views.play_song, name="play_song"),
    path('upload/', views.upload_song, name='upload_song'),
    path("callback/", spotify_callback, name="spotify_callback"),

]

# Serve uploaded files
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
