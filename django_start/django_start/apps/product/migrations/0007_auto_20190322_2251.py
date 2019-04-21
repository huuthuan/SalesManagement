# Generated by Django 2.1.7 on 2019-03-22 15:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_auto_20190316_1545'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imageproduct',
            old_name='url_1',
            new_name='url',
        ),
        migrations.RemoveField(
            model_name='imageproduct',
            name='url_2',
        ),
        migrations.RemoveField(
            model_name='imageproduct',
            name='url_3',
        ),
        migrations.RemoveField(
            model_name='imageproduct',
            name='url_4',
        ),
        migrations.RemoveField(
            model_name='imageproduct',
            name='url_5',
        ),
        migrations.AlterField(
            model_name='imageproduct',
            name='product',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='product.Product'),
        ),
    ]