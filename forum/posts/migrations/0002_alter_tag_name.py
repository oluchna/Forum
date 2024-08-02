# Generated by Django 5.0.7 on 2024-08-02 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(choices=[('TECH', 'Technology'), ('EDU', 'Education'), ('ENT', 'Entertainment'), ('HEA', 'Health'), ('LIFE', 'Lifestyle')], default='LIFE', max_length=50, unique=True),
        ),
    ]
