# Generated by Django 4.1.6 on 2023-02-06 19:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('newsarticle', '0002_rename_business_newscategory_newscategory_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsarticle',
            name='published',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='newsarticle',
            name='published_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]