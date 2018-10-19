#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from ...models.xxx_model import XXXModel


class XXXModelTestCase(unittest.TestCase):
    def setUp(self):
        self._xxx_model_instance = XXXModel()

    def test_hello(self):
        name = 'Leo'
        expected_result = 'Hello, Leo!'

        result = self._xxx_model_instance.hello(name)
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()
