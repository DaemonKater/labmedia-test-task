from django.core.management.base import BaseCommand
from payments.models import Client, Payment
from django.utils.dateparse import parse_datetime
from decimal import Decimal

class Command(BaseCommand):
    help = 'Загружает тестовые данные из задания в БД'

    def handle(self, *args, **kwargs):
        Payment.objects.all().delete()
        Client.objects.all().delete()

        # Данные клиентов из Таблицы 2
        clients_data =[
            {'id': 1, 'first_name': 'Ivan', 'last_name': 'Ivanov', 'country': 'Russia'},
            {'id': 2, 'first_name': 'Alexey', 'last_name': 'Smirnov', 'country': 'Russia'},
            {'id': 3, 'first_name': 'Sergey', 'last_name': 'Sidorov', 'country': 'USA'},
            {'id': 4, 'first_name': 'Dmitry', 'last_name': 'Petrov', 'country': 'USA'},
            {'id': 5, 'first_name': 'Oleg', 'last_name': 'Kolovin', 'country': 'Germany'},
        ]

        clients = {}
        for c_data in clients_data:
            client = Client.objects.create(**c_data)
            clients[client.id] = client

        # Данные платежей из Таблицы 1
        payments_data =[
            {'id': 1, 'payer_id': 5, 'amount': '100.0', 'percent': '13', 'pay_date': '2018-08-11T10:37:50+03:00'},
            {'id': 2, 'payer_id': 2, 'amount': '130.53', 'percent': '18', 'pay_date': '2018-08-15T15:32:43+03:00'},
            {'id': 3, 'payer_id': 4, 'amount': '55.11', 'percent': '13', 'pay_date': '2018-09-01T09:30:35+03:00'},
            {'id': 4, 'payer_id': 1, 'amount': '67.27', 'percent': '13', 'pay_date': '2018-09-04T19:25:11+03:00'},
            {'id': 5, 'payer_id': 3, 'amount': '143.74', 'percent': '22', 'pay_date': '2018-09-11T11:32:59+03:00'},
        ]

        for p_data in payments_data:
            Payment.objects.create(
                id=p_data['id'],
                payer=clients[p_data['payer_id']],
                amount=Decimal(p_data['amount']),
                percent=Decimal(p_data['percent']),
                pay_date=parse_datetime(p_data['pay_date'])
            )

        self.stdout.write(self.style.SUCCESS('Успешно: Тестовые данные загружены в базу данных!'))