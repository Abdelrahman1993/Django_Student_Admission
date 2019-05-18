# Generated by Django 2.2.1 on 2019-05-17 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='semester',
            field=models.IntegerField(choices=[('1', 'first'), ('2', 'second')]),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='grade',
            field=models.CharField(choices=[('1', 'one'), ('2', 'two'), ('3', 'three'), ('4', 'four')], max_length=1),
        ),
    ]