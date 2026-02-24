# Arquitetura – Mini SRE Lab

## Objetivo

Meu objetivo nesse projeto foi construir um laboratório prático de SRE que simula um ambiente de produção

Ele contém:

- Serviço web (Nginx)
- Monitoramento
- Coleta de métricas com Prometheus
- Definição e cálculo de SLI / SLO
- Gestão de Error Budget
- Injeção de falhas usando Chaos Engineering


Com isso foi criado um cenário fictício que simula erros que podem ocorrer no dia a dia, afetando nosso SLI/SLO/SLA e error Budget


## Arquitetura Geral
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
            

## Estrutura do Projeto
<img width="291" height="455" alt="image" src="https://github.com/user-attachments/assets/1010bb4e-eedb-49fb-b765-7a97ac2e528e" />




Vou resumir o que cada arquivo do meu projeto faz: 


## chaos/

chaos/chaos.sh

Um Script curto que eu criei, porém importante, ele vai simular as falhas controladas no Nginx e forçar respostas HTTP 500 temporariamente.
Simulando e permitindo validar SLIs, Slo e error Budget

chaos/Dockerfile
Container que executa o chaos.sh para simular falhas

## monitor/

monitor/Dockerfile

É o container responsável por executar o serviço monitor em Python.

monitor/monitor.py

Usando Python vamos realizar requisições HTTP durante alguns intervalos no Nginx para extrairmos os valores de requests_total e failures_total

monitor/requirements.txt

Lista as dependências Python do serviço:
requests
prometheus_client

## nginx/

nginx/Dockerfile

Aqui usamos a iamgem do nosso serviço web baseada em nginx:alpine, que representa a nossa aplicação que vai ser monitorada no nosso Lab

nginx/index.html

Nossa página que roda no Nginx
Ela é quem a gente verifica os status de HTTP(200,500 e etc) permitindo o cálculo de disponibilidade


## prometheus/

prometheus/prometheus.yml

Configura o Prometheus para:

Realizar scraping do serviço monitor

Definir intervalo de coleta

Carregar regras de SLO

prometheus/rules/slo_rules.yml
Aqui eu construi as rules para o prometheus:

sli:availability_5m

sli:error_rate_5m

slo:target (99%)

slo:error_budget

slo:burn_rate_5m

Responsável pelo cálculo real de SLI, SLO, error budget e burn rate.

Eu defini 5 minutos para que eu consiga subir o projeto e ter uma visualização boa no Grafana, consiga ver o SLI sendo afetado e as demais métricas



## Arquivos na raiz

docker-compose.yml
Orquestra todos os meus serviços do ambiente:

nginx

monitor

prometheus

grafana

chaos

load generator

Define rede interna, builds e dependências entre serviços.

README.md
Documentação do meu projeto em markdown


