# Generated by Django 3.2.7 on 2021-09-27 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=200)),
                ('description', models.TextField(max_length=1000)),
                ('timetoread', models.TextField(max_length=20)),
                ('content', models.TextField()),
            ],
        ),
    ]
