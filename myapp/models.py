from django.db import models

# Create your models here.
import os, shutil
from django.db import models
from django.core.validators import EmailValidator, RegexValidator, MinValueValidator, MaxValueValidator
from django.dispatch import receiver
from django.utils import timezone
from django.utils.timezone import now


class Autor(models.Model):
    jmeno = models.CharField(max_length=100, verbose_name="Křestní jméno")
    prijmeni = models.CharField(max_length=100, verbose_name="Křestní jméno")
    email = models.EmailField(max_length=256, verbose_name="E-mail")
    zivotopis = models.CharField(max_length=45, verbose_name="Životopis")
    bio = models.TextField(max_length=2000, verbose_name="Životopis")
    narozeni = models.DateField(verbose_name="Datum narození")
    umrti = models.DateField(verbose_name="Datum umrtí", null=False)


    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autoři'
        ordering = ['jmeno']

    def __str__(self):
        return self.jmeno


class Bydliste(models.Model):
    ulice = models.CharField(max_length=30, verbose_name="Název ulice", null=False)
    obec = models.CharField(max_length=45, verbose_name="Název obce", null=False)
    psc = models.CharField(max_length=7, verbose_name="PSČ", null=False)

    class Meta:
        verbose_name = 'Bydliště'
        verbose_name_plural = 'Bydliště'
        ordering = ['obec']

    def __str__(self):
        return self.obec


class Ctenar(models.Model):
    jmeno = models.CharField(max_length=100, verbose_name="Křestní jméno")
    prijmeni = models.CharField(max_length=100, verbose_name="Příjmení")
    email = models.EmailField(max_length=256, verbose_name="E-mail")
    bydliste = models.ForeignKey("Bydliste", verbose_name="Bydliště", on_delete=models.CASCADE)
    telefon = models.CharField(max_length=20, verbose_name='Telefon',
                               help_text='Telefonní číslo',
                               validators=[RegexValidator(regex='^(\\+420)? ?[1-9][0-9]{2}( ?[0-9]{3}){2}$',
                                                          message='Zadejte prosím platné telefonní číslo.'
                                                          )])

    class Meta:
        verbose_name = 'Čtenář'
        verbose_name_plural = 'Čtenáři'
        ordering = ['jmeno']

    def __str__(self):
        return self.jmeno


class Exemplar(models.Model):
    cena = models.CharField(max_length=10, verbose_name="Cena")
    isbn = models.CharField(max_length=17, verbose_name="ISBN")
    kniha_isbn = models.ForeignKey("Kniha", on_delete=models.CASCADE, verbose_name="Kniha")

    class Meta:
        verbose_name = 'Exemplář'
        verbose_name_plural = 'Exempláře'
        ordering = ['isbn']

    def __str__(self):
        return self.isbn


class Kniha(models.Model):
    isbn = models.CharField(max_length=17, verbose_name="ISBN knihy")
    titul = models.CharField(max_length=100, verbose_name="Titul knihy")
    strany = models.CharField(max_length=5, verbose_name="Počet stran")
    obsah = models.TextField(max_length=5000, verbose_name="Obsah knihy")
    #zanr = models.ForeignKey("Zanr", verbose_name="Zadejte zanr", on_delete=models.CASCADE)
    nakladatelstvi = models.ForeignKey("Nakladatelstvi", verbose_name="Nakladatelství knihy", on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Kniha'
        verbose_name_plural = 'Knihy'
        ordering = ['titul']

    def __str__(self):
        return self.titul


class Nakladatelstvi(models.Model):
    nazev = models.CharField(max_length=50, verbose_name="Název")

    class Meta:
        verbose_name = 'Nakladatelství'
        verbose_name_plural = 'Nakladatelství'
        ordering = ['nazev']

    def __str__(self):
        return self.nazev

