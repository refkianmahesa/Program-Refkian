from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import pymysql.cursors

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://lfwannaknow: YES@localhost/wisata'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    database='wisata',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
    )

# class Wisata(db.Model):

#     id = db.Column(db.Integer, primary_key=True)
#     daya_tarik = db.Column(db.Integer, unique=True, nullable=False)
#     aksesbilitas = db.Column(db.Integer, nullable=False)
#     fasilitas = db.Column(db.Integer, nullable=False)
#     pelayanan = db.Column(db.Integer, nullable=False)
#     kebersihan = db.Column(db.Integer, nullable=False)
#     promosi = db.Column(db.Integer, nullable=False)

#     def __repr__(self):
#         return f"<Wisata {self.daya_tarik}>"

# Initialize Fuzzy Logic variables
daya_tarik = ctrl.Antecedent(np.arange(0, 11, 1), 'daya_tarik')
aksesbilitas = ctrl.Antecedent(np.arange(0, 11, 1), 'aksesbilitas')
fasilitas = ctrl.Antecedent(np.arange(0, 11, 1), 'fasilitas')
pelayanan = ctrl.Antecedent(np.arange(0, 11, 1), 'pelayanan')
kebersihan = ctrl.Antecedent(np.arange(0, 11, 1), 'kebersihan')
promosi = ctrl.Antecedent(np.arange(0, 11, 1), 'promosi')

# Create Fuzzy sets for temperature
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

# Membuat sistem kontrol fuzzy
rule1 = ctrl.Rule( daya_tarik['sedikit'] | aksesbilitas['jauh'] | fasilitas['jelek'] | pelayanan['buruk'] | kebersihan['kotor'] | promosi['kurang'], peringkat['rendah'])
rule2 = ctrl.Rule(daya_tarik['normal'] & aksesbilitas['normal'] & fasilitas['normal'] & pelayanan['baik'] & kebersihan['bersih'] & promosi['cukup'], peringkat['sedang'])
rule3 = ctrl.Rule(daya_tarik['tinggi'] | aksesbilitas['dekat'] | fasilitas['baik'] | pelayanan['memuaskan'] | kebersihan['sangat_bersih'] | promosi['baik'], peringkat['tinggi'])


# Create Fuzzy Control System
peringkat_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
peringkat_sim = ctrl.ControlSystemSimulation(peringkat_ctrl)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    rankings = []

    tourist_places = [
        {"name": "tugu_rimau"},
        {"name": "tangga_2001"},
        {"name": "ayek_pacar"},
        {"name": "oziel_garden"},
        {"name": "green_paradise"},
        {"name": "tanjung_sakti"},
        {"name": "dempo_park"},
        {"name": "curup"},
        {"name": "kebun_raya"},
        {"name": "kampung4"},
        
    ]

    for place in tourist_places:
        place_name = place["name"]
        user_inputs = {
                "daya_tarik": float(request.form[f"daya_tarik_{place_name}"]),
                "aksesbilitas": float(request.form[f"aksesbilitas_{place_name}"]),
                "fasilitas": float(request.form[f"fasilitas_{place_name}"]),
                "pelayanan": float(request.form[f"pelayanan_{place_name}"]),
                "kebersihan": float(request.form[f"kebersihan_{place_name}"]),
                "promosi": float(request.form[f"promosi_{place_name}"])
            }
        
          # Calculate the ranking using your fuzzy logic system
        peringkat_sim.input['daya_tarik'] = user_inputs["daya_tarik"]
        peringkat_sim.input['aksesbilitas'] = user_inputs["aksesbilitas"]
        peringkat_sim.input['fasilitas'] = user_inputs["fasilitas"]
        peringkat_sim.input['pelayanan'] = user_inputs["pelayanan"]
        peringkat_sim.input['kebersihan'] = user_inputs["kebersihan"]
        peringkat_sim.input['promosi'] = user_inputs["promosi"]

        peringkat_sim.compute()
        # Get the ranking value
        ranking_value = peringkat_sim.output['peringkat']

        try:
            with db.cursor() as cursor_insert:
                
                place_name = place["name"]
                ranking_value = peringkat_sim.output['peringkat']
                daya_tarik = user_inputs["daya_tarik"]
                aksesbilitas = user_inputs["aksesbilitas"]
                fasilitas = user_inputs["fasilitas"]
                pelayanan = user_inputs["pelayanan"]
                kebersihan = user_inputs["kebersihan"]
                promosi = user_inputs["promosi"]

                
                sql = "INSERT INTO penilaian  (daya_tarik, aksesbilitas, fasilitas, pelayanan, kebersihan, promosi, tempat, peringkat) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                cursor_insert.execute(sql, (daya_tarik, aksesbilitas, fasilitas, pelayanan, kebersihan, promosi, place_name, ranking_value))
                db.commit()

            with db.cursor() as cursor_select:
                sql_select = "SELECT AVG(peringkat) as previous_ranking FROM penilaian WHERE tempat = %s"
                cursor_select.execute(sql_select, (place_name,))
                previous_ranking_result = cursor_select.fetchone()

                if previous_ranking_result:
                    previous_ranking = previous_ranking_result["previous_ranking"]
                    if previous_ranking is not None:
                        if previous_ranking < ranking_value:
                            improvement_message = f"The ranking of {place_name} has improved from {previous_ranking} to {ranking_value}"
                        else:
                            improvement_message = f"The ranking of {place_name} has not improved"
                    else:
                        improvement_message = "No previous ranking found for comparison."
                else:
                    previous_ranking = None
                    improvement_message = "No previous ranking found for comparison."


        except Exception as e:
            print(f"An error occurred: {e}")
            improvement_message = "An error occurred while fetching the previous ranking."


        # Append the place name and ranking to the rankings list
        rankings.append({"place": place_name, "ranking": ranking_value, "previous_ranking": previous_ranking})
    
    rankings.sort(key=lambda x: x["ranking"], reverse=True)

    try:
        with db.cursor() as cursor_select:
            sql_select = "SELECT tempat, AVG(peringkat) as average_ranking FROM penilaian GROUP BY tempat"
            cursor_select.execute(sql_select)
            average_ranking_results = cursor_select.fetchall()

            if average_ranking_results:
                # Sorting average_rankings based on average_ranking value in descending order
                average_rankings = sorted(
                    [{"place": result["tempat"], "average_ranking": result["average_ranking"]} for result in average_ranking_results],
                    key=lambda x: x["average_ranking"],
                    reverse=True
                )
            else:
                average_rankings = None

    except Exception as e:
        print(f"An error occurred: {e}")
        average_rankings = None
    
    return render_template('prediction.html', user_inputs=user_inputs, rankings=rankings, average_rankings=average_rankings)

if __name__ == '__main__':
    app.run(debug=True)
