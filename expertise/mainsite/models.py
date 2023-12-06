from django.db import models


class ObjectDefect(models.Model):


class ObjectDescription(models.Model):
    pass


class ProtocolUZK(models.Model):
    pass


class ExpertiseObject(models.Model):
    name = models.CharField(max_length=100)
    release_date = models.DateTimeField
    counterparty = models.TextField
    counterparty_division = models.TextField
    contract = models.TextField
    type = models.TextField
    expertise_type = models.TextField
    tech_num = models.TextField
    inv_num = models.TextField
    reg_num = models.TextField
    fac_num = models.TextField
    description = models.OneToOneField(ObjectDescription,
                                       on_delete=models.CASCADE,
                                       related_name="desc"
                                       )


class ObjectRVS(models.Model):

