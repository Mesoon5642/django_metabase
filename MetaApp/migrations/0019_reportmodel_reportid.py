# Generated by Django 3.2.6 on 2022-06-30 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MetaApp', '0018_reportmodel_readabletech'),
    ]

    operations = [
        migrations.AddField(
            model_name='reportmodel',
            name='reportid',
            field=models.IntegerField(default=0, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
