from ..lang import nutrients, units, numeric_values_re
from ..lang.util import gre

def split_energy(nutrients):
    """
    Splits energy nutrients from parsed nutrients, when kJ and kcal
    appear in a single row.

    >>> nutrients = {'columns': [{'rows': [
    ...   { 'name': 'Energy', 'amount': '10kJ 20kcal' }
    ... ]}]}
    >>> split_energy(nutrients)['columns'][0]['rows']
    [{'name': 'Energy', 'amount': '10kJ'}, {'name': 'Energy', 'amount': '20kcal'}]
    """
    if not nutrients: return

    # for each column
    for col in nutrients['columns']:
        # for each row in the column
        rows = col['rows']
        for i, row in enumerate(rows):
            # replace the value with the normalized values
            nrow = split_energy_row(row)
            if nrow is None:
                # no result
                pass
            elif len(nrow) == 1:
                # single replacement
                rows[i] = nrow
            else:
                # replace row with multiple returned items
                col['rows'] = rows[:i] + nrow + rows[i+1:]

    return nutrients

def split_energy_row(row):
    """
    Normalizes a single nutrient row.
    Returns nothing if no change is necessary, returns replacing rows if there is.

    >>> split_energy_row({ 'name': 'Energy', 'amount': '10kJ 100kcal' })
    [{'name': 'Energy', 'amount': '10kJ'}, {'name': 'Energy', 'amount': '100kcal'}]
    >>> split_energy_row({ 'name': 'Energy', 'amount': 'kJ 10 / kcal 100' })
    [{'name': 'Energy', 'amount': '10 kJ'}, {'name': 'Energy', 'amount': '100 kcal'}]
    >>> split_energy_row({ 'name': 'Energy', 'amount': '10kJ' })
    >>> split_energy_row({ 'name': 'Sugar', 'amount': '10kJ 100kcal' })
    """
    if row is None or row['name'] is None: return
    if not nutrients['Energy'].search(row['name']): return

    m_kJ, m_kcal = split_amounts_a(row['amount'])
    if m_kcal is None or m_kJ is None:
        m_kJ , m_kcal = split_amounts_b(row['amount'])
    if m_kcal is None or m_kJ is None:
        return

    r_kcal = row.copy()
    r_kcal['amount'] = m_kcal
    r_kJ = row.copy()
    r_kJ['amount'] = m_kJ

    # TODO keep original order
    return [r_kJ, r_kcal]

def split_amounts_a(amount):
    re_kcal = gre( r'(' + numeric_values_re.pattern + r')\s*(' + units['kcal'].pattern + r')')
    m_kcal = re_kcal.search(amount)
    if m_kcal is None: return [None, None]
    re_kJ = gre( r'(' + numeric_values_re.pattern + r')\s*(' + units['kJ'].pattern + r')' )
    m_kJ = re_kJ.search(amount)
    if m_kJ is None: return [None, None]

    return [m_kJ.group(0), m_kcal.group(0)]

def split_amounts_b(amount):
    re_kcal = gre( r'(' + units['kcal'].pattern + r')\s*(' + numeric_values_re.pattern + r')')
    m_kcal = re_kcal.search(amount)
    if m_kcal is None: return [None, None]
    re_kJ = gre( r'(' + units['kJ'].pattern + r')\s*(' + numeric_values_re.pattern + r')' )
    m_kJ = re_kJ.search(amount)
    if m_kJ is None: return [None, None]

    return [m_kJ.group(6) + ' ' + m_kJ.group(1), m_kcal.group(6) + ' ' + m_kcal.group(1)]
