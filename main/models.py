from django.db import models

# Create your models here.
class Agency(models.Model):
    agency_name = models.CharField(max_length=50)

    def __str__(self):
        return self.agency_name


class Member(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    email_address = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    agency = models.ForeignKey(Agency, null = True, on_delete = models.SET_NULL)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
    

class Campaign(models.Model):
    amount = models.FloatField(max_length=30)
    currency = models.TextChoices("Currency", "USD EUR GBP AUD CAD")

    client = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    # talent = models.ForeignKey(Talent, on_delete=models.SET_NULL)
    deliverables = models.CharField(max_length=500)

    # contract = 
    client_email = models.EmailField(max_length=50)
    client_name = models.CharField(max_length=50)
    campaign_status = models.TextChoices("Campaign status", "Unsigned Signed Completed Paid")

    def __str__(self):
        return self.id + ' ' + self.brand