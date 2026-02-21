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


## Arquivo: docker-compose.yml

O arquivo `docker-compose.yml` define a arquitetura do laboratório.

Ele orquestra dois serviços:

- `nginx`: serviço monitorado
- `monitor`: sistema de observabilidade

O Docker Compose cria automaticamente uma rede interna, permitindo que o monitor acesse o serviço via hostname `nginx`.

Essa separação simula uma arquitetura real onde o sistema de monitoramento é externo ao serviço monitorado.

## Arquivo: nginx/Dockerfile

O container `nginx` representa o serviço monitorado no laboratório.

Ele serve uma página estática via HTTP e simula um sistema em produção.  
É a partir dele que o monitor coleta SLIs de disponibilidade e latência.

A imagem é baseada em `nginx:alpine` para manter leveza e simplicidade.

## Arquivo: nginx/index.html

O arquivo `index.html` representa o conteúdo servido pelo container nginx.
Ele funciona como uma aplicação web simples que retorna HTTP 200 quando está saudável.




## Arquivo: monitor/Dockerfile


O container `monitor` é responsável por executar o sistema de observabilidade do projeto.

Ele realiza requisições HTTP periódicas ao serviço `nginx`, coletando métricas de disponibilidade e latência (SLIs).  
Essas métricas são comparadas com o SLO definido, permitindo simular consumo de error budget e violação de confiabilidade.

A imagem é baseada em `python:3.11-slim` para reduzir tamanho e manter o ambiente mínimo necessário para execução.

## Arquivo: monitor/requirements.txt

O arquivo `requirements.txt` define as dependências Python necessárias para o container de monitoramento.

Neste projeto utilizamos:

- **requests** → Biblioteca responsável por realizar requisições HTTP ao serviço Nginx.


## Arquivo: monitor/monitor.py

O arquivo `monitor.py` implementa um sistema simplificado de monitoramento inspirado em práticas de SRE.

Ele executa requisições HTTP periódicas ao serviço `nginx`, medindo:

- Disponibilidade (percentual de respostas HTTP 200)
- Latência (tempo de resposta)

Essas métricas representam os SLIs do sistema.

O script compara continuamente o SLI de disponibilidade com o SLO definido (99%).  
Caso a disponibilidade fique abaixo da meta, o sistema indica violação de SLO, simulando consumo de error budget.

