from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string


def send_email_to(send_to, username):
    try:
        html_plain = render_to_string('email.txt')
        html_content = render_to_string(
            "email_template.html", {'title': 'test email', 'username': username})
        # text_content=strip_tags(html_content)
        print(username)
        print(send_to)

        send_mail("Your Books Api ", html_plain, settings.EMAIL_HOST_USER, [
            send_to], html_message=html_content)

    except Exception as e:
        print(e)
