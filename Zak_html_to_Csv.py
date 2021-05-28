from bs4 import BeautifulSoup
import requests
import csv
source=requests.get("https://coreyms.com/").text
soup=BeautifulSoup(source,"lxml")

csv_file=open("web_scrape.csv","w")
csv_writer=csv.writer(csv_file)
csv_writer.writerow(["headlines","summary","youtube"])

for article in soup.find_all("article"):

        headline=article.h2.a.text
        print(headline)
        summary=article.find("div","entry-content").text
        print(summary)
        try:
            vid_src=article.find("iframe",class_="youtube-player")["src"]
            print(vid_src)
            print()
        except:
            vid_src=None
            print(vid_src)
            print()
        csv_writer.writerow([headline,summary,vid_src])
csv_file.close()
