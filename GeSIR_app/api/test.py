import random
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from api.models import Proveedor

def create_random_proveedor(num_proveedores):
    proveedor_list = []
    for i in range(num_proveedores):
        proveedor = Proveedor.objects.create(
            clave = random.randint(1,100),
            nombre = f"name{random.randint(1, 1000)}",
            estado = f"name{random.randint(1, 1000)}",
            estatus = True
        )
        proveedor_list.append(proveedor)
    return proveedor_list

class ProveedorListTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        num_Proveedor = 5
        self.proveedor_list = create_random_proveedor(num_Proveedor)
    
    def test_proveedor_list(self):
        url = reverse('all-proveedor-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)
        proveedor_expected_list = self.proveedor_list
        proveedor_list_result = response.data
        self.assertEqual(len(proveedor_list_result), len(proveedor_expected_list))
        
        for i in range(len(proveedor_expected_list)):
            proveedor_exp = proveedor_expected_list[i]
            proveedor_res = proveedor_list_result[i]
            
            self.assertEqual(proveedor_exp.clave, proveedor_res['clave'])
            self.assertEqual(proveedor_exp.nombre, proveedor_res['nombre'])
            self.assertEqual(proveedor_exp.estado, proveedor_res['estado'])
            self.assertEqual(proveedor_exp.estatus, proveedor_res['estatus'])
        