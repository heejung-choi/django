from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail, ResizeToFill


def profile_image_path(instance, filename):
    return f'user_{instance.username}/{filename}'


# Create your models here.
class User(AbstractUser):
    followers = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='followings'
    )
    image = ProcessedImageField(
        upload_to=profile_image_path,
        processors=[Thumbnail(200, 200)],
        format='JPEG',
        options={'quality': 80},
        default='no-image.png',
    )
