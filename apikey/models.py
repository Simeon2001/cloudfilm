from django.db import models
from account.models import User

class Keys(models.Model):
    user = models.fieldName = models.OneToOneField(User, on_delete=models.CASCADE)
    public_key = models.CharField(max_length=53, blank=False)
    private_key = models.CharField(max_length=53, blank=False)
    enc_public_key = models.TextField(max_length=250, blank=False)
    enc_private_key = models.TextField(max_length=250, blank=False)

    def __str__(self):
        return self.public_key

