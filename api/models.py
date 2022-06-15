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
        ("reddit", "reddit"),
        ("email", "email"),
    )

    social_map = {
        "facebook": {
            "url": "https://facebook.com/",
            "fa": "fa-brands fa-facebook",
        },
        "github": {
            "url": "https://github.com/",
            "fa": "fa-brands fa-github",
        },
        "twitter": {
            "url": "https://twitter.com/",
            "fa": "fa-brands fa-twitter",
        },
        "discord": {
            "url": "https://discordapp.com/users/",
            "fa": "fa-brands fa-discord",
        },
        "linkedin": {
            "url": "https://linkedin.com/in/",
            "fa": "fa-brands fa-linkedin-in",
        },
        "reddit": {
            "url": "https://reddit.com/user/",
            "fa": "fa-brands fa-reddit",
        },
        "email": {
            "url": "mailto:",
            "fa": "fa-solid fa-envelope",
        },
    }

    social_name = CharField(
        max_length=100,
        unique=True,
        null=False,
        blank=False,
        choices=social_choices,
    )
    username = CharField(max_length=100, null=False, blank=False)
    created_at = DateTimeField(auto_now_add=True, null=False, blank=False)

    def __str__(self) -> str:
        url = self.social_map[self.social_name]["url"] + self.username
        return url

    def social_url(self) -> str:
        return str(self)

    def social_fa(self):
        return self.social_map[self.social_name]["fa"]
