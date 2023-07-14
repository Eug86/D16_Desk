from django.urls import path
# Импортируем созданное нами представление
from .views import ann_list, ann_detail, CreateAnn, EditAnn
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   path('', ann_list, name='anns_list'),
   path('<int:pk>', ann_detail, name='ann_detail'),
   path('create', CreateAnn.as_view(), name='ann_create'),
   path('<int:pk>/edit', EditAnn.as_view(), name='edit_ann')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
