from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from .forms import SignUpForm
from django.shortcuts import render, get_object_or_404
import sys
sys.path.append("..")

from publicdesks.models import Ann


class SignUp(CreateView):
    model = User
    form_class = SignUpForm
    success_url = '/accounts/login'

    template_name = 'registration/signup.html'


def show_profile(request, pk):
    user = User.objects.get(id=pk)
    anns = Ann.objects.filter(author=user)
    ann = get_object_or_404(Ann, pk=pk)
    userreplys_count = ann.anns.count()

    return render(request, 'profile.html', {'user': user, 'anns': anns, 'userreplys_count': userreplys_count})






