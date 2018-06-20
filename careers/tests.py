from django.test import TestCase
from .models import Location,Application,Job

from django.core.files.uploadedfile import SimpleUploadedFile
# Create your tests


class JobTest(TestCase):

    """
    Test class that will test for a Job to make  sure its valid
    """

    image_upload = SimpleUploadedFile(name = 'test.jpg',content=open('careers/testsFolder/test.jpg',"rb").read(),content_type='image/jpg')


    def setUp(self):
        """
        Test method to setup the testing environments before tests are run
        """

        # Create test Job Locaion
        self.job_location=Location.objects.create(location_name="Kenya",country_extension="+254",location_image=self.image_upload)
        self.job_location.save()

        # Create test Job
        self.test_job=Job.objects.create(job_title='Test Job',job_description='test Job description',requirements='Test Job',responsibilities='Test Job',characteristics='Test Job',manager='james@moringaschool.com',type="Full Time",location=self.job_location)


    def tearDown(self):
        """
        Test method to destroy the testing environments before the next tests are run
        """
        Location.objects.all().delete()
        Job.objects.all().delete()


    def test_instance(self):
        """
        Test method to check instance of the Location object
        """
        stringified = self.test_job.job_title + " Job Model"
        self.assertTrue(isinstance(self.test_job,Job))
        self.assertEqual(self.test_job.__str__(),stringified)


    def test_save(self):
        self.test_job.save()
        saved_items_number = Job.objects.all()

        self.assertTrue(len(saved_items_number)==1)
        self.assertEqual(self.test_job,saved_items_number[0])


class LocationTest(TestCase):

    """
    Test class that will test for a Location to make  sure its valid
    """

    # Add test Image Upload
    image_upload = SimpleUploadedFile(name = 'test.jpg',content=open('careers/testsFolder/test.jpg',"rb").read(),content_type='image/jpeg')


    def setUp(self):
        """
        Test method to setup the testing environments before tests are run
        """

        self.job_location=Location.objects.create(location_name="Kenya",country_extension="+254",location_image=self.image_upload)


    def tearDown(self):
        """
        Test method to destroy the testing environments before the next tests are run
        """
        Location.objects.all().delete()


    def test_instance(self):
        """
        Test method to check instance of the Location object
        """
        stringified = self.job_location.location_name + " Location Model"
        self.assertTrue(isinstance(self.job_location,Location))
        self.assertEqual(self.job_location.__str__(),stringified)


    def test_save(self):
        self.job_location.save()
        saved_items_number = Location.objects.all()

        self.assertTrue(len(saved_items_number)==1)
        self.assertEqual(self.job_location,saved_items_number[0])



class ApplicationTest(TestCase):

    """
    Test class that will test for a user application o make  sure its valid
    """

    image_upload = SimpleUploadedFile(name = 'test.jpg',content=open('careers/testsFolder/test.jpg',"rb").read(),content_type='image/jpeg')


    def setUp(self):
        """
        Test method to setup the testing environments before tests are run
        """

        # Create test Job Locaion
        self.job_location=Location.objects.create(location_name="Kenya",country_extension="+254",location_image=self.image_upload)

        self.job_location.save()

        # Create test Job
        self.test_job=Job.objects.create(job_title='Test Job',job_description='test Job description',requirements='Test Job',responsibilities='Test Job',characteristics='Test Job',manager='james@moringaschool.com',type="Full Time",location=self.job_location)

        self.test_job.save()

        # Create test Application
        self.test_application = Application.objects.create(firstname='James',lastname='Muriuki',email='james@moringaschool.com',gender='Male',passport_photo=self.image_upload,phone_number='234567833',programming_languages='kmdedkmkmd',curriculum_vitae='https://realpython.com/testing-in-django-part-1-best-practices-and-examples/',cover_letter='https://realpython.com/testing-in-django-part-1-best-practices-and-examples/',job=self.test_job)



    def tearDown(self):
        """
        Test method to destroy the testing environments before the next tests are run
        """
        Location.objects.all().delete()
        Job.objects.all().delete()
        Application.objects.all().delete()

    def test_instance(self):
        """
        Test method to check instance of the Location object
        """
        stringified = self.test_application.firstname + " Application model"
        self.assertTrue(isinstance(self.test_application,Application))
        self.assertEqual(self.test_application.__str__(),stringified)


    def test_save(self):
        self.test_application.save()
        saved_items_number = Application.objects.all()

        self.assertTrue(len(saved_items_number)==1)
        self.assertEqual(self.test_application,saved_items_number[0])
