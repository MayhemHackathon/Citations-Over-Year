from bs4 import BeautifulSoup
import requests
import json

class metadataObj:
   metadata = {
    "doi": "undefined",
    "coreId": "undefined",
    "oai": "undefined",
    "identifiers": [],
    "title": "undefined",
    "authors": [],
    "enrichments": {
      "references": "undefined",
      "documentType": {
        "type": "undefined",
        "confidence": "undefined"
      },
      "citationCount": "undefined"
    },
    "contributors": [],
    "datePublished": "undefined",
    "abstract": "undefined",
    "downloadUrl": "undefined",
    "fullTextIdentifier": "undefined",
    "pdfHashValue": "undefined",
    "publisher": "undefined",
    "rawRecordXml": "undefined",
    "journals": [],
    "language": {
      "code": "undefined",
      "name": "undefined",
      "id": "undefined"
    },
    "relations": [],
    "year": "undefined",
    "topics": [],
    "subjects": [],
    "issn": "undefined",
    "fullText": "undefined"
    }

def main():

    keyword = "Thermodynamics"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}
    url = "http://scholar.google.com/scholar?hl=en&as_ylo=2012&as_yhi=2022&q=" + keyword

    request = requests.get(url, headers=headers)
    soup = BeautifulSoup(request.content, 'lxml')
    metadata_list = []

    for item in soup.select('[data-lid]'):

        currentArticle = metadataObj().metadata

        currentArticle["title"] = item.select("h3")[0].get_text()

        tempAuthor = item.select(".gs_a")[0].get_text().split("-")

        currentArticle["authors"] = tempAuthor[0].strip().split(',')[:2]
        currentArticle["contributors"] = tempAuthor[0].strip().split(',')[2:]

        currentArticle["enrichments"]["citationCount"] = ""

        journalYear = tempAuthor[1].split(",")

        currentArticle["datePublished"] = journalYear[-1].strip()
        currentArticle["year"] = currentArticle["datePublished"]

        print(currentArticle)

if __name__ == '__main__':
    main()
