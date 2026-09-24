import re

with open('src/routes/index.tsx', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Hero Heading
old1 = '''<h1 className="mt-6 text-4xl leading-[1.05] font-extrabold text-white sm:text-5xl md:text-7xl">
              Advanced Care for a{" "}
              <span className="relative inline-block">
                <span className="text-primary text-glow">{lang === "mr" ? "उज्ज्वल, निरोगी" : "Brighter, Healthier"}</span>
                <span aria-hidden className="absolute -inset-6 -z-10 rounded-full bg-primary/20 blur-2xl" />
              </span>{" "}
              <span className="relative inline-block">
                <span className="text-white text-glow-soft">{lang === "mr" ? "हास्य" : "Smile"}</span>
                <span aria-hidden className="absolute -inset-6 -z-10 rounded-full bg-primary/15 blur-2xl" />
              </span>
            </h1>'''
new1 = '''{lang === "mr" ? (
              <h1 className="mt-6 text-4xl leading-[1.05] font-extrabold text-white sm:text-5xl md:text-7xl">
                <span className="relative inline-block">
                  <span className="text-primary text-glow">उज्ज्वल, निरोगी</span>
                  <span aria-hidden className="absolute -inset-6 -z-10 rounded-full bg-primary/20 blur-2xl" />
                </span>{" "}
                <span className="relative inline-block">
                  <span className="text-white text-glow-soft">हास्यासाठी</span>
                  <span aria-hidden className="absolute -inset-6 -z-10 rounded-full bg-primary/15 blur-2xl" />
                </span>
                {" "}प्रगत काळजी
              </h1>
            ) : (
              <h1 className="mt-6 text-4xl leading-[1.05] font-extrabold text-white sm:text-5xl md:text-7xl">
                Advanced Care for a{" "}
                <span className="relative inline-block">
                  <span className="text-primary text-glow">Brighter, Healthier</span>
                  <span aria-hidden className="absolute -inset-6 -z-10 rounded-full bg-primary/20 blur-2xl" />
                </span>{" "}
                <span className="relative inline-block">
                  <span className="text-white text-glow-soft">Smile</span>
                  <span aria-hidden className="absolute -inset-6 -z-10 rounded-full bg-primary/15 blur-2xl" />
                </span>
              </h1>
            )}'''
code = code.replace(old1, new1)

# 2. Services
old2 = '''<h2 className="mt-4 text-3xl font-extrabold md:text-5xl">
              Expert{" "}
              <span className="text-primary text-glow-soft">{lang === "mr" ? "दंत काळजी" : "dental care"}</span>{" "}
              for every need
            </h2>'''
new2 = '''{lang === "mr" ? (
              <h2 className="mt-4 text-3xl font-extrabold md:text-5xl">
                प्रत्येक गरजेसाठी <span className="text-primary text-glow-soft">तज्ञ दंत काळजी</span>
              </h2>
            ) : (
              <h2 className="mt-4 text-3xl font-extrabold md:text-5xl">
                Expert <span className="text-primary text-glow-soft">dental care</span> for every need
              </h2>
            )}'''
code = code.replace(old2, new2)

# 3. Comprehensive
old3 = '''<h2 className="mt-4 text-3xl font-extrabold md:text-5xl">
            Comprehensive{" "}
            <span className="text-primary text-glow-soft">{lang === "mr" ? "दंत काळजी" : "dental care"}</span>{" "}
            for all ages
          </h2>'''
new3 = '''{lang === "mr" ? (
            <h2 className="mt-4 text-3xl font-extrabold md:text-5xl">
              सर्व वयोगटांसाठी <span className="text-primary text-glow-soft">सर्वसमावेशक दंत काळजी</span>
            </h2>
          ) : (
            <h2 className="mt-4 text-3xl font-extrabold md:text-5xl">
              Comprehensive <span className="text-primary text-glow-soft">dental care</span> for all ages
            </h2>
          )}'''
code = code.replace(old3, new3)

# 4. A higher standard
old4 = '''<h2 className="mt-4 text-3xl font-extrabold md:text-5xl">
              A higher standard of{" "}
              <span className="text-primary text-glow-soft">{lang === "mr" ? "दंत काळजी" : "dental care"}</span>
            </h2>'''
new4 = '''{lang === "mr" ? (
              <h2 className="mt-4 text-3xl font-extrabold md:text-5xl">
                <span className="text-primary text-glow-soft">दंत काळजीचा</span> उच्च दर्जा
              </h2>
            ) : (
              <h2 className="mt-4 text-3xl font-extrabold md:text-5xl">
                A higher standard of <span className="text-primary text-glow-soft">dental care</span>
              </h2>
            )}'''
code = code.replace(old4, new4)

# 5. Come in for a check-up
old5 = '''<h2 className="mt-4 text-3xl font-extrabold md:text-5xl">
              Come in for a{" "}
              <span className="text-primary text-glow-soft">{lang === "mr" ? "या" : "check-up"}</span>
            </h2>'''
new5 = '''{lang === "mr" ? (
              <h2 className="mt-4 text-3xl font-extrabold md:text-5xl">
                <span className="text-primary text-glow-soft">तपासणीसाठी</span> या
              </h2>
            ) : (
              <h2 className="mt-4 text-3xl font-extrabold md:text-5xl">
                Come in for a <span className="text-primary text-glow-soft">check-up</span>
              </h2>
            )}'''
code = code.replace(old5, new5)

# Before & After labels in results
old6 = '''<span className="rounded-full border border-white/30 bg-black/40 px-3 py-1 text-[0.65rem] font-semibold tracking-wider text-white/90 uppercase backdrop-blur-sm">
                        Before
                      </span>
                      <span className="rounded-full bg-primary/80 px-3 py-1 text-[0.65rem] font-semibold tracking-wider text-primary-foreground uppercase backdrop-blur-sm">
                        After
                      </span>'''
new6 = '''<span className="rounded-full border border-white/30 bg-black/40 px-3 py-1 text-[0.65rem] font-semibold tracking-wider text-white/90 uppercase backdrop-blur-sm">
                        {lang === "mr" ? "पूर्वी" : "Before"}
                      </span>
                      <span className="rounded-full bg-primary/80 px-3 py-1 text-[0.65rem] font-semibold tracking-wider text-primary-foreground uppercase backdrop-blur-sm">
                        {lang === "mr" ? "नंतर" : "After"}
                      </span>'''
code = code.replace(old6, new6)

# Before & After Heading
old7 = '''<h2 className="mt-4 text-3xl font-extrabold md:text-5xl">
              Before{" "}
              <span className="text-primary text-glow-soft">&amp;</span>{" "}
              After
            </h2>'''
new7 = '''{lang === "mr" ? (
              <h2 className="mt-4 text-3xl font-extrabold md:text-5xl">
                उपचारापूर्वी <span className="text-primary text-glow-soft">आणि</span> नंतर
              </h2>
            ) : (
              <h2 className="mt-4 text-3xl font-extrabold md:text-5xl">
                Before <span className="text-primary text-glow-soft">&amp;</span> After
              </h2>
            )}'''
code = code.replace(old7, new7)

with open('src/routes/index.tsx', 'w', encoding='utf-8') as f:
    f.write(code)

print("Headings replaced")
