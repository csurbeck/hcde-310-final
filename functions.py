import urllib.parse, urllib.request, urllib.error, json
import pprint  # Module that allows you print complicated data in a more readable way

baseurl = "https://api.dictionaryapi.dev/api/v2/entries/en/"


def getWordInfo(word):
    general_query = baseurl + word

    try:
        with urllib.request.urlopen(general_query) as f:
            word_info_request = f.read().decode('utf-8')
            info = json.loads(word_info_request)
            meanings = info[0]['meanings']
            defs_and_partspeech = []
            for meaning in meanings:
                defs_and_partspeech.append([meaning['partOfSpeech'], meaning['definitions'][0]['definition']])
            pprint.pprint(defs_and_partspeech)
            return defs_and_partspeech
    except urllib.error.HTTPError as err:
        print("There was an error with this request: ", err)
    except urllib.error.URLError as err:
        print("Failed to reach server.")
        print("Error reason:  " + err.reason)

getWordInfo("hello")
