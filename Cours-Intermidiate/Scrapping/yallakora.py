import requests
from bs4 import BeautifulSoup
import csv

# date = "3/18/2023"
date = "3/30/2023"
page = requests.get(f"https://www.yallakora.com/match-center/مركز-المباريات?date={date}")

def main(page) :
    src_code = page.content
    soup = BeautifulSoup(src_code,'lxml')
    champions = soup.find_all('div',{'class':'matchCard'})
    
    def get_champion_info(champion) :
        champion_title = champion.find('div',{'class':'title'}).find('h2').text.strip()
        all_match = champion.find('ul').find_all('li')

        print("___________________________________________________________________________")
        print(f"<<<| {champion_title} |>>>")
        nbr_match = len(all_match)
        for j in range(nbr_match) :
            #** get team
            teamA = all_match[j].find('div',{'class':'teamA'}).find('p').text.strip()
            teamB = all_match[j].find('div',{'class':'teamB'}).find('p').text.strip()
            score = all_match[j].find('div',{'class':'MResult'}).find_all('span',{'class':'score'})
            time = all_match[j].find('div',{'class':'MResult'}).find('span',{'class':'time'}).text.strip()

            print(f"{teamA} {score[0].text.strip()}-{score[1].text.strip()} {teamB} ==> [{time}]")
            f = open("data.csv" , "a" , encoding="utf-8")
            f.write(f"{teamA} , {score[0].text.strip()}-{score[1].text.strip()} , {teamB} , [{time}]\n")
            f.close()
            
        

    #** get all champion from list champion
    nbr_champions = len(champions)
    for i in range(nbr_champions) :
        get_champion_info(champions[i])

main(page)
