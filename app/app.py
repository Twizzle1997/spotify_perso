"""
@Date: 01/07/20: @Diem BUI: Add data (average time of songs,count the number
of songs by artists, count the number of bmp, count the number of songs by playlist) into the dashboard
    : Above work is implemented in  serve_data(feature) and dashbard()
    : Add the main() in order to initiate the DashBoard class

@Date: 01/07/20: @Diem BUI(update): add the regression relation between the intensity and the energy
"""

from bottle import route, run, template, request, response, error, install, os, sys, static_file
import sqlite3
import os
import configparser

from datamodeling import DashBoard
from DAL.Actualiser_Data import actualiser_data
from prediction.logisticRegressionPrediction import PredictLR
from bonus import IA_Vision


data_dashboard = DashBoard()
dirname = os.path.dirname(sys.argv[0])
Config = configparser.ConfigParser()
Config.read(r".\config.ini")
avg_duration = data_dashboard.avg_duration_songs()
count_nb_songs_by_playlist = data_dashboard.count_nb_songs_in_playlists()
count_songs_by_artist = data_dashboard.count_songs_by_artist_table_version()


@route('/popularity')
def popularity():
    return template(
        'popularity', copyrights=Config.get('Global', 'authors'), compagny=Config.get('Global', 'compagny'),
        project=Config.get('Global', 'project'),
        tracks=data_dashboard.get_tracks(), prediction='', real_pop='')


@route('/popularity', method='POST')
def popularity_submit():
    predict = PredictLR()
    return template(
        'popularity', copyrights=Config.get('Global', 'authors'), compagny=Config.get('Global', 'compagny'),
        project=Config.get('Global', 'project'),
        tracks=data_dashboard.get_tracks(),
        prediction=predict.get_predictionLR(request.POST['track'], data_dashboard), real_pop=data_dashboard.get_pop(request.POST['track']))


@route('/bonus')
def bonus():
    """BONUS : analyser les images d'une pochette d'album pour en extraire les objets (ressource en cours de construction).

    Returns:
        template: bonus

    """
    return template('bonus', copyrights=Config.get('Global', 'authors'), compagny=Config.get('Global', 'compagny'), image_path='', labels={})


@route('/bonus', method='POST')
def upload():
    """Upload image for the bonus.

    Returns:
        template: bonus w/ the image uploaded and and the label detection

    """
    upload_file = request.POST['uploadfile']
    print(upload_file.filename)
    name, ext = os.path.splitext(upload_file.filename)
    if ext.lower() not in ('.png', '.jpg', '.jpeg'):
        return "File extension not allowed."

    save_path = dirname+"/static/assets/img/tmp"
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    file_path = "{path}/{file}".format(path=save_path, file=upload_file.filename)
    if os.path.exists(file_path):
        os.remove(file_path)
    upload_file.save(file_path)  # appends upload.filename automatically

    # IA Vision
    ia_vision = IA_Vision(file_path)

    return template('bonus',
    copyrights=Config.get('Global', 'authors'),
    compagny=Config.get('Global', 'compagny'),
    image_path=upload_file.filename,
    labels=ia_vision.labels)

# Errors
@error(404)
def error404(error):
    return template('404')


# INDEX
@route('/')
@route('/index')
def dashboard():
    return template(
        'index', avgtimesong = avg_duration[0][0], maxtimesong = avg_duration[0][1], mintimesong = avg_duration[0][2],
        copyrights = Config.get('Global', 'authors'), compagny = Config.get('Global', 'compagny'),
        project = Config.get('Global', 'project'), count_songs_by_artist = count_songs_by_artist,
        countsongs = count_nb_songs_by_playlist
        )

# MISE A JOUR DE LA DATA
@route('/data-update', method='GET')
def data_update():
    try:
        actualiser_data()
    except:
        return 'Echec de la mise à jour des données'
    return 'Succès de la mise à jour des données'


@route('/get/data/<feature>')
def serve_data(feature):
	if feature == "artists":
		artist_filename = data_dashboard.count_songs_by_artist()
		return static_file(artist_filename, root=dirname+'/static/assets/img')
	if feature == "playlist":
		playlist_filename = data_dashboard.count_songs_by_playlist()
		return static_file(playlist_filename, root=dirname+'/static/assets/img')
	if feature == "bpm":
		bpm_filename = data_dashboard.count_songs_by_bpm()
		return static_file(bpm_filename , root=dirname+'/static/assets/img')
	if feature == "intensity":
		inten_filename = data_dashboard.regression_intensity_energy()
		return static_file(inten_filename , root=dirname+'/static/assets/img')
	'''
	if feature == "avgtimesong":
		avg_duration = dashboard.avg_duration_songs()
		return template('index', avgtimesong = avg_duration)
	'''

# Assets
# CSS
@route('/css/<filename:re:.*\.css>')
def send_css(filename):
	return static_file(filename, root=dirname+'/static/assets/css')


# JS
@route('/js/<filename:re:.*\.js>')
def send_js(filename):
	return static_file(filename, root=dirname+'/static/assets/js')


# jQuery
@route('/vendor/jquery/<filename:re:.*\.js>')
def send_jquery(filename):
	return static_file(filename, root=dirname+'/vendor/jquery')


# Bootstrap
@route('/vendor/bootstrap/js/<filename:re:.*\.js>')
def send_bootstrap(filename):
	return static_file(filename, root=dirname+'/vendor/bootstrap/js')


# jQuery Easing
@route('/vendor/jquery-easing/<filename:re:.*\.js>')
def send_jquery_easing(filename):
	return static_file(filename, root=dirname+'/vendor/jquery-easing')


# Font Awesome
# CSS
@route('/vendor/fontawesome-free/<filename:re:.*\.css>')
def send_fontawesome_css(filename):
	return static_file(filename, root=dirname+'/vendor/fontawesome-free')


# Webfonts
@route('/vendor/fontawesome-free/webfonts/<filename:re:.*\.woff>')
@route('/vendor/fontawesome-free/webfonts/<filename:re:.*\.woff2>')
def send_fontawesome_webfonts(filename):
	return static_file(filename, root=dirname+'/vendor/fontawesome-free/webfonts')


# Chart
@route('/vendor/chart.js/<filename:re:.*\.js>')
def send_chart(filename):
	return static_file(filename, root=dirname+'/vendor/chart.js')


# Démo
@route('/js/demo/<filename:re:.*\.js>')
def send_demo(filename):
	return static_file(filename, root=dirname+'/static/assets/js/demo')


@route('/vendor/datatables/<filename:re:.*\.css>')
@route('/vendor/datatables/<filename:re:.*\.js>')
def send_dt(filename):
    """Datatables

    Args:
        filename ([type]): [description]

    Returns:
        [type]: [description]
    """
    return static_file(filename, root=dirname+'/vendor/datatables')


# IMG
@route('/img/<filename:re:.*\.svg>')
@route('/img/<filename:re:.*\.png>')
@route('/img/<filename:re:.*\.ico>')
@route('/img/<filename:re:.*\.jpg>')
@route('/img/<filename:re:.*\.jpeg>')
def send_img(filename):
	return static_file(filename, root=dirname+'/static/assets/img')



if __name__ == "__main__":
    run(host='localhost', port=8080, debug=True)