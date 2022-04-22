# Generated by Django 4.0.4 on 2022-04-22 11:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sheets_bd', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RangeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('range_field', models.CharField(blank=True, max_length=120, null=True, verbose_name='Диапазон')),
            ],
            options={
                'verbose_name': 'Диапазон',
                'verbose_name_plural': 'Диапазоны',
            },
        ),
        migrations.CreateModel(
            name='SheetsResponses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('response', models.TextField(blank=True, null=True, verbose_name='Ответ из таблицы')),
                ('range_field', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sheets_bd.rangemodel', verbose_name='Диапазон')),
            ],
            options={
                'verbose_name': 'Ответ таблицы',
                'verbose_name_plural': 'Ответы таблиц',
            },
        ),
        migrations.AddField(
            model_name='clients',
            name='range_field',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sheets_bd.rangemodel', verbose_name='Диапазон'),
        ),
    ]