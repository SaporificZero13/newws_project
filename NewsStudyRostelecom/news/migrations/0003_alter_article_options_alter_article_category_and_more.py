# Generated by Django 4.2.6 on 2023-11-21 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0002_article_category"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="article",
            options={
                "ordering": ["title", "date"],
                "verbose_name": "Новость",
                "verbose_name_plural": "Новости",
            },
        ),
        migrations.AlterField(
            model_name="article",
            name="category",
            field=models.CharField(
                choices=[("E", "Economics"), ("S", "Science"), ("IT", "IT")],
                max_length=20,
                verbose_name="Категории",
            ),
        ),
        migrations.AlterField(
            model_name="article",
            name="date",
            field=models.DateTimeField(auto_now=True, verbose_name="Дата публикации"),
        ),
    ]
