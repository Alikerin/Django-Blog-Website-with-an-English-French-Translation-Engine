# Generated by Django 3.0.4 on 2020-03-21 20:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_remove_project_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='slug',
            field=models.SlugField(default='project-one', max_length=200, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(max_length=200),
        ),
        migrations.CreateModel(
            name='UserInput',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('input', models.TextField()),
                ('output', models.TextField()),
                ('target_language', models.CharField(choices=[('EN', 'English'), ('FR', 'French'), ('AR', 'Arabic')], default='EN', max_length=2)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_inputs', to='blog.Project')),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
    ]
