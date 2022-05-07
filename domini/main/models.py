from django.db import models

class UserInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(blank=True, null=True, max_length=20)
    age = models.IntegerField(blank=True, null=True)
    sex = models.CharField(blank=True, null=True, max_length=2)
    mobile_carrier = models.CharField(blank=True, null=True, max_length=20)
    credit_card = models.CharField(blank=True, null=True, max_length=100)
    mc_grade = models.CharField(blank=True, null=True, max_length=11)
    pay_application = models.CharField(blank=True, null=True, max_length=100)
    new_card_will = models.IntegerField(blank=True, null=True)
    new_mc_will = models.IntegerField(blank=True, null=True)
    new_app_will = models.IntegerField(blank=True, null=True)
    event_will = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_info'

class AirlineEvent(models.Model):
    id = models.IntegerField(primary_key=True)
    airline = models.CharField(blank=True, null=True, max_length=10)
    credit_card = models.CharField(blank=True, null=True, max_length=10)
    mobile_carrier = models.CharField(blank=True, null=True, max_length=10)
    pay_application = models.CharField(blank=True, null=True, max_length=10)
    min_cost = models.IntegerField(blank=True, null=True)
    is_weekend = models.IntegerField(blank=True, null=True)
    is_oneway = models.IntegerField(blank=True, null=True)
    is_event = models.IntegerField(blank=True, null=True)
    discount_type = models.CharField(blank=True, null=True, max_length=10)
    duplicate = models.IntegerField(blank=True, null=True)
    option = models.CharField(blank=True, null=True, max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'airline_events'