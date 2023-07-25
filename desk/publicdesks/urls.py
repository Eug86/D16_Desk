from django.urls import path
# Импортируем созданное нами представление
from .views import ann_list, ann_detail, userreply_detail, CreateAnn, EditAnn, DeleteAnn, CreateUserReply, userreply_approve, userreply_disapprove, userreply_remove, show_profile
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
   path('', ann_list, name='anns_list'),
   path('<int:pk>', ann_detail, name='ann_detail'),
   path('create', CreateAnn.as_view(), name='ann_create'),
   path('<int:pk>/edit', EditAnn.as_view(), name='edit_ann'),
   path('<int:pk>/rep_create', CreateUserReply.as_view(), name='edit_userreply'),
   path('<int:pk>/delete', DeleteAnn.as_view(), name='ann_delete'),
   path('userreply/<int:pk_rep>', userreply_detail, name='userreply_detail'),
   path('userreply/<int:pk_rep>/approve', userreply_approve, name='userreply_approve'),
   path('userreply/<int:pk_rep>/disapprove', userreply_disapprove, name='userreply_disapprove'),
   path('userreply/<int:pk>/remove/', userreply_remove, name='userreply_remove'),
   path('profile/<int:pk>', show_profile, name='page_user')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
