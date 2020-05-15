# Generated by Django 3.0.5 on 2020-04-15 14:25

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
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('short_desc', models.CharField(blank=True, max_length=250, null=True)),
                ('category', models.CharField(blank=True, max_length=50, null=True)),
                ('blog_image', models.ImageField(upload_to='Media/blog')),
                ('blog_content', models.TextField()),
                ('date_published', models.DateTimeField()),
                ('slug', models.SlugField(unique=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Blog Posts',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=80)),
                ('comment_content', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('approved_comment', models.BooleanField(default=False)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.Blog')),
            ],
            options={
                'verbose_name_plural': 'Comments',
                'ordering': ['date_created'],
            },
        ),
    ]