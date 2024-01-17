import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import tkinter as tk
from tkinter import ttk

# Membuat variabel input

# tempat_wisata = {
#     'Tangga 2001', 'Tugu Rimau', 'Ayek Pacar','Oziel Garden','Green Paradise','Agrowisata Tanjung Sakti','Dempo Park',
#     'Curup 7 Kenangan','Kebun Raya Dempo','Kampung 4'  
# }

daya_tarik = ctrl.Antecedent(np.arange(0, 11, 1), 'daya_tarik')
aksesbilitas = ctrl.Antecedent(np.arange(0, 11, 1), 'aksesbilitas')
fasilitas = ctrl.Antecedent(np.arange(0, 11, 1), 'fasilitas')
pelayanan = ctrl.Antecedent(np.arange(0, 11, 1), 'pelayanan')
kebersihan = ctrl.Antecedent(np.arange(0, 11, 1), 'kebersihan')
promosi = ctrl.Antecedent(np.arange(0, 11, 1), 'promosi')


# Mendefinisikan fungsi keanggotaan
daya_tarik['sedikit'] = fuzz.trimf(daya_tarik.universe, [0, 0, 5])
daya_tarik['normal'] = fuzz.trimf(daya_tarik.universe, [0, 5, 10])
daya_tarik['tinggi'] = fuzz.trimf(daya_tarik.universe, [5, 10, 10])

aksesbilitas['jauh'] = fuzz.trimf(aksesbilitas.universe, [0, 0, 5])
aksesbilitas['normal'] = fuzz.trimf(aksesbilitas.universe, [0, 5, 10])
aksesbilitas['dekat'] = fuzz.trimf(aksesbilitas.universe, [5, 10, 10])

fasilitas['jelek'] = fuzz.trimf(fasilitas.universe, [0, 0, 5])
fasilitas['normal'] = fuzz.trimf(fasilitas.universe, [0, 5, 10])
fasilitas['baik'] = fuzz.trimf(fasilitas.universe, [5, 10, 10])

pelayanan['buruk'] = fuzz.trimf(pelayanan.universe, [0, 0, 5])
pelayanan['baik'] = fuzz.trimf(pelayanan.universe, [0, 5, 10])
pelayanan['memuaskan'] = fuzz.trimf(pelayanan.universe, [5, 10, 10])

kebersihan['kotor'] = fuzz.trimf(kebersihan.universe, [0, 0, 5])
kebersihan['bersih'] = fuzz.trimf(kebersihan.universe, [0, 5, 10])
kebersihan['sangat_bersih'] = fuzz.trimf(kebersihan.universe, [5, 10, 10])

promosi['kurang'] = fuzz.trimf(promosi.universe, [0, 0, 5])
promosi['cukup'] = fuzz.trimf(promosi.universe, [0, 5, 10])
promosi['baik'] = fuzz.trimf(promosi.universe, [5, 10, 10])

# Membuat variabel output
peringkat = ctrl.Consequent(np.arange(0, 11, 1), 'peringkat')

# Mendefinisikan fungsi keanggotaan peringkat
peringkat['rendah'] = fuzz.trimf(peringkat.universe, [0, 0, 5])
peringkat['sedang'] = fuzz.trimf(peringkat.universe, [0, 5, 10])
peringkat['tinggi'] = fuzz.trimf(peringkat.universe, [5, 10, 10])

# Membuat aturan fuzzy (seperti sebelumnya)

# Membuat sistem kontrol fuzzy (seperti sebelumnya)

# Membuat GUI menggunakan Tkinter
root = tk.Tk()
root.title("Penentuan Peringkat Tempat Wisata dengan Fuzzy Logic")

frame = ttk.Frame(root)
frame.pack(padx=20, pady=20)

dt_label = ttk.Label(frame, text="Daya Tarik:")
dt_label.grid(row=0, column=0, sticky="w")
dt_slider = ttk.Scale(frame, from_=0, to=10)
dt_slider.grid(row=0, column=1)

aksesbilitas_label = ttk.Label(frame, text="Aksesbilitas:")
aksesbilitas_label.grid(row=1, column=0, sticky="w")
aksesbilitas_slider = ttk.Scale(frame, from_=0, to=10)
aksesbilitas_slider.grid(row=1, column=1)

fasilitas_label = ttk.Label(frame, text="Fasilitas:")
fasilitas_label.grid(row=2, column=0, sticky="w")
fasilitas_slider = ttk.Scale(frame, from_=0, to=10)
fasilitas_slider.grid(row=2, column=1)

pelayanan_label = ttk.Label(frame, text="Pelayanan:")
pelayanan_label.grid(row=3, column=0, sticky="w")
pelayanan_slider = ttk.Scale(frame, from_=0, to=10)
pelayanan_slider.grid(row=3, column=1)

kebersihan_label = ttk.Label(frame, text="Kebersihan:")
kebersihan_label.grid(row=4, column=0, sticky="w")
kebersihan_slider = ttk.Scale(frame, from_=0, to=10)
kebersihan_slider.grid(row=4, column=1)

promosi_label = ttk.Label(frame, text="Promosi:")
promosi_label.grid(row=5, column=0, sticky="w")
promosi_slider = ttk.Scale(frame, from_=0, to=10)
promosi_slider.grid(row=5, column=1)

places = {
    'Tangga 2001': {'daya_tarik': 7, 'aksesbilitas': 4, 'fasilitas': 6, 'pelayanan': 8, 'kebersihan': 9, 'promosi': 7},
    'Tugu Rimau': {'daya_tarik': 8, 'aksesbilitas': 6, 'fasilitas': 7, 'pelayanan': 7, 'kebersihan': 8, 'promosi': 6},
    'Ayek Pacar': {'daya_tarik': 5, 'aksesbilitas': 3, 'fasilitas': 4, 'pelayanan': 5, 'kebersihan': 5, 'promosi': 4},
    'Oziel Garden': {'daya_tarik': 6, 'aksesbilitas': 7, 'fasilitas': 8, 'pelayanan': 8, 'kebersihan': 9, 'promosi': 7},
    'Green Paradise': {'daya_tarik': 9, 'aksesbilitas': 8, 'fasilitas': 9, 'pelayanan': 9, 'kebersihan': 9, 'promosi': 8},
    'Agrowisata Tanjung Sakti': {'daya_tarik': 7, 'aksesbilitas': 6, 'fasilitas': 6, 'pelayanan': 7, 'kebersihan': 8, 'promosi': 6},
    'Dempo Park': {'daya_tarik': 8, 'aksesbilitas': 8, 'fasilitas': 8, 'pelayanan': 8, 'kebersihan': 8, 'promosi': 7},
    'Curup 7 Kenangan': {'daya_tarik': 6, 'aksesbilitas': 5, 'fasilitas': 6, 'pelayanan': 6, 'kebersihan': 7, 'promosi': 5},
    'Kebun Raya Dempo': {'daya_tarik': 7, 'aksesbilitas': 6, 'fasilitas': 7, 'pelayanan': 7, 'kebersihan': 8, 'promosi': 6},
    'Kampung 4': {'daya_tarik': 5, 'aksesbilitas': 4, 'fasilitas': 5, 'pelayanan': 6, 'kebersihan': 6, 'promosi': 5},
}

# Menggunakan sistem kontrol fuzzy yang telah dibuat sebelumnya
def hitung_peringkat(place_attributes):
    dt_value = place_attributes['daya_tarik']
    aksesbilitas_value = place_attributes['aksesbilitas']
    fasilitas_value = place_attributes['fasilitas']
    pelayanan_value = place_attributes['pelayanan']
    kebersihan_value = place_attributes['kebersihan']
    promosi_value = place_attributes['promosi']

    peringkat_sim.input['daya_tarik'] = dt_value
    peringkat_sim.input['aksesbilitas'] = aksesbilitas_value
    peringkat_sim.input['fasilitas'] = fasilitas_value
    peringkat_sim.input['pelayanan'] = pelayanan_value
    peringkat_sim.input['kebersihan'] = kebersihan_value
    peringkat_sim.input['promosi'] = promosi_value

    peringkat_sim.compute()
    return peringkat_sim.output['peringkat']

# Membuat sistem kontrol fuzzy
rule1 = ctrl.Rule(daya_tarik['sedikit'] | aksesbilitas['jauh'] | fasilitas['jelek'] | pelayanan['buruk'] | kebersihan['kotor'] | promosi['kurang'], peringkat['rendah'])
rule2 = ctrl.Rule(daya_tarik['normal'] & aksesbilitas['normal'] & fasilitas['normal'] & pelayanan['baik'] & kebersihan['bersih'] & promosi['cukup'], peringkat['sedang'])
rule3 = ctrl.Rule(daya_tarik['tinggi'] | aksesbilitas['dekat'] | fasilitas['baik'] | pelayanan['memuaskan'] | kebersihan['sangat_bersih'] | promosi['baik'], peringkat['tinggi'])


peringkat_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
peringkat_sim = ctrl.ControlSystemSimulation(peringkat_ctrl)

rankings = {}
for place, attributes in places.items():
    ranking = hitung_peringkat(attributes)
    rankings[place] = ranking

# Sort places by their rankings
sorted_places = sorted(rankings.items(), key=lambda x: x[1], reverse=True)

# Print the sorted places
for i, (place, ranking) in enumerate(sorted_places[:10]):
    print(f"Rank {i + 1}: {place} - Peringkat: {ranking:.2f}")





root.mainloop()
