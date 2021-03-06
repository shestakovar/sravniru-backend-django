# Generated by Django 3.2.7 on 2021-09-30 11:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CreditAmount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_from', models.IntegerField(db_column='from')),
                ('to', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerRequirement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('documents', models.IntegerField()),
                ('age', models.IntegerField()),
                ('manAgeAtRepayment', models.IntegerField()),
                ('femaleAgeAtRepayment', models.IntegerField()),
                ('lastExperience', models.IntegerField()),
                ('fullExperience', models.IntegerField()),
                ('salary', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='InitialAmount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_from', models.IntegerField(db_column='from')),
                ('to', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('license', models.CharField(max_length=255)),
                ('logo', models.URLField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='RateField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_from', models.DecimalField(db_column='from', decimal_places=2, max_digits=5)),
                ('to', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='TermField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_from', models.IntegerField(db_column='from')),
                ('to', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency', models.CharField(choices=[('RUB', 'RUB')], max_length=16)),
                ('creditAmount', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='backend.creditamount')),
                ('initialAmount', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='backend.initialamount')),
            ],
        ),
        migrations.CreateModel(
            name='Proposal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('alias', models.CharField(max_length=255)),
                ('customerRequirements', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='backend.customerrequirement')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='backend.organization')),
                ('rate', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='backend.rate')),
            ],
        ),
        migrations.CreateModel(
            name='Period',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('termUnit', models.CharField(choices=[('month', 'month')], max_length=5)),
                ('isFloatingRate', models.BooleanField()),
                ('rate', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='backend.ratefield')),
                ('rate_upper', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='periods', to='backend.rate')),
                ('term', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='backend.termfield')),
            ],
        ),
    ]
