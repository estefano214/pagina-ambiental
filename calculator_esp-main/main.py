from flask import Flask, render_template

app = Flask(__name__)

def result_calculate(size, lights, device):
    home_coef = 100
    light_coef = 0.04
    devices_coef = 5
    return size * home_coef + lights * light_coef + device * devices_coef

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<size>')
def lights(size):
    return render_template('lights.html', size=size)

@app.route('/<size>/<lights>')
def electronics(size, lights):
    return render_template('electronics.html', size=size, lights=lights)

@app.route('/<size>/<lights>/<device>')
def end(size, lights, device):
    result = result_calculate(int(size), int(lights), int(device))
    return render_template('end.html', result=result)

# 🔹 Rutas adicionales para tipos de luces
@app.route('/lights')
def lights_fixed():
    return render_template('lights.html')

@app.route('/led')
def led():
    return render_template('led.html')

@app.route('/fluorescente')
def fluorescente():
    return render_template('fluorescente.html')

# 🔹 Nueva ruta para el hogar ecológico
@app.route('/4')
def eco():
    return render_template('eco.html')

if __name__ == '__main__':
    app.run(debug=True)
