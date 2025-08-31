# posts/tests.py
from django.test import TestCase
from django.urls import reverse
from .models import Post, Author


class PostModelTest(TestCase):
    def setUp(self):
        self.author = Author.objects.create(name="Test Author")
        self.post = Post.objects.create(
            title="Test Post",
            content="This is a test post.",
            author=self.author,
        )

    def test_post_has_title(self):
        self.assertEqual(self.post.title, "Test Post")

    def test_post_has_content(self):
        self.assertEqual(self.post.content, "This is a test post.")

    def test_post_has_author(self):
        self.assertEqual(self.post.author.name, "Test Author")

    def test_post_str(self):
        self.assertEqual(str(self.post), "Test Post by Test Author")


class PostViewTest(TestCase):
    def setUp(self):
        self.author = Author.objects.create(name="Test Author")
        self.post = Post.objects.create(
            title="Test Post",
            content="This is a test post.",
            author=self.author,
        )

    def test_post_list_view(self):
        response = self.client.get(reverse("post_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Post")
        self.assertContains(response, "Test Author")

    def test_post_detail_view(self):
        response = self.client.get(reverse("post_detail", args=[self.post.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Post")
        self.assertContains(response, "This is a test post.")
        self.assertContains(response, "Test Author")

    def test_post_create_view(self):
        response = self.client.post(
            reverse("post_create"),
            {"title": "New Post", "content": "New content",
                "author_name": "New Author"},
        )
        self.assertEqual(response.status_code, 302)  # Redirect after creation
        new_post = Post.objects.get(title="New Post")
        self.assertEqual(new_post.author.name, "New Author")
        self.assertEqual(new_post.content, "New content")

    def test_post_update_view(self):
        response = self.client.post(
            reverse("post_update", args=[self.post.pk]),
            {"title": "Updated Post", "content": "Updated content",
                "author_name": "Test Author"},
        )
        self.assertEqual(response.status_code, 302)  # Redirect after update
        updated_post = Post.objects.get(pk=self.post.pk)
        self.assertEqual(updated_post.title, "Updated Post")
        self.assertEqual(updated_post.content, "Updated content")
        self.assertEqual(updated_post.author.name, "Test Author")

    def test_post_delete_view(self):
        response = self.client.post(
            reverse("post_delete", args=[self.post.pk]))
        self.assertEqual(response.status_code, 302)  # Redirect after deletion
        with self.assertRaises(Post.DoesNotExist):
            Post.objects.get(pk=self.post.pk)
