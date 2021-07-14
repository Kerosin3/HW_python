# Generated by Django 3.2.5 on 2021-07-14 14:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sector',
            name='stock',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='stocks.stock'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='financials',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='stocks.financials'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='prices',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='stocks.prices'),
        ),
    ]
