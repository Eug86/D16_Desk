from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Ann(models.Model):
    TYPE = (
        ('Tanki', 'Танки'),
        ('Hils', 'Хилы'),
        ('DD', 'ДД'),
        ('Sales', 'Торговцы'),
        ('Gildmasters', 'Гилдмастеры'),
        ('Questgivers', 'Квестгиверы'),
        ('Kuznets', 'Кузнецы'),
        ('Kozhevniki', 'Кожевники'),
        ('Zelevars', 'Зельевары'),
        ('Magicmasters', 'Мастера заклинаний'),
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    time_in = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=64)
    text = models.TextField()
    category = models.CharField(max_length=32, choices=TYPE, default='Tanki')
    upload = models.ImageField(upload_to='image/', null=True, blank=True)

    def __str__(self):
        return f'{self.title}: {self.text}'

    def get_absolute_url(self):
        return reverse('ann_detail', args=[str(self.id)])

    def preview(self):
        preview = f'{self.text[:50]} ...'
        return preview


class UserReply(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    ann = models.ForeignKey(Ann, on_delete=models.CASCADE, related_name='anns')
    approved_userreply = models.BooleanField(default=False, null=True, blank=True)
    time_in = models.DateTimeField(auto_now_add=True)

    def approve(self):
        ''' approve response/comment '''
        self.approved_userreply = True
        self.save()

    def disapprove(self):
        ''' disapprove response/comment '''
        self.approved_userreply = False
        self.save()


    def get_absolute_url(self):
        return f'http://127.0.0.1:8000/anns/{self.ann.id}'





