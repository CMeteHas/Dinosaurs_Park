import random
import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import ImageTk, Image

class Dinosaur:
    def __init__(self, name, species, power):
        self.name = name
        self.species = species
        self.power = power
        self.photo_path = None

class DinosaurPark:
    def __init__(self):
        self.dinosaurs = []

    def add_dinosaur(self, dinosaur):
        self.dinosaurs.append(dinosaur)

    def remove_dinosaur(self, dinosaur):
        self.dinosaurs.remove(dinosaur)

    def list_dinosaurs(self):
        dinosaur_list = []
        for dinosaur in self.dinosaurs:
            dinosaur_info = f"Name: {dinosaur.name}, Species: {dinosaur.species}, Power: {dinosaur.power}"
            dinosaur_list.append(dinosaur_info)
        return dinosaur_list

    def get_random_dinosaur(self):
        if self.dinosaurs:
            return random.choice(self.dinosaurs)
        else:
            return None

    def get_species_list(self):
        species_list = set()
        for dinosaur in self.dinosaurs:
            species_list.add(dinosaur.species)
        return list(species_list)

    def get_name_list(self):
        name_list = []
        for dinosaur in self.dinosaurs:
            name_list.append(dinosaur.name)
        return name_list
    
    def get_power_list(self):
        power_list = []
        for dinosaur in self.dinosaurs:
            power_list.append(dinosaur)
        return power_list

def add_dinosaur():
    name = name_entry.get()
    species = species_entry.get()
    power_txt = power_entry.get()
    power = int(power_txt)
    if name and species and power:
        dinosaur = Dinosaur(name, species, power)
        park.add_dinosaur(dinosaur)
        messagebox.showinfo("Bilgi", f"Yeni dinozor eklendi: {name} {species} ({power})")
        name_entry.delete(0, tk.END)
        species_entry.delete(0, tk.END)
        power_entry.delete(0,tk.END)
        refresh_dinosaur_list()
    else:
        messagebox.showerror("Hata", "Lütfen dinozor adı ve türünü girin.")

def remove_random_dinosaur():
    dinosaur = park.get_random_dinosaur()
    if dinosaur:
        park.remove_dinosaur(dinosaur)
        messagebox.showinfo("Bilgi", f"Rastgele bir dinozor kaldırıldı: {dinosaur.name} ({dinosaur.species})")
        refresh_dinosaur_list()
    else:
        messagebox.showinfo("Bilgi", "Dinozor yok, kaldırılacak dinozor bulunamadı.")

def add_photo(dinosaur):
    file_path = filedialog.askopenfilename(title="Fotoğraf Seç", filetypes=[("Image files", "*.jpg *.jpeg *.png")])
    if file_path:
        dinosaur.photo_path = file_path
        messagebox.showinfo("Bilgi", "Fotoğraf başarıyla eklendi.")
        refresh_dinosaur_list()

def refresh_dinosaur_list():
    listbox.delete(0, tk.END)
    for dinosaur in park.dinosaurs:
        dinosaur_info = f"Name: {dinosaur.name}, Species: {dinosaur.species}, Power: {dinosaur.power}"
        listbox.insert(tk.END, dinosaur_info)
        if dinosaur.photo_path:
            photo = Image.open(dinosaur.photo_path)
            photo = photo.resize((50, 50), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(photo)
            photo_label = tk.Label(root, image=photo)
            photo_label.image = photo
            photo_label.pack(side=tk.LEFT)
        else:
            empty_label = tk.Label(root, width=8)
            empty_label.pack(side=tk.LEFT)
        photo_button = tk.Button(root, text="Fotoğraf Ekle", command=lambda d=dinosaur: add_photo(d))
        photo_button.pack(side=tk.LEFT)

# Dinozor parkı oluşturma
park = DinosaurPark()

# Tkinter arayüzü
root = tk.Tk()
root.title("Dinozor Parkı")

name_label = tk.Label(root, text="Dinozor Adı:")
name_label.pack()

name_entry = tk.Entry(root)
name_entry.pack()

species_label = tk.Label(root, text="Dinozor Türü:")
species_label.pack()

species_entry = tk.Entry(root)
species_entry.pack()

power_label = tk.Label(root, text="Dinozorun Gücü: ")
power_label.pack()

power_entry = tk.Entry(root)
power_entry.pack()

add_button = tk.Button(root, text="Dinozor Ekle", command=add_dinosaur)
add_button.pack()

remove_button = tk.Button(root, text="Rastgele Dinozor Kaldır", command=remove_random_dinosaur)
remove_button.pack()

listbox = tk.Listbox(root)
listbox.pack(fill=tk.BOTH, expand=True)

refresh_dinosaur_list()

root.mainloop()
