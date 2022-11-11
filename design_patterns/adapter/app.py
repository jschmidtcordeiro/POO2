from json_parser import JsonParser
from adapter import Adapter

code = 1

if code == 0:
    f = open('data.json',)

    p = JsonParser()

    data_parsed = p.parse(f)

    print(data_parsed)

    f.close()

elif code == 1:
    f = open('data.csv',)

    p = Adapter()

    data_parsed = p.parse(f)

    print(data_parsed)

    f.close()