# SSB Preparation Flask App
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ppdt')
def ppdt():
    return render_template('ppdt.html')

@app.route('/ppdt/practice/<int:num>')
def ppdt_practice(num):
    if 1 <= num <= 10:
        image_filename = f'images/ppdt{num}.jpg'
        return render_template('ppdt_practice.html', num=num, image_filename=image_filename)
    else:
        return "Invalid practice number", 404

@app.route('/ppdt/samples')
def ppdt_samples():
    sample_images = [
        'images/ppdt_sample1.png',
        'images/ppdt_sample2.png',
        'images/ppdt_sample3.png',
        'images/ppdt_sample4.png',
    ]
    return render_template('ppdt_samples.html', sample_images=sample_images)

@app.route('/psychology')
def psychology():
    return render_template('psychology_main.html')

@app.route('/gto')
def gto():
    return render_template('gto_main.html')

@app.route('/interview')
def interview():
    return render_template('interview.html')

@app.route('/psychology/what')
def psychology_what():
    return render_template('psychology_what.html')

@app.route('/psychology/tat')
def psychology_tat():
    return render_template('psychology_tat.html')

@app.route('/psychology/wat')
def psychology_wat():
    return render_template('psychology_wat.html')

@app.route('/psychology/srt')
def psychology_srt():
    return render_template('psychology_srt.html')

@app.route('/psychology/sdt')
def psychology_sdt():
    return render_template('psychology_sdt.html')

@app.route('/gto/what')
def gto_what():
    return render_template('gto_what.html')

@app.route('/gto/gd')
def gto_gd():
    return render_template('gto_gd.html')

@app.route('/gto/gpe')
def gto_gpe():
    return render_template('gto_gpe.html')

@app.route('/gto/io')
def gto_io():
    return render_template('gto_io.html')

@app.route('/gto/pgt')
def gto_pgt():
    return render_template('gto_pgt.html')

@app.route('/gto/hgt')
def gto_hgt():
    return render_template('gto_hgt.html')

@app.route('/gto/ct')
def gto_ct():
    return render_template('gto_ct.html')

if __name__ == '__main__':
    app.run(debug=True) 