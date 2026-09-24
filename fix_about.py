import re

with open('src/routes/index.tsx', 'r', encoding='utf-8') as f:
    code = f.read()

def repl(en, mr):
    global code
    code = code.replace(en, f'{{lang === "mr" ? "{mr}" : "{en}"}}')

repl("Solapur&apos;s caring centre for everyday and cosmetic dentistry", "दैनंदिन आणि कॉस्मेटिक दंतचिकित्सेसाठी सोलापूरचे काळजीवाहू केंद्र")

repl("Dhanvantari Multispeciality Dental Clinic sits inside Dhanvantari Nursing Home\n                premises at Shete Nagar, Laxmi Peth. Dr. Sanika Sudha Kiranchandra Phadke, B.D.S.\n                (MUHS), brings fellowship training in general dentistry and in smile designing &amp;\n                cosmetic dentistry to every treatment plan.", "धन्वंतरी मल्टीस्पेशालिटी डेंटल क्लिनिक शेटे नगर, लक्ष्मी पेठ येथील धन्वंतरी नर्सिंग होमच्या आवारात आहे. डॉ. सानिका सुधा किरणचंद्र फडके, बी.डी.एस. (MUHS), प्रत्येक उपचार योजनेत सामान्य दंतचिकित्सा आणि स्माईल डिझायनिंग व कॉस्मेटिक दंतचिकित्सेतील त्यांचे विशेष प्रशिक्षण (फेलोशिप) आणतात.")

repl("From a simple cleaning to a full smile makeover, you get a proper diagnosis, honest\n                options and a clear cost before anything starts — in a thoroughly sterilised,\n                comfortable setting.", "साध्या साफसफाईपासून ते संपूर्ण स्माईल मेकओव्हरपर्यंत, तुम्हाला योग्य निदान, प्रामाणिक पर्याय आणि सर्वकाही सुरू होण्यापूर्वी स्पष्ट खर्च मिळतो — एका संपूर्ण निर्जंतुक आणि आरामदायी वातावरणात.")

# The array of bullet points
code = code.replace('"Fellowship in General Dentistry"', 'lang === "mr" ? "फेलोशिप इन जनरल डेंटिस्ट्री" : "Fellowship in General Dentistry"')
code = code.replace('"Fellowship in Smile Designing"', 'lang === "mr" ? "फेलोशिप इन स्माईल डिझायनिंग" : "Fellowship in Smile Designing"')
code = code.replace('"Fellowship in Cosmetic Dentistry"', 'lang === "mr" ? "फेलोशिप इन कॉस्मेटिक डेंटिस्ट्री" : "Fellowship in Cosmetic Dentistry"')
code = code.replace('"IDA Fellowship programme"', 'lang === "mr" ? "IDA फेलोशिप कार्यक्रम" : "IDA Fellowship programme"')

with open('src/routes/index.tsx', 'w', encoding='utf-8') as f:
    f.write(code)

print("About section fixed")
