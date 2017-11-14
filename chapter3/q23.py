# ==国名== → 国名 レベル1 
import sys

for line in sys.stdin:
    if line.startswith('=='):
        sec_name = line.strip('= \n')
        level = int(line.count('=')/2 - 1)
        print(sec_name, 'レベル'+str(level))