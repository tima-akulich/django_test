# Generated by Django 2.1 on 2018-08-20 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_author_created_by'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
