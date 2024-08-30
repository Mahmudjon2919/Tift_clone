from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from apps.common.models import District
from apps.education.models import Direction



class Gender(models.TextChoices):
    MALE = "male", "Male"
    FEMALE = "female", "Female"

class ApplicationStatusChoices(models.TextChoices):
    PENDING = "pending", "Pending"
    ACCEPTED = "accepted", "Accepted"
    REJECTED = "rejected", "Rejected"


class Application(models.Model):
    user=models.ForeignKey(User, on_delete=models.PROTECT)
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    password=models.CharField(max_length=9)
    pinfl=models.CharField(max_length=14)
    gender=models.CharField(max_length=6, choices=Gender.choices)
    birth_data=models.DateField()
    direction=models.ForeignKey(Direction, on_delete=models.SET_NULL, null=True,blank=True)
    status=models.CharField(max_length=16, choices=ApplicationStatusChoices.choices)
    district=models.ForeignKey(District, on_delete=models.SET_NULL, null=True, blank=True)


    accepted_at=models.DateTimeField(null=True, blank=True)
    created=models.DateTimeField(auto_now=True)

    def __str__(self) ->str:
        return f"(self.first_name) (self.last_name)"

    def save(self, *args, **kwargs) -> None:
        if (self.status == ApplicationStatusChoices.ACCEPTED or
            self.status == ApplicationStatusChoices.REJECTED) and not self.accepted_at:
            self.accepted_at = datetime.now()
        super().save(*args, **kwargs)
