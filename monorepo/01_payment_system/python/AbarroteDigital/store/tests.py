from django.test import TestCase

from store.models import Product, Category
import decimal

class ProductTestCase(TestCase):
    def setUp(self):
        try:
            self.category1 = Category.objects.get(name='Procesadores')
        except Category.DoesNotExist:
            self.category1 = Category.objects.create(name='Procesadores')
        try:
            self.category2 = Category.objects.get(name='Tarjetas gráficas')
        except Category.DoesNotExist:
            self.category2 = Category.objects.create(name='Tarjetas gráficas')
        try:
            self.category3 = Category.objects.get(name='Memoria RAM')
        except Category.DoesNotExist:
            self.category3 = Category.objects.create(name='Memoria RAM')
        
        try:
            self.product1 = Product.objects.get(name='Procesador Intel Core i7')
        except Product.DoesNotExist:
            # Crea producto en caso de que no exista
            self.product1 = Product.objects.create(
                name='Procesador Intel Core i7',
                category=self.category1,
                price=299.99,
                description='Potente procesador Intel Core i7 para tu PC.'
            )
        try:
            self.product2 = Product.objects.get(name='Tarjeta gráfica NVIDIA GeForce RTX 3080')
        except Product.DoesNotExist:
            self.product2 = Product.objects.create(
                name='Tarjeta gráfica NVIDIA GeForce RTX 3080',
                category=self.category2,
                price=699.99,
                description='Tarjeta gráfica de alto rendimiento para gaming.'
            )
        try:
            self.product3 = Product.objects.get(name='Memoria RAM Corsair Vengeance RGB')
        except Product.DoesNotExist:
            self.product3 = Product.objects.create(
                name='Memoria RAM Corsair Vengeance RGB',
                category=self.category3,
                price=129.99,
                description='Módulo de memoria RAM DDR4 con iluminación RGB.'
            )

    def test_product_name(self):
        product = Product.objects.get(name='Procesador Intel Core i7')
        self.assertEqual(product.name, 'Procesador Intel Core i7')

    def test_product_price(self):
        product = Product.objects.get(name='Procesador Intel Core i7')
        self.assertAlmostEqual(product.price, decimal.Decimal(299.99), places=2)
    
    def test_product_category(self):
        product = Product.objects.get(name='Procesador Intel Core i7')
        self.assertEqual(product.category, self.category1)
    
