# 🤖 Chatbot WhatsApp Escolar - IEE/SC

Chatbot para atendimento automatizado via WhatsApp da **Secretaria Escolar do IEE/SC**, desenvolvido em **Python (Flask)**, hospedado no **Render** e integrado à **API Z-API**. Oferece suporte 24h para solicitações comuns da comunidade escolar, como documentos, matrícula, horários e outros.

---

## 📌 Funcionalidades

- ✅ Respostas automáticas via WhatsApp
- ✅ Integração com a [Z-API](https://z-api.io/)
- ✅ Implantação no Render (deploy contínuo)
- ✅ Suporte 24 horas
- ✅ Fácil personalização de mensagens
- ✅ Escalável para múltiplos setores ou escolas

---

## 🛠️ Tecnologias Utilizadas

- Python 3.10+
- Flask
- API Z-API
- JSON
- Render (deploy cloud)

---

## 📂 Estrutura do Projeto

---
chatbot-whatsapp/
│
├── app.py # Arquivo principal da aplicação Flask
├── templates/ # (Se aplicável) Páginas HTML para debug ou admin
├── static/ # Arquivos estáticos (imagens, CSS, etc)
├── requirements.txt # Dependências do projeto
└── README.md # Documentação do projeto


---

## 🚀 Como Executar Localmente

> ⚠️ Necessário ter o Python 3.10+ instalado

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/chatbot-whatsapp-render.git
cd chatbot-whatsapp-render
```
Crie e ative um ambiente virtual:
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
---
Instale as dependências:
pip install -r requirements.txt
---
Configure o .env com sua API_KEY, INSTANCE_ID e URL da Z-API:
API_URL=https://api.z-api.io/instanceXXXX
API_TOKEN=seu_token_aqui
---
Rode a aplicação:
python app.py

---

🌐 Deploy na Nuvem (Render)
Este projeto está hospedado gratuitamente no Render, com deploy automático via GitHub. Sempre que há um novo push, a aplicação é atualizada.

📸 Exemplo de Uso
Abaixo, uma simulação de uso no WhatsApp:


🧠 Próximas Melhorias
 Adicionar painel administrativo (ex: com Streamlit)

 Armazenar logs em banco de dados

 Suporte a múltiplos departamentos

 Melhorar entendimento de linguagem natural (ex: com spaCy ou Rasa)

 Implementar autenticação com RA ou matrícula

📄 Licença
Este projeto está sob a licença MIT.

👨‍🏫 Autor
Desenvolvido por Ivan Souza de Melo
Professor de Ciência de Dados | Desenvolvimento Web | IEE/SC







