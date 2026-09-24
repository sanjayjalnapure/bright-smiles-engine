with open('src/routes/index.tsx', 'r', encoding='utf-8') as f:
    code = f.read()

# We need to move STATS, SERVICES, WHY, CASES inside Home()
# Wait, it's easier to just pass 'lang' to them like getNav(lang).
# Let's change them to functions taking lang.

# STATS
code = code.replace('const STATS = [', 'const getStats = (lang: Language) => [')
code = code.replace('STATS.map(', 'getStats(lang).map(')

# SERVICES
code = code.replace('const SERVICES = [', 'const getServices = (lang: Language) => [')
code = code.replace('SERVICES.map(', 'getServices(lang).map(')

# WHY
code = code.replace('const WHY = [', 'const getWhy = (lang: Language) => [')
code = code.replace('WHY.map(', 'getWhy(lang).map(')

# CASES
code = code.replace('const CASES = [', 'const getCases = (lang: Language) => [')
code = code.replace('CASES.map(', 'getCases(lang).map(')
code = code.replace('CASES.length', 'getCases(lang).length')
code = code.replace('CASES.slice', 'getCases(lang).slice')

with open('src/routes/index.tsx', 'w', encoding='utf-8') as f:
    f.write(code)

print("Scope fixed")
