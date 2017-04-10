# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-13 14:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dividend_Payout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('div_per_share', models.DecimalField(decimal_places=5, max_digits=8)),
            ],
        ),
        migrations.CreateModel(
            name='Dividend_Yield',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('div_yield', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Fair_Value',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, null=True)),
                ('fair', models.DecimalField(decimal_places=2, max_digits=8, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Financial_Ratio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quarter', models.CharField(choices=[('Q1', 'Q1'), ('Q2', 'Q2'), ('Q3', 'Q3'), ('Q4', 'Q4')], max_length=2, null=True)),
                ('eps', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Financial_Statement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('net_asset', models.DecimalField(decimal_places=2, max_digits=10)),
                ('net_profit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('rental_income', models.DecimalField(decimal_places=2, max_digits=10)),
                ('retained_earning', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='General_Information',
            fields=[
                ('short_name', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=100)),
                ('fund_type', models.CharField(choices=[('Leasehold & Freehold', 'Leasehold & Freehold'), ('Leasehold', 'Leasehold'), ('Freehold', 'Freehold')], default='Leasehold', max_length=20)),
                ('property_type', models.CharField(max_length=50)),
                ('ipo_date', models.IntegerField()),
                ('dividend_payout_amount_per_year', models.SmallIntegerField()),
                ('listed_share', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Period_Table',
            fields=[
                ('period', models.DateField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.AddField(
            model_name='financial_statement',
            name='period',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='valuation.Period_Table'),
        ),
        migrations.AddField(
            model_name='financial_statement',
            name='short_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='valuation.General_Information'),
        ),
        migrations.AddField(
            model_name='financial_ratio',
            name='period',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='valuation.Period_Table'),
        ),
        migrations.AddField(
            model_name='financial_ratio',
            name='short_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='valuation.General_Information'),
        ),
        migrations.AddField(
            model_name='fair_value',
            name='period',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='valuation.Period_Table'),
        ),
        migrations.AddField(
            model_name='fair_value',
            name='short_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='short_name_fk', to='valuation.General_Information'),
        ),
        migrations.AddField(
            model_name='dividend_yield',
            name='period',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='valuation.Period_Table'),
        ),
        migrations.AddField(
            model_name='dividend_yield',
            name='short_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='valuation.General_Information'),
        ),
        migrations.AddField(
            model_name='dividend_payout',
            name='period',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='valuation.Period_Table'),
        ),
        migrations.AddField(
            model_name='dividend_payout',
            name='short_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='valuation.General_Information'),
        ),
    ]