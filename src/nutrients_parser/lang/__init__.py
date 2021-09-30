from .util import join_gres, join_gre_dicts
from . import en
from . import nl

# TODO allow choosing the languages you want to include

nutrient_headings_re = join_gres([en.nutrient_headings_re, nl.nutrient_headings_re])

nutrients = join_gre_dicts([en.nutrients, nl.nutrients])
nutrient_names_re = join_gres([en.nutrient_names_re, nl.nutrient_names_re])

units = join_gre_dicts([en.units, nl.units])
units_re = join_gres([en.units_re, nl.units_re])
numeric_values_re = join_gres([en.numeric_values_re, nl.numeric_values_re])