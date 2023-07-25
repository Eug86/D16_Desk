from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives

from .models import UserReply, Ann, User


def send_notifications(pk, text, user, mail):

    html_context = render_to_string(
        'userreply_created_email.html',
        {
            'text': text,
            'user': user,
            'link': f'{settings.SITE_URL}/anns/userreply/{pk}',

        }
    )

    msg = EmailMultiAlternatives(
            subject='Новый отклик на ваше объявление',
            body=text,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[mail, ]
        )

    msg.attach_alternative(html_context, 'text/html')
    msg.send()


def send_notifications1(pk, text, user, mail):

    html_context = render_to_string(
        'approve_reply_email.html',
        {
            'text': text,
            'user': user,
            'link': f'{settings.SITE_URL}/anns/userreply/{pk}',

        }
    )

    msg = EmailMultiAlternatives(
            subject='Ваш отклик принят',
            body=text,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[mail, ]
        )

    msg.attach_alternative(html_context, 'text/html')
    msg.send()


@receiver(post_save, sender=UserReply)
def notify_about_new_userreply(sender, instance, created, **kwargs):
    if created:
        user = Ann.objects.get(id=(UserReply.objects.get(id=instance.pk).ann_id)).author
        mail = User.objects.get(username=user).email

        send_notifications(instance.pk, instance.text, user, mail)


@receiver(post_save, sender=UserReply)
def notify_about_approve_userreply(sender, instance, created, **kwargs):
    if UserReply.objects.get(id=instance.pk).approved_userreply:
        user = User.objects.get(id=UserReply.objects.get(id=instance.pk).author.id)
        mail = User.objects.get(username=user).email

        send_notifications1(instance.pk, instance.text, user, mail)



