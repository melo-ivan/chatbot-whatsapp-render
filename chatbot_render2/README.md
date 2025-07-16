# Chatbot WhatsApp - Secretaria Escolar

Este projeto é um chatbot simples para WhatsApp, com integração via Z-API e hospedagem gratuita na Render.

## 🚀 Como usar

1. Suba este projeto no GitHub
2. Faça deploy na [Render](https://render.com)
3. Configure a variável de ambiente `ZAPI_URL` com sua instância Z-API
4. Aponte o Webhook da Z-API para `https://SEU-BOT.onrender.com/webhook`

## 🔧 Variáveis de Ambiente

Crie um arquivo `.env` com:

```
ZAPI_URL=https://api.z-api.io/instances/seu_id/token/seu_token/send-text
```

## 🧠 Fluxo de opções

1 - Transferência de Escola  
2 - Declaração de Matrícula  
3 - Histórico Escolar  
4 - Lista de Material  
5 - Troca de Turno/Turma  
6 - Justificativa de Faltas  
7 - Vagas para Novos Alunos
