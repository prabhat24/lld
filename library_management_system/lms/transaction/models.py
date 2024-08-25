import uuid
from datetime import datetime as dt

import pytz
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib import admin

from books.models import *
from zauth.models import User, Member
from core.model_mixins import FullAuditMixin

# Create your models here.


class Transaction(FullAuditMixin):
    class Meta:
        abstract = True

    item = models.ForeignKey(BookItem, null=False, blank=False, on_delete=models.PROTECT)
    member = models.ForeignKey(Member, null=False, blank=False, on_delete=models.CASCADE)
    # TODO - remove slug to be a 128 bits to 64 bit
    slug = models.UUIDField(
                          default=uuid.uuid4,
                          unique=True,
                          editable=False
                          )

class LendingModel(Transaction):
    class IssueStatus(models.TextChoices):
        LOANED = "LOANED", _("LOANED")
        CANCELED = "CANCELED", _("CANCELED")
        CLOSED = "CLOSED", _("CLOSED")
    issued_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    status = models.CharField(choices=IssueStatus, null=False, blank=False, max_length=10, default=IssueStatus.LOANED)
    due_date = models.DateField(null=True, blank=True)
    return_date = models.DateField(null=True, blank=True)
    metadata = models.JSONField(null=True, blank=True, verbose_name="to store fine inncured on this lending order for historical purposes")

    @property
    def panalty(self):
        if  self.days_since_issue > 0:
            days_diff_fine = self.days_since_issue * 100 
            fine = self.item.price if days_diff_fine > self.item.price else days_diff_fine
            return fine
        return 0
        
    @property
    def days_since_issue(self):
        if self.status == self.IssueStatus.LOANED:
            return (dt.now(tz=pytz.timezone("Asia/Kolkata")).date() - self.due_date).days
        return 0

class ReservationModel(Transaction):
    class ReservationStatusEnum(models.TextChoices):
        WAITING = "WAITING", _("WAITING")
        CANCELED = "CANCELED", _("CANCELED")
        CLOSED = "CLOSED", _("CLOSED")
    status = models.CharField(choices=ReservationStatusEnum, null=False, blank=False, default=ReservationStatusEnum.WAITING, max_length=10)


    

# admin registration
admin.site.register(LendingModel)
admin.site.register(ReservationModel)