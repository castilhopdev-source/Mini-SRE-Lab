#!/bin/sh

# ------------------------------------------------------------
# Chaos Script - Mini SRE Lab
#
# Este script injeta falhas controladas no Nginx para simular
# incidentes reais e testar observabilidade (Prometheus/Grafana).
#
# Funcionamento:
# - A cada 120 segundos, cria uma configuração temporária no Nginx
#   que força retorno HTTP 500 para todas as requisições.
# - Mantém o erro ativo por 20 segundos.
# - Remove a configuração e recarrega o Nginx.
# - Repete o processo indefinidamente.
#
# Objetivo:
# - Validar alertas
# - Testar métricas de erro
# - Simular cenário de indisponibilidade
# ------------------------------------------------------------

while true; do
  sleep 120

  echo "Injetando 500 por 20s"
  docker exec sre_nginx sh -c "
  cat <<EOF > /etc/nginx/conf.d/chaos.conf
  server {
      listen 80;
      location / {
          return 500;
      }
  }
EOF
  nginx -s reload
  "

  sleep 20

  echo "Removendo chaos"
  docker exec sre_nginx sh -c "
  rm -f /etc/nginx/conf.d/chaos.conf
  nginx -s reload
  "

done


