# Generated by Django 4.2.1 on 2023-05-19 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='type',
            field=models.CharField(choices=[('I', 'Income'), ('E', 'Expense')], max_length=50, verbose_name='Type'),
        ),
    ]
