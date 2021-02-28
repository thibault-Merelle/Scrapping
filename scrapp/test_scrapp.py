import unittest
from scrapp import scrapp_VR

    #### test vintage ride #####

class TestVR(unittest.TestCase):

    def test_setup_VR(self):
        myclass = scrapp_VR()
        myclass.page
        self.assertEqual(myclass.page.status_code == 200)
