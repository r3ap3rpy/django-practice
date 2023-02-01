from django.test import TestCase
from django.urls import reverse
# Create your tests here.
from django.test import TestCase

# Create your tests here.

class DemoTest(TestCase):
    def test_ping_get(self):
        response = self.client.get("/ping/")
        self.assertEqual(response.status_code,200)
        self.assertEqual(
            response.content.decode("utf8"), "pong"
        )

    def test_ping_head(self):
        response = self.client.get("/ping/")
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.content,b"pong")
        self.assertGreater(int(response["Content-Length"]),0)
    
    def test_ping_options(self):
        response = self.client.options("/ping/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(int(response["Content-Length"]),0)

        for method in ["GET","HEAD","OPTIONS"]:
            with self.subTest(method=method):
                self.assertIn(method, response["Allow"],f"{method} not in ALLOW header")

    def test_ping_method_not_allowed(self):
        not_allowed = ["post","put","patch","delete","trace"]
        for method in not_allowed:
            with self.subTest(method = method):
                call_method=getattr(self.client,method)
                response = call_method("/ping/")
                self.assertEqual(response.status_code, 405)

    def test_status_get(self):
        url = reverse("site_status")
        self.assertEqual(url,"/status/")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        #self.assertTemplateUsed(response,"base.html")
        #self.assertTemplateUsed(
        #    response, "testapp/base.html"
        #)
        ##self.assertTemplateUsed(
        ##    response,"testapp/status.html"
        ##)
        self.assertIn("status",response.context)
        self.assertEqual(response.context["status"],"Good")
        ##self.assertInHTML(
        ##    "<p>Status is Good</p>",
        ##    response.content.decode("utf8")
        ##)
        templates = [
            "base.html",
            "testapp/base.html",
            "testapp/status.html"
        ]
        for t_name in templates:
            with self.subTest(template=t_name):
                self.assertTemplateUsed(response, t_name)
        