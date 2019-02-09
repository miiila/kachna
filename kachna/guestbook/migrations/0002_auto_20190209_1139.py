# Generated by Django 2.1.5 on 2019-02-09 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guestbook', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='post_author_email',
            new_name='author_email',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='post_author_name',
            new_name='author_name',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='post_text',
            new_name='text',
        ),
        migrations.RemoveField(
            model_name='post',
            name='post_timestamp',
        ),
        migrations.AddField(
            model_name='post',
            name='timestamp',
            field=models.DateTimeField(auto_now=True, verbose_name='date published'),
        ),
    ]