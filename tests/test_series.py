from math_series.series import fibonacci
from math_series.series import lucas
from math_series.series import sum_series

def test_import():
  assert fibonacci

def test_fibonacci8():
  actual = fibonacci(8)
  expected = 21
  assert actual == expected

def test_fibonacci9():
  actual = fibonacci(9)
  expected = 34
  assert actual == expected

def test_lucas6():
  actual = lucas(6)
  expected = 18
  assert actual == expected

def test_lucas7():
  actual = lucas(7)
  expected = 29
  assert actual == expected

def test_sum_series5():
  assert sum_series(5) == fibonacci(5)

def test_sum_series7():
  actual = sum_series(2,2,1)
  expected = 3
  assert actual == expected

def test_sum_series9():
  actual = sum_series(5,2,1)
  expected = 11
  assert actual == expected
  
