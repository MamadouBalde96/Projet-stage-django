# Generated by Django 3.1.2 on 2021-05-15 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0022_auto_20210515_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listes',
            name='niveau',
            field=models.CharField(choices=[('L1', 'Licence 1'), ('L2', 'Licence 2'), ('L3', 'Licence 3'), ('M1', 'Master 1'), ('M1', 'Master 2')], default='L1', max_length=2),
        ),
    ]
