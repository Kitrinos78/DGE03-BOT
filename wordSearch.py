def show_origin(soup):
    try:
        origin = soup.find('span', {'unbox': 'wordorigin'})
        wordOrigin = origin.text + '\n'
        return wordOrigin
    except AttributeError:
        pass


def show_definitions(soup):
    print()
    senseList = []
    senses = soup.find_all('li', class_='sense')
    for s in senses:
        definition = s.find('span', class_='def').text
        wordDefinitions = "- " + definition
        return wordDefinitions
      
