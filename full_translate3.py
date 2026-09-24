import re

with open('src/routes/index.tsx', 'r', encoding='utf-8') as f:
    code = f.read()

def repl(en, mr):
    global code
    code = code.replace(f'"{en}"', f'lang === "mr" ? "{mr}" : "{en}"')
    code = code.replace(f'>{en}<', f'>{{lang === "mr" ? "{mr}" : "{en}"}}<')
    code = code.replace(f'> {en} <', f'> {{lang === "mr" ? "{mr}" : "{en}"}} <')
    code = code.replace(f'{en} {{', f'{{lang === "mr" ? "{mr} " : "{en} "}}{{')

# Missing ones
repl('Come in for a', 'तपासणीसाठी')
repl('check-up', 'या')
repl('Check-ups, scaling, tooth-coloured fillings, root canal treatment and extractions - done gently and hygienically.', 'तपासणी, स्केलिंग, दात-रंगाचे फिलिंग, रूट कॅनॉल उपचार आणि दात काढणे - हळुवारपणे आणि स्वच्छतेने केले जाते.')
repl('From routine check-ups to smile makeovers - planned around your teeth, your comfort and your budget.', 'नियमित तपासणीपासून ते स्माईल मेकओव्हरपर्यंत - तुमचे दात, तुमची सोय आणि तुमचे बजेट लक्षात घेऊन नियोजन केले जाते.')
repl('for every need', 'प्रत्येक गरजेसाठी')
repl('Show less', 'कमी दाखवा')
repl('View all', 'सर्व पहा')
repl('cases', 'प्रकरणे')

with open('src/routes/index.tsx', 'w', encoding='utf-8') as f:
    f.write(code)

print("Third wave applied!")
