import json

with open('../resources/monster.json', 'r') as f:
    content = f.read()

with open('../resources/monster-define.js', 'w') as f:
    f.write('let monster_kinds = ')
    f.write(content)
    f.write(';\n\n')
    f.write('let ped_order = ')
    f.write(json.dumps(['ダークドレアム'], ensure_ascii=False, indent=2))
    f.write(';\n\n')
