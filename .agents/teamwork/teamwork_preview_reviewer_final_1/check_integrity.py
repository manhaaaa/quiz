import json
import sys
import io

if sys.platform == "win32":
    if hasattr(sys.stdout, "buffer"):
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

with open(r'D:\c++\quiz_game\questions.json', encoding='utf-8') as f:
    qjson = json.load(f)

print(f'Inspecting short options (len <= 4):')
for q in qjson:
    for opt in q['options']:
        if len(opt) <= 4:
            print(f'QID {q["id"]} (Topic {q["topicId"]} - {q["topicName"]}):')
            print(f'  Question: {q["question"]}')
            print(f'  Options: {q["options"]}')
            print(f'  Answer: {q["answer"]}')
            print('-'*40)
            break
