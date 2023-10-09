# Generated by Django 4.2.5 on 2023-09-27 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_remove_contact_num_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='last_name',
            new_name='Telephone',
        ),
        migrations.AddField(
            model_name='contact',
            name='email',
            field=models.EmailField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='message',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
