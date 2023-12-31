# Generated by Django 4.1.3 on 2022-11-28 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SignUpUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.TextField()),
                ('last_name', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('password', models.TextField()),
                ('college_name', models.TextField()),
                ('qualification', models.TextField()),
                ('phone', models.BigIntegerField()),
            ],
        ),
    ]
