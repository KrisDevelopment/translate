# translate
Run scripts to translate human lang using AI

Translation Service

Use the /translate endpoint to translate text from one language to another.

Send a POST request with JSON body containing 'text', 'src_lang', and 'dest_lang'.

# EXAMPLE 1:
Example:

    {
        "text": "Hello, world!",
        "src_lang": "english",
        "dest_lang": "bulgarian"
    }

# EXAMPLE 2:
curl -X POST http://127.0.0.1:20881/translate -H "Content-Type: application/json" -d '{"text": "Hello, world!", "src_lang": "english", "dest_lang": "bulgarian"}'
----
# Accepted Language Codes:

afrikaans
albanian
amharic
arabic
armenian
azerbaijani
basque
belarusian
bengali
bosnian
bulgarian
catalan
cebuano
chichewa
chinese (simplified)
chinese (traditional)
corsican
croatian
czech
danish
dutch
english
esperanto
estonian
filipino
finnish
french
frisian
galician
georgian
german
greek
gujarati
haitian creole
hausa
hawaiian
hebrew
hebrew
hindi
hmong
hungarian
icelandic
igbo
indonesian
irish
italian
japanese
javanese
kannada
kazakh
khmer
korean
kurdish (kurmanji)
kyrgyz
lao
latin
latvian
lithuanian
luxembourgish
macedonian
malagasy
malay
malayalam
maltese
maori
marathi
mongolian
myanmar (burmese)
nepali
norwegian
odia
pashto
persian
polish
portuguese
punjabi
romanian
russian
samoan
scots gaelic
serbian
sesotho
shona
sindhi
sinhala
slovak
slovenian
somali
spanish
sundanese
swahili
swedish
tajik
tamil
telugu
thai
turkish
ukrainian
urdu
uyghur
uzbek
vietnamese
welsh
xhosa
yiddish
yoruba
zulu