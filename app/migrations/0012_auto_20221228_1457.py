# Generated by Django 3.1 on 2022-12-28 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20221228_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job_post',
            name='max_salary',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='job_post',
            name='min_salary',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='job_post',
            name='package',
            field=models.CharField(max_length=10, null=True),
        ),
    ]