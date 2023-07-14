from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import CreateView, UpdateView
from .models import Ann, User
from .forms import AnnForm


def ann_list(request):
    anns = Ann.objects.all()
    return render(request, 'anns.html', {'anns': anns})


def ann_detail(request, pk):
    ann = get_object_or_404(Ann, pk=pk)
    return render(request, 'ann_detail.html', {'ann': ann})


class CreateAnn(PermissionRequiredMixin, CreateView):
    permission_required = ('publicdesks.add_ann',)
    # Указываем нашу разработанную форму
    form_class = AnnForm
    # модель товаров
    model = Ann
    # и новый шаблон, в котором используется форма.
    template_name = 'edit_ann.html'
    raise_exception = True

    def form_valid(self, form):
        # создаем форму, но не отправляем его в БД, пока просто держим в памяти
        fields = form.save(commit=False)
        # Через реквест передаем недостающую форму, которая обязательна
        fields.author = User.objects.get(username=self.request.user)
        # Наконец сохраняем в БД
        fields.save()
        return super().form_valid(form)

class EditAnn(PermissionRequiredMixin, UpdateView):
    permission_required = ('publicdesks.change_ann',)
    # Указываем нашу разработанную форму
    form_class = AnnForm
    # модель товаров
    model = Ann
    # и новый шаблон, в котором используется форма.
    template_name = 'edit_ann.html'



