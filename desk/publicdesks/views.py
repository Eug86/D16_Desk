from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, View
from .models import Ann, UserReply
from .filters import AnnFilter
from .forms import AnnForm
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required




class AnnList(ListView):
    # Указываем модель, объекты которой мы будем выводить
    model = Ann
    # Поле, которое будет использоваться для сортировки объектов
    ordering = 'time_in'
    # Указываем имя шаблона, в котором будут все инструкции о том,
    # как именно пользователю должны быть показаны наши объекты
    template_name = 'anns.html'
    # Это имя списка, в котором будут лежать все объекты.
    # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    context_object_name = 'Anns'
    paginate_by = 10

    # Переопределяем функцию получения списка товаров
    def get_queryset(self):
        # Получаем обычный запрос
        queryset = super().get_queryset()
        # Используем наш класс фильтрации.
        # self.request.GET содержит объект QueryDict, который мы рассматривали
        # в этом юните ранее.
        # Сохраняем нашу фильтрацию в объекте класса,
        # чтобы потом добавить в контекст и использовать в шаблоне.
        self.filterset = AnnFilter(self.request.GET, queryset)
        # Возвращаем из функции отфильтрованный список товаров
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавляем в контекст объект фильтрации.
        context['filterset'] = self.filterset
        return context


class AnnDetail(DetailView):
    # Модель всё та же, но мы хотим получать информацию по отдельному товару
    model = Ann
    # Используем другой шаблон — product.html
    template_name = 'ann.html'
    # Название объекта, в котором будет выбранный пользователем продукт
    context_object_name = 'Ann'


class SearchList(ListView):
    # Указываем модель, объекты которой мы будем выводить
    model = Ann
    # Поле, которое будет использоваться для сортировки объектов
    ordering = 'time_in'
    # Указываем имя шаблона, в котором будут все инструкции о том,
    # как именно пользователю должны быть показаны наши объекты
    template_name = 'search.html'
    # Это имя списка, в котором будут лежать все объекты.
    # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    context_object_name = 'Anns'
    paginate_by = 5

    # Переопределяем функцию получения списка товаров
    def get_queryset(self):
        # Получаем обычный запрос
        queryset = super().get_queryset()
        # Используем наш класс фильтрации.
        # self.request.GET содержит объект QueryDict, который мы рассматривали
        # в этом юните ранее.
        # Сохраняем нашу фильтрацию в объекте класса,
        # чтобы потом добавить в контекст и использовать в шаблоне.
        self.filterset = AnnFilter(self.request.GET, queryset)
        # Возвращаем из функции отфильтрованный список товаров
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавляем в контекст объект фильтрации.
        context['filterset'] = self.filterset
        return context


class CreateAnn(PermissionRequiredMixin, CreateView):
    permission_required = ('publicdesks.add_ann',)
    # Указываем нашу разработанную форму
    form_class = AnnForm
    # модель товаров
    model = Ann
    # и новый шаблон, в котором используется форма.
    template_name = 'edit_ann.html'

    #
    # def send_notification(self, request, *args, **kwargs):
    #
    #     # отправляем письмо
    #     send_mail(
    #         subject='Вы подписаны на данную категорию',
    #         # имя клиента и дата записи будут в теме для удобства
    #         message='Новая статья в данной категории',  # сообщение с кратким описанием проблемы
    #         from_email='potashev1982@yandex.ru',  # здесь указываете почту, с которой будете отправлять (об этом попозже)
    #         recipient_list=['potashev_e@mail.ru', ]  # здесь список получателей. Например, секретарь, сам врач и т. д.
    #     )
    #
    #     return redirect('post_list')


class EditAnn(PermissionRequiredMixin, UpdateView):
    permission_required = ('publicdesks.change_ann',)
    # Указываем нашу разработанную форму
    form_class = AnnForm
    # модель товаров
    model = Ann
    # и новый шаблон, в котором используется форма.
    template_name = 'edit_ann.html'


class DeleteAnn(PermissionRequiredMixin, DeleteView):
    permission_required = ('publicdesks.delete_ann',)
    # модель товаров
    model = Ann
    # и новый шаблон, в котором используется форма.
    template_name = 'delete_ann.html'
    success_url = reverse_lazy('ann_list')


#class MyView(PermissionRequiredMixin, View):
#    permission_required = ('<app>.<action>_<model>',
#                           '<app>.<action>_<model>')

