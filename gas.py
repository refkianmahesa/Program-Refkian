from flask import Flask, render_template, request
import numpy as np
import skfuzzy as fuzz

app = Flask(__name__)

# Membuat variabel lingustik dan fungsi keanggotaan
daya_tarik = np.arange(0, 11, 1)
aksesbilitas = np.arange(0, 11, 1)
fasilitas = np.arange(0, 11, 1)
pelayanan = np.arange(0, 11, 1)
kebersihan = np.arange(0, 11, 1)
promosi = np.arange(0, 11, 1)
peringkat = np.arange(0, 101, 1)

# Membuat fungsi keanggotaan untuk setiap variabel
daya_tarik_lo = fuzz.trimf(daya_tarik, [0, 0, 5])
daya_tarik_md = fuzz.trimf(daya_tarik, [0, 5, 10])
daya_tarik_hi = fuzz.trimf(daya_tarik, [5, 10, 10])

aksesbilitas_lo = fuzz.trimf(aksesbilitas, [0, 0, 5])
aksesbilitas_md = fuzz.trimf(aksesbilitas, [0, 5, 10])
aksesbilitas_hi = fuzz.trimf(aksesbilitas, [5, 10, 10])

fasilitas_lo = fuzz.trimf(fasilitas, [0, 0, 5])
fasilitas_md = fuzz.trimf(fasilitas, [0, 5, 10])
fasilitas_hi = fuzz.trimf(fasilitas, [5, 10, 10])

pelayanan_lo = fuzz.trimf(pelayanan, [0, 0, 5])
pelayanan_md = fuzz.trimf(pelayanan, [0, 5, 10])
pelayanan_hi = fuzz.trimf(pelayanan, [5, 10, 10])

kebersihan_lo = fuzz.trimf(kebersihan, [0, 0, 5])
kebersihan_md = fuzz.trimf(kebersihan, [0, 5, 10])
kebersihan_hi = fuzz.trimf(kebersihan, [5, 10, 10])

promosi_lo = fuzz.trimf(promosi, [0, 0, 5])
promosi_md = fuzz.trimf(promosi, [0, 5, 10])
promosi_hi = fuzz.trimf(promosi, [5, 10, 10])

# Definisikan fungsi keanggotaan untuk variabel-variabel lainnya

# Membuat aturan fuzzy
rules = []

# Fungsi yang menggabungkan semua aturan fuzzy
def fuzzy_inference(features):
    aggregated = np.zeros_like(peringkat)
    for feature in features:
        daya_tarik_level_lo = fuzz.interp_membership(daya_tarik, daya_tarik_lo, feature[0])
        daya_tarik_level_md = fuzz.interp_membership(daya_tarik, daya_tarik_md, feature[0])
        daya_tarik_level_hi = fuzz.interp_membership(daya_tarik, daya_tarik_hi, feature[0])

        aksesbilitas_level_lo = fuzz.interp_membership(aksesbilitas, aksesbilitas_lo, feature[0])
        aksesbilitas_level_md = fuzz.interp_membership(aksesbilitas, aksesbilitas_md, feature[0])
        aksesbilitas_level_hi = fuzz.interp_membership(aksesbilitas, aksesbilitas_hi, feature[0])

        pelayanan_level_lo = fuzz.interp_membership(pelayanan, pelayanan_lo, feature[0])
        pelayanan_level_md = fuzz.interp_membership(pelayanan, pelayanan_md, feature[0])
        pelayanan_level_hi = fuzz.interp_membership(pelayanan, pelayanan_hi, feature[0])

        fasilitas_level_lo = fuzz.interp_membership(fasilitas, fasilitas_lo, feature[0])
        fasilitas_level_md = fuzz.interp_membership(fasilitas, fasilitas_md, feature[0])
        fasilitas_level_hi = fuzz.interp_membership(fasilitas, fasilitas_hi, feature[0])

        kebersihan_level_lo = fuzz.interp_membership(kebersihan, kebersihan_lo, feature[0])
        kebersihan_level_md = fuzz.interp_membership(kebersihan, kebersihan_md, feature[0])
        kebersihan_level_hi = fuzz.interp_membership(kebersihan, kebersihan_hi, feature[0])

        promosi_level_lo = fuzz.interp_membership(promosi, promosi_lo, feature[0])
        promosi_level_md = fuzz.interp_membership(promosi, promosi_md, feature[0])
        promosi_level_hi = fuzz.interp_membership(promosi, promosi_hi, feature[0])
        
        # Hitung tingkat keanggotaan untuk variabel-variabel lainnya
        
        # Terapkan aturan fuzzy
        for rule in rules:
            rule_activation = np.fmin(daya_tarik_level_lo, rule[0])
            rule_activation = np.fmin(aksesbilitas_level_lo, rule_activation)
            rule_activation = np.fmin(fasilitas_level_lo, rule_activation)
            rule_activation = np.fmin(pelayanan_level_lo, rule_activation)
            rule_activation = np.fmin(kebersihan_level_lo, rule_activation)
            rule_activation = np.fmin(promosi_level_lo, rule_activation)
            
            # Gabungkan hasil aturan
            aggregated = np.fmax(aggregated, np.fmin(rule_activation, peringkat))
            
        return aggregated
    
destinations = [
    {
        'name': 'Tugu Rimau',
        'image': 'tugu_rimau.jpeg',
        'features': [
            {'name': 'daya_tarik', 'label': 'Daya Tarik'},
            {'name': 'aksesbilitas', 'label': 'Aksesbilitas'},
            {'name': 'fasilitas', 'label': 'Fasilitas'},
            {'name': 'pelayanan', 'label': 'Pelayanan'},
            {'name': 'kebersihan', 'label': 'Kebersihan'},
            {'name': 'promosi', 'label': 'Promosi'}
        ]
    },

    {
        'name': 'Tangga 2001',
        'image': 'tangga_2001.jpg',
        'features': [
            {'name': 'daya_tarik', 'label': 'Daya Tarik'},
            {'name': 'aksesbilitas', 'label': 'Aksesbilitas'},
            {'name': 'fasilitas', 'label': 'Fasilitas'},
            {'name': 'pelayanan', 'label': 'Pelayanan'},
            {'name': 'kebersihan', 'label': 'Kebersihan'},
            {'name': 'promosi', 'label': 'Promosi'}
        ]
    },
     {
        'name': 'Ayek Pacar',
        'image': 'tugu_rimau.jpeg',
        'features': [
            {'name': 'daya_tarik', 'label': 'Daya Tarik'},
            {'name': 'aksesbilitas', 'label': 'Aksesbilitas'},
            {'name': 'fasilitas', 'label': 'Fasilitas'},
            {'name': 'pelayanan', 'label': 'Pelayanan'},
            {'name': 'kebersihan', 'label': 'Kebersihan'},
            {'name': 'promosi', 'label': 'Promosi'}
        ]
    },
     {
        'name': 'Oziel Garden',
        'image': 'green_paradise.jpg',
        'features': [
            {'name': 'daya_tarik', 'label': 'Daya Tarik'},
            {'name': 'aksesbilitas', 'label': 'Aksesbilitas'},
            {'name': 'fasilitas', 'label': 'Fasilitas'},
            {'name': 'pelayanan', 'label': 'Pelayanan'},
            {'name': 'kebersihan', 'label': 'Kebersihan'},
            {'name': 'promosi', 'label': 'Promosi'}
        ]
    },
     {
        'name': 'Agrowisata Tanjung Sakti',
        'image': 'tanjung_sakti.jpg',
        'features': [
            {'name': 'daya_tarik', 'label': 'Daya Tarik'},
            {'name': 'aksesbilitas', 'label': 'Aksesbilitas'},
            {'name': 'fasilitas', 'label': 'Fasilitas'},
            {'name': 'pelayanan', 'label': 'Pelayanan'},
            {'name': 'kebersihan', 'label': 'Kebersihan'},
            {'name': 'promosi', 'label': 'Promosi'}
        ]
    },
     {
        'name': 'Dempo Park',
        'image': 'dempo_park.jpeg',
        'features': [
            {'name': 'daya_tarik', 'label': 'Daya Tarik'},
            {'name': 'aksesbilitas', 'label': 'Aksesbilitas'},
            {'name': 'fasilitas', 'label': 'Fasilitas'},
            {'name': 'pelayanan', 'label': 'Pelayanan'},
            {'name': 'kebersihan', 'label': 'Kebersihan'},
            {'name': 'promosi', 'label': 'Promosi'}
        ]
    },
     {
        'name': 'Curup 7 Kenangan',
        'image': 'curup.jpeg',
        'features': [
            {'name': 'daya_tarik', 'label': 'Daya Tarik'},
            {'name': 'aksesbilitas', 'label': 'Aksesbilitas'},
            {'name': 'fasilitas', 'label': 'Fasilitas'},
            {'name': 'pelayanan', 'label': 'Pelayanan'},
            {'name': 'kebersihan', 'label': 'Kebersihan'},
            {'name': 'promosi', 'label': 'Promosi'}
        ]
    },
     {
        'name': 'Kebun Raya Dempo',
        'image': 'kebun_raya.jpeg',
        'features': [
            {'name': 'daya_tarik', 'label': 'Daya Tarik'},
            {'name': 'aksesbilitas', 'label': 'Aksesbilitas'},
            {'name': 'fasilitas', 'label': 'Fasilitas'},
            {'name': 'pelayanan', 'label': 'Pelayanan'},
            {'name': 'kebersihan', 'label': 'Kebersihan'},
            {'name': 'promosi', 'label': 'Promosi'}
        ]
    },
     {
        'name': 'Kampung 4',
        'image': 'kampung4.jpeg',
        'features': [
            {'name': 'daya_tarik', 'label': 'Daya Tarik'},
            {'name': 'aksesbilitas', 'label': 'Aksesbilitas'},
            {'name': 'fasilitas', 'label': 'Fasilitas'},
            {'name': 'pelayanan', 'label': 'Pelayanan'},
            {'name': 'kebersihan', 'label': 'Kebersihan'},
            {'name': 'promosi', 'label': 'Promosi'}
        ]
    },
]

@app.route('/')
def index():
    return render_template('index.html', destinations=destinations)

@app.route('/predict', methods=['POST'])
def predict():
    # Ambil data form dari request
    features = []
    
    for destination in destinations:
        feature_vector = []
        for feature in ['daya_tarik', 'aksesbilitas', 'fasilitas', 'pelayanan', 'kebersihan', 'promosi']:
            feature_value = float(request.form[f'{destination}_{feature}'])
            feature_vector.append(feature_value)
        features.append(feature_vector)
    
    # Hitung peringkat berdasarkan aturan fuzzy
    rankings = fuzzy_inference(features)

    # Sorting peringkat dan kembalikan hasil
    ranked_destinations = list(zip(destinations, rankings))
    ranked_destinations.sort(key=lambda x: x[1], reverse=True)
    
    return render_template('prediction.html', rankings=ranked_destinations)

if __name__ == '__main__':
    app.run(debug=True)
