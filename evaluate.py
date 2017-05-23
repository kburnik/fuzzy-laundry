#!/usr/bin/env python
from laundry import compute_washing_parameters

"""Runs the washing machine fuzzy logic for all possible inputs with a
   resolution of 0.5. The ouput columns are the inputs and the computed
   output."""

def frange(x, y, step):
  while x <= y:
    yield x
    x += step

for laundry_weight_kg in frange(0.0, 8.0, 0.5):
  for dirt_level in frange(1.0, 10.0, 0.5):
    washing_params = compute_washing_parameters(laundry_weight_kg, dirt_level)
    powder_amount_grams = washing_params["powder_amount_grams"]
    print laundry_weight_kg, dirt_level, powder_amount_grams
