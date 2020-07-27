# Generated by Django 3.0.8 on 2020-07-23 11:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=600, null=True, unique=True)),
                ('subtitle', models.CharField(blank=True, max_length=600, null=True)),
                ('date_published', models.DateTimeField(auto_now_add=True, null=True)),
                ('featured_image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('content', models.CharField(blank=True, max_length=20000000, null=True)),
                ('slug', models.SlugField(blank=True, max_length=600, null=True, unique=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('tag', models.ManyToManyField(to='blogs.Tag')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('date_posted', models.DateTimeField(auto_now_add=True, null=True)),
                ('website', models.CharField(blank=True, max_length=100, null=True)),
                ('comment_content', models.CharField(blank=True, max_length=1000, null=True)),
                ('comment_reply', models.CharField(blank=True, max_length=600, null=True)),
                ('post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blogs.Post')),
            ],
        ),
    ]