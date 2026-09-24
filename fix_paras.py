import re

with open('src/routes/index.tsx', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Welcome
old_welcome = '>Welcome to Dhanvantari Dental Clinic<'
new_welcome = '>{lang === "mr" ? "धन्वंतरी डेंटल क्लिनिकमध्ये आपले स्वागत आहे" : "Welcome to Dhanvantari Dental Clinic"}<'
code = code.replace(old_welcome, new_welcome)

# 2. View treatments
old_view = '>View treatments<'
new_view = '>{lang === "mr" ? "उपचार पहा" : "View treatments"}<'
code = code.replace(old_view, new_view)

# 3. Visit the clinic
old_visit = '>Visit the clinic<'
new_visit = '>{lang === "mr" ? "क्लिनिकला भेट द्या" : "Visit the clinic"}<'
code = code.replace(old_visit, new_visit)

# 4. Real results
old_real = '>Real results<'
new_real = '>{lang === "mr" ? "खरे परिणाम" : "Real results"}<'
code = code.replace(old_real, new_real)

# 5. Get directions
old_get = '>Get directions<'
new_get = '>{lang === "mr" ? "दिशानिर्देश मिळवा" : "Get directions"}<'
code = code.replace(old_get, new_get)

with open('src/routes/index.tsx', 'w', encoding='utf-8') as f:
    f.write(code)

print("Short strings replaced")
