# Generated by Django 5.0.1 on 2024-01-24 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend1', '0012_alter_categorydb_company_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorydb',
            name='comapnyname',
            field=models.EmailField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='categorydb',
            name='company_id',
            field=models.IntegerField(null=True),
        ),
    ]
