# coding: utf-8

from flask import Flask, render_template, request
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map, icons

from firebase import firebase


app = Flask(__name__, template_folder="templates")


# you can set key as config
app.config['GOOGLEMAPS_KEY'] = "AIzaSyA1njsn06UVdJUBzU4nOCaNRUPbZLUInic"

# you can also pass key here
GoogleMaps(
    app,
    key="AIzaSyA1njsn06UVdJUBzU4nOCaNRUPbZLUInic"
)

@app.route("/")
def index():
    return "Hello, nothing here :)\n"

@app.route("/graph")
def graph():
    return render_template('graph.html')
    
@app.route("/project1")
def mapview():
    lines = [{
            'stroke_color': '#00FF00',
            'stroke_opacity': 1.0,
            'stroke_weight': 2,
            'path': [
                (28.514847, 77.382421),
                (28.487425, 77.429385),
                (28.446928, 77.475509),
                (28.443844, 77.480666),
                (28.444388, 77.484172),
                (28.451825, 77.494692),
                (28.450198, 77.496305),
                (28.434499, 77.506926),
                (28.388586, 77.529767),
                (28.280175, 77.564509),
                (28.264663, 77.568474),
                (28.180037, 77.565576),
                (28.081683, 77.569557),
                (28.038103, 77.592931),
                (28.017064, 77.594287),
                (28.005581, 77.598231),
                (27.994107, 77.606210),
                (27.987663, 77.609054),
                (27.965054, 77.610710),
                (27.957328, 77.613798),
                (27.940356, 77.625419),
                (27.881771, 77.665392),
                (27.878277, 77.670980),
                (27.868405, 77.695271),
                (27.866331, 77.699761),
                (27.846195, 77.720375)
            ],
            'infobox': ("<h4> <b>Terracon Delhi - Agra link</b><br></h4>"
                        "<h5>Terracon limited</h5>"
                        )
        },
        {
            'stroke_color': '#FF0000',
            'stroke_opacity': 1.0,
            'stroke_weight': 2,
            'path': [
                (27.840228, 77.723937),
                (27.836753, 77.725295),
                (27.832438, 77.726735),
                (27.823271, 77.727194),
                (27.763327, 77.712529),
                (27.754928, 77.713179),
                (27.703815, 77.733479),
                (27.696294, 77.735410),
                (27.651359, 77.732575),
                (27.591149, 77.748784),
                (27.585641, 77.749184),
                (27.569093, 77.746803),
                (27.563033, 77.747245),
                (27.560269, 77.747928),
                (27.552779, 77.752372),
                (27.498151, 77.781948),
                (27.442616, 77.777562)
            ],
            'infobox': ("<h4> <b>Indra Road Project</b><br></h4>"
                        "<h5>Mr. Aditya Pal</h5>"
                        )
        }]

    fullmap = Map(
        identifier="fullmap",
        varname="fullmap",
        style=(
            "height:90%;"
            "width:100%;"
            "top:0;"
            "left:0;"
            "position:absolute;"
            "z-index:200;"
        ),
        lat=37.4419,
        lng=-122.1419,
        markers=[(28.514847, 77.382421),(27.442616, 77.777562)],
        polylines=lines,
        fit_markers_to_bounds = True
        # maptype = "TERRAIN"
    )
    return render_template(
        'example_fullmap.html',
        fullmap=fullmap,
        # GOOGLEMAPS_KEY=request.args.get('apikey')
    ) 

@app.route("/project2")
def mapview2():
    lines = [{
            'stroke_color': '#00FF00',
            'stroke_opacity': 1.0,
            'stroke_weight': 2,
            'path': [
                (28.677978, 75.439144),
                (28.688271, 75.462739),
                (28.704897, 75.478876),
                (28.741740, 75.492644),
                (28.825503, 75.565816)
            ],
            'infobox': ("<h4> <b>Indra Road Project</b><br></h4>"
                        "<h5>Mr. Aditya Pal</h5>"
                        )
        },
        {
            'stroke_color': '#FF0000',
            'stroke_opacity': 1.0,
            'stroke_weight': 2,
            'path': [
                (28.825503, 75.565816),
                (28.826812, 75.572952),
                (28.827948, 75.575265),
                (28.830956, 75.576710),
                (28.842521, 75.574421),
                (28.860451, 75.590470)
            ],
            'infobox': ("<h4> <b>Indra Road Project</b><br></h4>"
                        "<h5>Mr. Aditya Pal</h5>"
                        )
        }]

    fullmap = Map(
        identifier="fullmap",
        varname="fullmap",
        style=(
            "height:90%;"
            "width:100%;"
            "top:0;"
            "left:0;"
            "position:absolute;"
            "z-index:200;"
        ),
        lat=28.4419,
        lng=-75.1419,
        markers=[(28.677978, 75.439144),(28.860451, 75.590470)],
        polylines=lines,
        fit_markers_to_bounds = True
        # maptype = "TERRAIN"
    )
    return render_template(
        'example_fullmap.html',
        fullmap=fullmap,
        # GOOGLEMAPS_KEY=request.args.get('apikey')
    )    

@app.route("/project3")
def mapview3():
    lines = [{
            'stroke_color': '#FF0000',
            'stroke_opacity': 1.0,
            'stroke_weight': 2,
            'path': [
                (26.677978, 76.439144),
                (26.688271, 76.462739),
                (26.704897, 76.478876),
                (26.741740, 76.492644),
                (26.825503, 76.565816)
            ],
            'infobox': ("<h4> <b>Indra Road Project</b><br></h4>"
                        "<h5>Mr. Aditya Pal</h5>"
                        )
        },
        {
            'stroke_color': '#00FF00',
            'stroke_opacity': 1.0,
            'stroke_weight': 2,
            'path': [
                (26.825503, 76.565816),
                (26.826812, 76.572952),
                (26.827948, 76.575265),
                (26.830956, 76.576710),
                (26.842521, 76.574421),
                (26.860451, 76.590470)
            ],
            'infobox': ("<h4> <b>Indra Road Project</b><br></h4>"
                        "<h5>Mr. Aditya Pal</h5>"
                        )
        }]

    fullmap = Map(
        identifier="fullmap",
        varname="fullmap",
        style=(
            "height:90%;"
            "width:100%;"
            "top:0;"
            "left:0;"
            "position:absolute;"
            "z-index:200;"
        ),
        lat=28.4419,
        lng=-75.1419,
        markers=[(26.677978, 76.439144),(26.860451, 76.590470)],
        polylines=lines,
        fit_markers_to_bounds = True
        # maptype = "TERRAIN"
    )
    return render_template(
        'example_fullmap.html',
        fullmap=fullmap,
        # GOOGLEMAPS_KEY=request.args.get('apikey')
    )    


@app.route('/holes')
def test():
    locations = []
    links = []
    db = firebase.FirebaseApplication('https://hackathon-74ece.firebaseio.com', None)
    response = db.get('/Pothole_Reports', None)

    result = dict(response)

    ans = ""

    for hashi in result.keys():
        try:
            for time in result[hashi].keys():
                if "GPS_Coordinates" in result[hashi][time].keys():
                    locations.append((result[hashi][time]["GPS_Coordinates"].split(',')[0], result[hashi][time]["GPS_Coordinates"].split(',')[1]))
                if "DownloadUrl" in result[hashi][time].keys():
                    links.append(result[hashi][time]["DownloadUrl"])
        except:
            continue

    markerss = []
    for i in range(len(locations)):
        temp_dict = {}
        temp_dict['icon'] = "https://user-images.githubusercontent.com/29799995/71303612-34e10f80-23e1-11ea-8f97-7ca8d5a327fc.png"
        temp_dict['lat'] = locations[i][0]
        temp_dict['lng'] = locations[i][1]
        temp_dict['infobox'] = (
                    "<h4>Road damage<br>reported</h4>"
                    "<img style=\"width:128px;height:128px;\" src='{}'>".format(links[i])
                )

        markerss.append(temp_dict)

    fullmap = Map(
        identifier="fullmap",
        varname="fullmap",
        style=(
            "height:90%;"
            "width:100%;"
            "top:0;"
            "left:0;"
            "position:absolute;"
            "z-index:200;"
        ),
        lat=37.4419,
        lng=-122.1419,
        markers=markerss,
        cluster=True,
        fit_markers_to_bounds = True
        # maptype = "TERRAIN"
    )
    return render_template(
        'example_fullmap.html',
        fullmap=fullmap,
        # GOOGLEMAPS_KEY=request.args.get('apikey')
    )

@app.route('/clickpost/', methods=['POST'])
def clickpost():
    # Now lat and lon can be accessed as:
    lat = request.form['lat']
    lng = request.form['lng']
    print(lat)
    print(lng)
    return "ok"

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
