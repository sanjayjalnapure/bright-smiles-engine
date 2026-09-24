import re

with open('src/routes/index.tsx', 'r', encoding='utf-8') as f:
    code = f.read()

replacements = {
    'Welcome to Dhanvantari Dental Clinic': 'धन्वंतरी डेंटल क्लिनिकमध्ये आपले स्वागत आहे',
    
    'Gentle, modern dentistry in Solapur under the care of Dr. Sanika Sudha Kiranchandra\n              Phadke - general dentistry, smile designing and cosmetic dentistry in one calm clinic.': 
    'डॉ. सानिका सुधा किरणचंद्र फडके यांच्या देखरेखीखाली सोलापुरातील सौम्य, आधुनिक दंतचिकित्सा - एकाच शांत क्लिनिकमध्ये सामान्य दंतचिकित्सा, स्माईल डिझायनिंग आणि कॉस्मेटिक दंतचिकित्सा.',
    
    'View treatments': 'उपचार पहा',
    
    'Visit the clinic': 'क्लिनिकला भेट द्या',
    
    'From routine check-ups to smile makeovers - planned around your teeth, your comfort\n              and your budget.': 
    'नियमित तपासणीपासून ते स्माईल मेकओव्हरपर्यंत - तुमचे दात, तुमची सोय आणि तुमचे बजेट लक्षात घेऊन नियोजन केले जाते.',
    
    'Real results': 'खरे परिणाम',
    
    'After\n            </h2>': 'नंतर\n            </h2>',
    
    'Every smile tells a story. See real transformations by Dr. Sanika\n              Phadke — documented with the patient&apos;s consent.': 
    'प्रत्येक हास्य एक कथा सांगते. डॉ. सानिका फडके यांनी केलेले खरे बदल पहा - जे रुग्णांच्या संमतीने दस्तऐवजीकरण केले आहेत.',
    
    'Get directions': 'दिशानिर्देश मिळवा',
    
    'Advanced training, careful hands and a calm environment — so treatment feels simple\n              and safe.': 
    'प्रगत प्रशिक्षण, काळजीपूर्वक हाताळणी आणि एक शांत वातावरण — जेणेकरून उपचार सोपे आणि सुरक्षित वाटतात.',
    
    'Dr. Sanika combines careful clinical dentistry with an eye for aesthetics. Every\n                  visit begins with a proper diagnosis and a plain explanation of your options — so\n                  you always know what is being done and why. Patients come to her for pain-free\n                  routine treatment as much as for smile makeovers.': 
    'डॉ. सानिका सौंदर्यदृष्टीसह काळजीपूर्वक क्लिनिकल दंतचिकित्सेची सांगड घालतात. प्रत्येक भेटीची सुरुवात योग्य निदानाने आणि तुमच्या पर्यायांच्या स्पष्ट स्पष्टीकरणाने होते — जेणेकरून तुम्हाला नेहमी माहित असते की काय आणि का केले जात आहे. स्माईल मेकओव्हर प्रमाणेच वेदनारहित नियमित उपचारांसाठीही रुग्ण त्यांच्याकडे येतात.',
    
    'Dhanvantari Multispeciality': 'धन्वंतरी मल्टीस्पेशालिटी',
    
    'Expert dental care in Solapur — general dentistry, smile designing and cosmetic\n              dentistry.': 
    'सोलापुरातील तज्ञ दंत काळजी — सामान्य दंतचिकित्सा, स्माईल डिझायनिंग आणि कॉस्मेटिक दंतचिकित्सा.'
}

for en, mr in replacements.items():
    code = code.replace(en, f'{{lang === "mr" ? {mr} : {en}}}')

with open('src/routes/index.tsx', 'w', encoding='utf-8') as f:
    f.write(code)

print("Multiline text replaced")
