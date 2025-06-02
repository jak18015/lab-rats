import re
import requests
import json
import base64

lang = 'en'
text = 'Jacob Kellermeier'

data = {
    'f.req': json.dumps([
        [
            [
                'jQ1olc',
                json.dumps([
                    text,
                    lang,
                    None,
                    json.dumps(None),
                ]),
                None,
                'generic',
            ]
        ]
    ]),
}

response = requests.post('https://translate.google.com/_/TranslateWebserverUi/data/batchexecute', data=data)

if response.status_code == 200:
    match = re.search(r'//OE[^\\\\]+', response.text)
    if match:
        with open('google-translate/name.mp3', 'wb') as f:
            f.write(base64.b64decode(match.group(0)))
    else:
        print('error Match')
else:
    print('error HTTP')