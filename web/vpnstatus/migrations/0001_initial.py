# Generated by Django 3.2.25 on 2025-04-20 10:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VPNStatusCheck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wireguard_handshake_time', models.DateTimeField(blank=True, null=True)),
                ('gateway_ping_rtt_ms', models.PositiveIntegerField(blank=True, null=True)),
                ('demo_ping_rtt_ms', models.PositiveIntegerField(blank=True, null=True)),
                ('vulnbox_ping_rtt_ms', models.PositiveIntegerField(blank=True, null=True)),
                ('demo_service_ok', models.BooleanField()),
                ('vulnbox_service_ok', models.BooleanField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.team')),
            ],
            options={
                'verbose_name': 'VPN status check',
            },
        ),
    ]
