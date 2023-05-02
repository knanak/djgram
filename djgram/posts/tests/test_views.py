from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth import get_user_model

class TestPosts(TestCase):
    def setUp(self):
        User=get_user_model()
        self.user=User.objects.create_user(
            username='nana', email='nana@nana.com', password="123"
        )

    def test_get_posts(self):
        url=reverse('posts:post_create')
        response=self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'posts/create.html')

    
    def test_post_posts(self):
        login=self.client.login(username='nana', password='123')
        self.assertTrue(login)

        url=reverse('posts:post_create') 
        image = SimpleUploadedFile('test.jpg', b'sth')      
        response=self.client.post(url, {"image":image, "caption": "test"})

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "posts/base.html")


    def test_post_posts_notLogin(self):
        
        url=reverse('users:post_create')
        image = SimpleUploadedFile('test.jpg', b'sth')      
        response=self.client.post(url, {"image":image, "caption": "test"})

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "users/main.html")