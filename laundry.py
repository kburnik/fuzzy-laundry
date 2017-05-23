#!/usr/bin/env python
from ranges import *
import json


def compute_fuzzy_powder_amount(laundry_amount_fuzzy, dirt_level_fuzzy):
  """Computes the fuzzy output (powder amount) based on the fuzzy input params
     (laundry amount and dirt level)."""

  expert_rule_map = {
     (Quantity.SMALL, Level.LOW): Quantity.SMALL,
     (Quantity.MEDIUM, Level.LOW): Quantity.MEDIUM,
     (Quantity.LARGE, Level.LOW): Quantity.MEDIUM,
     (Quantity.SMALL, Level.HIGH): Quantity.MEDIUM,
     (Quantity.MEDIUM, Level.HIGH): Quantity.LARGE,
     (Quantity.LARGE, Level.HIGH): Quantity.LARGE}
  """Maps the expert rules as:
     (laundry_amount_fuzzy, dirt_level_fuzzy) -> powder_amount_fuzzy"""

  fuzzy_input_parameters = (laundry_amount_fuzzy, dirt_level_fuzzy)
  fuzzy_output = expert_rule_map.get(fuzzy_input_parameters, None)

  if fuzzy_output is None:
    raise Exception(
        "Case not covered for (laundry_amount = %s, dirt_level = %s)" %
        (laundry_amount_fuzzy, dirt_level_fuzzy))
  else:
    return fuzzy_output


def compute_washing_parameters(laundry_weight_kg, dirt_level):
  """Computes required washing parameters based on provided sensor and user
     input (all inputs are numerical values)."""
  if laundry_weight_kg < 0.0 or laundry_weight_kg > 8.0:
    raise Exception("Invalid value for laundry weight: %lf" % laundry_weight_kg)

  if dirt_level < 1.0 or dirt_level > 10.0:
    raise Exception("Invalid value for dirt level: %lf" % dirt_level)

  # Encode numerical to fuzzy.
  laundry_amount_fuzzy = fuzzify_laundry(laundry_weight_kg)
  dirt_level_fuzzy = fuzzify_dirty(dirt_level)

  # Apply the expert rules.
  powder_amount_fuzzy = compute_fuzzy_powder_amount(laundry_amount_fuzzy,
                                                    dirt_level_fuzzy)

  # Decode the fuzzy result to numerical amount.
  powder_amount_grams = defuzzify(powder_amount_fuzzy)

  return {"powder_amount_grams": powder_amount_grams}


if __name__ == "__main__":
  laundry_weight_kg = float(raw_input("Laundry weight (kg) [0-8]: "))
  dirt_level = float(raw_input("Dirt level [1-10]: "))
  washing_parameters = compute_washing_parameters(laundry_weight_kg, dirt_level)
  print json.dumps(washing_parameters, indent=2)
