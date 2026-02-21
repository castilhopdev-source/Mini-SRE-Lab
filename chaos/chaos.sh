#!/bin/sh

while true; do
  echo "💥 Killing nginx..."
  docker kill sre_nginx
  sleep 30
done