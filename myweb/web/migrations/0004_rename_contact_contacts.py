# Generated by Django 4.2.5 on 2023-09-27 10:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_rename_last_name_contact_telephone_contact_email_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='contact',
            new_name='Contacts',
        ),
    ]