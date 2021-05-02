# Generated by Django 3.0.5 on 2021-04-29 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-pub_date'], 'verbose_name_plural': 'comments'},
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ['-pub_date'], 'verbose_name_plural': 'reviews'},
        ),
        migrations.RemoveConstraint(
            model_name='review',
            name='unique_review',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='title',
        ),
        migrations.AddConstraint(
            model_name='review',
            constraint=models.UniqueConstraint(fields=('text',), name='unique_review'),
        ),
    ]