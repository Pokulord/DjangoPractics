# Generated by Django 4.1 on 2023-08-07 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='blog/images/2023/none.jpg', upload_to='blog/images/%Y'),
        ),
    ]