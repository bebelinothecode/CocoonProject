# Generated by Django 4.1.6 on 2023-02-06 18:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsarticle', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newscategory',
            old_name='business',
            new_name='newscategory',
        ),
        migrations.RemoveField(
            model_name='newscategory',
            name='entertainment',
        ),
        migrations.RemoveField(
            model_name='newscategory',
            name='generalNews',
        ),
        migrations.RemoveField(
            model_name='newscategory',
            name='healthAndMedicine',
        ),
        migrations.RemoveField(
            model_name='newscategory',
            name='historicalNews',
        ),
        migrations.RemoveField(
            model_name='newscategory',
            name='lifestyle',
        ),
        migrations.RemoveField(
            model_name='newscategory',
            name='technology',
        ),
    ]