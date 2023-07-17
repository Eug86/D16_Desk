from django.urls import path
# Импортируем созданное нами представление
from .views import ann_list, ann_detail, userreply_detail, CreateAnn, EditAnn, CreateUserReply
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   path('', ann_list, name='anns_list'),
   path('<int:pk>', ann_detail, name='ann_detail'),
   path('create', CreateAnn.as_view(), name='ann_create'),
   path('<int:pk>/edit', EditAnn.as_view(), name='edit_ann'),
   path('<int:pk>/rep_create', CreateUserReply.as_view(), name='edit_userreply'),
   path('userreply/<int:pk_rep>', userreply_detail, name='userreply_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
