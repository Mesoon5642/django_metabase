# Generated by Django 3.2.6 on 2022-06-27 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MetaApp', '0010_reportmodel_cryptoamount'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminUserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=300)),
                ('password', models.CharField(max_length=100)),
                ('verified', models.BooleanField()),
            ],
        ),
    ]