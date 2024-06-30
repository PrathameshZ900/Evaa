from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class ServiceUser(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=254, unique=True)
    age = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])

    class Gender(models.TextChoices):
        MALE = "M", "Male"
        FEMALE = "F", "Female"
        OTHER = "O", "Other"

    gender = models.CharField(max_length=1, choices=Gender.choices)

    def __str__(self):
        return self.name

class Service(models.Model):
    TYPE_OF_RECHARGES = [
        ("Mobile Recharge", "Mobile Recharge"),
        ("DTH Recharge", "DTH Recharge"),
        ("Insurance Payment", "Insurance Payment")
    ]
    MODE_OF_PAYMENTS = [
        ("UPI", "Unified Payments Interface"),
        ("IB", "Internet Banking"),
        ("CP", "Card Payment")
    ]
    type_of_recharges = models.CharField(max_length=20, choices=TYPE_OF_RECHARGES)
    mode_of_payments = models.CharField(max_length=3, choices=MODE_OF_PAYMENTS)
    company = models.CharField(max_length=150)

    def __str__(self):
        return self.company

class Subscription(models.Model):
    service_user = models.ForeignKey(ServiceUser, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.service_user.name

