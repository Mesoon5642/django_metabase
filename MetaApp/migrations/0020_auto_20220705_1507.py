# Generated by Django 3.2.6 on 2022-07-05 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MetaApp', '0019_reportmodel_reportid'),
    ]

    operations = [
        migrations.AddField(
            model_name='suspectmodel',
            name='locations',
            field=models.ManyToManyField(to='MetaApp.RelevantLocationModel'),
        ),
        migrations.AddField(
            model_name='suspectmodel',
            name='susid',
            field=models.IntegerField(default=0, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='reportmodel',
            name='reportid',
            field=models.IntegerField(default=0, verbose_name='ID'),
        ),
    ]
