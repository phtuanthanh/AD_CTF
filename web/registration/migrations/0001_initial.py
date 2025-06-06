# Generated by Django 3.2.25 on 2025-04-20 10:31

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import web.registration.fields
import web.registration.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('net_number', models.PositiveSmallIntegerField(null=True, unique=True)),
                ('informal_email', models.EmailField(max_length=254, verbose_name='Informal email address')),
                ('image', web.registration.fields.ThumbnailImageField(blank=True, upload_to=web.registration.models._gen_image_name)),
                ('affiliation', models.CharField(blank=True, max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('nop_team', models.BooleanField(db_index=True, default=False)),
            ],
        ),
        migrations.CreateModel(
            name='TeamDownload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(help_text='Name within the per-team filesystem hierarchy, see "TEAM_DOWNLOADS_ROOT" setting', max_length=100, validators=[django.core.validators.RegexValidator('^[^/]+$', message='Must not contain slashes')])),
                ('description', models.TextField()),
            ],
        ),
    ]
