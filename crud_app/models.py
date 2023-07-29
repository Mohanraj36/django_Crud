from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

from CRUD.settings import TIME_ZONE
# Create your models here.

class Note(models.Model):
    user = models.ForeignKey(User, on_delete = models.DO_NOTHING)
    # created_date = models.DateTimeField(null=False, blank=False, default = datetime.datetime.now)
    created_date = models.DateTimeField(default=timezone.now, null=True, blank = True)
    title = models.CharField(max_length = 30, null= False, blank= False)
    description = models.TextField(max_length = 1000, null = False, blank= False)

    # def __str__(self):
    #     return self.user