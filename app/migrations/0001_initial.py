# Generated by Django 3.0.5 on 2021-11-04 09:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Auction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object', models.CharField(max_length=50)),
                ('description', models.CharField(default='', max_length=256)),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('open_date', models.DateTimeField(auto_now_add=True)),
                ('close_date', models.DateTimeField()),
                ('total_bet', models.IntegerField(default=0)),
                ('open_price', models.FloatField(default=0)),
                ('close_price', models.FloatField(default=0)),
                ('winner', models.CharField(default='', max_length=256)),
                ('active', models.BooleanField(default=True)),
                ('json_details_file', models.TextField(default='')),
                ('tx', models.CharField(default='', max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', max_length=256)),
                ('wallet', models.FloatField(default=1000)),
                ('total_bet', models.IntegerField(default=0)),
                ('wins', models.IntegerField(default=0)),
                ('active', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
