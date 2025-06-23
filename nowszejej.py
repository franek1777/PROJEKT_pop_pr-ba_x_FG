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
        response_html = BeautifulSoup(response, "html.parser")
        longitude = float(response_html.select(".longitude")[1].text.replace(",", "."))
        latitude = float(response_html.select(".latitude")[1].text.replace(",", "."))
        print(longitude)
        print(latitude)
        return [latitude, longitude]

class Client:
    def __init__(self, name, location, facility_name):
        self.name = name
        self.location = location
        self.facility_name = facility_name
        self.coordinates = self.get_coordinates()
        self.marker = map_widget.set_marker(self.coordinates[0], self.coordinates[1])

    def get_coordinates(self) -> list:
        import requests
        from bs4 import BeautifulSoup
        url = f"https://pl.wikipedia.org/wiki/{self.location}"
        response = requests.get(url).text
        response_html = BeautifulSoup(response, "html.parser")
        longitude = float(response_html.select(".longitude")[1].text.replace(",", "."))
        latitude = float(response_html.select(".latitude")[1].text.replace(",", "."))
        print(longitude)
        print(latitude)
        return [latitude, longitude]

class Worker:
    def __init__(self, name, location, facility_name):
        self.name = name
        self.location = location
        self.facility_name = facility_name
        self.coordinates = self.get_coordinates()
        self.marker = map_widget.set_marker(self.coordinates[0], self.coordinates[1])

    def get_coordinates(self) -> list:
        import requests
        from bs4 import BeautifulSoup
        url = f"https://pl.wikipedia.org/wiki/{self.location}"
        response = requests.get(url).text
        response_html = BeautifulSoup(response, "html.parser")
        longitude = float(response_html.select(".longitude")[1].text.replace(",", "."))
        latitude = float(response_html.select(".latitude")[1].text.replace(",", "."))
        print(longitude)
        print(latitude)
        return [latitude, longitude]

def create_clients():
    i = listbox_lista_obiketow.index(ACTIVE)
    selected_facility = sports_facilities[i].name
    visible_clients = [c for c in clients if c.facility_name == selected_facility]
    for c in visible_clients:
        c.marker = map_widget.set_marker(c.coordinates[0], c.coordinates[1])

def create_workers():
    i = listbox_lista_obiketow.index(ACTIVE)
    selected_facility = sports_facilities[i].name
    visible_workers = [w for w in workers if w.facility_name == selected_facility]
    for w in visible_workers:
        w.marker = map_widget.set_marker(w.coordinates[0], w.coordinates[1])

def add_facility():
    name = entry_name.get()
    location = entry_location.get()
    facility = SportsFacility(name, location)
    sports_facilities.append(facility)

    entry_name.delete(0, END)
    entry_location2.delete(0, END)
    entry_location.delete(0, END)
    entry_name.focus()

    show_facilities()

def show_facilities():
    listbox_lista_obiketow.delete(0, END)
    for idx, facility in enumerate(sports_facilities):
        listbox_lista_obiketow.insert(idx, f'{idx + 1}. {facility.name}')

def remove_facility():
    i = listbox_lista_obiketow.index(ACTIVE)
    sports_facilities[i].marker.delete()
    sports_facilities.pop(i)
    show_facilities()

def edit_facility():
    i = listbox_lista_obiketow.index(ACTIVE)
    name = sports_facilities[i].name
    location = sports_facilities[i].location

    entry_name.insert(0, name)
    entry_location.insert(0, location)

    button_dodaj_placowke.config(text='zapisz', command=lambda: update_facility(i))

def update_facility(i):
    new_name = entry_name.get()
    new_location = entry_location.get()

    sports_facilities[i].name = new_name
    sports_facilities[i].location = new_location

    sports_facilities[i].marker.delete()
    sports_facilities[i].coordinates = sports_facilities[i].get_coordinates()
    sports_facilities[i].marker = map_widget.set_marker(sports_facilities[i].coordinates[0], sports_facilities[i].coordinates[1])

    entry_name.delete(0, END)
    entry_location.delete(0, END)
    entry_location2.delete(0, END)
    entry_name.focus()

    button_dodaj_placowke.config(text='Dodaj obiekt', command=add_facility)
    show_facilities()

def show_facility_workers():
    i = listbox_lista_obiketow.index(ACTIVE)
    name = sports_facilities[i].name
    location = sports_facilities[i].location
    label_szczegoly_name_wartosc.config(text=name)
    label_szczegoly_location_wartosc.config(text=location)
    label_szczegoly_location2_wartosc.config(text='...')
    create_workers()
    map_widget.set_position(sports_facilities[i].coordinates[0], sports_facilities[i].coordinates[1])
    map_widget.set_zoom(17)

def show_facility_clients():
    i = listbox_lista_obiketow.index(ACTIVE)
    name = sports_facilities[i].name
    location = sports_facilities[i].location
    label_szczegoly_name_wartosc.config(text=name)
    label_szczegoly_location_wartosc.config(text=location)
    label_szczegoly_location2_wartosc.config(text='...')
    create_clients()
    map_widget.set_position(sports_facilities[i].coordinates[0], sports_facilities[i].coordinates[1])
    map_widget.set_zoom(17)