import re

with open('src/routes/index.tsx', 'r', encoding='utf-8') as f:
    code = f.read()

def repl(en, mr):
    global code
    # Try replacing as a JS string
    code = code.replace(f'"{en}"', f'lang === "mr" ? "{mr}" : "{en}"')
    # Try replacing as JSX text
    code = code.replace(f'>{en}<', f'>{{lang === "mr" ? "{mr}" : "{en}"}}<')
    # Try replacing with leading/trailing spaces in JSX
    code = code.replace(f'> {en} <', f'> {{lang === "mr" ? "{mr}" : "{en}"}} <')

# Texts from Hero
repl('Dhanvantari', 'धन्वंतरी')
repl('Multispeciality Dental Clinic', 'मल्टीस्पेशालिटी डेंटल क्लिनिक')
repl('Brighter, Healthier', 'उज्ज्वल, निरोगी')
repl('Smile.', 'हास्य.')
repl('Smile', 'हास्य')
repl('Gentle, modern dentistry in Solapur under the care of Dr. Sanika Sudha Kiranchandra Phadke.', 'सोलापुरात डॉ. सानिका सुधा किरणचंद्र फडके यांच्या देखरेखीखाली सौम्य, आधुनिक दंतचिकित्सा.')
repl('B.D.S. (MUHS) | Fellowship in General Dentistry | Fellowship in Smile Designing &amp; Implant Dentistry', 'B.D.S. (MUHS) | फेलोशिप इन जनरल डेंटिस्ट्री | फेलोशिप इन स्माईल डिझायनिंग अँड इम्प्लांट डेंटिस्ट्री')

# Texts from About
repl('About the clinic', 'क्लिनिकबद्दल')
repl('More than just a', 'केवळ एका')
repl('dental clinic', 'डेंटल क्लिनिकपेक्षा अधिक')
repl('Dhanvantari Multispeciality Dental Clinic sits inside Dhanvantari Nursing Home premises in Solapur, Maharashtra. We built this clinic to provide honest, precise dentistry that respects your time and comfort.', 'धन्वंतरी मल्टीस्पेशालिटी डेंटल क्लिनिक हे महाराष्ट्रातील सोलापूर येथील धन्वंतरी नर्सिंग होमच्या आवारात आहे. तुमचा वेळ आणि सोयीचा आदर करणारी प्रामाणिक, अचूक दंतचिकित्सा देण्यासाठी आम्ही हे क्लिनिक बनवले आहे.')
repl('From a simple cleaning to a full smile makeover, you get a proper diagnosis, honest options and gentle care.', 'साध्या साफसफाईपासून ते संपूर्ण स्माईल मेकओव्हरपर्यंत, तुम्हाला योग्य निदान, प्रामाणिक पर्याय आणि सौम्य काळजी मिळते.')

# Texts from Services
repl('Our services', 'आमच्या सेवा')
# Advanced care in 'Advanced' span and 'dental care' span
repl('Advanced', 'प्रगत')
repl('dental care', 'दंत काळजी')
repl('From routine check-ups to smile makeovers — planned around your teeth, your comfort and your goals.', 'नियमित तपासणीपासून ते स्माईल मेकओव्हरपर्यंत - तुमचे दात, तुमची सोय आणि तुमची ध्येये लक्षात घेऊन नियोजन केले जाते.')

# Texts from Before/After
repl('Every smile tells a story. See real transformations by Dr. Sanika', 'प्रत्येक हास्य एक कथा सांगते. डॉ. सानिका यांनी केलेले खरे बदल पहा')
repl('All photographs are of actual patients treated at Dhanvantari Clinic. Results may vary.', 'सर्व छायाचित्रे धन्वंतरी क्लिनिकमध्ये उपचार घेतलेल्या प्रत्यक्ष रुग्णांची आहेत. परिणाम भिन्न असू शकतात.')

# Visit clinic
repl('Visit clinic', 'क्लिनिकला भेट द्या')
repl('State-of-the-art', 'अत्याधुनिक')
repl('Dhanvantari Nursing Home premises, 142/A, Shete Nagar, Laxmi Peth, Solapur - 413001', 'धन्वंतरी नर्सिंग होम परिसर, १४२/अ, शेटे नगर, लक्ष्मी पेठ, सोलापूर - ४१३००१')

# Why choose us
repl('Why choose us', 'आम्हाला का निवडावे')
repl('Excellence in', 'उत्कृष्टता')
repl('Advanced training, careful hands and a calm environment — so treatment feels simple and safe.', 'प्रगत प्रशिक्षण, काळजी घेणारे हात आणि शांत वातावरण - ज्यामुळे उपचार सोपे आणि सुरक्षित वाटतात.')

# Doctor
repl('Meet your dentist', 'तुमच्या डेंटिस्टला भेटा')
repl('Dr. Sanika Sudha Kiranchandra Phadke', 'डॉ. सानिका सुधा किरणचंद्र फडके')
repl('Dr. Sanika combines careful clinical dentistry with an eye for aesthetics. Every diagnosis is thoroughly explained, and every treatment is precise.', 'डॉ. सानिका काळजीपूर्वक क्लिनिकल दंतचिकित्सा आणि सौंदर्यशास्त्राची जोड देतात. प्रत्येक निदान सविस्तर समजावून सांगितले जाते आणि प्रत्येक उपचार अचूक असतो.')
repl('Her focus is on minimally invasive dentistry — saving as much of your natural tooth as possible while delivering a beautiful, long-lasting result.', 'त्यांचा भर किमान आक्रमक दंतचिकित्सेवर (minimally invasive dentistry) आहे - सुंदर, दीर्घकाळ टिकणारा परिणाम देताना तुमचे नैसर्गिक दात जास्तीत जास्त वाचवणे.')

# Contact
repl('Contact us', 'आमच्याशी संपर्क साधा')
repl('Get in touch', 'संपर्कात रहा')
repl('Call or message us and we will find a time that suits you.', 'आम्हाला कॉल करा किंवा मेसेज करा आणि आम्ही तुमच्या सोयीची वेळ शोधू.')

# Footer
repl('Dental Clinic', 'डेंटल क्लिनिक')
repl('Expert dental care in Solapur — general dentistry, smile designing and cosmetic treatments.', 'सोलापुरात तज्ञ दंत काळजी — सामान्य दंतचिकित्सा, स्माईल डिझायनिंग आणि कॉस्मेटिक उपचार.')
repl('Explore', 'अन्वेषण करा')
repl('Reach us', 'आमच्याशी संपर्क साधा')
repl('Quick Links', 'क्विक लिंक्स')
repl('FAQs', 'सामान्य प्रश्न')
repl('Privacy Policy', 'गोपनीयता धोरण')
repl('Terms', 'अटी आणि शर्ती')
repl('Book Appointment', 'अपॉइंटमेंट बुक करा')
repl('Switch to Marathi', 'मराठी मध्ये बदला')
repl('Switch to English', 'इंग्रजी मध्ये बदला')

# Extra missed ones
repl('Treatments', 'उपचार')
repl('Safety First', 'सुरक्षा प्रथम')
repl('Our Clinic', 'आमचे क्लिनिक')
repl('Contact Us', 'आमच्याशी संपर्क साधा')


with open('src/routes/index.tsx', 'w', encoding='utf-8') as f:
    f.write(code)

print("Second wave of translations applied!")
