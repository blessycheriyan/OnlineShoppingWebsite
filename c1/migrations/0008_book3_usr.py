# Generated by Django 2.2.5 on 2019-12-13 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('c1', '0007_auto_20191213_1050'),
    ]

    operations = [
        migrations.AddField(
            model_name='book3',
            name='usr',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]