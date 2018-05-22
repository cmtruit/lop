# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test.client import Client
from django.test import TestCase
import unittest


class ApiTestCase(unittest.TestCase):
    def setUp(self):
        self.client = Client()
    def testApiPage(self):
        response = self.client.get('/api/')
        self.assertEqual(response.status_code, 200)
