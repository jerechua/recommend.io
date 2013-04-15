from django.db import models

class BaseModel(models.Model):
    modify_time = models.DateTimeField(auto_now=True)
    create_time = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True