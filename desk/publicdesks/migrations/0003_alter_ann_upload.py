# Generated by Django 4.2.3 on 2023-07-13 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicdesks', '0002_alter_ann_upload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ann',
            name='upload',
            field=models.ImageField(blank=True, null=True, upload_to='image/'),
        ),
    ]
