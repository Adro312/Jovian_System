# Generated by Django 3.2.8 on 2022-10-01 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Galery',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(null=True, upload_to='images/galery/')),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('redImage', models.ImageField(null=True, upload_to='images/red_img/', verbose_name='Red_Image')),
                ('greenImage', models.ImageField(null=True, upload_to='images/green_img/', verbose_name='Green_Image')),
                ('blueImage', models.ImageField(null=True, upload_to='images/blue_img/', verbose_name='Blue_Image')),
            ],
        ),
    ]
