# Generated by Django 2.2.6 on 2019-11-05 10:03

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('category', models.CharField(choices=[('WAR', 'WARRANTS'), ('OTH', 'OTHER OFFENSES'), ('LAR', 'LARCENY/THEFT'), ('VEH', 'VEHICLE THEFT'), ('VAN', 'VANDALISM'), ('NON', 'NON-CRIMINAL'), ('ROB', 'ROBBERY'), ('AS', 'ASSAULT'), ('WEA', 'WEAPON LAWS'), ('BUR', 'BURGLARY'), ('SUS', 'SUSPICIOUS OCC'), ('DRU', 'DRUNKENNESS'), ('FOR', 'FORGERY/COUNTERFEITING'), ('NAR', 'DRUG/NARCOTIC'), ('STO', 'STOLEN PROPERTY'), ('SEC', 'SECONDARY CODES'), ('TRE', 'TRESPASS'), ('MIS', 'MISSING PERSON'), ('FR', 'FRAUD'), ('KID', 'KIDNAPPING'), ('RUN', 'RUNAWAY'), ('DRI', 'DRIVING UNDER THE INFLUENCE'), ('SOF', 'SEX OFFENSES FORCIBLE'), ('PRO', 'PROSTITUTION'), ('DIS', 'DISORDERLY CONDUCT'), ('ARS', 'ARSON'), ('FAM', 'FAMILY OFFENSES'), ('LIQ', 'LIQUOR LAWS'), ('BRI', 'BRIBERY'), ('EMB', 'EMBEZZLEMENT'), ('SUI', 'SUICIDE'), ('LOI', 'LOITERING'), ('SONF', 'SEX OFFENSES NON FORCIBLE'), ('EXT', 'EXTORTION'), ('GAM', 'GAMBLING'), ('BC', 'BAD CHECKS'), ('TE', 'TREA'), ('RV', 'RECOVERED VEHICLE'), ('POR', 'PORNOGRAPHY/OBSCENE MAT')], max_length=55)),
                ('severity', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
                ('state', models.CharField(max_length=35)),
                ('statecode', models.CharField(max_length=2)),
                ('city', models.CharField(max_length=40)),
                ('time_created', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
            ],
        ),
    ]
