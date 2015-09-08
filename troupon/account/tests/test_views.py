
from django.test import TestCase, Client
from django.core.urlresolvers import resolve
from django.contrib.auth.models import User
from django.utils.datastructures import MultiValueDictKeyError



class UserSignInViewTestCase(TestCase):
    """Test that post and get requests to signin routes is successful
    """

    def setUp(self):
        self.client = Client()
        self.user = User(username='johndoe@gmail.com')
        self.user.set_password('12345')
        self.user.save()

    def test_view_get_auth_signin(self):
        """Test that user request for signin page binds to a view called
            the class name `UserSigninView`.
        """

        response = resolve('/account/signin/')
        self.assertEquals(response.func.__name__, 'UserSigninView')

    def test_view_post_auth_signin(self):
        """Test that user post to signin route has a session
        """
        data = {'email': 'johndoe@gmail.com', 'password': '12345'}
        response = self.client.post('/account/signin/', data)
        self.assertIn('deals', response.content)


class ForgotPasswordViewTestCase(TestCase):
    
    def setUp(self):
        # create a test client:
        self.client = Client()
        # register a sample user:
        self.user = User (
            username = 'JohnDoe', 
            email = 'johndoe@somedomain.com',
            first_name = 'John',
            last_name = 'Doe'
        )
        self.user.set_password('notsosecret12345')
        self.user.save()

    def test_recovery_email_sent_for_registered_user(self):
        response = self.client.post('/account/recovery/', {"email": self.user.email})
        self.assertIn('registered_user', response.context)
        self.assertIn('recovery_mail_status', response.context)
        self.assertIsInstance(response.context['recovery_mail_status'], int)

    def test_recovery_email_not_sent_for_unregistered_user(self):
        response = self.client.post('/account/recovery/', {"email":"unregistereduser@somedomain.com" })
        self.assertNotIn('registered_user', response.context)
        self.assertNotIn('recovery_mail_status', response.context)
# -*- coding: utf-8 -*-

