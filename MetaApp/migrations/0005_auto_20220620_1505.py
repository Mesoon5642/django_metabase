# Generated by Django 3.2.6 on 2022-06-20 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MetaApp', '0004_auto_20220620_1415'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reportmodel',
            old_name='medialinks',
            new_name='mainlink',
        ),
        migrations.RemoveField(
            model_name='reportmodel',
            name='crimecategory',
        ),
        migrations.RemoveField(
            model_name='reportmodel',
            name='govreport',
        ),
        migrations.RemoveField(
            model_name='reportmodel',
            name='platform',
        ),
        migrations.RemoveField(
            model_name='reportmodel',
            name='time',
        ),
        migrations.AddField(
            model_name='reportmodel',
            name='eventname',
            field=models.CharField(default='exit', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reportmodel',
            name='target',
            field=models.CharField(choices=[('I', 'Assault'), ('S', 'Sexual Violence'), ('PB', 'Public Building'), ('O', 'Other')], default='exit', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reportmodel',
            name='targetother',
            field=models.CharField(default='N/A', max_length=200),
        ),
        migrations.AddField(
            model_name='reportmodel',
            name='techinvolved',
            field=models.CharField(choices=[('VR', 'Virtual Reality'), ('MLT', 'Multiplayer Online Videogame'), ('CR', 'Chatroom/Forum'), ('CC', 'Cryptocurrency')], default='N/A', max_length=100),
        ),
    ]