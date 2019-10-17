import unittest

from geometry import Vector2

class TestVector2Arithmetic(unittest.TestCase):
    def setUp(self):
        self.v1 = Vector2(3, 4)
        self.v2 = Vector2(5, 6)

    def test_add(self):
        v3 = self.v1 + self.v2
        self.assertEqual(v3, Vector2(8, 10))

    def test_sub(self):
        v3 = self.v2 - self.v1
        self.assertEqual(v3, Vector2(2, 2))

    def test_mul(self):
        u = self.v1 * 3
        self.assertEqual(u, Vector2(9, 15))


'''
class TestVector2Conversions(unittest.TestCase):
    def test_from_angle(self):
        v = Vector2.from_angle(0)
        self.assertEqual(v, Vector2(1, 0))

    def test_magnitude(self):
        v = Vector2(1, 0)
        m = v.magnitude()
        self.assertEqual(m, 1)

    def test_direction(self):
        v = Vector2(1, 0)
        d = v.direction()
        self.assertEqual(d, 0)

    def test_normalized(self):
        v = Vector2(2, 0)
        n = v.normalized()
        self.assertEqual(n, Vector2(1, 0))
'''


if __name__ == '__main__':
    unittest.main()

