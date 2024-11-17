# Generated by Django 5.1.1 on 2024-11-10 19:31

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_person_license_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='age',
        ),
        migrations.RemoveField(
            model_name='person',
            name='license_type',
        ),
        migrations.AddField(
            model_name='motorbike',
            name='is_automatic',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='person',
            name='date_of_birth',
            field=models.DateField(default=datetime.date(2000, 1, 1)),
        ),
        migrations.CreateModel(
            name='Ride',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_favourite', models.BooleanField(default=False)),
                ('motorbike', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.motorbike')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.person')),
            ],
        ),
        migrations.AddField(
            model_name='person',
            name='motorbikes',
            field=models.ManyToManyField(through='api.Ride', to='api.motorbike'),
        ),
        migrations.DeleteModel(
            name='DrivingPermission',
        ),
    ]
