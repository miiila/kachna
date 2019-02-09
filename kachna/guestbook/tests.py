from django.test import TestCase
from django.test import Client
from django.urls import reverse
from .models import Post

client = Client()

class QuestionIndexViewTests(TestCase):
    def test_no_posts(self):
        response = self.client.get(reverse('guestbook:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Ještě nikdo nic nenapsal.")
        self.assertEqual(len(response.context['posts']), 0)

    def test_new_post(self):
        Post.objects.create(
            author_name='test', author_email='test@test.test', text='Testovací post')
        response = self.client.get(reverse('guestbook:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Testovací post")
        self.assertEqual(len(response.context['posts']), 1)

