# Generated by Django 4.1.7 on 2023-03-23 10:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_doctors_student_user_id_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('chronic_diseases', models.CharField(max_length=200)),
                ('medicines', models.CharField(max_length=200)),
                ('allergics', models.CharField(max_length=200)),
            ],
        ),
    ]