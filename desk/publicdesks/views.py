from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import CreateView, UpdateView
from .models import Ann, User, UserReply
from .forms import AnnForm, UserReplyForm


def ann_list(request):
    anns = Ann.objects.all()
    return render(request, 'anns.html', {'anns': anns})


def ann_detail(request, pk):
    ann = get_object_or_404(Ann, pk=pk)
    userreplys = ann.anns.order_by('-time_in')
    userreplys_count = ann.anns.count()

    return render(request, 'ann_detail.html', {'ann': ann, 'userreplys': userreplys, 'userreplys_count': userreplys_count})


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


class CreateUserReply(PermissionRequiredMixin, CreateView):
    permission_required = ('publicdesks.add_userreply',)
    # Указываем нашу разработанную форму
    form_class = UserReplyForm
    # модель товаров
    model = UserReply
    # и новый шаблон, в котором используется форма.
    template_name = 'edit_userreply.html'
    raise_exception = True

    def form_valid(self, form):
        # создаем форму, но не отправляем его в БД, пока просто держим в памяти
        fields = form.save(commit=False)
        # Через реквест передаем недостающую форму, которая обязательна
        fields.author = User.objects.get(username=self.request.user)
        fields.ann_id = self.kwargs['pk']
        # Наконец сохраняем в БД
        fields.save()
        return super().form_valid(form)


def userreply_detail(request, pk_rep):
    userreply = get_object_or_404(UserReply, pk=pk_rep)
    return render(request, 'userreply_detail.html', {'userreply': userreply})


def userreply_approve(request, pk_rep):
    ''' Accept response - Button on 'article-detail' and 'dashboard' pages'''
    userreply = get_object_or_404(UserReply, pk=pk_rep)
    userreply.approve()
    return redirect('ann_detail', pk=userreply.ann.pk)


def userreply_disapprove(request, pk_rep):
    ''' Unaccept response and remove approvement - Button on 'article-detail' and 'dashboard' pages'''
    userreply = get_object_or_404(UserReply, pk=pk_rep)
    userreply.disapprove()
    return redirect('ann_detail', pk=userreply.ann.pk)


def userreply_remove(request, pk):
    ''' Delete comment - Button on 'article-detail' and 'dashboard' pages'''
    userreply = get_object_or_404(UserReply, pk=pk)
    userreply.delete()
    return redirect('ann_detail', pk=userreply.ann.pk)
