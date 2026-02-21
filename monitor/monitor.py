import requests
import time
from prometheus_client import start_http_server, Counter

REQUESTS_TOTAL = Counter('requests_total', 'Total requests made')
FAILURES_TOTAL = Counter('failures_total', 'Total failures detected')

start_http_server(8000)

while True:
    try:
        REQUESTS_TOTAL.inc()
        response = requests.get("http://nginx", timeout=2)

        if response.status_code != 200:
            FAILURES_TOTAL.inc()

    except Exception:
        FAILURES_TOTAL.inc()

    time.sleep(5)
    

    #📄 Arquivo: monitor.py
#🎯 Objetivo
#Simular um sistema de monitoramento externo que:
#Realiza requisições periódicas ao serviço nginx
#Mede disponibilidade (SLI)
#Compara com um SLO definido
#Detecta violação de confiabilidade

#📌 O que faz:

#import requests e import time
#requests → biblioteca para fazer requisições HTTP
#time → medir latência e controlar intervalo
#💡 Conceito SRE:
#Você está criando um probe externo, simulando tráfego real.

#URL = "http://nginx"
#📌 O que faz:
#Define o alvo do monitoramento.
#No docker-compose, o serviço nginx é acessível pelo nome do container.
#👉 Isso usa a rede interna do Docker.

#TOTAL = 0
#SUCCESS = 0

#📌 O que faz:
#TOTAL → total de requisições feitas
#SUCCESS → total de respostas 200
#Isso é a base para calcular disponibilidade.

#SLO = 99.0
#📌 O que faz:
#Define a meta de disponibilidade.
#Você está dizendo:
#Quero que pelo menos 99% das requisições sejam bem-sucedidas.
#Isso representa o Service Level Objective (SLO).

#while True:
#Monitoramento contínuo.
#Simula ferramenta como:
#Prometheus
#Datadog
#Mas em versão simplificada.

#TOTAL += 1
#Conta cada tentativa de requisição.

#🌐 Tentativa de requisição
#start = time.time()
#response = requests.get(URL, timeout=2)
#latency = time.time() - start

#📌 O que acontece:
#Marca o tempo antes da requisição
#Executa HTTP GET
#Calcula tempo de resposta
#Você está medindo dois SLIs:
#Disponibilidade
#Latência

#✅ Se status 200
#if response.status_code == 200:
#    SUCCESS += 1
#    status = "OK"
#else:
#    status = "ERROR"

#Aqui você define:
#200 → sucesso
#Qualquer outro status → falha lógica

#❌ Se exceção (timeout, queda)
#except Exception:
#    status = "DOWN"

#Isso captura:
#Container parado
#Timeout
#Falha de rede
#Representa indisponibilidade total.

#📊 Cálculo do SLI
#availability = (SUCCESS / TOTAL) * 100
#Aqui está o seu Service Level Indicator.
#Fórmula real usada em produção:
#Disponibilidade = (Requisições válidas / Total de requisições) * 100

#📢 Log atual:
#print(f"Req: {TOTAL} | Status: {status} | Availability: {availability:.2f}%")
#Isso simula log de monitoramento.
#Em ambiente real isso iria para:
#Log centralizado
#Dashboard
#Sistema de métricas

#🚨 Verificação do SLO:
#if availability < SLO:
#    print("⚠️ SLO VIOLATED!")
#Aqui você está aplicando o conceito de:
#Comparar SLI real com SLO definido.
#Se cair abaixo de 99% → violação.
#Isso significa:
#Error budget foi consumido além do permitido
#Mudanças deveriam ser pausadas
#Foco deve ser estabilidade
