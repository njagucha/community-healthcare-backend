# Generated by Django 4.2.4 on 2024-06-22 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='kiharubnd',
            options={'verbose_name_plural': 'Kiharu Bnd'},
        ),
        migrations.AlterModelOptions(
            name='kiharuhealthfacilitiescleaned',
            options={'verbose_name_plural': 'Kiharu Health Facilities'},
        ),
        migrations.AlterModelOptions(
            name='landmarks',
            options={'verbose_name_plural': 'Landmarks'},
        ),
    ]
