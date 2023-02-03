from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.defaultfilters import striptags
from django.template.loader import render_to_string


def send_mail_template(subject, template_name, context, recipient_list,
                       from_email=settings.DEFAULT_FROM_EMAIL, fail_silently=False):
    # renderiza o template em um arquivo HTML
    message_html = render_to_string(template_name, context)
    # remove as tags HTML
    message_txt = striptags(message_html)
    # cria o e-mail com o conteudo alternativo
    email = EmailMultiAlternatives(
        subject=subject, body=message_txt, from_email=from_email, to=recipient_list
    )
    email.attach_alternative(message_html, 'text/html')
    email.send(fail_silently=fail_silently)
