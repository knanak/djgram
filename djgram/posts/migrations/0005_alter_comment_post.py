# Generated by Django 4.1.8 on 2023-05-02 12:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("posts", "0004_alter_comment_post"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="post",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="comment_post", to="posts.post"
            ),
        ),
    ]