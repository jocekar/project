# Generated by Django 4.0.1 on 2023-06-19 01:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminfolder', '0005_alter_skill_skill'),
    ]

    operations = [
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, null=True)),
                ('music', models.FileField(upload_to='mp-4/%y')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='adminfolder.category')),
            ],
        ),
    ]