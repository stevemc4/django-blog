# Generated by Django 2.2.19 on 2021-03-30 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='post',
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='posts', to='blog.Tag'),
        ),
    ]