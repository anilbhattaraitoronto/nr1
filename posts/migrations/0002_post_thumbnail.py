# Generated by Django 2.1.7 on 2019-03-12 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='photos/posts/%Y'),
        ),
    ]
