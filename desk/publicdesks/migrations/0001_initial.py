# Generated by Django 4.2.3 on 2023-07-10 04:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ann',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_in', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=64)),
                ('text', models.TextField()),
                ('category', models.CharField(choices=[('Tanki', 'Танки'), ('Hils', 'Хилы'), ('DD', 'ДД'), ('Sales', 'Торговцы'), ('Gildmasters', 'Гилдмастеры'), ('Questgivers', 'Квестгиверы'), ('Kuznets', 'Кузнецы'), ('Kozhevniki', 'Кожевники'), ('Zelevars', 'Зельевары'), ('Magicmasters', 'Мастера заклинаний')], default='Tanki', max_length=32)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserReply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('status', models.BooleanField(default=False)),
                ('time_in', models.DateTimeField(auto_now_add=True)),
                ('ann', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publicdesks.ann')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]