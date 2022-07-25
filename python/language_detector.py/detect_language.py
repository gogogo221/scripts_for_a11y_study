from langdetect import detect
import requests
import html2text

def Detect_Lang(url):
    response = requests.get(url) # Requests to get url html
    rep = response.text # html 
    txt=html2text.html2text(rep) # converting html to text
    response.close() # Close your Request
    return detect(txt) # Return language value Exp: (en, ar, pl, es) ...


def main():
   print(Detect_Lang("https://www.infoworld.com/article/3239675/virtualenv-and-venv-python-virtual-environments-explained.html"))

if __name__ == "__main__":
    main()