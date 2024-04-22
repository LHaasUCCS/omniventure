from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('members/', views.member_list.as_view(), name='member_list'),
    path('member/<str:pk>', views.member_detail.as_view(), name='member_detail'),
    path('member/create/', views.member_create.as_view(), name='member_create'),
    path('member/<str:pk>/delete/', views.member_delete.as_view(), name='member_delete'),
    path('member/<str:pk>/update/', views.member_update.as_view(), name='member_update'),
    path('member/create_edit_success/', views.member_edit, name='member_edit_message'),
    path('login/', auth_views.LoginView.as_view(template_name='omniventure_app/login.html'), name='user_login'),
    path('logout/', auth_views.LogoutView.as_view(), name='user_logout'),
    path('register/', views.register, name='register'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='omniventure_app/login.html'), name='login'),
    path('<str:pk>/add_character/', views.add_character, name='add_character'),
    path('delete_character/<str:pk>/', views.delete_character.as_view(), name='delete_character'),
    path('character/<str:pk>/', views.character_detail.as_view(), name='character_detail'),
    path('<str:pk>/update/', views.edit_character.as_view(), name='edit_character'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
