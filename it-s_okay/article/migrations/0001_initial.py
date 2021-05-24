# Generated by Django 3.2.3 on 2021-05-24 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('area', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('kakao_url', models.CharField(max_length=200)),
                ('meeting_time', models.DateTimeField()),
                ('headcount', models.IntegerField()),
                ('state', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('anonymous', models.IntegerField()),
            ],
        ),
    ]
