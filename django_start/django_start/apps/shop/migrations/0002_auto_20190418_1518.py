# Generated by Django 2.1.7 on 2019-04-18 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='address',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='shop',
            name='description',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='shop',
            name='email',
            field=models.EmailField(max_length=75, null=True),
        ),
        migrations.AlterField(
            model_name='shop',
            name='phone',
            field=models.CharField(max_length=11, null=True),
        ),
    ]
