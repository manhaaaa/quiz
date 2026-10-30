with open(r'D:\c++\quiz_game\index.html', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'finishSession' in line or "'results'" in line:
        print(f'{i+1}: {line.strip()[:100]}')

import re
with open(r'D:\c++\quiz_game\index.html', encoding='utf-8') as f:
    text = f.read()

print("Onclick containing results:")
for m in re.finditer(r'onclick=["\'][^"\']*results[^"\']*["\']', text):
    print(" ", m.group(0))

print("Onclick containing finish:")
for m in re.finditer(r'onclick=["\'][^"\']*finish[^"\']*["\']', text):
    print(" ", m.group(0))
