from tkinter import *
import tkintermapview

sports_facilities: list = []
clients: list = []
workers: list = []

class SportsFacility:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.coordinates = self.get_coordinates()
        self.marker = map_widget.set_marker(self.coordinates[0], self.coordinates[1])

    def get_coordinates(self) -> list:
        import requests
        from bs4 import BeautifulSoup
        url = f"https://pl.wikipedia.org/wiki/{self.location}"
        response = requests.get(url).text
        soup = BeautifulSoup(response, "html.parser")
        longitude = float(soup.select(".longitude")[1].text.replace(",", "."))
        latitude = float(soup.select(".latitude")[1].text.replace(",", "."))
        return [latitude, longitude]

class Client:
    def __init__(self, name, location, location2):
        self.name = name
        self.location = location
        self.location2 = location2
        self.coordinates = self.get_coordinates()
        self.marker = map_widget.set_marker(self.coordinates[0], self.coordinates[1])

    def get_coordinates(self) -> list:
        import requests
        from bs4 import BeautifulSoup
        url = f"https://pl.wikipedia.org/wiki/{self.location}"
        response = requests.get(url).text
        soup = BeautifulSoup(response, "html.parser")
        longitude = float(soup.select(".longitude")[1].text.replace(",", "."))
        latitude = float(soup.select(".latitude")[1].text.replace(",", "."))
        return [latitude, longitude]

class Worker:
    def __init__(self, name, location, location2):
        self.name = name
        self.location = location
        self.location2 = location2
        self.coordinates = self.get_coordinates()
        self.marker = map_widget.set_marker(self.coordinates[0], self.coordinates[1])

    def get_coordinates(self) -> list:
        import requests
        from bs4 import BeautifulSoup
        url = f"https://pl.wikipedia.org/wiki/{self.location}"
        response = requests.get(url).text
        soup = BeautifulSoup(response, "html.parser")
        longitude = float(soup.select(".longitude")[1].text.replace(",", "."))
        latitude = float(soup.select(".latitude")[1].text.replace(",", "."))
        return [latitude, longitude]


def add_sports_facility(location=None):
    name = name
    location =location
    facility = SportsFacility(name, location)
    sports_facilities.append(facility)

    entry_name.delete(0, END)
    entry_location.delete(0, END)
    entry_name.focus()
    show_sports_facilities()

def show_sports_facilities():
    listbox_lista_obiektow.delete(0, END)
    for idx, facility in enumerate(sports_facilities):
        listbox_lista_obiektow.insert(idx, f"{idx+1}. {facility.name}")

def remove_sports_facility():
    i = listbox_lista_obiektow.index(ACTIVE)
    sports_facilities[i].marker.delete()
    sports_facilities.pop(i)
    show_sports_facilities()

def edit_sports_facility():
    i = listbox_lista_obiektow.index(ACTIVE)
    name = sports_facilities[i].name
    location = sports_facilities[i].location

    entry_name.insert(0, name)
    entry_location.insert(0, location)
    button_dodaj_placowke.config(text='Zapisz', command=lambda: update_sports_facility(i))

def update_sports_facility(i):
    new_name = entry_name.get()
    new_location = entry_location.get()

    sports_facilities[i].name = new_name
    sports_facilities[i].location = new_location
    sports_facilities[i].marker.delete()
    sports_facilities[i].coordinates = sports_facilities[i].get_coordinates()
    sports_facilities[i].marker = map_widget.set_marker(sports_facilities[i].coordinates[0], sports_facilities[i].coordinates[1])

    entry_name.delete(0, END)
    entry_location.delete(0, END)
    entry_name.focus()
    button_dodaj_placowke.config(text='Dodaj obiekt', command=add_sports_facility)
    show_sports_facilities()
