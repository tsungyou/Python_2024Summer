from flask import Flask, jsonify, request, render_template
import pandas as pd
from datetime import datetime, timedelta
from config import *
app = Flask(__name__)

place_df = pd.read_csv('database/place.csv')

@app.route("/", methods=["GET", "POST"])
def homePage():

    df = pd.read_csv(target_data_path + "final.csv")
    print(type(df['dt'].iloc[0]))
    if request.method == "POST":
        # try:
        #     time = request.form.get("time", "").strip()
        #     classroom = request.form.get("classroom", "").strip()
        #     df = df[df['dt'].str]
        # except Exception as e:
        #     print(e)
        try:
            date = request.form.get("date", "").strip()
            print(date)
            df = df[df['dt'].apply(lambda x: (datetime.strptime(x, "%Y-%m-%d") - datetime.now()).days > 0)]
        except Exception as e:
            print("date", e)
    table_json = df.to_dict(orient="records")
    columns = df.columns.tolist()
    return render_template(
        'home.html', 
        table=table_json, 
        columns=columns, 
        google_maps_api_key=google_map_api_key,
        init_lat = default_lat,
        init_lng = default_lng)

@app.route("/maps", methods=["GET", "POST"])
def homeWithMaps():
    return render_template('home_maps.html', google_maps_api_key=google_map_api_key)

@app.route("/maps1", methods=["GET", "POST"])
def homeMapGV():
    return render_template('home1.html')

@app.route("/get_location/<classroom>")
def get_location(classroom):
    try:
        # Find the matching row in place_df
        location = place_df[place_df['classroom'] == classroom].iloc[0]
        print(location.values[-1])
        # print(location['latitude'], location['longitude'])
        return jsonify({
            'success': True,
            'lat': location.values[-2],
            'lng': location.values[-1]
        })
    except (IndexError, KeyError, ValueError) as e:
        print("Error", e)
        return jsonify({
            'success': False,
            'error': str(e)
        })

if __name__ == "__main__":
    app.run(debug=True)