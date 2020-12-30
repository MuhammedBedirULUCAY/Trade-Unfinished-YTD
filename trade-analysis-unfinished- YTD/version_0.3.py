from re import findall
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import selenium


def get_datas(sites):

    for url in sites:
        print(url)

    for url in sites:
        url = sites;
        print(url);
        myheaders = {"User-Agent" : "Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; Lumia 950) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Mobile Safari/537.36 Edge/15.14977"}
        veriler = []

        r = requests.get(url,headers = myheaders)

        while r.status_code == 406:
            nval = input("Enter new headers")
            r = requests.get(url,headers = {"User-Agent" : nval})
            soup = BeautifulSoup(r.content(),"lxml")
            datas = soup.find("table",attrs={"id" : "curr_table"}).select("table > tbody")
            for data in datas:
                veriler = data.text.split("\n")

        dates = []
        nows = []
        opens = []
        highest = [] 
        lowest = [] 
        volume = [] 
        differents = []

        c = 0
        for i in veriler:
            type = c % 8 - 2  
            if type >= 0:
                if type == 0:
                    dates.append(i)
                elif type == 1:
                    nows.append(i)
                elif type == 2:
                    opens.append(i)
                elif type == 3:
                    highest.append(i)
                elif type == 4:
                    lowest.append(i)    
                else :
                    var = i.split(" ")
                    volume.append(var[0])
                    differents.append(var[1])    
            c += 1
        
        print("DATE\t\tNOW\tOPENS\t  HIGH\t     LOW      VOLUME\t DIFFERENT")
        for i in range(0,len(dates)):
            print(dates[i]," > ",nows[i]," > ",opens[i], " > ",highest[i], " > ",lowest[i], " > ",volume[i], " > ", differents[i])
        print("===============================================================================================================")


def main():

    base = "https://tr.investing.com"
    directory = "~/Downloads"
    data = "-historical-data"
    url = "https://tr.investing.com/equities"
    
    headers = {"User-Agent" : "Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; Lumia 950) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Mobile Safari/537.36 Edge/15.14977"}
    
    source = requests.get(url,headers = headers)
    print(source)
    
    while source.status_code ==  406:
        nval = input("Enter new headers : ")
        source = requests.get(url,headers = {"User-Agent" : nval})
    
    print(source)
    
    soup = BeautifulSoup(source.content,"lxml")

    tablo = soup.find_all("td", attrs={"class" : "bold left noWrap elp plusIconTd"})
    filter = soup.find("select",attrs={"id":"stocksFilter"})
    
    dowland_sites = []
    for cmpny in tablo:
        dowland_sites.append(base + str(cmpny.a.get('href'))+data)
    
    print("++++++++++++++++++++++++++++++++++++")
    get_datas(dowland_sites)
    print("++++++++++++++++++++++++++++++++++++")

    
if __name__ == "__main__":
    main()    
    
