from django.apps import apps
from django.contrib.staticfiles import finders
from django.test import SimpleTestCase
from django.urls import reverse


class HomePageTests(SimpleTestCase):

    def test_homepage_status_code(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_homepage_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home.html')

    def test_homepage_content(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, 'Welcome to Our Platform')

    def test_homepage_modules(self):
        response = self.client.get(reverse('home'))

        modules = [
            'Accounts',
            'Nutrition',
            'Fitness',
            'AI Assistant',
            'Analytics',
        ]

        for module in modules:
            with self.subTest(module=module):
                self.assertContains(response, module)


class ProjectConfigurationTests(SimpleTestCase):

    def test_project_apps_registered(self):
        project_apps = [
            'accounts',
            'nutrition',
            'fitness',
            'ai_agent',
            'analytics',
        ]

        for app in project_apps:
            with self.subTest(app=app):
                self.assertTrue(apps.is_installed(app))

    def test_static_css_exists(self):
        self.assertIsNotNone(
            finders.find('css/style.css')
        )