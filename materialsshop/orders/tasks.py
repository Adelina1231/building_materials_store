from celery import shared_task
from django.core.mail import send_mail
from .models import Order


@shared_task
def order_created(order_id):
    """
    Задача для отправки уведомления по электронной почте
    при успешном создании заказа.
    """
    order = Order.objects.get(id=order_id)
    subject = f'№ Заказа {order_id}'
    message = f'Дорогой {order.first_name},\n\nВы успешно разместили заказ.\
                Ваш № заказа {order.id}.'
    mail_sent = send_mail(subject,
                          message,
                          'admin@materialsshop.com',
                          [order.email])
    return mail_sent
