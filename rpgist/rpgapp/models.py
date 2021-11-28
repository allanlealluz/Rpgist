from django.db import models

class Personagem(models.Model):
    name = models.CharField(max_length=250)
    life = models.IntegerField()
    str = models.IntegerField()
    defense = models.IntegerField()
    int = models.IntegerField()
    sab = models.IntegerField()
    agi = models.IntegerField()
    mag = models.IntegerField()
    chak = models.IntegerField()
    values = (
        ('adm','Administrador'),
        ('com','Comum')
    )
    perm = models.CharField(choices=values,max_length=10)
class Habs(models.Model):
    habname = models.CharField(max_length=250)
    habdesc = models.TextField()
    fk = models.ForeignKey(Personagem,on_delete=models.CASCADE)
    cust = models.CharField(max_length=250)
class User(models.Model):
    name = models.CharField(max_length=250)
    password = models.CharField(max_length=32)