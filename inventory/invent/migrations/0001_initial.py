# Generated by Django 5.1.7 on 2025-03-16 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('quantity_present', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=19)),
                ('quantity_sold', models.IntegerField()),
                ('sales', models.DecimalField(decimal_places=2, max_digits=19)),
                ('stock_date', models.DateField()),
                ('last_sales_date', models.DateField(auto_now=True)),
            ],
        ),
    ]
