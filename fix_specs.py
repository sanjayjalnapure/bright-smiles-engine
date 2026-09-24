import re

with open('src/routes/index.tsx', 'r', encoding='utf-8') as f:
    code = f.read()

code = code.replace(
    '<span className="text-xl">3</span>\n                Specialities',
    '<span className="text-xl">3</span>\n                {lang === "mr" ? "वैशिष्ट्ये" : "Specialities"}'
)

with open('src/routes/index.tsx', 'w', encoding='utf-8') as f:
    f.write(code)

print("Specialities fixed")
