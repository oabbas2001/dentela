# Generated by Django 4.1.7 on 2023-03-23 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_user_profile_photo_alter_doctors_certificate_photo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_photo',
            field=models.ImageField(default='media/id/meow_lostcat (1).png', upload_to='media/profiles_photo/% email/'),
        ),
    ]