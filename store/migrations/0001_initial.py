# Generated by Django 3.2.18 on 2023-02-17 11:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
            ],
            options={
                'db_table': 'Course',
                'ordering': ['department'],
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=300)),
            ],
            options={
                'db_table': 'Department',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('dob', models.DateField()),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=50)),
                ('phone_number', models.IntegerField()),
                ('mail_id', models.CharField(max_length=100)),
                ('address', models.TextField(max_length=300)),
                ('purpose', models.CharField(max_length=200)),
                ('materials_provide', models.CharField(max_length=300)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.course')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.department')),
            ],
            options={
                'db_table': 'Form',
            },
        ),
        migrations.AddField(
            model_name='course',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.department'),
        ),
    ]