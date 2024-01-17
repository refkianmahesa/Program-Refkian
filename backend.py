from flask import Flask, render_template, request
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

app = Flask(__name__)

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

peringkat = ctrl.Consequent(np.arange(0, 11, 1), 'peringkat')
peringkat['rendah'] = fuzz.trimf(peringkat.universe, [0, 0, 5])
peringkat['sedang'] = fuzz.trimf(peringkat.universe, [0, 5, 10])
peringkat['tinggi'] = fuzz.trimf(peringkat.universe, [5, 10, 10])

# Create a ControlSystem and a ControlSystemSimulation
peringkat_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
peringkat_sim = ctrl.ControlSystemSimulation(peringkat_ctrl)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate_ranking', methods=['POST'])
def calculate_ranking():
    dt_value = int(request.form['daya_tarik'])
    aksesbilitas_value = int(request.form['aksesbilitas'])
    fasilitas_value = int(request.form['fasilitas'])
    pelayanan_value = int(request.form['pelayanan'])
    kebersihan_value = int(request.form['kebersihan'])
    promosi_value = int(request.form['promosi'])

    # Calculate the ranking
    attributes = {
        'daya_tarik': dt_value,
        'aksesbilitas': aksesbilitas_value,
        'fasilitas': fasilitas_value,
        'pelayanan': pelayanan_value,
        'kebersihan': kebersihan_value,
        'promosi': promosi_value
    }

    # Integrate your Fuzzy Logic calculation here
    peringkat_sim.input['daya_tarik'] = dt_value
    peringkat_sim.input['aksesbilitas'] = aksesbilitas_value
    peringkat_sim.input['fasilitas'] = fasilitas_value
    peringkat_sim.input['pelayanan'] = pelayanan_value
    peringkat_sim.input['kebersihan'] = kebersihan_value
    peringkat_sim.input['promosi'] = promosi_value

    peringkat_sim.compute()
    ranking = peringkat_sim.output['peringkat']

    return render_template('result.html', ranking=ranking)

if __name__ == '__main__':
    app.run(debug=True)
