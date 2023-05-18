from store.models import Product, Category

def initialize_products():
    # Crear categorías
    category1 = Category.objects.create(name='Procesadores')
    category2 = Category.objects.create(name='Tarjetas gráficas')
    category3 = Category.objects.create(name='Memoria RAM')

    # Crear productos
    product1 = Product.objects.create(
        name='Procesador Intel Core i7',
        category=category1,
        price=299.99,
        description='Potente procesador Intel Core i7 para tu PC.'
    )
    product2 = Product.objects.create(
        name='Tarjeta gráfica NVIDIA GeForce RTX 3080',
        category=category2,
        price=699.99,
        description='Tarjeta gráfica de alto rendimiento para gaming.'
    )
    product3 = Product.objects.create(
        name='Memoria RAM Corsair Vengeance RGB',
        category=category3,
        price=129.99,
        description='Módulo de memoria RAM DDR4 con iluminación RGB.'
    )
