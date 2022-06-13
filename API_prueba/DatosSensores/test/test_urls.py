from django.test import SimpleTestCase
from django.urls import reverse, resolve
from DatosSensores.views import 

class TestUrls(SimpleTestCase):

    #Esto se repite con cada uno de los URL
    def test_advice_url_is_resolved(self):
            url = reverse('advice')
#            self.assertEquals(resolve(url).func, aqui va el view de advice )
