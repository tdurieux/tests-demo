from ..find import find

def test_find():
  print(find(([29, 28, 27, 26])))

def test_decreasing_order():
  min, max = find([29, 28, 27, 26])
  assert min == 26
  assert max == 29
  
def test_any_random_numbers():
  min, max = find([29, 37, 4, 5])
  assert min == 4
  assert max == 37


def test_increasing_order():
  min, max = find([26, 27, 28, 29])
  assert min == 26
  assert max == 29

def test_empty_numbers():
  min, max = find([])
  assert min is None
  assert max is None
