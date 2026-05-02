from django.db import models

class Client(models.Model):
    """
    Модель клиента (Таблица 2 из задания).
    """
    first_name = models.CharField(max_length=100, verbose_name="Имя")
    last_name = models.CharField(max_length=100, verbose_name="Фамилия")
    country = models.CharField(max_length=100, verbose_name="Страна")

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Payment(models.Model):
    """
    Модель платежа (Таблица 1 из задания).
    Связана с клиентом через ForeignKey (Один ко Многим).
    Для финансов используем DecimalField во избежание потерь точности.
    """
    payer = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='payments', verbose_name="Плательщик")
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Сумма")
    percent = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Процент")
    pay_date = models.DateTimeField(verbose_name="Дата платежа")

    class Meta:
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"
        ordering = ['pay_date'] 

    def __str__(self):
        return f"Платеж {self.id} от {self.payer} на сумму {self.amount}"