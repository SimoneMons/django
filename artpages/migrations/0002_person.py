# Generated by Django 4.0.5 on 2022-06-15 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artpages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('address', models.TextField()),
            ],
        ),
    ]
