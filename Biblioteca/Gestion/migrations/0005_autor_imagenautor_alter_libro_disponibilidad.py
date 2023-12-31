# Generated by Django 4.2.7 on 2023-12-18 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gestion', '0004_libro_rating_alter_libro_disponibilidad'),
    ]

    operations = [
        migrations.AddField(
            model_name='autor',
            name='imagenAutor',
            field=models.ImageField(blank=True, null=True, upload_to='autores/'),
        ),
        migrations.AlterField(
            model_name='libro',
            name='disponibilidad',
            field=models.CharField(choices=[('disponible', 'disponible'), ('no disponible', 'no disponible'), ('reservado', 'reservado')], default='disponible', max_length=20),
        ),
    ]
