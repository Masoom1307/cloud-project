# Generated by Django 5.0.7 on 2024-08-21 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lmsreporting', '0002_rename_date_subimtted_issue_date_submitted'),
    ]

    operations = [
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
