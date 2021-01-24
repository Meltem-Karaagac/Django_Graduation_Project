# Generated by Django 3.1.5 on 2021-01-23 20:12

import blog.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210120_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=110),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='blog.category'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='django.jpg', upload_to=blog.models.user_directory_path),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=230),
        ),
    ]
