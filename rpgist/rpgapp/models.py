from django.db import models

class Personagem(models.Model):
    name = models.CharField(max_length=250)
    life = models.IntegerField(default=0)
    str = models.IntegerField(default=0)
    defense = models.IntegerField(default=0)
    int = models.IntegerField(default=0)
    sab = models.IntegerField(default=0)
    agi = models.IntegerField(default=0)
    mag = models.IntegerField(default=0)
    chak = models.IntegerField(default=0)
    values = (
        ('adm','Administrador'),
        ('com','Comum')
    )
    perm = models.CharField(choices=values,max_length=10)
class Habs(models.Model):
    habname = models.CharField(max_length=250)
    habdesc = models.TextField()
    fk = models.ForeignKey(Personagem,on_delete=models.CASCADE)
    cust = models.CharField(max_length=250,default=0)
class User2(models.Model):
    name = models.CharField(max_length=250)
    password = models.CharField(max_length=32)