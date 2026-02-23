# 🏗️ Arquitetura – Mini SRE Lab

## 🎯 Objetivo

Construir um laboratório prático de SRE que simula um ambiente de produção contendo:

- 🌐 Serviço web (Nginx)
- 📊 Monitoramento sintético
- 🔍 Coleta de métricas com Prometheus
- 📈 Definição e cálculo de SLI / SLO
- 💰 Gestão de Error Budget
- 🔥 Injeção de falhas com Chaos Engineering

O objetivo é demonstrar, de forma prática, como medir confiabilidade,
avaliar impacto de incidentes e analisar consumo de orçamento de erro.

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
<img width="291" height="455" alt="image" src="https://github.com/user-attachments/assets/1010bb4e-eedb-49fb-b765-7a97ac2e528e" />




📌 Descrição dos Serviços e Arquivos
📁 chaos/

chaos/chaos.sh
Script responsável por injetar falhas controladas no Nginx.
A cada intervalo definido, força respostas HTTP 500 temporariamente, simulando incidentes e permitindo validar SLIs, SLO e consumo de error budget.

chaos/Dockerfile
Define a imagem baseada em docker:cli, permitindo executar comandos docker exec para modificar dinamicamente a configuração do Nginx durante os testes de chaos engineering.

📁 monitor/

monitor/Dockerfile
Define a imagem Docker do serviço de monitoramento sintético, baseada em python:3.11-slim, incluindo as dependências necessárias para geração e exposição de métricas.

monitor/monitor.py
Serviço responsável por:

Realizar requisições HTTP periódicas ao Nginx

Incrementar requests_total

Incrementar failures_total em caso de erro ou exceção

Expor métricas no formato Prometheus na porta 8000

Atua como um synthetic monitor, fornecendo os dados brutos para cálculo de SLI e SLO no Prometheus.

monitor/requirements.txt
Lista as dependências Python do serviço:

requests

prometheus_client

📁 nginx/

nginx/Dockerfile
Define a imagem do serviço web baseado em nginx:alpine, que representa a aplicação monitorada no laboratório.

nginx/index.html
Página estática servida pelo Nginx.
Quando saudável, retorna HTTP 200, permitindo o cálculo de disponibilidade.

📁 prometheus/

prometheus/prometheus.yml
Configura o Prometheus para:

Realizar scraping do serviço monitor

Definir intervalo de coleta

Carregar regras de SLO

prometheus/rules/slo_rules.yml
Define recording rules para:

sli:availability_5m

sli:error_rate_5m

slo:target (99%)

slo:error_budget

slo:burn_rate_5m

Responsável pelo cálculo real de SLI, SLO, error budget e burn rate.

📄 Arquivos na raiz

docker-compose.yml
Orquestra todos os serviços do ambiente:

nginx

monitor

prometheus

grafana

chaos

load generator

Define rede interna, builds e dependências entre serviços.

README.md
Documentação principal do projeto, explicando arquitetura, objetivos e conceitos de SRE implementados.


