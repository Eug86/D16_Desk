from django.urls import path
# Импортируем созданное нами представление
from .views import AnnList, AnnDetail, SearchList, CreateAnn, DeleteAnn, EditAnn

urlpatterns = [
   path('', AnnList.as_view(), name='ann_list'),
   path('<int:pk>', AnnDetail.as_view(), name='ann_detail'),
   path('search', SearchList.as_view(), name='ann_search'),
   path('create', CreateAnn.as_view(), name='ann_create'),
   path('<int:pk>/edit', EditAnn.as_view(), name='ann_edit'),
   path('<int:pk>/delete', DeleteAnn.as_view(), name='ann_delete'),
]
