# Generated by Django 5.1.6 on 2025-02-13 18:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_for_planogram', models.CharField(blank=True, max_length=250, null=True, verbose_name='Planogram category name')),
                ('custom_id', models.CharField(help_text='Unique identifier', max_length=250, verbose_name='Custom ID')),
            ],
        ),
        migrations.CreateModel(
            name='Planogram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(help_text='Category where planogram is attached', on_delete=django.db.models.deletion.PROTECT, related_name='planograms', related_query_name='planogram', to='app.category', verbose_name='Category')),
            ],
        ),
        migrations.CreateModel(
            name='TaskPlanogram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('planogram', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task_links', related_query_name='task_link', to='app.planogram')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='planogram_links', related_query_name='planogram_link', to='app.task')),
            ],
        ),
    ]
