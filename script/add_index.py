import os
import sys
def add_index(fin,fout):
    with open(fin, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    idi = open("id.md","w")
    new_lines = []
    count = 0
    bc = 0
    bcd = 0
    idi.write(f'# 目录\n')
    for line in lines:
        if line.startswith('### '):
            new_lines.append(f'### {count}.{bc}.{bcd} {line[4:]}')
            bcd += 1
        elif line.startswith('## '):  
            bcd = 1
            bc += 1
            new_lines.append(f'## {count}.{bc} {line[3:]}')
            idi.write(f'  {count}.{bc} {line[3:]}')
        elif line.startswith('# '):
            count += 1
            new_lines.append(f'# 第{count}章 {line[2:]}')
            idi.write(f'第{count}章 {line[2:]}')
            bc = 0
        else:
            new_lines.append(line)

    with open(fout, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    idi.close()


if __name__ == '__main__':
    add_index(sys.argv[1],sys.argv[2])
