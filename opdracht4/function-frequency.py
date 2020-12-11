import json
from pathlib import Path

json_file = Path(r'C:\Users\Admin\Documents\Development\Python-fundamentals\opdracht4\json_files\dictionary.json')
my_list = ['Hello', 'World', 0.5, 0.5, 'No', False, False]

def frequency(a_list):
    freq = [a_list.count(i) for i in a_list]
    return dict(list(zip(a_list, freq)))

data = json.dumps(frequency(my_list))

json_file.write_text(data)