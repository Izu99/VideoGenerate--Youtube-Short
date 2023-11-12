import requests
def get_quote():
    response = requests.get('https://zenquotes.io/api/random')
    if response.status_code == 200:
        data = response.json()
        quote = data[0]['q']
        author = data[0]['a']
        return "\"" + quote + "\"", "- " +author
    else:
        return None
    
def main():
    quote = get_quote() 
    if quote:
        pass
    else:
        print('Failed to get quote from API')

if __name__ == "__main__":
    main()
# end main
