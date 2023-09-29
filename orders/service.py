from django.core.mail import send_mail
from customers.models import Customer


class Send_Email_Notification:

    def _get_email(self, serial: str) -> list[str]:
        customers = Customer.objects.filter(order__robot_serial=serial).values('email')
        return list(i['email'] for i in customers)

    def send_email(self, instance):
        serial = instance.serial
        model = instance.model
        version = instance.version
        data = self._get_email(serial=serial)
        send_mail(
            subject='Уведомление о наличии',
            message=f"Добрый день!\n"
                    f"Недавно вы интересовались нашим роботом модели {model}, версии {version}.\n"
                    f"Этот робот теперь в наличии. Если вам подходит этот вариант - пожалуйста, свяжитесь с нами",
            from_email='',
            recipient_list=data,
            fail_silently=False,
        )
