# Generated by Django 3.0.5 on 2020-04-19 10:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0007_auto_20200416_1134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='author',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='blog',
            name='category',
            field=models.CharField(blank=True, choices=[('FAMILY_RELATIONSHIPS', 'Family Relationships'), ('ROMANTIC_RELATIONSHIPS', 'Romantic Relationships'), ('WORKPLACE_RELATIONSHIPS', 'Workplace Relationships'), ('COMMUNNITY_RELATIONSHIPS', 'Community Relationships')], default='FAMILY_RELATIONSHIPS', max_length=100, null=True),
        ),
    ]