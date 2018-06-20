from django.test import TestCase
from ..models import Location,Application,Job

from django.core.files.uploadedfile import SimpleUploadedFile
# Create your tests

class ApplicationTest(TestCase):

    """
    Test class that will test for a user application o make  sure its valid
    """
