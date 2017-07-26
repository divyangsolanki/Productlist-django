# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import migrations

def create_initial_products(apps, schema_editor):
    Product = apps.get_model('catalog', 'Product')

    Product(name='Salame', description='Salame Toscano', price=12).save()
    Product(name='Olio Balsamico', description='Olio balsamico di Modena', price=10).save()
    Product(name='Parmigiano', description='Parmigiano Reggiano', price=8.50).save()
    Product(name='Olio', description='Olio Oliva Toscano', price=13).save()
    Product(name='Porchetta', description='Porchetta toscana cotta a legna', price=7.50).save()
    Product(name='Cantucci', description='Cantucci di Prato', price=4).save()
    Product(name='Vino Rosso', description='Vino Rosso del Chianti', price=9.50).save()
    Product(name='Brigidini', description='Brigidini di Lamporecchio', price=3.50).save()

def create_initial_reviews(apps, schema_editor):
    Review = apps.get_model('catalog','Review')

    Review(product_id='1',title='review 1',review='nice product',rating=1,created_by_id='1').save()
    Review(product_id='2',title='review 2',review='nice product',rating=1,created_by_id='1').save()


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_review'),
    ]

    operations = [
        migrations.RunPython(create_initial_products),
        migrations.RunPython(create_initial_reviews),
    ]
