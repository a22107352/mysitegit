# Generated by Django 4.2.1 on 2023-06-09 00:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('login', '0004_alter_cadeira_ects_alter_cadeira_ranking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadeira',
            name='ects',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='cadeira',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='cadeira',
            name='nome',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='cadeira',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
