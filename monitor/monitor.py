# ------------------------------------------------------------
# Monitor Service - Mini SRE Lab
#
# Serviço responsável por verificar periodicamente a
# disponibilidade do Nginx e expor métricas no formato
# Prometheus.
#
# Funcionamento:
# - A cada 5 segundos, realiza uma requisição HTTP ao Nginx.
# - Incrementa requests_total a cada tentativa.
# - Incrementa failures_total quando a resposta não é 200
#   ou ocorre erro/timeout.
# - Expõe as métricas na porta 8000 para scraping do Prometheus.
#
# Objetivo:
# - Calcular taxa de erro
# - Simular SLI de disponibilidade
# - Validar alertas e dashboards
# ------------------------------------------------------------

import requests
import time
from prometheus_client import start_http_server, Counter, Gauge



REQUESTS_TOTAL = Counter('requests_total', 'Total requests made')
FAILURES_TOTAL = Counter('failures_total', 'Total failures detected')

#availability_gauge = Gauge('sre_availability_sli', 'Current availability SLI')


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
    