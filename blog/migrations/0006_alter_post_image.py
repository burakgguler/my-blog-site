# Generated by Django 4.0.1 on 2022-05-07 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_post_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='posts/mouintains.png', upload_to='posts'),
        ),
    ]
