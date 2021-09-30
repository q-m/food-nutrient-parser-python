# Nutrients parser

A Python package to parse nutrient declarations into structured data. At this
moment it works with HTML pages and a number of JSON formats. The idea is that
you can give any piece of data, from whatever source, and this package will do
its best to find nutritional information, returning it in a structured form.

_Under development, work in progress, does not fully work yet._

## Install

TODO

## Use

### HTML

```python
from nutrients_parser import parse_html

html = """
  <table>
    <tr><th></th><th>per 100g</th><th>per portion</th></tr>
    <tr><td>Energy</td><td>195 kJ</td><td>20 kJ</td></tr>
    <tr><td>Energy</td><td>47 kcal</td><td>5 kcal</td></tr>
    <tr><td>Sugar</td><td>5 gram</td><td>0,5 gr</td></tr>
    <tr><td>Salt</td><td>2.0 g</td><td>0.2 g</td></tr>
  </table>
"""

print(parse_html(html))
```

```
{
  columns: [
    {
      per: { name: "100g", value: 100, unit: "g", text: "per 100g" },
      prepared: None,
      rows: [
        { name: "Energy", amount: { value: 195,   unit: "kJ",   text: "195 kJ"  } },
        { name: "Energy", amount: { value:  20,   unit: "kJ",   text: "47 kcal" } },
        { name: "Sugar",  amount: { value:   5,   unit: "gram", text: "5 gram"  } },
        { name: "Salt",   amount: { value:   2.0, unit: "g",    text: "2.0 g"   } }
      ],
    },
    {
      per: { name: "portion", value: None, unit: None, text: "per portion" },
      prepared: None,
      rows: [
        { name: "Energy", amount: { value: 20,   unit: "kJ",   text: "20 kJ"  } },
        { name: "Energy", amount: { value:  5,   unit: "kJ",   text: "5 kcal" } },
        { name: "Sugar",  amount: { value:  0.5, unit: "gram", text: "0,5 gr" } },
        { name: "Salt",   amount: { value:  0.2, unit: "g",    text: "0.2 g"  } }
      ]
    }
  ]
]
```

### JSON

```python
import json
from nutrients_parser import parse_data

data = """
{
  "nutrients": [
    {"name":"Energie","type":"ENER-","value":"1141 kJ (273 kcal)","dailyValue":""},
    {"name":"Koolhydraten","type":"CHOAVL","value":"18 g","dailyValue":""},
    {"name":"Eiwitten","type":"PRO-","value":"7 g","dailyValue":""},
    {"name":"Zout","type":"SALTEQ","value":"0.9 g","dailyValue":""}
  ],
  "preparationState":"Onbereide",
  "basisQuantity":"100 Gram"
}
"""

print(parse_data(json.loads(data)))
```

```
{
columns: [
    {
      per: { name: "100 Gram", value: 100, unit: "g", text: "100 Gram" },
      prepared: False,
      rows: [
        { name: "Energie",  code: "ENER-",  amount: { value: 1141,   unit: "kJ",   text: "1141 kJ"  } },
        { name: "Energie",  code: "ENER-",  amount: { value:  273,   unit: "kcal", text: "273 kcal" } },
        { name: "Eiwitten", code: "CHOAVL", amount: { value:    7,   unit: "g",    text: "7 g"      } },
        { name: "Zout",     code: "SALTEQ", amount: { value:    0.9, unit: "g",    text: "0.9 g"    } },
      ]
    }
  ]
}
```


## Develop


# License

This project is licensed under the [MIT license](LICENSE).
