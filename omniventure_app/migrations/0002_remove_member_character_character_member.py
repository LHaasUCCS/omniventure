# Generated by Django 4.2 on 2024-04-15 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('omniventure_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='character',
        ),
        migrations.AddField(
            model_name='character',
            name='member',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='characters', to='omniventure_app.member'),
            preserve_default=False,
        ),
    ]
