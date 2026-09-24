
import re

with open("src/routes/index.tsx", "r", encoding="utf-8") as f:
    c = f.read()

c = c.replace(
    "Welcome to Dhanvantari Dental Clinic",
    "{lang === \"mr\" ? \"धन्वंतरी डेंटल क्लिनिकमध्ये आपले स्वागत आहे\" : \"Welcome to Dhanvantari Dental Clinic\"}"
)

c = c.replace(
    "Gentle, modern dentistry in Solapur under the care of Dr. Sanika Sudha Kiranchandra\n              Phadke - general dentistry, smile designing and cosmetic dentistry in one calm clinic.",
    "{lang === \"mr\" ? `डॉ. सानिका सुधा किरणचंद्र फडके यांच्या देखरेखीखाली सोलापुरातील सौम्य, आधुनिक दंतचिकित्सा - एकाच शांत क्लिनिकमध्ये सामान्य दंतचिकित्सा, स्माईल डिझायनिंग आणि कॉस्मेटिक दंतचिकित्सा.` : `Gentle, modern dentistry in Solapur under the care of Dr. Sanika Sudha Kiranchandra\n              Phadke - general dentistry, smile designing and cosmetic dentistry in one calm clinic.`}"
)

c = c.replace(
    "View treatments",
    "{lang === \"mr\" ? \"उपचार पहा\" : \"View treatments\"}"
)

c = c.replace(
    "Visit the clinic",
    "{lang === \"mr\" ? \"क्लिनिकला भेट द्या\" : \"Visit the clinic\"}"
)

c = c.replace(
    "From routine check-ups to smile makeovers - planned around your teeth, your comfort\n              and your budget.",
    "{lang === \"mr\" ? `नियमित तपासणीपासून ते स्माईल मेकओव्हरपर्यंत - तुमचे दात, तुमची सोय आणि तुमचे बजेट लक्षात घेऊन नियोजन केले जाते.` : `From routine check-ups to smile makeovers - planned around your teeth, your comfort\n              and your budget.`}"
)

c = c.replace(
    "Real results",
    "{lang === \"mr\" ? \"खरे परिणाम\" : \"Real results\"}"
)

c = c.replace(
    "Every smile tells a story. See real transformations by Dr. Sanika\n              Phadke - documented with the patient&apos;s consent.",
    "{lang === \"mr\" ? `प्रत्येक हास्य एक कथा सांगते. डॉ. सानिका फडके यांनी केलेले खरे बदल पहा - जे रुग्णांच्या संमतीने दस्तऐवजीकरण केले आहेत.` : `Every smile tells a story. See real transformations by Dr. Sanika\n              Phadke - documented with the patient&apos;s consent.`}"
)

c = c.replace(
    "Before\n                      </span>",
    "{lang === \"mr\" ? \"पूर्वी\" : \"Before\"}\n                      </span>"
)
c = c.replace(
    "After\n                      </span>",
    "{lang === \"mr\" ? \"नंतर\" : \"After\"}\n                      </span>"
)

c = c.replace(
    "Get directions",
    "{lang === \"mr\" ? \"दिशानिर्देश मिळवा\" : \"Get directions\"}"
)

c = c.replace(
    "Advanced training, careful hands and a calm environment - so treatment feels simple\n              and safe.",
    "{lang === \"mr\" ? `प्रगत प्रशिक्षण, काळजीपूर्वक हाताळणी आणि एक शांत वातावरण — जेणेकरून उपचार सोपे आणि सुरक्षित वाटतात.` : `Advanced training, careful hands and a calm environment - so treatment feels simple\n              and safe.`}"
)

c = c.replace(
    "Dr. Sanika combines careful clinical dentistry with an eye for aesthetics. Every\n                  visit begins with a proper diagnosis and a plain explanation of your options - so\n                  you always know what is being done and why. Patients come to her for pain-free\n                  routine treatment as much as for smile makeovers.",
    "{lang === \"mr\" ? `डॉ. सानिका सौंदर्यदृष्टीसह काळजीपूर्वक क्लिनिकल दंतचिकित्सेची सांगड घालतात. प्रत्येक भेटीची सुरुवात योग्य निदानाने आणि तुमच्या पर्यायांच्या स्पष्ट स्पष्टीकरणाने होते — जेणेकरून तुम्हाला नेहमी माहित असते की काय आणि का केले जात आहे. स्माईल मेकओव्हर प्रमाणेच वेदनारहित नियमित उपचारांसाठीही रुग्ण त्यांच्याकडे येतात.` : `Dr. Sanika combines careful clinical dentistry with an eye for aesthetics. Every\n                  visit begins with a proper diagnosis and a plain explanation of your options - so\n                  you always know what is being done and why. Patients come to her for pain-free\n                  routine treatment as much as for smile makeovers.`}"
)

c = c.replace(
    "Dhanvantari Multispeciality",
    "{lang === \"mr\" ? \"धन्वंतरी मल्टीस्पेशालिटी\" : \"Dhanvantari Multispeciality\"}"
)

c = c.replace(
    "Expert dental care in Solapur - general dentistry, smile designing and cosmetic\n              dentistry.",
    "{lang === \"mr\" ? `सोलापुरातील तज्ञ दंत काळजी — सामान्य दंतचिकित्सा, स्माईल डिझायनिंग आणि कॉस्मेटिक दंतचिकित्सा.` : `Expert dental care in Solapur - general dentistry, smile designing and cosmetic\n              dentistry.`}"
)

c = c.replace(
    "Call or message us and we will find a time that suits you.",
    "{lang === \"mr\" ? \"आम्हाला कॉल किंवा मेसेज करा आणि आम्ही तुम्हाला सोयीची वेळ देऊ.\" : \"Call or message us and we will find a time that suits you.\"}"
)

# 1. Hero
c = c.replace(
    "<h1 className=\"mt-6 text-4xl leading-[1.05] font-extrabold text-white sm:text-5xl md:text-7xl\">\n              Advanced Care for a{\" \"}\n              <span className=\"relative inline-block\">\n                <span className=\"text-primary text-glow\">{lang === \"mr\" ? \"उज्ज्वल, निरोगी\" : \"Brighter, Healthier\"}</span>\n                <span aria-hidden className=\"absolute -inset-6 -z-10 rounded-full bg-primary/20 blur-2xl\" />\n              </span>{\" \"}\n              <span className=\"relative inline-block\">\n                <span className=\"text-white text-glow-soft\">{lang === \"mr\" ? \"हास्य\" : \"Smile\"}</span>\n                <span aria-hidden className=\"absolute -inset-6 -z-10 rounded-full bg-primary/15 blur-2xl\" />\n              </span>\n            </h1>",
    "{lang === \"mr\" ? (\n              <h1 className=\"mt-6 text-4xl leading-[1.05] font-extrabold text-white sm:text-5xl md:text-7xl\">\n                <span className=\"relative inline-block\">\n                  <span className=\"text-primary text-glow\">उज्ज्वल, निरोगी</span>\n                  <span aria-hidden className=\"absolute -inset-6 -z-10 rounded-full bg-primary/20 blur-2xl\" />\n                </span>{\" \"}\n                <span className=\"relative inline-block\">\n                  <span className=\"text-white text-glow-soft\">हास्यासाठी</span>\n                  <span aria-hidden className=\"absolute -inset-6 -z-10 rounded-full bg-primary/15 blur-2xl\" />\n                </span>\n                {\" \"}प्रगत काळजी\n              </h1>\n            ) : (\n              <h1 className=\"mt-6 text-4xl leading-[1.05] font-extrabold text-white sm:text-5xl md:text-7xl\">\n                Advanced Care for a{\" \"}\n                <span className=\"relative inline-block\">\n                  <span className=\"text-primary text-glow\">Brighter, Healthier</span>\n                  <span aria-hidden className=\"absolute -inset-6 -z-10 rounded-full bg-primary/20 blur-2xl\" />\n                </span>{\" \"}\n                <span className=\"relative inline-block\">\n                  <span className=\"text-white text-glow-soft\">Smile</span>\n                  <span aria-hidden className=\"absolute -inset-6 -z-10 rounded-full bg-primary/15 blur-2xl\" />\n                </span>\n              </h1>\n            )}"
)

# 2. Services
c = c.replace(
    "<h2 className=\"mt-4 text-3xl font-extrabold md:text-5xl\">\n              Expert{\" \"}\n              <span className=\"text-primary text-glow-soft\">{lang === \"mr\" ? \"दंत काळजी\" : \"dental care\"}</span>{\" \"}\n              for every need\n            </h2>",
    "{lang === \"mr\" ? (\n              <h2 className=\"mt-4 text-3xl font-extrabold md:text-5xl\">\n                प्रत्येक गरजेसाठी <span className=\"text-primary text-glow-soft\">तज्ञ दंत काळजी</span>\n              </h2>\n            ) : (\n              <h2 className=\"mt-4 text-3xl font-extrabold md:text-5xl\">\n                Expert <span className=\"text-primary text-glow-soft\">dental care</span> for every need\n              </h2>\n            )}"
)

# 3. Before & After
c = c.replace(
    "<h2 className=\"mt-4 text-3xl font-extrabold md:text-5xl\">\n              Before{\" \"}\n              <span className=\"text-primary text-glow-soft\">&amp;</span>{\" \"}\n              After\n            </h2>",
    "{lang === \"mr\" ? (\n              <h2 className=\"mt-4 text-3xl font-extrabold md:text-5xl\">\n                उपचारापूर्वी <span className=\"text-primary text-glow-soft\">आणि</span> नंतर\n              </h2>\n            ) : (\n              <h2 className=\"mt-4 text-3xl font-extrabold md:text-5xl\">\n                Before <span className=\"text-primary text-glow-soft\">&amp;</span> After\n              </h2>\n            )}"
)

# 4. Comprehensive
c = c.replace(
    "<h2 className=\"mt-4 text-3xl font-extrabold md:text-5xl\">\n            Comprehensive{\" \"}\n            <span className=\"text-primary text-glow-soft\">{lang === \"mr\" ? \"दंत काळजी\" : \"dental care\"}</span>{\" \"}\n            for all ages\n          </h2>",
    "{lang === \"mr\" ? (\n            <h2 className=\"mt-4 text-3xl font-extrabold md:text-5xl\">\n              सर्व वयोगटांसाठी <span className=\"text-primary text-glow-soft\">सर्वसमावेशक दंत काळजी</span>\n            </h2>\n          ) : (\n            <h2 className=\"mt-4 text-3xl font-extrabold md:text-5xl\">\n              Comprehensive <span className=\"text-primary text-glow-soft\">dental care</span> for all ages\n            </h2>\n          )}"
)

# 5. A higher standard
c = c.replace(
    "<h2 className=\"mt-4 text-3xl font-extrabold md:text-5xl\">\n              A higher standard of{\" \"}\n              <span className=\"text-primary text-glow-soft\">{lang === \"mr\" ? \"दंत काळजी\" : \"dental care\"}</span>\n            </h2>",
    "{lang === \"mr\" ? (\n              <h2 className=\"mt-4 text-3xl font-extrabold md:text-5xl\">\n                <span className=\"text-primary text-glow-soft\">दंत काळजीचा</span> उच्च दर्जा\n              </h2>\n            ) : (\n              <h2 className=\"mt-4 text-3xl font-extrabold md:text-5xl\">\n                A higher standard of <span className=\"text-primary text-glow-soft\">dental care</span>\n              </h2>\n            )}"
)

# 6. Come in for a check-up
c = c.replace(
    "<h2 className=\"mt-4 text-3xl font-extrabold md:text-5xl\">\n              Come in for a{\" \"}\n              <span className=\"text-primary text-glow-soft\">{lang === \"mr\" ? \"या\" : \"check-up\"}</span>\n            </h2>",
    "{lang === \"mr\" ? (\n              <h2 className=\"mt-4 text-3xl font-extrabold md:text-5xl\">\n                <span className=\"text-primary text-glow-soft\">तपासणीसाठी</span> या\n              </h2>\n            ) : (\n              <h2 className=\"mt-4 text-3xl font-extrabold md:text-5xl\">\n                Come in for a <span className=\"text-primary text-glow-soft\">check-up</span>\n              </h2>\n            )}"
)

with open("src/routes/index.tsx", "w", encoding="utf-8") as f:
    f.write(c)

print("Done")

