class Quantity:
  """Enum representing a quantity (either laundry or powder)."""
  SMALL = "malo"
  MEDIUM = "srednje"
  LARGE = "puno"


class Level:
  """Enum representing a level or a custom degree (i.e. level of dirt)."""
  LOW = "malo"
  HIGH = "puno"


def fuzzify_laundry(value):
  """Encodes the laundry weight to it's fuzzy description."""
  if value < 3.0:
    return Quantity.SMALL
  elif value >= 3.0 and value < 5.0:
    return Quantity.MEDIUM
  else:
    return Quantity.LARGE


def fuzzify_dirty(value):
  """Encodes the dirt level to it's fuzzy description."""
  if value < 5.0:
    return Level.LOW
  else:
    return Level.HIGH


def defuzzify(value):
  """Decodes the powder amount fuzzy description to weight in grams."""
  if value == Quantity.SMALL:
    return 30.0
  elif value == Quantity.MEDIUM:
    return 90.0
  else:
    return 150.0

