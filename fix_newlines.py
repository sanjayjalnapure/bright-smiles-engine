import re

with open('src/routes/index.tsx', 'r', encoding='utf-8') as f:
    code = f.read()

# Fix the first broken one
bad1 = ' : "Dhanvantari Multispeciality Dental Clinic sits inside Dhanvantari Nursing Home\n                premises at Shete Nagar, Laxmi Peth. Dr. Sanika Sudha Kiranchandra Phadke, B.D.S.\n                (MUHS), brings fellowship training in general dentistry and in smile designing &amp;\n                cosmetic dentistry to every treatment plan."}'
good1 = ' : Dhanvantari Multispeciality Dental Clinic sits inside Dhanvantari Nursing Home\n                premises at Shete Nagar, Laxmi Peth. Dr. Sanika Sudha Kiranchandra Phadke, B.D.S.\n                (MUHS), brings fellowship training in general dentistry and in smile designing &amp;\n                cosmetic dentistry to every treatment plan.}'
code = code.replace(bad1, good1)

# Fix the second broken one
bad2 = ' : "From a simple cleaning to a full smile makeover, you get a proper diagnosis, honest\n                options and a clear cost before anything starts — in a thoroughly sterilised,\n                comfortable setting."}'
good2 = ' : From a simple cleaning to a full smile makeover, you get a proper diagnosis, honest\n                options and a clear cost before anything starts — in a thoroughly sterilised,\n                comfortable setting.}'
code = code.replace(bad2, good2)

with open('src/routes/index.tsx', 'w', encoding='utf-8') as f:
    f.write(code)

print("Fixed syntax")
