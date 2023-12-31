# Generated by Django 4.0.1 on 2023-06-21 13:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminfolder', '0006_music'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='skill',
            field=models.IntegerField(null=True),
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, null=True)),
                ('song', models.FileField(upload_to='song/')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='adminfolder.category')),
            ],
        ),
    ]
