from django.db.models import Model, CharField, DateTimeField
from django.contrib import admin

# Create your models here.
class Social(Model):
    social_choices = (("facebook.com", "facebook"),)

    social_name = CharField(
        max_length=100,
        unique=True,
        null=False,
        blank=False,
        choices=social_choices,
    )
    username = CharField(max_length=100, null=False)
    created_at = DateTimeField(auto_now_add=True, null=False, blank=False)

    def __str__(self):
        return self.social_name + "/" + self.username

    def social_url(self):
        return self.social_name + "/" + self.username
