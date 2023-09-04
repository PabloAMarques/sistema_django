from django.db import models

class Proposal(models.Model):
    document = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    approved = models.BooleanField(default=False)
