# Generated by Django 5.1 on 2024-11-28 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cofee', '0005_alter_register_email_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='Password',
            field=models.CharField(max_length=500),
        ),
    ]
