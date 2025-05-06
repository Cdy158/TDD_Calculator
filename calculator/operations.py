def test_add(self):
    self.assertEqual(add(2, 3), 5)
    self.assertEqual(add(-1, 1), 0)
    self.assertEqual(add(0, 0), 0)

def add(a, b):
    return a + b

def test_subtract(self):
    self.assertEqual(subtract(5, 3), 2)
    self.assertEqual(subtract(3, 5), -2)
    self.assertEqual(subtract(0, 0), 0)
  
def subtract(a, b):
    return a - b

def test_multiply(self):
    self.assertEqual(multiply(2, 3), 6)
    self.assertEqual(multiply(-1, 5), -5)
    self.assertEqual(multiply(0, 100), 0)

def multiply(a, b):
    return a * b

def test_divide(self):
    self.assertEqual(divide(6, 3), 2)
    self.assertEqual(divide(5, 2), 2.5)
    with self.assertRaises(ZeroDivisionError):
        divide(10, 0)

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


