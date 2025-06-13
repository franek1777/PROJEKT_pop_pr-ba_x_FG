from tkinter import *
import tkintermapview

import requests
from bs4 import BeautifulSoup

# Bazy danych
sports_facilities = []
clients = []
workers = []


class SportsFacility:
    def __init__(self, facility_type, location):
        self.facility_type = facility_type
        self.location = location
        self.coordinates = self.get_coordinates()

    def get_coordinates(self):
        try:
            url = f"https://pl.wikipedia.org/wiki/{self.location}"
            response = requests.get(url).text
            soup = BeautifulSoup(response, "html.parser")
            latitude = float(soup.select(".latitude")[1].text.replace(",", "."))
            longitude = float(soup.select(".longitude")[1].text.replace(",", "."))
            return [latitude, longitude]
        except Exception as e:
            print(f"Błąd przy pobieraniu współrzędnych dla {self.location}: {e}")
            return [0, 0]


class Client:
    def __init__(self, name, illness, facility_location):
        self.name = name
        self.illness = illness
        self.facility_location = facility_location
        self.coordinates = self.get_coordinates()

    def get_coordinates(self):
        try:
            url = f"https://pl.wikipedia.org/wiki/{self.facility_location}"
            response = requests.get(url).text
            soup = BeautifulSoup(response, "html.parser")
            latitude = float(soup.select(".latitude")[1].text.replace(",", "."))
            longitude = float(soup.select(".longitude")[1].text.replace(",", "."))
            return [latitude, longitude]
        except Exception as e:
            print(f"Błąd przy pobieraniu współrzędnych klienta: {e}")
            return [0, 0]


class Worker:
    def __init__(self, name, facility_name, location):
        self.name = name
        self.facility_name = facility_name
        self.location = location
        self.coordinates = self.get_coordinates()

    def get_coordinates(self):
        try:
            url = f"https://pl.wikipedia.org/wiki/{self.location}"
            response = requests.get(url).text
            soup = BeautifulSoup(response, "html.parser")
            latitude = float(soup.select(".latitude")[1].text.replace(",", "."))
            longitude = float(soup.select(".longitude")[1].text.replace(",", "."))
            return [latitude, longitude]
        except Exception as e:
            print(f"Błąd przy pobieraniu współrzędnych pracownika: {e}")
            return [0, 0]


root = Tk()
root.geometry("1200x760")
root.title("System Zarządzania Kompleksami Sportowymi")

ramka_lista_obiektow = Frame(root)
ramka_formularz = Frame(root)
ramka_szczegoly_obiektow = Frame(root)
ramka_mapa = Frame(root)

ramka_lista_obiektow.grid(row=0, column=0)
ramka_formularz.grid(row=0, column=1)
ramka_szczegoly_obiektow.grid(row=1, column=0, columnspan=2)
ramka_mapa.grid(row=2, column=0, columnspan=2)

# Mapa
map_widget = tkintermapview.TkinterMapView(ramka_mapa, width=1200, height=500, corner_radius=5)
map_widget.grid(row=0, column=0, columnspan=2)
map_widget.set_position(52.23, 21.0)
map_widget.set_zoom(6)

# Formularz (przykładowy)
Label(ramka_formularz, text="Formularz").grid(row=0, column=0, columnspan=2)
Label(ramka_formularz, text="Imię:").grid(row=1, column=0, sticky=W)
entry_name = Entry(ramka_formularz)
entry_name.grid(row=1, column=1)
Label(ramka_formularz, text="Miejscowość:").grid(row=2, column=0, sticky=W)
entry_location = Entry(ramka_formularz)
entry_location.grid(row=2, column=1)

# Przykładowy przycisk dodania kompleksu

def dodaj_sports_facility():
    name = entry_name.get()
    location = entry_location.get()
    obiekt = SportsFacility(name, location)
    sports_facilities.append(obiekt)
    map_widget.set_marker(obiekt.coordinates[0], obiekt.coordinates[1], text=name)

Button(ramka_formularz, text="Dodaj kompleks", command=dodaj_sports_facility).grid(row=3, column=0, columnspan=2)

root.mainloop()