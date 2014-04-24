"""
Downloads and parses the variables table from the documentation
author: chris @ sihrc
"""

#Python Modules
import urllib2, unicodedata, re
from bs4 import BeautifulSoup as Soup

#Local Modules
import config
from wrappers import debug

@debug
def download(datafile):
    """
    From get_features.py\n
    Downloads the documentation as text file from HTML
    """
    page = urllib2.urlopen(config.tables.format(datafile.lower())).read()
    with open(config.path("..","data",datafile,"data", "tables.txt"), 'wb') as f:
        f.write(page)
    return page


@debug
def read_tables(datafile):
    """
    From get_features.py
    Parses the HTML as plain text
    Returns dictionary of {titles:variables}
    """
    path = config.path("..","data",datafile,"data", "tables.txt")
    if not config.os.path.exists(path):
        page = download(datafile)
    else:
        with open(path, 'rb') as f:
            page = f.read()
    start = page.find("<a name=\"DVariable\">")
    page = page[start:]
    end = page.find("<a name=\"Appendix1\">")
    soup = Soup(page[:end])
    titles, tables = [], []
    # print soup.find_all("table", {"class", "contentStyle"})
    # raw_input()
    found_titles = soup.find_all("p", {"class":"contentStyle"})[2:]
    if len(found_titles) == 0:
        found_titles = soup.find_all("caption")
        print found_titles
        for title in found_titles:
            titles.append(title.text.encode("utf-8"))
            tables.append([var.text.encode("utf-8") for var in title.parent.find_all("th")[3:]])
    else:
        for title in found_titles:
            titles.append(title.text.encode('utf-8'))
            tables.append([var.text.encode("utf-8") for var in title.find_next_sibling("table").find_all("th")[3:]])
   
    variables = dict(zip(titles,tables))
    print variables
    if len(titles) == len(tables) and titles != [] and [] not in tables:
        return True
    else:
        print tables
        print titles
        return False


if __name__ == "__main__":
    import sys
    print read_tables(sys.argv[1])