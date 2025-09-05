from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Hello World :)<h1>'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f"Hello {name}"


@app.route('/c/<fahrenheit>')
def convert_fahrenheit_to_celsius(fahrenheit):
    """Transform entered temperature from Fahrenheit to Celsius."""
    celsius = 5 / 9 * (float(fahrenheit) - 32)
    return f"Input fahrenheit value:{fahrenheit}  -  Output: {celsius:.2f}"


@app.route('/f/<celsius>')
def convert_celsius_to_fahrenheit(celsius):
    """Alter entered Celsius temperature to Fahrenheit."""
    fahrenheit = float(celsius) * 9.0 / 5 + 32
    return f"Input celsius value:{celsius}  -  Output: {fahrenheit:.2f}"


if __name__ == '__main__':
    app.run()


