# Generated by Django 5.0.3 on 2024-03-18 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livraria1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Editora',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('site', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
