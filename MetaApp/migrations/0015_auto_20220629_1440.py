# Generated by Django 3.2.6 on 2022-06-29 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MetaApp', '0014_alter_reportmodel_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='EvidenceModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200)),
                ('datefound', models.CharField(max_length=100)),
                ('description', models.CharField(default='', max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='RelevantLocationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('description', models.CharField(max_length=2000)),
            ],
        ),
        migrations.AddField(
            model_name='reportmodel',
            name='closed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='reportmodel',
            name='author',
            field=models.CharField(default='Superuser', max_length=200),
        ),
        migrations.CreateModel(
            name='SuspectModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200)),
                ('description', models.CharField(default='', max_length=2000)),
                ('age', models.IntegerField(default=18)),
                ('guilty', models.BooleanField(default=False)),
                ('evidence', models.ManyToManyField(to='MetaApp.EvidenceModel')),
            ],
        ),
        migrations.AddField(
            model_name='reportmodel',
            name='evidence',
            field=models.ManyToManyField(to='MetaApp.EvidenceModel'),
        ),
        migrations.AddField(
            model_name='reportmodel',
            name='relevantlocation',
            field=models.ManyToManyField(to='MetaApp.RelevantLocationModel'),
        ),
        migrations.AddField(
            model_name='reportmodel',
            name='suspects',
            field=models.ManyToManyField(to='MetaApp.SuspectModel'),
        ),
    ]
