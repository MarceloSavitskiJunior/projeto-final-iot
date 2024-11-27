import RPi.GPIO as gpio 
import time as delay
from app import app
from flask import render_template, jsonify
import requests
from urllib.request import urlopen

gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)

ledVermelho, ledVerde = 11, 12

statusVermelho = ""
statusVerde = ""
isEmpty = False
pin_t = 15
pin_e = 16
lixeira_v = 20

urlBase = 'https://api.thingspeak.com/channels/'
readKey = '/last?key=EPU1LWLGRPCX2JSG'
keyWrite = 'EPU1LWLGRPCX2JSG'
channels = '2746109'
field1 = '/fields/1/'
sensorDistancia = '&field1='

gpio.setup(pin_t, gpio.OUT)
gpio.setup(pin_e, gpio.IN)

gpio.setup(ledVermelho, gpio.OUT)
gpio.setup(ledVerde, gpio.OUT)

gpio.output(ledVermelho, gpio.LOW)
gpio.output(ledVerde, gpio.LOW)

def distancia():
    gpio.output(pin_t, True)
    delay.sleep(0.000001)
    gpio.output(pin_t, False)
    tempo_i = delay.time()
    tempo_f = delay.time()
    while gpio.input(pin_e) == False:
        tempo_i = delay.time()
    while gpio.input(pin_e) == True:
        tempo_f = delay.time()
    temp_d = tempo_f - tempo_i
    distancia = (temp_d*34300) / 2
    return distancia

def status_led_vermelho():
    if gpio.input(ledVermelho) == 1:
        statusVermelho = 'LED vermelho ON'
    else:
        statusVermelho = 'LED vermelho OFF'

    return statusVermelho

def status_led_verde():
    if gpio.input(ledVerde) == 1:
        statusVerde = 'LED verde ON'
    else:
        statusVerde = 'LED verde OFF'

    return statusVerde

def isEmpty(distancia):
    valorRecebido = distancia

    print("Distancia = %.1f CM" % valorRecebido)
    espaco_d = (valorRecebido/lixeira_v)*100

    print("Espaço disponível = %.1f" % espaco_d, '%' )
    espaco_o = 100 - espaco_d
    
    print("Espaço ocupado = %.1f" % espaco_o, '%')

    if espaco_d > 15:
        return False
    else:
        return True

def consultarOcupacao():
    consultaOcupacao = requests.get(urlBase + channels + field1 + readKey)
    print(consultaOcupacao.text)

    return consultaOcupacao

def enviarDadosOcupacao(ocupacao):
    urlDados = (urlBase + keyWrite + sensorDistancia + str(ocupacao))
    retorno = requests.post(urlDados)

    if retorno.status_code == 200:
        print('Dados envidados com sucesso')
    else:
        print('Erro ao enviar dados: '+ retorno.status_code)
        delay.sleep(20)

@app.route("/")
def index():
    templateData = {
        'ledRed': status_led_vermelho(),
        'ledGreen': status_led_verde()
    }
    return render_template('index.html', **templateData)

@app.route("/led_vermelho/<action>")
def led_vermelho(action):
    templateData = {
        'ledRed': status_led_vermelho(),
        'ledGreen': status_led_verde()
    }
    if action == 'on':
        gpio.output(ledVermelho, gpio.HIGH)
    if action == 'off':
        gpio.output(ledVermelho, gpio.LOW)

    return render_template('index.html', **templateData)



@app.route("/led_verde/<action>")
def led_verde(action):
    templateData = {
        'ledRed': status_led_vermelho(),
        'ledGreen': status_led_verde()
    }
    if action == 'on':
        gpio.output(ledVerde, gpio.HIGH)
    if action == 'off':
        gpio.output(ledVerde, gpio.LOW)

    return render_template('index.html', **templateData)



@app.route("/lixeira/<action>")
def lixeira(action):
    templateData = {
        'ledRed': status_led_vermelho(),
        'ledGreen': status_led_verde()
    }
    if action == 'abrir':
        print(distancia())


        distancia_real = distancia()

        if isEmpty(distancia_real):
            for i in range(3):
                gpio.output(ledVermelho, gpio.LOW)
                gpio.output(ledVerde, gpio.HIGH)
                delay.sleep(0.5)

                gpio.output(ledVerde, gpio.LOW)
                delay.sleep(0.5)

        else:
            for i in range(3):
                gpio.output(ledVerde, gpio.LOW)
                gpio.output(ledVermelho, gpio.HIGH)
                delay.sleep(0.5)

                gpio.output(ledVermelho, gpio.LOW)
                delay.sleep(0.5)

        if isEmpty(distancia_real):
            gpio.output(ledVerde, gpio.HIGH)
            gpio.output(ledVermelho, gpio.LOW)
        else:
            gpio.output(ledVermelho, gpio.HIGH)
            gpio.output(ledVerde, gpio.LOW)
        
    if action == 'fechar':
        gpio.output(ledVerde, gpio.LOW)

    enviarDadosOcupacao()
    return render_template('index.html', **templateData)


@app.route('/get_occupancy')
def get_occupancy():
    url = f'https://api.thingspeak.com/channels/2746109/fields/5.json?results=1'
    response = requests.get(url)
    data = response.json()
    print(data)

    if data['feeds']:
        ocupacao = float(data['feeds'][-1]['field1'])
        print(ocupacao)
    else:
        ocupacao = 0

    return jsonify(ocupacao=ocupacao)

