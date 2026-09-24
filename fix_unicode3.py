import re

with open('src/routes/index.tsx', 'r', encoding='utf-8') as f:
    code = f.read()

code = code.replace('lang === "mr" ? "??????????" : "Home"', 'lang === "mr" ? "मुख्यपृष्ठ" : "Home"')
code = code.replace('lang === "mr" ? "???????????" : "About Us"', 'lang === "mr" ? "आमच्याबद्दल" : "About Us"')
code = code.replace('lang === "mr" ? "??????" : "Results"', 'lang === "mr" ? "परिणाम" : "Results"')
code = code.replace('lang === "en" ? "?????" : "EN"', 'lang === "en" ? "मराठी" : "EN"')
code = code.replace('lang === "mr" ? "?????????? ??? ???" : "Book Appointment"', 'lang === "mr" ? "अपॉइंटमेंट बुक करा" : "Book Appointment"')
code = code.replace('{lang === "en" ? "Switch to Marathi (?????)" : "Switch to English"}', '{lang === "en" ? "मराठी (Marathi)" : "English (इंग्रजी)"}')
code = code.replace('lang === "mr" ? "????????, ?????? ?????????? ????? ??????" : "Advanced Care for a Brighter, Healthier Smile."', 'lang === "mr" ? "उज्ज्वल, निरोगी हास्यासाठी प्रगत काळजी." : "Advanced Care for a Brighter, Healthier Smile."')
code = code.replace('lang === "mr" ? "????? ????? ??? ???" : "Book Your Consultation"', 'lang === "mr" ? "तुमचा सल्ला बुक करा" : "Book Your Consultation"')
code = code.replace('lang === "mr" ? "??????? ???? ???" : "Explore Our Services"', 'lang === "mr" ? "आमच्या सेवा पहा" : "Explore Our Services"')


with open('src/routes/index.tsx', 'w', encoding='utf-8') as f:
    f.write(code)
print("done correctly this time")
