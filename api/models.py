from django.db.models import Model, CharField, DateTimeField
from django.contrib import admin

# Create your models here.
class Social(Model):
    social_choices = (
        ("facebook", "facebook"),
        ("github", "github"),
        ("twitter", "twitter"),
        ("discord", "discord"),
        ("linkedin", "linkedin"),
    )

    social_name = CharField(
        max_length=100,
        unique=True,
        null=False,
        blank=False,
        choices=social_choices,
    )
    username = CharField(max_length=100, null=False, blank=False)
    created_at = DateTimeField(auto_now_add=True, null=False, blank=False)

    def __str__(self):
        social_map = {
            "facebook": "facebook.com/",
            "github": "github.com/",
            "twitter": "twitter.com/",
            "discord": "https://discordapp.com/users/",
            "linkedin": "linkedin.com/in/",
        }
        url = social_map[self.social_name] + self.username
        return url

    def social_url(self):
        return str(self)
