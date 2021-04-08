# Generated by Django 3.1.7 on 2021-04-06 16:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='accounts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=200)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('tel', models.CharField(max_length=200)),
                ('birth_date', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('date_of_employment', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='time_tracker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('stop_time', models.DateTimeField()),
                ('rate', models.DecimalField(decimal_places=2, max_digits=6)),
                ('total_time', models.DateTimeField()),
                ('contact_name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='contacts.contacts')),
                ('user_name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.accounts')),
            ],
        ),
    ]