from django.test import TestCase
# Create your tests here. Maybe functional tests
from libs.hello_world import hello_world


class LibTestCase(TestCase):
    def setUp(self):
        self.lib_hello_world_fun = hello_world
    
    def test_lib_hello_world(self):
        res = self.lib_hello_world_fun()
        self.assertEqual(res, 'hello-world')
