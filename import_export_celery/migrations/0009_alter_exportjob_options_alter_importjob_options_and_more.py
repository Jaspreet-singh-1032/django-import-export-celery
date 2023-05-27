# Generated by Django 4.1.9 on 2023-05-27 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('import_export_celery', '0008_alter_exportjob_id_alter_importjob_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='exportjob',
            options={'verbose_name': 'Export job', 'verbose_name_plural': 'Export jobs'},
        ),
        migrations.AlterModelOptions(
            name='importjob',
            options={'verbose_name': 'Import job', 'verbose_name_plural': 'Import jobs'},
        ),
        migrations.AlterField(
            model_name='exportjob',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='exportjob',
            name='site_of_origin',
            field=models.TextField(default='', max_length=255, verbose_name='Site of origin'),
        ),
        migrations.AlterField(
            model_name='importjob',
            name='errors',
            field=models.TextField(blank=True, default='', verbose_name='Errors'),
        ),
        migrations.AlterField(
            model_name='importjob',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
