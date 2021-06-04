def urbanSearch(soup):
    try:
        urban = soup.find("div", attrs={"class": "meaning"})
        wordUrban = urban.text + '\n'
        return wordUrban
    except AttributeError:
        pass

    
def urbanExample(soup):
    try:
        urban = soup.find("div", attrs={"class": "example"})
        wordUrban = urban.text + '\n'
        return wordUrban
    except AttributeError:
        pass
