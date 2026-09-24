import re

with open('src/routes/index.tsx', 'r', encoding='utf-8') as f:
    code = f.read()

def repl(en, mr):
    global code
    code = code.replace(f'"{en}"', f'lang === "mr" ? "{mr}" : "{en}"')
    # Also replace instances that might be JSX text
    code = code.replace(f'>{en}<', f'>{{lang === "mr" ? "{mr}" : "{en}"}}<')

# Stats
repl('Fellowships', 'फेलोशिप्स')
repl('Core Specialities', 'मुख्य वैशिष्ट्ये')
repl('Sterile Protocol', 'निर्जंतुक प्रोटोकॉल')
repl('Doctor Attention', 'डॉक्टरांचे लक्ष')

# Services
repl('General Dentistry', 'सामान्य दंतचिकित्सा')
repl('Compassionate checkups, cleanings, and preventative care.', 'सहानुभूतीपूर्ण तपासणी, क्लिनिंग आणि प्रतिबंधात्मक काळजी.')
repl('Smile Designing', 'स्माईल डिझायनिंग')
repl('Creating customized smiles using advanced digital planning.', 'प्रगत डिजिटल नियोजनाचा वापर करून सानुकूलित हास्य तयार करणे.')
repl('Cosmetic Dentistry', 'कॉस्मेटिक दंतचिकित्सा')
repl('Enhancing aesthetics with veneers, whitening, and bonding.', 'व्हेनियर्स, व्हाइटनिंग आणि बाँडिंगसह सौंदर्य वाढवणे.')
repl('Painless Root Canals', 'वेदनारहित रूट कॅनॉल')
repl('Endodontic treatment utilizing precise laser and rotary techniques.', 'अचूक लेसर आणि रोटरी तंत्राचा वापर करून एंडोडॉन्टिक उपचार.')
repl('Digital X-Ray', 'डिजिटल एक्स-रे')
repl('Instant, high-definition imaging with low radiation dose.', 'कमी रेडिएशन डोससह झटपट, हाय-डेफिनिशन इमेजिंग.')
repl('3D Printing', '3D प्रिंटिंग')
repl('In-house production of surgical guides, retainers, and provisional crowns.', 'सर्जिकल गाइड्स, रिटेनर्स आणि तात्पुरत्या क्राउन्सचे इन-हाउस उत्पादन.')
repl('Advanced Dental Chair Unit', 'प्रगत डेंटल चेअर युनिट')
repl('A fully equipped, ergonomic dental chair unit designed for patient comfort and precise treatment delivery.', 'रुग्णांच्या सोयीसाठी आणि अचूक उपचारांसाठी पूर्णपणे सुसज्ज डेंटल चेअर युनिट.')

# Headings & Subheadings
repl('OUR TREATMENTS', 'आमचे उपचार')
repl('Comprehensive Dental Care', 'सर्वसमावेशक दंत काळजी')
repl('REAL RESULTS', 'खरे परिणाम')
repl('Before & After', 'पूर्वी आणि नंतर')
repl('Before &amp; After', 'पूर्वी आणि नंतर')
repl('Every smile tells a story. See real transformations by Dr. Sanika Phadke.', 'प्रत्येक हास्य एक कथा सांगते. डॉ. सानिका फडके यांनी केलेले खरे बदल पहा.')
repl('WHY CHOOSE US', 'आम्हाला का निवडावे')
repl('Excellence in Every Smile', 'प्रत्येक हास्यात उत्कृष्टता')
repl('MEET YOUR DOCTOR', 'तुमच्या डॉक्टरांना भेटा')
repl('Expertise You Can Trust', 'तुम्ही विश्वास ठेवू शकता असे कौशल्य')
repl('GET IN TOUCH', 'संपर्कात रहा')
repl('Visit Our Clinic', 'आमच्या क्लिनिकला भेट द्या')

# Cases
repl('Complete Smile Makeover', 'संपूर्ण स्माईल मेकओव्हर')
repl('Gap closure, shape correction, and teeth whitening achieved through customized ceramic restorations for a flawless smile.', 'सानुकूलित सिरॅमिक रिस्टोरेशनद्वारे गॅप बंद करणे, आकार सुधारणे आणि दात पांढरे करणे.')
repl('Deep Scaling & Polishing', 'डीप स्केलिंग आणि पॉलिशिंग')
repl('Complete removal of heavy tartar, calculus, and stains to restore healthy gums and clean teeth.', 'निरोगी हिरड्या आणि स्वच्छ दात पुनर्संचयित करण्यासाठी टार्टर आणि डाग पूर्णपणे काढून टाकणे.')
repl('Single Tooth Restoration', 'सिंगल टूथ रिस्टोरेशन')
repl('A discolored, non-vital front tooth flawlessly restored to match natural teeth using a metal-free ceramic crown.', 'धातू-मुक्त सिरॅमिक क्राउन वापरून नैसर्गिक दातांशी जुळण्यासाठी रंगहीन दात पुनर्संचयित केला.')
repl('Diastema (Gap) Closure', 'गॅप क्लोजर (Diastema)')
repl('Unappealing gaps between upper and lower teeth closed beautifully using customized tooth-colored restorations.', 'वरच्या आणि खालच्या दातांमधील अंतर दात-रंगाच्या रिस्टोरेशनचा वापर करून सुंदरपणे बंद केले.')
repl('Composite Bonding', 'कंपोझिट बाँडिंग')
repl('Front teeth gaps closed and surface imperfections masked with aesthetic, minimally invasive composite bonding.', 'दातांमधील अंतर बंद केले आणि कंपोझिट बाँडिंगसह पृष्ठभागावरील अपूर्णता झाकली.')
repl('Orthodontic Alignment', 'ऑर्थोडोंटिक अलाइनमेंट')
repl('Severe crowding and misalignment corrected to achieve a perfectly straight, harmonious smile.', 'परिपूर्ण सरळ, कर्णमधुर हास्य प्राप्त करण्यासाठी गर्दी आणि चुकीची संरेखन दुरुस्त केली.')

# Why Us
repl('State-of-the-Art Technology', 'अत्याधुनिक तंत्रज्ञान')
repl('We use the latest dental technology for precise diagnoses and minimally invasive treatments.', 'आम्ही अचूक निदान आणि कमीत कमी आक्रमक उपचारांसाठी अद्ययावत दंत तंत्रज्ञान वापरतो.')
repl('Patient-Centric Approach', 'रुग्ण-केंद्रित दृष्टीकोन')
repl('Your comfort is our priority. We take time to understand your needs and explain all treatment options.', 'तुमची सोय ही आमची प्राथमिकता आहे. आम्ही तुमच्या गरजा समजून घेतो आणि सर्व उपचार पर्याय समजावून सांगतो.')
repl('Strict Sterilization', 'कठोर निर्जंतुकीकरण')
repl('We follow rigorous 100% sterilization protocols to ensure the highest standards of safety and hygiene.', 'सुरक्षा आणि स्वच्छतेचे सर्वोच्च मानके सुनिश्चित करण्यासाठी आम्ही १००% निर्जंतुकीकरण प्रोटोकॉलचे पालन करतो.')

# Doctor Details
repl('FAGD (Fellowship in Advanced General Dentistry)', 'FAGD (प्रगत सामान्य दंतचिकित्सा फेलोशिप)')
repl('Fellowship in Implant Dentistry (ICOI)', 'इम्प्लांट डेंटिस्ट्री फेलोशिप (ICOI)')
repl('Certified Digital Smile Design Professional', 'प्रमाणित डिजिटल स्माईल डिझाईन व्यावसायिक')

# Contact
repl('Clinic timings', 'क्लिनिकची वेळ')
repl('Mon–Sat: 11 AM – 1 PM & 5 PM – 10 PM\\nSunday: 11 AM – 2 PM', 'सोम-शनि: सकाळी ११ ते दुपारी १ आणि संध्याकाळी ५ ते रात्री १०\\nरविवार: सकाळी ११ ते दुपारी २')
repl('Call us', 'आम्हाला कॉल करा')
repl('Email us', 'आम्हाला ईमेल करा')

with open('src/routes/index.tsx', 'w', encoding='utf-8') as f:
    f.write(code)

print("Translation applied!")
