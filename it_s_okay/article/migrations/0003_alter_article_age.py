# Generated by Django 3.2.3 on 2021-05-24 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20210524_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='age',
            field=models.CharField(choices=[('ten', '10대'), ('twenty', '20대'), ('third', '30대'), ('forty', '40대')], max_length=20),
        ),
    ]