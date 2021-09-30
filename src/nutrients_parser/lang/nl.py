# Dutch language matchers
from .util import *

nutrient_headings_re = gre(r'''
    voedingswaarden? |
    nutri[eë]nt(en)? \s* (tabel)?
''')

vitamin_re_fn = lambda s: gresb(r'vit(\.|amine)\s+' + s)

nutr_of_which = r'(waarvan\s+|)'

nutrients = {
    'Energy':  gresb(r'energ(y|[inr]e|etis(ch)?e) \s* (waarden?)? | calorie[eë]n'),
    'Protein': gresb(r'( e[ir]w[ir]t(ten)? | prote[iï]n(en)? )'), 
    'Sugar':   gresb(nutr_of_which + r'suikers?'),
    'Fat':             gresb(r'vet(gehalte|ten|stoffen)?'),
    'Fat saturated':   gresb(nutr_of_which + r'verzadigde?(\s+vet(ten)?)?|vet(ten)?\s+verzadigde?'),
    'Fat unsaturated': gresb(nutr_of_which + r'onverzadigde?(\s+vet(ten)?)?|vet(ten)?\s+onverzadigde?'),
    'Fat trans':       gresb(nutr_of_which + r'trans\s+vet(ten)?|vet(ten)?\s+trans'),
    'Carbohydrate': gresb(r'koolhydraat | koolhydraten | glucide[sn]'),
    'Biotin':      vitamin_gre(vitamin_re_fn(r'H|B8'), ['biotine']),
    'Vitamin A':   vitamin_gre(vitamin_re_fn('A'), ['retinol', r'carot(\.|een)']),
    'Vitamin B':   vitamin_gre(vitamin_re_fn('B')),
    'Vitamin B1':  vitamin_gre(vitamin_re_fn('B1')),
    'Vitamin B2':  vitamin_gre(vitamin_re_fn('B2')),
    'Vitamin B3':  vitamin_gre(vitamin_re_fn('B3')),
    'Vitamin B4':  vitamin_gre(vitamin_re_fn('B4')),
    'Vitamin B5':  vitamin_gre(vitamin_re_fn('B5')),
    'Vitamin B6':  vitamin_gre(vitamin_re_fn('B6')),
    'Vitamin B11': vitamin_gre(vitamin_re_fn('B11'), ['foliumzuur']),
    'Vitamin B12': vitamin_gre(vitamin_re_fn('B12')),
    'Vitamin C':   vitamin_gre(vitamin_re_fn('C')),
    'Vitamin D':   vitamin_gre(vitamin_re_fn('D')),
}

nutrient_names_re = join_gres(nutrients.values())

units = {
    'kcal': gre(r'kcal | kilo(-|\s+)?calori[eë]n?'),
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
