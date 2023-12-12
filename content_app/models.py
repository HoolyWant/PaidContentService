from django.db import models
from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Channel(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='владелец', **NULLABLE)
    title = models.CharField(max_length=150, verbose_name='название')
    description = models.TextField(verbose_name='описание')
    image = models.ImageField(upload_to='channels/', verbose_name='изображение', **NULLABLE)
    made_at = models.DateTimeField()
    subscribers = models.IntegerField()
    publications_count = models.PositiveIntegerField(default=0, verbose_name='кол-во публикаций', **NULLABLE)


class Publication(models.Model):
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE, verbose_name='канал', **NULLABLE)
    title = models.CharField()
    content = models.TextField()
    image = models.ImageField(upload_to='publications/', verbose_name='изображение', **NULLABLE)
    is_free = models.BooleanField()
    made_at = models.DateTimeField()
    views_count = models.IntegerField(default=0, verbose_name='кол-во просмотров', **NULLABLE)


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь', **NULLABLE)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE, verbose_name='канал', **NULLABLE)
    subscription_status = models.BooleanField(default=False, verbose_name='статус подписки')

    class Meta:
        verbose_name = 'подписка'
        verbose_name_plural = 'подписки'

    def __str__(self):
        return f'{self.user}, {self.channel}, {self.subscription_status}'


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь', **NULLABLE)
    payment_date = models.DateTimeField(auto_now_add=True, verbose_name='дата оплаты')
    channel = models.ForeignKey(Channel,  on_delete=models.CASCADE, verbose_name='курс', **NULLABLE)
    amount = models.PositiveIntegerField(default=0, verbose_name='сумма оплаты', **NULLABLE)
    link = models.CharField(max_length=500, verbose_name='ссылка', **NULLABLE)

    class Meta:
        verbose_name = 'оплата'
        verbose_name_plural = 'оплаты'

    def __str__(self):
        return self.amount
