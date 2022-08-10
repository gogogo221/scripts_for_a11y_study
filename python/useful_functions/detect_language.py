from langdetect import detect
import requests
import html2text

from func_timeout import func_timeout



def detect_language(url):
    try:
        #func_timeout is to make sure program doesnt stall trying to get url
        response = func_timeout(10, requests.get, args=(url,) )  # Requests to get url html
    except:
        return "PAGE LOAD ERROR"
    rep = response.text # html 
    txt=html2text.html2text(rep) # converting html to text
    response.close() # Close your Request
    lang = ""
    try:
        lang = detect(txt)
    except: 
        lang = "NO TEXT"
    return lang# Return language value Exp: (en, ar, pl, es) ...

#test code
def main():
   print(detect_language("http://1xbet-sx.xyz"))

if __name__ == "__main__":
    main()