from googletrans import Translator

translator = Translator(service_urls=[
      'translate.google.co.th',

    ])
translations = translator.translate(['ออกเสียง'], dest='hmn')
for translation in translations:
    print(translation.origin, ' -> ', translation.text)