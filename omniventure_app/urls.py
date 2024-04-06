from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('members/', views.member_list.as_view(), name='member_list'),
    path('member/<str:pk>', views.member_detail.as_view(), name='member_detail'),
    path('member/create/', views.member_create.as_view(), name='member_create'),
    path('member/<str:pk>/delete/', views.member_delete.as_view(), name='member_delete'),
    path('member/<str:pk>/update/', views.member_update.as_view(), name='member_update'),
    path('member/create_edit_success/', views.member_edit, name='member_edit_message'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
