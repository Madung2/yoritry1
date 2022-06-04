# Generated by Django 3.2.5 on 2022-06-04 07:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Diffcate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('difficulty', models.CharField(default='', max_length=50)),
            ],
            options={
                'db_table': 'difficulty',
            },
        ),
        migrations.CreateModel(
            name='Timecate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timecost', models.CharField(default='', max_length=50)),
            ],
            options={
                'db_table': 'timecost',
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('img_url', models.CharField(default='', max_length=200)),
                ('ingredient', models.TextField()),
                ('cookstep', models.TextField()),
                ('recipe_author', models.CharField(default='', max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('difficulty', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='post.diffcate')),
                ('timecost', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='post.timecate')),
            ],
            options={
                'db_table': 'recipe',
            },
        ),
    ]
