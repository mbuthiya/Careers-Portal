from django.test import TestCase
from ..models import Location,Application,Job

from django.core.files.uploadedfile import SimpleUploadedFile
# Create your tests
# get image upload




class JobTest(TestCase):

    """
    Test class that will test for a Job to make  sure its valid
    """

    def setUp(self):
        """
        Test method to setup the testing environments before tests are run
        """
        image_upload = SimpleUploadedFile(name = 'test.JPG',content=open('test.JPG',"rb").read(),content_type='image/jpeg')


    def tearDown(self):
        """
        Test method to destroy the testing environments before the next tests are run
        """



class LocationTest(TestCase):

    """
    Test class that will test for a Location to make  sure its valid
    """

    def setUp(self):
        """
        Test method to setup the testing environments before tests are run
        """
        image_upload = SimpleUploadedFile(name = 'test.JPG',content=open('test.JPG',"rb").read(),content_type='image/jpeg')


    def tearDown(self):
        """
        Test method to destroy the testing environments before the next tests are run
        """



class ApplicationTest(TestCase):

    """
    Test class that will test for a user application o make  sure its valid
    """

    def setUp(self):
        """
        Test method to setup the testing environments before tests are run
        """
        image_upload = SimpleUploadedFile(name = 'test.JPG',content=open('test.JPG',"rb").read(),content_type='image/jpeg')


    def tearDown(self):
        """
        Test method to destroy the testing environments before the next tests are run
        """
