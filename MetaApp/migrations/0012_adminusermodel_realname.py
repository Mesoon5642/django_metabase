# Generated by Django 3.2.6 on 2022-06-28 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MetaApp', '0011_adminusermodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='adminusermodel',
            name='realname',
            field=models.CharField(default='John Doe', max_length=200),
            preserve_default=False,
        ),
    ]