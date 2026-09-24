import re

with open('src/routes/index.tsx', 'r', encoding='utf-8') as f:
    code = f.read()

old_btn = '\View all \ cases\'
new_btn = 'lang === "mr" ? \सर्व \ प्रकरणे पहा\ : \View all \ cases\'
code = code.replace(old_btn, new_btn)

with open('src/routes/index.tsx', 'w', encoding='utf-8') as f:
    f.write(code)

print("Button fixed!")
