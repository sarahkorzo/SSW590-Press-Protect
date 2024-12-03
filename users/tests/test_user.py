from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

class UserTestCase(TestCase):
    def setUp(self):
        # Create users with different roles
        User = get_user_model()

        # Admin user
        self.admin_user = User.objects.create_superuser(
            username='adminuser', email='admin@example.com', password='adminpassword'
        )

        # Editor user
        self.editor_user = User.objects.create_user(
            username='editoruser', email='editor@example.com', password='editorpassword'
        )
        self.editor_user.is_editor = True
        self.editor_user.save()

        # Marketer user
        self.marketer_user = User.objects.create_user(
            username='marketeruser', email='marketer@example.com', password='marketerpassword'
        )
        self.marketer_user.is_marketer = True
        self.marketer_user.save()

        # Viewer user
        self.viewer_user = User.objects.create_user(
            username='vieweruser', email='viewer@example.com', password='viewerpassword'
        )
        self.viewer_user.is_viewer = True
        self.viewer_user.save()

        # URLs for testing
        self.admin_dashboard_url = reverse('admin-dashboard')  # Updated
        self.editor_dashboard_url = reverse('editor-dashboard')  # Updated
        self.marketer_dashboard_url = reverse('marketer-dashboard')  # Updated
        self.viewer_dashboard_url = reverse('viewer-dashboard')  # Updated
        self.article_list_url = reverse('article_list')
        self.article_details_url = reverse('article_detail', kwargs={'article_id': 1})  # Updated

    def test_admin_access(self):
        # Log in as admin and check access to the admin dashboard
        self.client.login(username='adminuser', password='adminpassword')
        response = self.client.get(self.admin_dashboard_url)
        self.assertEqual(response.status_code, 200)

    def test_editor_access(self):
        # Log in as editor and check access to the editor dashboard
        self.client.login(username='editoruser', password='editorpassword')
        response = self.client.get(self.editor_dashboard_url)
        self.assertEqual(response.status_code, 200)

    def test_marketer_access(self):
        # Log in as marketer and check access to marketer dashboard
        self.client.login(username='marketeruser', password='marketerpassword')
        response = self.client.get(self.marketer_dashboard_url)
        self.assertEqual(response.status_code, 200)

    def test_viewer_access(self):
        # Log in as viewer and check access to article list
        self.client.login(username='vieweruser', password='viewerpassword')
        response = self.client.get(self.article_list_url)
        self.assertEqual(response.status_code, 200)

    def test_article_details(self):
        # Log in as viewer and check access to article details
        self.client.login(username='vieweruser', password='viewerpassword')
        response = self.client.get(self.article_details_url)
        self.assertEqual(response.status_code, 200)
