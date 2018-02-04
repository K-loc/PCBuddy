from flask import Flask, render_template, request, redirect, url_for
from flask_uploads import UploadSet, configure_uploads, IMAGES
from pathlib import Path
import google_vision

app = Flask(__name__)

photos = UploadSet('photos', IMAGES)

app.config['UPLOADED_PHOTOS_DEST'] = 'C:\\Users\\Kevin\\Desktop\\PCBuddy\\static\\img'

configure_uploads(app, photos)

@app.route('/', methods = ['GET', 'POST'])
def home_page():
     if request.method == 'POST' and 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        file_path = Path('C:\\Users\\Kevin\\Desktop\\PCBuddy\\static\\img') / filename
        label = google_vision.detect_part(file_path)
        if label == '':
            return redirect(url_for('error'))
        else:
            return redirect(url_for(label))

     return render_template('front/home.html')

@app.route('/About')
def about():
    return render_template('information/about.html')

@app.route('/Error')
def error():
    return render_template('information/error.html')

@app.route('/Motherboard')
def motherboard():
    return render_template('information/motherboard.html')

@app.route("/Sound")
def sound_card():
    return render_template('information/sound_card.html')

@app.route('/CPU')
def cpu():
    return render_template('information/cpu.html')

@app.route('/GPU')
def video_card():
    return render_template('information/video_card.html')

@app.route('/Power')
def power_supply():
    return render_template('information/power_supply.html')

@app.route('/RAM')
def random_access_memory():
    return render_template('information/random_access_memory.html')

@app.route('/HDD')
def hard_disk_drive():
    return render_template('information/hard_disk_drive.html')

@app.route('/Case')
def computer_case():
    return render_template('information/computer_case.html')

@app.route('/OpticalDrive')
def optical_disk_drive():
    return render_template('information/optical_disc_drive.html')



if __name__ == '__main__':
    app.run(debug=True)
