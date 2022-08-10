# Generated by Django 3.2.12 on 2022-08-09 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0008_merge_0005_question_0007_auto_20220809_1422'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_date', models.DateTimeField(verbose_name='date published')),
                ('username', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('contactNumber', models.IntegerField(default=23480000000)),
                ('company', models.CharField(max_length=150)),
                ('userAddress', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.DeleteModel(
            name='Questions',
        ),
    ]