import re
with open('src/routes/index.tsx', 'r', encoding='utf-8') as f:
    code = f.read()

# Make a copy for backup
with open('src/routes/index.tsx.bak', 'w', encoding='utf-8') as f:
    f.write(code)

if 'useState<Language>' not in code:
    code = code.replace(
        'function Home() {',
        'export type Language = "en" | "mr";\n\nfunction Home() {\n  const [lang, setLang] = useState<Language>("en");'
    )

    # Insert language toggle button
    btn = '''<button
              onClick={() => setLang(l => l === "en" ? "mr" : "en")}
              className="hidden items-center justify-center rounded-full border border-primary/30 px-3 py-1.5 text-xs font-semibold text-primary transition-colors hover:bg-primary/10 sm:flex"
            >
              {lang === "en" ? "?????" : "EN"}
            </button>'''
    
    code = code.replace(
        '<div className="flex items-center gap-3">',
        f'<div className="flex items-center gap-3">\n            {btn}'
    )
    
    # Also for mobile menu
    mobile_btn = '''<button
                    onClick={() => setLang(l => l === "en" ? "mr" : "en")}
                    className="w-full rounded-xl border border-primary/30 py-3 text-center text-sm font-semibold text-primary"
                  >
                    {lang === "en" ? "Switch to Marathi (?????)" : "Switch to English"}
                  </button>'''
    
    code = code.replace(
        '<nav className="mt-8 flex flex-col gap-4">',
        f'<nav className="mt-8 flex flex-col gap-4">\n                  {mobile_btn}'
    )

    with open('src/routes/index.tsx', 'w', encoding='utf-8') as f:
        f.write(code)
    print("Injected state and buttons")
else:
    print("Already injected")
