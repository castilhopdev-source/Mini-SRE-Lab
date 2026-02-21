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


sre-lab/
├── docker-compose.yml
├── nginx/
│ ├── Dockerfile
│ └── index.html
├── monitor/
│ ├── Dockerfile
│ ├── monitor.py
│ └── requirements.txt
└── README.md
