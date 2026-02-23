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
                +----------------------+
                |      Load Gen        |
                | (curl loop infinito) |
                +----------+-----------+
                           |
                           ↓
                +----------------------+
                |        NGINX         |
                |   Serviço Web (80)   |
                +----------+-----------+
                           |
                           ↓
                +----------------------+
                |      Monitor App     |
                |  - requests_total    |
                |  - failures_total    |
                +----------+-----------+
                           |
                           ↓
                +----------------------+
                |      Prometheus      |
                |  - SLI              |
                |  - SLO              |
                |  - Burn Rate        |
                +----------+-----------+
                           |
                           ↓
                +----------------------+
                |       Grafana        |
                |  Dashboards & Alerts |
                +----------------------+

                +----------------------+
                |       Chaos          |
                |  Injeta HTTP 500     |
                +----------------------+
            
Tudo rodando com:

- 👉 Docker  
- 👉 Docker Compose  

## 📂 Estrutura do Projeto

<img width="303" height="410" alt="image" src="https://github.com/user-attachments/assets/da5b0f42-f18a-4beb-bc31-c29340b1ced1" />



## 📌 Descrição dos Serviços e Arquivos

### 📁 chaos/

- **chaos/chaos.sh**  
  Script responsável por simular falhas no ambiente, interrompendo serviços para testar disponibilidade, SLI e consumo de error budget.

- **chaos/dockerfile**  
  Define a imagem Docker utilizada para executar os testes de chaos engineering no ambiente controlado.

---

### 📁 monitor/

- **monitor/dockerfile**  
  Define a imagem Docker do serviço de monitoramento, incluindo dependências Python necessárias para execução do monitor.

- **monitor/monitor.py**  
  Aplicação responsável por:
  - Realizar requisições HTTP ao serviço alvo (nginx)
  - Calcular o SLI de disponibilidade
  - Comparar com o SLO definido
  - Exibir alertas quando o error budget é consumido

- **monitor/requirements.txt**  
  Lista de dependências Python utilizadas pelo serviço de monitoramento.

---

### 📁 nginx/

- **nginx/dockerfile**  
  Define a imagem Docker do serviço web baseado em NGINX.

- **nginx/index.html**  
  Página estática servida pelo NGINX, utilizada como endpoint de teste para cálculo de disponibilidade.

---

### 📄 Arquivos na raiz

- **docker-compose.yml**  
  Orquestra os serviços do ambiente (nginx, monitor e chaos), definindo redes, build e dependências.

- **prometheus.yml**  
  Arquivo de configuração do Prometheus para coleta de métricas do ambiente.

- **README.md**  
  Documentação principal do projeto.

