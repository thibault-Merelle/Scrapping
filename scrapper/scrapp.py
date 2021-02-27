from bs4 import BeautifulSoup
import requests


class scrapp_VR:

    def __init__(self):
        self.page = requests.get("https://www.vintagerides.com/calendrier-des-departs")
        self.soup = BeautifulSoup(self.page.content, 'html.parser')
        self.mytitle = []
        self.mydest = []
        self.mydates_begin = []
        self.mydates_end = []
        self.mydates_year = []
        self.mylevel = []
        self.dict = {}
        self.list_dict = []

    
    def find_title(self):
        for item in self.soup.find_all(class_='departurecard-title'):
            self.mytitle.append(item.text.strip())


    def find_dates(self):
        for item in self.soup.find_all(class_='tripcard-departure-dates'):
            year = item.text.split()[-1]
            tempo_list = item.text.split(str(year))
            tempo_list[-1] = str(year)
            self.mydates_begin.append(tempo_list[0])
            self.mydates_end.append(tempo_list[1])
            self.mydates_year.append(tempo_list[-1])


    def find_destinations_levels(self):
        i=0
        for item in self.soup.find_all(class_='infos-info'):
            tempo_list = item.text.split()
            if i%2!=0:
                if len(item) > 1:
                    self.mylevel.append("-".join(tempo_list[1:]))
                else:
                    self.mylevel.append("".join(tempo_list[1:]))
            else :
                if len(item) > 1:
                    self.mydest.append("-".join(tempo_list[1:]))
                else:
                    self.mydest.append("".join(tempo_list[1:]))
            i+=1
    def create_dict(self):
        for ii, i in enumerate(self.mytitle):
            self.dict = {"title" : i, "destination" : self.mydest[ii], "departure_date" : self.mydates_begin[ii], "end_date" : self.mydates_end[ii], "year" : self.mydates_year[ii], "level" : self.mylevel[ii]}
            self.list_dict.append(self.dict)

