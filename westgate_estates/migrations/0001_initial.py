# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Commercial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('owner_name', models.CharField(max_length=72)),
                ('owner_address', models.CharField(max_length=250)),
                ('property_address', models.CharField(max_length=250)),
                ('town', models.CharField(max_length=60)),
                ('postcode1', models.CharField(max_length=12)),
                ('postcode2', models.CharField(max_length=12)),
                ('summary', models.CharField(max_length=1200)),
                ('description', models.CharField(max_length=1200)),
                ('branch_id', models.CharField(max_length=60)),
                ('status_id', models.CharField(max_length=60)),
                ('bedrooms', models.CharField(max_length=6)),
                ('price', models.CharField(max_length=12)),
                ('price_qualifier', models.CharField(max_length=12)),
                ('prop_sub_id', models.CharField(max_length=20)),
                ('create_date', models.CharField(max_length=20)),
                ('update_date', models.CharField(max_length=20)),
                ('display_address', models.CharField(max_length=350)),
                ('published_flag', models.CharField(max_length=8)),
                ('let_date_available', models.CharField(max_length=30)),
                ('let_furn_id', models.CharField(max_length=50)),
                ('let_rent_frequency', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='LET_FURN_ID',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.CharField(unique=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='LET_RENT_FREQUENCY',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.CharField(unique=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PRICE_QUALIFIER',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.CharField(unique=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PROP_SUB_ID',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.CharField(unique=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PUBLISHED_FLAG',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.CharField(unique=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Residential',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('AGENT_REF', models.CharField(unique=True, max_length=12)),
                ('SLUG', autoslug.fields.AutoSlugField(editable=False, populate_from=b'AGENT_REF', always_update=True, unique=True)),
                ('ADDRESS_1', models.CharField(max_length=250)),
                ('ADDRESS_2', models.CharField(max_length=250)),
                ('ADDRESS_3', models.CharField(max_length=250)),
                ('ADDRESS_4', models.CharField(max_length=250)),
                ('TOWN', models.CharField(max_length=60)),
                ('POSTCODE1', models.CharField(max_length=12)),
                ('POSTCODE2', models.CharField(max_length=12)),
                ('SUMMARY', models.CharField(max_length=1200)),
                ('DESCRIPTION', models.CharField(max_length=1200)),
                ('BRANCH_ID', models.CharField(max_length=60)),
                ('BEDROOMS', models.CharField(max_length=6)),
                ('PRICE', models.CharField(max_length=12)),
                ('CREATE_DATE', models.CharField(max_length=20)),
                ('UPDATE_DATE', models.CharField(max_length=20)),
                ('DISPLAY_ADDRESS', models.CharField(max_length=350)),
                ('LET_DATE_AVAILABLE', models.CharField(max_length=30)),
                ('MEDIA_IMAGE_00', models.CharField(max_length=200)),
                ('MEDIA_IMAGE_01', models.CharField(max_length=200)),
                ('MEDIA_IMAGE_02', models.CharField(max_length=200)),
                ('MEDIA_IMAGE_03', models.CharField(max_length=200)),
                ('MEDIA_IMAGE_04', models.CharField(max_length=200)),
                ('MEDIA_IMAGE_05', models.CharField(max_length=200)),
                ('MEDIA_IMAGE_06', models.CharField(max_length=200)),
                ('MEDIA_IMAGE_07', models.CharField(max_length=200)),
                ('MEDIA_IMAGE_08', models.CharField(max_length=200)),
                ('MEDIA_IMAGE_09', models.CharField(max_length=200)),
                ('MEDIA_IMAGE_10', models.CharField(max_length=200)),
                ('MEDIA_IMAGE_11', models.CharField(max_length=200)),
                ('MEDIA_IMAGE_12', models.CharField(max_length=200)),
                ('MEDIA_IMAGE_13', models.CharField(max_length=200)),
                ('MEDIA_IMAGE_14', models.CharField(max_length=200)),
                ('MEDIA_IMAGE_15', models.CharField(max_length=200)),
                ('MEDIA_IMAGE_16', models.CharField(max_length=200)),
                ('MEDIA_IMAGE_17', models.CharField(max_length=200)),
                ('MEDIA_IMAGE_18', models.CharField(max_length=200)),
                ('MEDIA_IMAGE_19', models.CharField(max_length=200)),
                ('MEDIA_FLOOR_PLAN_00', models.CharField(max_length=200)),
                ('MEDIA_FLOOR_PLAN_TEXT_00', models.CharField(max_length=200)),
                ('MEDIA_FLOOR_PLAN_01', models.CharField(max_length=200)),
                ('MEDIA_FLOOR_PLAN_TEXT_01', models.CharField(max_length=200)),
                ('MEDIA_IMAGE_60', models.CharField(max_length=200)),
                ('MEDIA_IMAGE_TEXT_60', models.CharField(max_length=200)),
                ('MEDIA_IMAGE_61', models.CharField(max_length=200)),
                ('MEDIA_IMAGE_TEXT_61', models.CharField(max_length=200)),
                ('MEDIA_DOCUMENT_50', models.CharField(max_length=200)),
                ('MEDIA_DOCUMENT_TEXT_50', models.CharField(max_length=200)),
                ('MEDIA_DOCUMENT_51', models.CharField(max_length=200)),
                ('MEDIA_DOCUMENT_TEXT_51', models.CharField(max_length=200)),
                ('MEDIA_DOCUMENT_52', models.CharField(max_length=200)),
                ('MEDIA_DOCUMENT_TEXT_52', models.CharField(max_length=200)),
                ('MEDIA_DOCUMENT_53', models.CharField(max_length=200)),
                ('MEDIA_DOCUMENT_TEXT_53', models.CharField(max_length=200)),
                ('MEDIA_DOCUMENT_00', models.CharField(max_length=200)),
                ('MEDIA_DOCUMENT_TEXT_00', models.CharField(max_length=200)),
                ('MEDIA_DOCUMENT_01', models.CharField(max_length=200)),
                ('MEDIA_DOCUMENT_TEXT_01', models.CharField(max_length=200)),
                ('MEDIA_VIRTUAL_TOUR_01', models.CharField(max_length=200)),
                ('MEDIA_VIRTUAL_TOUR_TEXT_01', models.CharField(max_length=200)),
                ('MEDIA_VIRTUAL_TOUR_02', models.CharField(max_length=200)),
                ('MEDIA_VIRTUAL_TOUR_TEXT_02', models.CharField(max_length=200)),
                ('LET_FURN_ID', models.ForeignKey(to='westgate_estates.LET_FURN_ID')),
                ('LET_RENT_FREQUENCY', models.ForeignKey(to='westgate_estates.LET_RENT_FREQUENCY')),
                ('PRICE_QUALIFIER', models.ForeignKey(to='westgate_estates.PRICE_QUALIFIER')),
                ('PROP_SUB_ID', models.ForeignKey(to='westgate_estates.PROP_SUB_ID')),
                ('PUBLISHED_FLAG', models.ForeignKey(to='westgate_estates.PUBLISHED_FLAG')),
            ],
        ),
        migrations.CreateModel(
            name='STATUS_ID',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.CharField(unique=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TRANS_TYPE_ID',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.CharField(unique=True, max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='residential',
            name='STATUS_ID',
            field=models.ForeignKey(to='westgate_estates.STATUS_ID'),
        ),
        migrations.AddField(
            model_name='residential',
            name='TRANS_TYPE_ID',
            field=models.ForeignKey(to='westgate_estates.TRANS_TYPE_ID'),
        ),
    ]
