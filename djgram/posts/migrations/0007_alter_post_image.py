# Generated by Django 4.1.8 on 2023-05-04 02:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("posts", "0006_rename_comment_comment_contents"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="image",
            field=models.ImageField(upload_to="image"),
        ),
    ]