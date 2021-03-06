# Generated by Django 2.0.1 on 2018-04-13 15:58

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
            name='CheckPoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(default=0, help_text='Check point number')),
                ('time', models.FloatField(default=0.0, help_text='Check point time in seconds')),
                ('slide_number', models.IntegerField(default=0, help_text='Slide number')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(help_text='Comment text', max_length=300)),
                ('author', models.ForeignKey(blank=True, help_text='Comment author', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, help_text='Course title', max_length=100, null=True)),
                ('description', models.TextField(blank=True, help_text='Course description', max_length=1000, null=True)),
                ('audio', models.FileField(help_text='Audio file', null=True, upload_to='')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('left', models.FloatField(default=0.0, help_text='Coordinate from left')),
                ('top', models.FloatField(default=0.0, help_text='Coordinate from top')),
            ],
        ),
        migrations.CreateModel(
            name='Pointer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.FloatField(default=0.0, help_text='Pointer start time')),
                ('end_time', models.FloatField(default=0.0, help_text='Pointer end time')),
                ('course', models.ForeignKey(help_text='Pointer', on_delete=django.db.models.deletion.CASCADE, to='courses.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(default=0, help_text='Slide number')),
                ('image', models.ImageField(help_text='Slide image', upload_to='')),
                ('course', models.ForeignKey(help_text='Course frame', on_delete=django.db.models.deletion.CASCADE, to='courses.Course')),
            ],
        ),
        migrations.AddField(
            model_name='point',
            name='pointer',
            field=models.ForeignKey(help_text='Pointer point', on_delete=django.db.models.deletion.CASCADE, to='courses.Pointer'),
        ),
        migrations.AddField(
            model_name='comment',
            name='slide',
            field=models.ForeignKey(help_text='Comment to slide', on_delete=django.db.models.deletion.CASCADE, to='courses.Slide'),
        ),
        migrations.AddField(
            model_name='checkpoint',
            name='course',
            field=models.ForeignKey(help_text='Course check point', on_delete=django.db.models.deletion.CASCADE, to='courses.Course'),
        ),
    ]
