# Generated by Django 2.2.5 on 2019-12-28 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('c1', '0014_auto_20191228_1016'),
    ]

    operations = [
        migrations.CreateModel(
            name='book5',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usr', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('date', models.CharField(max_length=20)),
                ('quantity', models.IntegerField()),
                ('totalprice', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='book4',
        ),
    ]
