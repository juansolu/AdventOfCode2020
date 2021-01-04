import re
import itertools

# part 1

def update_mask(mask_string):
    return mask_string.split('=')[1].strip()

def update_mem(mem, line, mask):
    m = re.search(r'\d+', line)
    key = int(m.group(0))
    val = mem[key]
    import pdb; pdb.set_trace()
    for i, v in enumerate(mask):
        if v == 'X':
            pass
        elif v == '1':
            val = val | (2 ** (36 - i - 1))
        elif v == '0':
            val = val & ~(2 ** (36 - i - 1))
    print(f"key={key} new_val_with_mask={val}")
    mem[key] = val
    return mem

def run(code):
    mem = {}
    mask = ""
    for line in code:
        if 'mask' in line:
            mask = update_mask(line)
            continue
        elif 'mem' in line:
            exec(line)
            mem = update_mem(mem, line, mask)
    return sum([mem[key] for key in mem])

with open('input.txt', 'r') as fp:
    code = fp.read().strip().split('\n')
    result = run(code)
    print(result)