def urbanSearch(soup):
    try:
        urban = soup.find("div", attrs={"class": "meaning"})
        wordUrban = urban.text + '\n'
        return wordUrban
    except AttributeError:
        pass
