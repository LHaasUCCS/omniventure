from django.db import models
from django.urls import reverse
from django.core.exceptions import ValidationError, PermissionDenied
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


# Create your models here   
class Member(models.Model):

    def validate_image_size(image):
        width, height = image.width, image.height
        if width > 1000 or height > 1000:  # Set your desired maximum width and height
            raise ValidationError(
                _('The image dimensions exceed the allowed size of 1000x1000 pixels.')
        )
    
    def user_directory_path(instance, filename): 
        # file will be uploaded to MEDIA_ROOT / user_<id>/<filename> 
        return 'member_{0}/{1}'.format(instance.pk, filename) 
    
    # Fields here
    # -----------------------------------------------
    user = models.OneToOneField(User, on_delete=models.CASCADE)


    image = models.ImageField(upload_to=user_directory_path,
        blank=True,
        validators=[validate_image_size]
    )
    name = models.CharField(max_length = 200, blank = False, primary_key = True)
    pronouns = models.CharField(max_length = 40, blank = True)
    active_times = models.CharField(max_length = 200, blank = True)
    about = models.CharField(max_length = 200, blank = True)
    discord = models.CharField(max_length = 100, blank = True)
    discord_message_check = models.BooleanField(default = False)
    
    

    

    # For verification of profiles by admin before posting
    is_active = models.BooleanField(default = False)

    class Meta:
        permissions = [
            ('can_edit', 'Can edit member'),
            ('delete', 'Can delete member'),
        ]

    def can_edit(self, user):
        return user.is_superuser or self.pk is None or user == self.user # Customize this according to your requirements

    def delete(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        if user and (user.is_superuser or user == self.user):
            super().delete(*args, **kwargs)
        else:
            raise PermissionDenied("You don't have permission to delete this member")


    def save(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        if user and not self.pk:  # Only check if it's a new member
            existing_member = Member.objects.filter(user=user).exists()
            if existing_member:
                raise ValidationError("You can only create one member per user account")
            self.is_active = False  # Newly created members require admin approval
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
        return reverse('member_detail', args=[str(self.id)])
    
    
class Character(models.Model):
    # character id to parse ffxivcollect
    character_id = models.IntegerField(unique=True)
    # these fields will be populated by the return of ffxivcollect
    name = models.CharField(max_length=100, primary_key=True)
    server = models.CharField(max_length=100)
    data_center = models.CharField(max_length=100)
    portrait = models.URLField()
    avatar = models.URLField()

    # Additional fields for user input
    background = models.CharField(max_length=2000)
    personality = models.CharField(max_length=200)
    pronouns = models.CharField(max_length=100)

    member = models.ForeignKey(Member, related_name='characters', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
        return reverse('character_detail', args=[str(self.name)])
