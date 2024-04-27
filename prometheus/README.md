# Instalación de Prometheus
Prometheus es un sistema de monitorización y alerta de código abierto diseñado para clústeres Kubernetes.

Antes de comenzar, asegúrate de tener los siguientes requisitos previos:

* Un clúster de Kubernetes en ejecución.
* La herramienta de línea de comandos kubectl instalada.
* El gestor de paquetes Helm instalado.

Prometheus es necesario para la recopilación y almacenamiento de datos en Grafana. Sigue estos pasos para instalar Prometheus en Kubernetes:

Agrega el repositorio Helm de Prometheus:

    helm repo add prometheus-community https://prometheus-community.github.io/helm-charts

Actualiza el repositorio Helm:

    helm repo update

Instala Prometheus usando Helm:

    helm install prometheus prometheus-community/prometheus

Verifica que Prometheus esté en ejecución:

    kubectl port-forward service/prometheus-server 9090:80

Abre un navegador web e ingresa a http://localhost:9090. Deberías ver la interfaz web de Prometheus.