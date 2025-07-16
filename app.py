from flask import Flask, request, jsonify
import requests
import os
from datetime import datetime

app = Flask(__name__)

ZAPI_URL = os.getenv("ZAPI_URL")  # Exemplo: https://api.z-api.io/instances/seu_id/token/seu_token/send-text

def get_dynamic_link():
    month_links = {{
        1: "bit.ly/docfacil1", 2: "bit.ly/docfacil2", 3: "bit.ly/docfacil3",
        4: "bit.ly/docfacil4", 5: "bit.ly/docfacil5", 6: "bit.ly/docfacil6",
        7: "bit.ly/docfacil7", 8: "bit.ly/docfacil8", 9: "bit.ly/docfacil9",
        10: "bit.ly/docfacil10", 11: "bit.ly/docfacil11", 12: "bit.ly/docfacil12"
    }}
    current_month = datetime.now().month
    return month_links.get(current_month, "bit.ly/docfacil")

def processar_mensagem(msg):
    op = msg.strip()
    link = get_dynamic_link()
    if op == "1":
        return f"📄 *Transferência de Escola*\nAcesse o link {link}, preencha os dados e leve os documentos necessários."
    elif op == "2":
        return "📜 *Declaração de Matrícula*\nProcure a Secretaria com os documentos para assinar e carimbar a declaração."
    elif op == "3":
        return f"📚 *Histórico Escolar*\nAcesse o link {link} e preencha o formulário."
    elif op == "4":
        return "📦 *Lista de Material*\nDo 1º ao 9º ano disponível no site da EDA. Ensino Médio não possui lista."
    elif op == "5":
        return "🔄 *Troca de turno ou turma*\nProcure a Assessoria de Ensino pessoalmente. Só o responsável legal pode fazer isso."
    elif op == "6":
        return "🏥 *Justificativa de Falta*\nSomente presencialmente no SOE, com atestado."
    elif op == "7":
        return "👶 *Vagas para novos alunos*\nInformaremos quando houver vagas disponíveis."
    else:
        return ("Olá! Digite o número da sua solicitação:\n"
                "1️⃣ Transferência de Escola\n"
                "2️⃣ Declaração de Matrícula\n"
                "3️⃣ Histórico Escolar\n"
                "4️⃣ Lista de Material\n"
                "5️⃣ Troca de Turno/Turma\n"
                "6️⃣ Justificativa de Faltas\n"
                "7️⃣ Vagas para Novos Alunos")

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    msg = data.get('message', {{}}).get('text')
    phone = data.get('message', {{}}).get('from')

    if msg and phone:
        resposta = processar_mensagem(msg)

        # Enviar resposta pela Z-API
        payload = {{
            "phone": phone,
            "message": resposta
        }}
        headers = {{"Content-Type": "application/json"}}
        requests.post(ZAPI_URL, json=payload, headers=headers)

    return jsonify({{"status": "mensagem recebida"}}), 200

@app.route('/', methods=['GET'])
def home():
    return "Bot rodando com sucesso!"

if __name__ == '__main__':
    app.run(debug=True)
