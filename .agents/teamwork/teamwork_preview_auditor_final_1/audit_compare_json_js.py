import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('D:/c++/quiz_game/questions.json', 'r', encoding='utf-8') as f:
    json_data = json.load(f)

with open('D:/c++/quiz_game/questions.js', 'r', encoding='utf-8') as f:
    js_raw = f.read().strip()

# Strip `window.QUIZ_QUESTIONS = ` and trailing `;`
js_clean = re.sub(r'^\s*(?:window\.)?(?:const|let|var)?\s*[a-zA-Z0-9_$]+\s*=\s*', '', js_raw, count=1)
js_clean = re.sub(r';\s*$', '', js_clean)
js_data = json.loads(js_clean)

print(f"Comparing questions.json ({len(json_data)} items) with questions.js ({len(js_data)} items)...")

if len(json_data) != len(js_data):
    print(f"FAIL: Length mismatch: JSON={len(json_data)}, JS={len(js_data)}")
    sys.exit(1)

mismatches = 0
for i in range(len(json_data)):
    q_json = json_data[i]
    q_js = js_data[i]
    if q_json != q_js:
        print(f"Mismatch at index {i} (ID {q_json.get('id')})")
        mismatches += 1

if mismatches == 0:
    print("SUCCESS: questions.json and questions.js are 100% identical in structure and data content!")
else:
    print(f"FAIL: {mismatches} mismatches found between JSON and JS!")
    sys.exit(1)
