# Generated by Django 2.2.5 on 2019-12-28 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('c1', '0016_auto_20191228_1033'),
    ]

    operations = [
        migrations.CreateModel(
            name='book6',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usr', models.IntegerField()),
                ('drsid', models.IntegerField(max_length=30)),
                ('date', models.CharField(max_length=20)),
                ('quantity', models.IntegerField()),
                ('totalprice', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='book5',
        ),
    ]