import requests
from bs4 import BeautifulSoup


file = open("players.txt", "a")
alph = "ABCDEFGHIJKLM"  #need this to split beacuse of this piece of shit website
alph2 = "NOPQRSTUVWXYZ" #more than 20 requests/min will put you in timeout, wait in between calls
url = "https://www.pro-football-reference.com/players/"

for j in range(len(alph2)):
    newurl = url + alph2[j] + "/"
    response = requests.get(newurl)

    soup = BeautifulSoup(response.content, 'lxml')

    p_tag = soup.find_all("p")
    a_tag = soup.find_all("a")

    for i in range(len(a_tag)):
        href = a_tag[i].attrs['href']

        check = "/players/" + alph2[j] + "/"

        if check in href:
            file.write(a_tag[i].text)
            file.write("\n")
        
        if a_tag[i].text == "Return to Top":
            break
