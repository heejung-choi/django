# Generated by Django 2.1.15 on 2020-06-26 04:34

import accounts.models
from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_followers'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(default='no-image.jpg', upload_to=accounts.models.profile_image_path),
        ),
    ]