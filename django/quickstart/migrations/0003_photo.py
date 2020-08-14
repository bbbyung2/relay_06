# Generated by Django 3.1 on 2020-08-14 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0002_remove_diary_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=255)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('tag', models.CharField(max_length=255, null=True)),
            ],
        ),
    ]