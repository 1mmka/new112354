# Generated by Django 4.2.4 on 2023-09-01 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_todolist_options_remove_todolist_body_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TakeImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='uploads')),
            ],
        ),
    ]
