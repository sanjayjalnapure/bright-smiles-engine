import re

with open('src/routes/index.tsx', 'r', encoding='utf-8') as f:
    code = f.read()

# Make NAV a function
code = code.replace('const NAV = [', 'const getNav = (lang: Language) => [')
code = code.replace('{ label: "Home", href: "#home" }', '{ label: lang === "mr" ? "??????????" : "Home", href: "#home" }')
code = code.replace('{ label: "About Us", href: "#about" }', '{ label: lang === "mr" ? "???????????" : "About Us", href: "#about" }')
code = code.replace('{ label: "Services", href: "#services" }', '{ label: lang === "mr" ? "????" : "Services", href: "#services" }')
code = code.replace('{ label: "Results", href: "#results" }', '{ label: lang === "mr" ? "??????" : "Results", href: "#results" }')
code = code.replace('{ label: "Our Doctor", href: "#doctor" }', '{ label: lang === "mr" ? "???? ??????" : "Our Doctor", href: "#doctor" }')
code = code.replace('{ label: "Contact", href: "#contact" }', '{ label: lang === "mr" ? "??????" : "Contact", href: "#contact" }')
code = code.replace('NAV.map(', 'getNav(lang).map(')

# Update Hero section
code = code.replace(
    'Advanced Care for a Brighter, Healthier Smile.',
    '{lang === "mr" ? "???????, ?????? ?????????? ????? ?????." : "Advanced Care for a Brighter, Healthier Smile."}'
)
code = code.replace(
    'Book Your Consultation',
    '{lang === "mr" ? "????? ????? ??? ???" : "Book Your Consultation"}'
)
code = code.replace(
    'Explore Our Services',
    '{lang === "mr" ? "?????? ???? ???" : "Explore Our Services"}'
)
code = code.replace(
    'Book Appointment',
    '{lang === "mr" ? "?????????? ??? ???" : "Book Appointment"}'
)

# Replace top-level occurrences that might be tricky if we don't watch out
# Header button:
# <a href="#contact" ...>Book Appointment</a> (Wait, I replaced exactly 'Book Appointment')

with open('src/routes/index.tsx', 'w', encoding='utf-8') as f:
    f.write(code)

print("Translated Nav and Hero")
