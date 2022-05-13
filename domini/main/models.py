from django.db import models

class UserInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    age = models.IntegerField(blank=True, null=True)
    sex = models.CharField(blank=True, null=True, max_length=2)
    
    card_samsung = models.CharField(blank=True, null=True, max_length=5)
    card_shinhan = models.CharField(blank=True, null=True, max_length=5)
    card_kb = models.CharField(blank=True, null=True, max_length=5)
    card_bc = models.CharField(blank=True, null=True, max_length=5)
    card_hyundai = models.CharField(blank=True, null=True, max_length=5)
    card_nh = models.CharField(blank=True, null=True, max_length=5)
    card_lotte = models.CharField(blank=True, null=True, max_length=5)
    card_woori = models.CharField(blank=True, null=True, max_length=5)

    mc_skt = models.CharField(blank=True, null=True, max_length=5)
    mc_kt = models.CharField(blank=True, null=True, max_length=5)
    mc_lgu = models.CharField(blank=True, null=True, max_length=5)
    mc_vip = models.CharField(blank=True, null=True, max_length=5)

    pay_kakao = models.CharField(blank=True, null=True, max_length=5)
    pay_naver = models.CharField(blank=True, null=True, max_length=5)
    pay_payco = models.CharField(blank=True, null=True, max_length=5)
    pay_smile = models.CharField(blank=True, null=True, max_length=5)

    class Meta:
        managed = False
        db_table = 'user_info'

class AirlineEvent(models.Model):
    id = models.IntegerField(primary_key=True)
    airline = models.CharField(blank=True, null=True, max_length=10)
    
    card_samsung = models.CharField(blank=True, null=True, max_length=5)
    card_shinhan = models.CharField(blank=True, null=True, max_length=5)
    card_kb = models.CharField(blank=True, null=True, max_length=5)
    card_bc = models.CharField(blank=True, null=True, max_length=5)
    card_hyundai = models.CharField(blank=True, null=True, max_length=5)
    card_nh = models.CharField(blank=True, null=True, max_length=5)
    card_lotte = models.CharField(blank=True, null=True, max_length=5)
    card_woori = models.CharField(blank=True, null=True, max_length=5)

    mc_skt = models.CharField(blank=True, null=True, max_length=5)
    mc_kt = models.CharField(blank=True, null=True, max_length=5)
    mc_lgu = models.CharField(blank=True, null=True, max_length=5)
    mc_vip = models.CharField(blank=True, null=True, max_length=5)

    pay_kakao = models.CharField(blank=True, null=True, max_length=5)
    pay_naver = models.CharField(blank=True, null=True, max_length=5)
    pay_payco = models.CharField(blank=True, null=True, max_length=5)
    pay_smile = models.CharField(blank=True, null=True, max_length=5)

    min_cost = models.IntegerField(blank=True, null=True)
    discount = models.IntegerField(blank=True, null=True)
    is_weekend = models.CharField(blank=True, null=True, max_length=10)
    is_oneway = models.CharField(blank=True, null=True, max_length=10)
    is_event = models.CharField(blank=True, null=True, max_length=10)
    discount_type = models.CharField(blank=True, null=True, max_length=10)
    duplicate = models.CharField(blank=True, null=True, max_length=10)
    option = models.CharField(blank=True, null=True, max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'airline_events'