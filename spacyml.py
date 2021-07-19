import spacy


nlp = spacy.load("en_core_web_lg")
doc = nlp("""Hi how are you
Let's look for phones under 10000 rupees
Yes, I also need a phones
Xiaomi will be good
but how much does it cost
Redmi phone is also good
I want to Doctors""")
print(doc.text)
print({(ent.text.strip(), ent.label_) for ent in doc.ents})