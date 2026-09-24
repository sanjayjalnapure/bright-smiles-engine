with open('src/routes/index.tsx', 'r', encoding='utf-8') as f:
    code = f.read()

# Fix 1: Solapur&apos;s inside a JS string -> Solapur's
code = code.replace("Solapur&apos;s caring centre", "Solapur's caring centre")

# Fix 2: &amp; inside template literal for about section -> &
code = code.replace("in smile designing &amp;\n                cosmetic dentistry to every treatment plan.", "in smile designing &\n                cosmetic dentistry to every treatment plan.")

# Fix 3: patient&apos;s inside template literal -> patient's
code = code.replace("patient&apos;s consent", "patient's consent")

with open('src/routes/index.tsx', 'w', encoding='utf-8') as f:
    f.write(code)

print("Done fixing HTML entities")
