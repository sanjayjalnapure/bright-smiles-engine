import re

with open('src/routes/index.tsx', 'r', encoding='utf-8') as f:
    code = f.read()

code = code.replace(
    '\n                Multispeciality Dental Clinic\n              </span>',
    '\n                {lang === "mr" ? "मल्टीस्पेशालिटी डेंटल क्लिनिक" : "Multispeciality Dental Clinic"}\n              </span>'
)

code = code.replace(
    'All photographs are of actual patients treated at Dhanvantari\n              Multispeciality Dental Clinic and published with consent.\n              Individual results may vary.',
    '{lang === "mr" ? "सर्व छायाचित्रे धन्वंतरी मल्टीस्पेशालिटी डेंटल क्लिनिकमध्ये उपचार घेतलेल्या प्रत्यक्ष रुग्णांची आहेत आणि त्यांच्या संमतीने प्रकाशित केली आहेत. वैयक्तिक परिणाम भिन्न असू शकतात." : "All photographs are of actual patients treated at Dhanvantari Multispeciality Dental Clinic and published with consent. Individual results may vary."}'
)

code = code.replace(
    'All photographs are of actual patients treated at Dhanvantari\n              Multispeciality Dental Clinic and published with consent.',
    '{lang === "mr" ? "सर्व छायाचित्रे धन्वंतरी मल्टीस्पेशालिटी डेंटल क्लिनिकमध्ये उपचार घेतलेल्या प्रत्यक्ष रुग्णांची आहेत आणि त्यांच्या संमतीने प्रकाशित केली आहेत." : "All photographs are of actual patients treated at Dhanvantari Multispeciality Dental Clinic and published with consent."}'
)

with open('src/routes/index.tsx', 'w', encoding='utf-8') as f:
    f.write(code)

print("Remaining text fixed")
