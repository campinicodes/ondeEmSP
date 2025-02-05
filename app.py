from flask import Flask, render_template, request, jsonify
import os
import json

app = Flask(__name__)
UPLOAD_FOLDER = 'static/models/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Carregar o JSON na inicialização
JSON_FILE = "dados_lotes.json"  # Certifique-se de que este arquivo esteja na mesma pasta ou forneça o caminho correto
with open(JSON_FILE, 'r') as f:
    lotes_data = json.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    # Verifique se ambos os arquivos foram enviados
    if 'file' not in request.files:
        return jsonify({'error': 'file missing'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'no selected file'}), 400
    
    # Salvar os arquivos
    filename = os.path.join('static/models', file.filename)
    file.save(filename)
    return jsonify({'message': 'Upload realizado com sucesso', 'filename': file.filename})

@app.route('/get_info', methods=['GET'])
def get_info():
    """
    Retorna todos os dados do JSON no formato JSON.
    """
    return jsonify(lotes_data)

def extract_lote_data(filename):
    """
    Extrai as informações do lote do JSON com base no nome do arquivo.
    O nome do arquivo deve estar no formato: setor_028_quadra_046_lote_0321.dae
    """
    try:
        # Separar o nome do arquivo para obter setor, quadra e lote
        parts = filename.split("_")
        
        # Verificar se o formato é válido (setor, quadra e lote no lugar certo)
        if len(parts) < 6:
            print(f"Formato inválido no nome do arquivo: {filename}")
            return None  # Formato inválido
        
        setor = parts[1]
        quadra = parts[3]
        lote_nome = parts[5].split(".")[0]  # Alterado para lote_nome para evitar conflito com variável 'lote'
        
        # Filtrar os dados do JSON
        match = next(
            (lote for lote in lotes_data if lote["setor"] == setor and lote["quadra"] == quadra and lote["lote"] == lote_nome),
            None
        )
        
        if not match:
            print(f"Nenhum dado correspondente encontrado para: {filename}")
            return None  # Nenhum dado correspondente encontrado
        
        return match  # Retorna o lote correspondente
    except Exception as e:
        print(f"Erro ao extrair dados do lote: {e}")
        return None

if __name__ == '__main__':
    app.run(debug=True)
