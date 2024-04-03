from django.db import models
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# Create your models here.
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
    
    image = models.ImageField(upload_to=user_directory_path,
        blank=True,
         validators=[validate_image_size]
    )
    name = models.CharField(max_length = 200, blank = False, primary_key = True)
    pronouns = models.CharField(max_length = 40, blank = True)
    active_times = models.CharField(max_length = 200, blank = True)
    main_character = 0 #placeholder
    about = models.CharField(max_length = 200, blank = True)
    discord = models.CharField(max_length = 100, blank = True)
    discord_message_check = models.BooleanField(default = False)
    is_active = models.BooleanField(default = False)

def __str__(self):
    return self.title
    
def get_absolute_url(self):
    return reverse('member_detail', args=[str(self.id)])


