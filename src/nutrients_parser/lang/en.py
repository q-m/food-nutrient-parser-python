# English language matchers
from .util import *

nutrient_headings_re = gre(r'''
    nutritions? |
    nutrition(al) \s+ values? |
    nutrition(al)? \s* :? \s* tablet?
''')

vitamin_re_fn = lambda s: gresb(r'vit(\.|amin)\s+' + s)

nutrients = {
    'Energy': gresb(r'energ(y|etic) \s* (values?)? | calories'),
    'Protein': gresb(r'proteins?'), 
    'Sugar': gresb(r'sugars?'),
    'Fat':             gresb(r'fats?|fatty\s+acids?'),
    'Fat saturated':   gresb(r'(fats?\s+)?saturate[sd]|fatty\s+acids?\s+saturated'),
    'Fat unsaturated': gresb(r'(fats?\s+)?unsaturate[sd]|fatty\s+acids?\s+unsaturated'),
    'Fat trans':       gresb(r'(fats?\s+)trans|trans\s+(fats?)|fatty\s+acids?\s+(double\s+)?trans'),
    'Carbohydrate': gresb(r'carbo[- ]?hydrates?'),
    'Biotin':      vitamin_gre(vitamin_re_fn(r'H|B8'), ['biotin']),
    'Vitamin A':   vitamin_gre(vitamin_re_fn('A')),
    'Vitamin B':   vitamin_gre(vitamin_re_fn('B')),
    'Vitamin B1':  vitamin_gre(vitamin_re_fn('B1')),
    'Vitamin B2':  vitamin_gre(vitamin_re_fn('B2')),
    'Vitamin B3':  vitamin_gre(vitamin_re_fn('B3')),
    'Vitamin B4':  vitamin_gre(vitamin_re_fn('B4')),
    'Vitamin B5':  vitamin_gre(vitamin_re_fn('B5')),
    'Vitamin B6':  vitamin_gre(vitamin_re_fn('B6')),
    'Vitamin B11': vitamin_gre(vitamin_re_fn('B11')),
    'Vitamin B12': vitamin_gre(vitamin_re_fn('B12')),
    'Vitamin C':   vitamin_gre(vitamin_re_fn('C')),
    'Vitamin D':   vitamin_gre(vitamin_re_fn('D')),
}

nutrient_names_re = join_gres(nutrients.values())

units = {
    'kcal': gre(r'kcal | kilo(-|\s+)?calories?'),
    'kJ': gre(r'kJ | kilo(-|\s+)?joules?'),
    'µg': gre(r'µg | microgr(am)?s? '),
    'mg': gre(r'mg | mgr | milligr(am)?s? '),
    'g': gre(r'g | gr | gram | grams'),
    'kg': gre(r'kg | kilo | kilogram'),
    'ml': gre(r'ml | milliliter'),
    'l': gre(r'l(iter)?'),
}

units_re = join_gres(units.values())
numeric_values_re = re.compile(r' (?<![0-9,.]) ( \d+ | [.,]\d+ | \d+[.,]\d+ ) (?![0-9,.])', flags=re.VERBOSE)