# 🎙 Assistente de Voz com IA (ChatGPT Local)

> Projeto desenvolvido no **Bootcamp Bradesco - GenAI & Dados (DIO)**  
> Foco em integração de IA, processamento de áudio e automação inteligente.

Sistema de interação por voz com pipeline completo:

**Fala → Transcrição → IA → Resposta → Voz**

---

## 📌 Visão Geral

Este projeto implementa um assistente de voz local capaz de:
- capturar áudio do microfone,
- converter fala em texto (Speech-to-Text),
- processar linguagem natural com IA,
- gerar respostas inteligentes,
- converter texto em áudio (Text-to-Speech).

Tudo executando **localmente**.

---

## 🚀 Funcionalidades

- 🎙 Captura de áudio  
- 🧠 Transcrição automática (`faster-whisper`)  
- 🤖 Processamento com ChatGPT (OpenAI API)  
- 🔊 Resposta em áudio (TTS)  
- ⚙️ Execução local  

---

## 🧠 Arquitetura do Sistema

```text
Áudio → Speech-to-Text → LLM → Processamento → Text-to-Speech → Áudio

---

##  Tecnologias Utilizadas

- **Python**
- **faster-whisper**
- **OpenAI API**
- **sounddevice**
- **gTTS**
- **scipy**

---

## 📂 Estrutura do Projeto

voz_chatgpt/
├── app.py
├── recorder.py
├── whisper_stt.py
├── chatgpt_api.py
├── tts.py
├── requirements.txt
└── .env

---

## ▶️ Execução

```bash
pip install -r requirements.txt
python app.py

---

## 🎯 Objetivo do Projeto

Projeto criado como parte do portfólio prático do **Bootcamp Bradesco - GenAI & Dados | DIO**, com foco em:

- Inteligência Artificial aplicada  
- Processamento de linguagem natural (NLP)  
- Processamento de áudio  
- Integração de APIs  
- Automação inteligente  
- Arquitetura de sistemas baseados em IA  

---

## 🔮 Possíveis Evoluções

- Assistente de voz contínuo  
- Hotword (wake word)  
- Interface gráfica  
- Memória de contexto  
- LLM local (offline)  
- Conversa multi-turn  
- Multi-idioma automático  
- API própria  

---

## 👤 Autor

**Enio Ramon**
Projeto educacional e de portfólio — **Bootcamp Bradesco - GenAI & Dados | DIO**


