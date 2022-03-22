import threading
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string


class SendEmailtoUser(threading.Thread):

    def __init__(self,send_to,username):
        self.send_to=send_to
        self.username=username
        threading.Thread.__init__(self)

    def run(self):
        try:
            html_plain = render_to_string('email.txt')
            html_content = render_to_string(
                "email_template.html", {'title': 'test email', 'username': self.username})
            # text_content=strip_tags(html_content)
            # print(self.username)
            # print(self.send_to)

            send_mail("Your Books Api ", html_plain, settings.EMAIL_HOST_USER, [
                self.send_to], html_message=html_content)
            return True

        except Exception as e:
            print(e)
        return False
