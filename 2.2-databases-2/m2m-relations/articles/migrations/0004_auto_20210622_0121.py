# Generated by Django 3.2.4 on 2021-06-21 22:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20210622_0111'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['tagname'], 'verbose_name': 'Раздел', 'verbose_name_plural': 'Разделы'},
        ),
        migrations.RenameField(
            model_name='tag',
            old_name='name',
            new_name='tagname',
        ),
    ]
