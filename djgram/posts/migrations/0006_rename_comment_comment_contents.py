# Generated by Django 4.1.8 on 2023-05-03 04:11

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("posts", "0005_alter_comment_post"),
    ]

    operations = [
        migrations.RenameField(
            model_name="comment",
            old_name="comment",
            new_name="contents",
        ),
    ]