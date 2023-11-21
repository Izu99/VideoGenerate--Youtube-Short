import requests
import json
import time


def text_to_speech(text):
    apikey = "7230722f1emsha65e0f7abc2613dp15bef0jsn8de9c6eeab35"  # get your free API key from https://rapidapi.com/k_1/api/large-text-to-speech/
    filename = "test-file.wav"

    headers = {'content-type': "application/json",
            'x-rapidapi-host': "large-text-to-speech.p.rapidapi.com", 'x-rapidapi-key': apikey}
    response = requests.request("POST", "https://large-text-to-speech.p.rapidapi.com/tts",
                            data=json.dumps({"text": text}), headers=headers)
    id = json.loads(response.text)['id']
    eta = json.loads(response.text)['eta']
    print(f'Waiting {eta} seconds for the job to finish...')
    time.sleep(eta)
    response = requests.request(
        "GET", "https://large-text-to-speech.p.rapidapi.com/tts", headers=headers, params={'id': id})
    while "url" not in json.loads(response.text):
        response = requests.request(
            "GET", "https://large-text-to-speech.p.rapidapi.com/tts", headers=headers, params={'id': id})
        print(f'Waiting some more...')
        time.sleep(3)
    url = json.loads(response.text)['url']
    response = requests.request("GET", url)
    with open(filename, 'wb') as f:
        f.write(response.content)
    print(f'File saved to {filename} ! \nOr download here: {url}')
    return filename

if __name__ == "__main__":
    text_to_speech()
# end main
