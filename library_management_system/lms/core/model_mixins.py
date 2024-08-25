from django.db import models


class CreationAuditMixin(models.Model):
    """ CreationAuditMixin documentation
    """
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=255, blank=True, editable=False)

    class Meta:
        abstract = True


class ModificationAuditMixin(models.Model):
    """ ModificationAuditMixin documentation
    """
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.CharField(max_length=255, blank=True, editable=False)

    class Meta:
        abstract = True


class FullAuditMixin(CreationAuditMixin, ModificationAuditMixin):

    class Meta:
        abstract = True