
from flask import Flask, request, jsonify
import joblib
import numpy as np

# Carregar o modelo salvo
modelo = joblib.load('modelo_regressao_linear.pkl')

# Criar o aplicativo Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "API de Previsão de Salário com Regressão Linear"

# Definir a rota para previsões
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Receber os dados enviados na requisição (espera-se que os dados sejam um JSON com a chave 'horas_estudo_mes')
        data = request.get_json()
        horas_estudo_mes = np.array(data['horas_estudo_mes']).reshape(-1, 1)
        
        # Fazer a previsão
        salario_predito = modelo.predict(horas_estudo_mes)
        
        # Retornar a previsão em formato JSON
        return jsonify({'salario_predito': salario_predito[0]})
    
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    # Rodar o servidor na porta 5000
    app.run(debug=True, host='0.0.0.0', port=5000)
