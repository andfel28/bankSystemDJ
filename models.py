from django.db import models
#my_user = models.ForeignKey(User, on_delete=models.CASCADE)


class OWNER_CUE(models.Model):
    idOwner   = models.IntegerField( null=False, blank=False, primary_key=True)
    nameOwner = models.CharField(max_length=200)

class CUENTA(models.Model):

    idCue = models.IntegerField(primary_key=True)
    balance= models.IntegerField(default=0, blank=False)
    idOwnerCue= models.ForeignKey(OWNER_CUE,on_delete=models.CASCADE)

class INSCRITAS_CUE:
    idCuePadre =models.ForeignKey(CUENTA,on_delete =models.CASCADE)
    idCueHijo = models.ForeignKey(CUENTA,on_delete =models.CASCADE)
