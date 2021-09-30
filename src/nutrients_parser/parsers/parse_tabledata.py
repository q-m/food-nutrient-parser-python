from ..lang import *

def parse_tabledata(data):
    """
    Parses tabular values into a nutrients structure.

    >>> data = [
    ...   ['Energy', '195 kJ', '20 kJ'],
    ...   ['Salt', '4 g', '0.4 g'],
    ... ]
    >>> parse_tabledata(data) == {
    ...   'columns': [
    ...     {
    ...       'rows': [
    ...         { 'name': 'Energy', 'amount': '195 kJ' },
    ...         { 'name': 'Salt', 'amount': '4 g' },
    ...       ]
    ...     },
    ...     {
    ...       'rows': [
    ...         { 'name': 'Energy', 'amount': '20 kJ' },
    ...         { 'name': 'Salt', 'amount': '0.4 g' },
    ...       ]
    ...     }
    ...   ]
    ... }
    True
    """
    if len(data) == 0: return { 'columns': [] }

    # Identify column with nutrient names
    nutrient_col = find_nutrient_column(data)
    if nutrient_col is None:
        print("Could not determine nutrient column")
        return

    # Gather results
    columns = {}
    for row in data:
        # skip empty rows
        if len(row) <= nutrient_col:
            continue
        # separate nutrient from values
        row_cols = row.copy()
        row_nutrient = row_cols.pop(nutrient_col)
        for i, col in enumerate(row_cols):
            if col is None or col.strip() == '': continue
            if i not in columns: columns[i] = []
            columns[i].append({ 'name': row_nutrient, 'amount': col })

    return { 'columns': list([{ 'rows': row } for row in columns.values()]) }

def find_nutrient_column(data):
    """
    Find the most probably column containing nutrient names.

    >>> data = [['Energy', '195 kJ', '20 kJ']]
    >>> find_nutrient_column(data)
    0
    >>> data = [[None, 'Energy', '195 kJ', '20 kJ']]
    >>> find_nutrient_column(data)
    1
    >>> data = [[None, 'Energy', '195 kJ Energy', '20 kJ']]
    >>> find_nutrient_column(data)
    1
    >>> data = [[None, 'Energy (kJ)', '195', '20']]
    >>> find_nutrient_column(data)
    1
    >>> data = [
    ...   [None,   'Energy (kJ)', '195'],
    ...   ['Salt', 'Salt (g)',    '195 g'],
    ...   ['',     'Salt',        '195 g salt'],
    ... ]
    >>> find_nutrient_column(data)
    1
    """
    column_scores = {}

    for row in data:
        for i, col in enumerate(row):
            if i not in column_scores: column_scores[i] = 0
            if col is None:
                pass
            elif nutrient_names_re.fullmatch(col):
                # exact match is one point
                column_scores[i] += 1
            elif nutrient_names_re.search(col):
                # else if string contains a nutrient a bit less
                column_scores[i] += 0.4

    columns = list(column_scores.items())
    columns.sort(key=lambda a: a[1], reverse=True)
    if len(columns) > 0:
        return columns[0][0]
    else:
        return None