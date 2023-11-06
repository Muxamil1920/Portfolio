# Generated by Django 4.2.4 on 2023-11-06 17:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0002_alter_contact_id_alter_contact_number"),
    ]

    operations = [
        migrations.AddField(
            model_name="contact",
            name="email",
            field=models.CharField(default="default value", max_length=50),
        ),
        migrations.AddField(
            model_name="contact",
            name="subject",
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="contact",
            name="id",
            field=models.AutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="contact",
            name="number",
            field=models.IntegerField(),
        ),
    ]
