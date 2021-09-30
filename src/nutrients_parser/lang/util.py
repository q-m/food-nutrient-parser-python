import re

def gresb(s):
    return re.compile(r'\s*\b(' + s + r')(\b|$)\s*', flags=re.IGNORECASE|re.VERBOSE)

def gres(s):
    return re.compile(r'\s*' + s + r'\s*', flags=re.IGNORECASE|re.VERBOSE)

def gre(s):
    return re.compile(s, flags=re.IGNORECASE|re.VERBOSE)

def join_gres(res):
    return gre('|'.join(['(' + r.pattern + ')' for r in res]))

def join_gre_dicts(dicts):
    result = dict()
    # gather all gres
    for d in dicts:
        for key, regex in d.items():
            if key not in result:
                result[key] = [regex]
            else:
                result[key].append(regex)
    # then combine them
    for key, regexes in result.items():
        result[key] = join_gres(regexes)
    return result

def vitamin_gre(vitamin_re, aliases=[]):
    '''
    Greates a regular expression for a vitamin, optionally combined with aliases.

    >>> import re
    >>> vitamin_gre(re.compile('foo\\\\.?')).pattern
    'foo\\\\.?'
    >>> r = vitamin_gre(re.compile(r'Vit(\\.|amin)\\s+X'), ['Foo', 'Bar'])
    >>> [nutrient for nutrient in [
    ...   "Vit. X",
    ...   "Vitamin X",
    ...   "Foo",
    ...   "Bar",
    ...   "Vitamin X / Foo",
    ...   "Vitamin X / Bar",
    ...   "Vitamin X / Foo / Bar",
    ...   "Vitamin X / Bar / Foo",
    ...   "Bar / Vitamin X / Foo",
    ...   "Foo / Bar / Vitamin X",
    ...   "Foo / Vitamin X",
    ...   "Vitamin X (Foo)",
    ...   "Vitamin X (Bar)",
    ...   "Vitamin X ( Bar )",
    ...   "Bar (Foo)",
    ...   "Bar (Vitamin X)",
    ...   "Bar (Vitamin X+Foo)",
    ...   "Bar (Vitamin X + Foo)",
    ...   "Bar (Vit. X + Foo)",
    ... ] if not r.fullmatch(nutrient)]
    []
    '''
    if len(aliases) == 0:
        return vitamin_re

    names = [vitamin_re.pattern] + aliases
    n = '(' + '|'.join(names) + ')'

    return gresb(''.join([
        n,
        r'(\s*[/]\s*' + n + r')*',
        r'(\s*\(\s*' + n + r'(\s*[+]\s*' + n + r')*\s*\))?'
    ]))