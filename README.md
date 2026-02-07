🎙 Assistente de Voz com IA (ChatGPT Local)

Projeto desenvolvido no Bootcamp Bradesco - GenAI & Dados (DIO), com foco em integração de IA, processamento de áudio e automação inteligente.

Este sistema implementa um pipeline completo de interação por voz:
fala → transcrição → IA → resposta → voz, executando localmente no computador.

🚀 Funcionalidades

🎙 Captura de áudio via microfone

🧠 Transcrição automática com faster-whisper

🤖 Processamento de linguagem natural com ChatGPT (OpenAI API)

🔊 Síntese de voz (Text-to-Speech)

⚙️ Execução local (sem Colab ou browser)

🧠 Arquitetura do Sistema
Áudio → Speech-to-Text → LLM → Processamento → Text-to-Speech → Áudio

🛠 Tecnologias Utilizadas

Python

faster-whisper

OpenAI API

sounddevice

gTTS

scipy

📂 Estrutura do Projeto
voz_chatgpt/
├── app.py
├── recorder.py
├── whisper_stt.py
├── chatgpt_api.py
├── tts.py
├── requirements.txt
└── .env

▶️ Execução do Projeto
pip install -r requirements.txt
python app.py

📌 Objetivo do Projeto

Desenvolver um assistente de voz inteligente como projeto prático de portfólio, aplicando conceitos de:

Inteligência Artificial aplicada

Processamento de linguagem natural (NLP)

Processamento de áudio

Integração de APIs

Arquitetura de sistemas inteligentes

Automação com IA

🧪 Possíveis Evoluções

Conversa contínua

Hotword (wake word)

Interface gráfica

Memória de contexto

LLM local (offline)

API própria

Multi-idioma automático

Assistente pessoal inteligente

👤 Autor

Enio Silva
Projeto desenvolvido para fins educacionais e de portfólio no Bootcamp Bradesco - DIO.
