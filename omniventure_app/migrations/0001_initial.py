# Generated by Django 4.2 on 2024-04-14 19:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import omniventure_app.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('character_id', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('server', models.CharField(max_length=100)),
                ('data_center', models.CharField(max_length=100)),
                ('portrait', models.URLField()),
                ('avatar', models.URLField()),
                ('background', models.CharField(max_length=2000)),
                ('personality', models.CharField(max_length=200)),
                ('pronouns', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('image', models.ImageField(blank=True, upload_to=omniventure_app.models.Member.user_directory_path, validators=[omniventure_app.models.Member.validate_image_size])),
                ('name', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('pronouns', models.CharField(blank=True, max_length=40)),
                ('active_times', models.CharField(blank=True, max_length=200)),
                ('about', models.CharField(blank=True, max_length=200)),
                ('discord', models.CharField(blank=True, max_length=100)),
                ('discord_message_check', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('character', models.ManyToManyField(blank=True, related_name='members', to='omniventure_app.character')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': [('can_edit', 'Can edit member'), ('delete', 'Can delete member')],
            },
        ),
    ]
