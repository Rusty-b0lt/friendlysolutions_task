# Generated by Django 3.2.16 on 2022-10-25 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('album_id', models.IntegerField()),
                ('width', models.IntegerField()),
                ('height', models.IntegerField()),
                ('dominant_color', models.CharField(max_length=7)),
                ('file', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
