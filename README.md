# 🏗️ Arquitetura – Mini SRE Lab

## 🎯 Objetivo

Simular:

- Serviço web (**nginx**)
- Monitor externo
- Coleta de SLIs
- Comparação com SLO
- Simulação de falhas
- Cálculo de error budget

---

## 🧱 Arquitetura Geral
            +------------------+
            |   Monitor App    |
            |  (Python)        |
            |  - Calcula SLI   |
            |  - Valida SLO    |
            |  - Alerta        |
            +--------+---------+
                     |
                     | HTTP
                     ↓
            +------------------+
            |     NGINX        |
            |  (App alvo)      |
            |  Porta 80        |
            +------------------+
            
Tudo rodando com:

- 👉 Docker  
- 👉 Docker Compose  

## 📂 Estrutura do Projeto


<img width="660" height="299" alt="image" src="https://github.com/user-attachments/assets/377e9ff8-e48f-4657-b8b1-78cbc5d19aa2" />

