# Generated by Django 4.1.8 on 2023-05-02 03:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("posts", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="caption",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="post",
            name="image",
            field=models.ImageField(upload_to=""),
        ),
    ]
