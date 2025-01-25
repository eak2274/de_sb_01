import locale
import sys
import requests

print("Preferred Encoding (locale):", locale.getpreferredencoding())
print("Default Encoding (sys):", sys.getdefaultencoding())
print("Terminal Encoding (sys.stdout):", sys.stdout.encoding)

response = requests.get('https://zenquotes.io/api/random')
quote = response.json()[0]['q']
print('Quote of the day: "{}"'.format(quote))
print()
print(response.json())