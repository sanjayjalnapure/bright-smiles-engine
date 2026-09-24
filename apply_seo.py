import re

# 1. Update __root.tsx
with open('src/routes/__root.tsx', 'r', encoding='utf-8') as f:
    root_code = f.read()

# Add JSON-LD and hreflang
json_ld = '''
      {
        tag: "script",
        attrs: { type: "application/ld+json" },
        children: JSON.stringify({
          "@context": "https://schema.org",
          "@type": ["Dentist", "LocalBusiness"],
          "name": "Dhanvantari Multispeciality Dental Clinic",
          "image": "https://dhanvantaridentalcare.in/assets/clinic-entrance-new.jpg",
          "@id": "https://dhanvantaridentalcare.in",
          "url": "https://dhanvantaridentalcare.in",
          "telephone": "+919168362233",
          "priceRange": "₹₹",
          "address": {
            "@type": "PostalAddress",
            "streetAddress": "142/A, Dhanvantari Nursing Home premises, Shete Nagar, Laxmi Peth",
            "addressLocality": "Solapur",
            "addressRegion": "Maharashtra",
            "postalCode": "413001",
            "addressCountry": "IN"
          },
          "geo": {
            "@type": "GeoCoordinates",
            "latitude": 17.6715,
            "longitude": 75.9104
          },
          "openingHoursSpecification": [
            {
              "@type": "OpeningHoursSpecification",
              "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
              "opens": "09:00",
              "closes": "11:00"
            },
            {
              "@type": "OpeningHoursSpecification",
              "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
              "opens": "18:00",
              "closes": "22:00"
            },
            {
              "@type": "OpeningHoursSpecification",
              "dayOfWeek": "Sunday",
              "opens": "10:00",
              "closes": "14:00"
            }
          ],
          "sameAs": [
            "https://dhanvantaridentalcare.in/"
          ]
        })
      }
'''

# Insert JSON-LD into meta/links array in __root.tsx? Wait, head() returns meta and links.
# Let's insert it into the links array, or as a script tag if supported by Tanstack Router. 
# Actually, head: () => ({ scripts: [ { type: "application/ld+json", children: '...' } ] })
# Let's find the head object in __root.tsx
root_head_regex = r"(head:\s*\(\)\s*=>\s*\(\{\s*)(meta:\s*\[.*?\])(,\s*links:\s*\[.*?\])"
if "scripts:" not in root_code:
    root_code = re.sub(r"(links:\s*\[[\s\S]*?\])", r"\1,\n    scripts: [" + json_ld + "    ]", root_code)

# Add alternate hreflang to links
root_code = root_code.replace('href: "/favicon.ico", type: "image/x-icon" },',
                              'href: "/favicon.ico", type: "image/x-icon" },\n      { rel: "alternate", hrefLang: "mr", href: "https://dhanvantaridentalcare.in/" },\n      { rel: "canonical", href: "https://dhanvantaridentalcare.in/" }')


with open('src/routes/__root.tsx', 'w', encoding='utf-8') as f:
    f.write(root_code)

# 2. Update index.tsx
with open('src/routes/index.tsx', 'r', encoding='utf-8') as f:
    index_code = f.read()

# Fix &amp; and &apos;
index_code = index_code.replace("designing &amp;\n                cosmetic dentistry", "designing &\n                cosmetic dentistry")
index_code = index_code.replace("patient&apos;s consent", "patient's consent")

# Update meta tags in index.tsx
meta_regex = r"(meta:\s*\[\s*\{.*?title.*?\},).*?(\],\s*\n\s*\}\),\s*\n\s*component:\s*Home,)"

new_meta = '''
      { title: "Dhanvantari Dental Clinic Solapur | Dr. Sanika Phadke" },
      {
        name: "description",
        content:
          "Advanced dental care in Solapur — general dentistry, smile designing and cosmetic dentistry by Dr. Sanika Phadke. Call 9168362233.",
      },
      { name: "keywords", content: "dental clinic solapur, dentist solapur, smile design solapur, cosmetic dentistry solapur, dhanvantari dental, Dr Sanika Phadke, root canal solapur, teeth cleaning solapur, best dentist solapur" },
      { property: "og:url", content: "https://dhanvantaridentalcare.in/" },
      { property: "og:title", content: "Dhanvantari Dental Clinic Solapur | Dr. Sanika Phadke" },
      { property: "og:site_name", content: "Dhanvantari Multispeciality Dental Clinic" },
      { property: "og:locale", content: "en_IN" },
      {
        property: "og:description",
        content:
          "General dentistry, smile designing and cosmetic dentistry at Dhanvantari Nursing Home premises, Solapur.",
      },
      { property: "og:image", content: "https://dhanvantaridentalcare.in/assets/clinic-entrance-new.jpg" },
      { property: "og:type", content: "website" },
      { name: "twitter:card", content: "summary_large_image" },
      { name: "twitter:title", content: "Dhanvantari Dental Clinic Solapur" },
      { name: "twitter:description", content: "Advanced dental care in Solapur — general dentistry, smile designing and cosmetic dentistry." },
      { name: "twitter:image", content: "https://dhanvantaridentalcare.in/assets/clinic-entrance-new.jpg" },
      { name: "geo.region", content: "IN-MH" },
      { name: "geo.placename", content: "Solapur" },
      { name: "geo.position", content: "17.6715;75.9104" },
      { name: "ICBM", content: "17.6715, 75.9104" },
'''

index_code = re.sub(r"meta:\s*\[[\s\S]*?\],\s*\n\s*\}\),\s*\n\s*component:\s*Home,", "meta: [\n" + new_meta + "    ],\n  }),\n  component: Home,", index_code)

with open('src/routes/index.tsx', 'w', encoding='utf-8') as f:
    f.write(index_code)

print("SEO updates applied successfully.")
