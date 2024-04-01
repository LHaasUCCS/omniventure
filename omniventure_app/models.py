from django.db import models
from django.urls import reverse

# Create your models here.
class Member(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length = 200, blank = False)
    pronouns = models.CharField(max_length = 40)
    active_times = models.DateTimeField()
    main_character = 0 #placeholder
    about = models.CharField(max_length = 200)
    discord = models.CharField(max_length = 100)
    discord_message_check = models.BooleanField(default = False)
    is_active = models.BooleanField(default = False)
