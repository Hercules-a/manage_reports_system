from django.db import models
from django.contrib.auth.models import User


class Car(models.Model):
    name = models.CharField(max_length=10, verbose_name='nazwa', unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'samochód'
        verbose_name_plural = 'samochody'


class Part(models.Model):
    name = models.CharField(max_length=100, verbose_name='nazwa')
    number = models.CharField(max_length=14, help_text='Wprowadz nr czesci w formacie 0X0000000XX',
                              verbose_name='numer', unique=True)
    car = models.ManyToManyField(Car)

    def __str__(self):
        return '{} {}'.format(self.number, self.name)

    class Meta:
        verbose_name = 'część'
        verbose_name_plural = 'części'


class PartStage(models.Model):
    part = models.ForeignKey(Part, on_delete=models.PROTECT, related_name='part_stage')
    stage = models.CharField(max_length=10, verbose_name='stan')

    def __str__(self):
        return '{} {}'.format(self.stage, self.part)

    class Meta:
        unique_together = ['part', 'stage']
        verbose_name = 'stan generacyjny częśći'
        verbose_name_plural = 'stany generacyjne częśći'


class Problem(models.Model):
    number = models.IntegerField(verbose_name='numer', unique=True)
    car = models.ForeignKey(Car, on_delete=models.PROTECT)
    description = models.TextField(verbose_name='opis')

    def __str__(self):
        return '{} {}'.format(self.number, self.description)

    class Meta:
        verbose_name = 'problem'
        verbose_name_plural = 'problemy'


class Order(models.Model):
    number = models.IntegerField(verbose_name='numer', unique_for_year='date_time_delivery')
    part = models.ManyToManyField(PartStage, related_name='order')
    amount_part = models.IntegerField(help_text='Wprowadz liczbe mierzonych czesci', default=1,
                                      verbose_name='liczba części')
    date_time_delivery = models.DateTimeField(verbose_name='data dostarczenia')
    date_time_collect = models.DateTimeField(null=True, blank=True, verbose_name='data odbioru')
    knnr = models.IntegerField(help_text='Wprowadz nr w formacie 0000000', null=True, blank=True)
    measuring_specification = models.TextField(verbose_name='specyfikacja pomiaru')
    measuring_reason = models.TextField(verbose_name='powód pomiaru')
    client = models.ForeignKey(User, on_delete=models.PROTECT)
    problem = models.ForeignKey(Problem, on_delete=models.PROTECT, related_name='order')

    CHOICES = [(0, 'Serie'),
               (1, '0-serie'),
               (2, 'PVS'),
               (3, 'Versuch'), ]
    production_stage = models.IntegerField(choices=CHOICES, verbose_name='etap produkcyjny', default=False)

    def parts(self):
        parts = ''
        for element in self.part.all():
            if element == self.part.last():
                parts += element.part.name
            else:
                parts += '{}, '.format(element.part.name)
        return parts

    def __str__(self):
        return '{} {} {}'.format(self.number, self.parts(), self.measuring_specification)

    class Meta:
        verbose_name = 'zlecenie'
        verbose_name_plural = 'zlecenia'
