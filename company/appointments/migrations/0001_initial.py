# Generated by Django 3.1.6 on 2021-02-01 19:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('_employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='people.employee')),
            ],
        ),
    ]
