# Generated by Django 2.0 on 2019-01-29 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_auto_20190127_2356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='sex',
            field=models.CharField(choices=[('MAN', 'MAN'), ('WOMAN', 'WOMAN'), ('DK/NA', 'DK/NA')], default='DK/NA', max_length=500),
        ),
    ]