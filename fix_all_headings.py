import re

with open('src/routes/index.tsx', 'r', encoding='utf-8') as f:
    lines = f.readlines()

def replace_lines(start_idx, end_idx, new_str):
    global lines
    lines[start_idx-1:end_idx] = [new_str + '\n']

# Bottom-up replacement to not mess up indices!

# 5. Come in for a check-up (760 to 763)
replace_lines(760, 763, '''            {lang === "mr" ? (
              <h2 className="mt-4 text-3xl font-extrabold md:text-5xl">
                <span className="text-primary text-glow-soft">तपासणीसाठी</span> या
              </h2>
            ) : (
              <h2 className="mt-4 text-3xl font-extrabold md:text-5xl">
                Come in for a <span className="text-primary text-glow-soft">check-up</span>
              </h2>
            )}''')

# 4. A higher standard of dental care (669 to 672)
replace_lines(669, 672, '''            {lang === "mr" ? (
              <h2 className="mt-4 text-3xl font-extrabold md:text-5xl">
                <span className="text-primary text-glow-soft">दंत काळजीचा</span> उच्च दर्जा
              </h2>
            ) : (
              <h2 className="mt-4 text-3xl font-extrabold md:text-5xl">
                A higher standard of <span className="text-primary text-glow-soft">dental care</span>
              </h2>
            )}''')

# 3. Comprehensive dental care for all ages (632 to 636)
replace_lines(632, 636, '''          {lang === "mr" ? (
            <h2 className="mt-4 text-3xl font-extrabold md:text-5xl">
              सर्व वयोगटांसाठी <span className="text-primary text-glow-soft">सर्वसमावेशक दंत काळजी</span>
            </h2>
          ) : (
            <h2 className="mt-4 text-3xl font-extrabold md:text-5xl">
              Comprehensive <span className="text-primary text-glow-soft">dental care</span> for all ages
            </h2>
          )}''')

# 2. Services Heading (486 to 490)
replace_lines(486, 490, '''            {lang === "mr" ? (
              <h2 className="mt-4 text-3xl font-extrabold md:text-5xl">
                प्रत्येक गरजेसाठी <span className="text-primary text-glow-soft">तज्ञ दंत काळजी</span>
              </h2>
            ) : (
              <h2 className="mt-4 text-3xl font-extrabold md:text-5xl">
                Expert <span className="text-primary text-glow-soft">dental care</span> for every need
              </h2>
            )}''')

# 1. Hero Heading (331 to 340)
replace_lines(331, 340, '''            {lang === "mr" ? (
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
            )}''')

with open('src/routes/index.tsx', 'w', encoding='utf-8') as f:
    f.writelines(lines)

print("Headings fully replaced by line indices")
