# 5. Instalación de Grafana
Grafana es una plataforma de análisis y visualización de métricas.

Añadir el Repositorio de Grafana
    
    helm repo add grafana https://grafana.github.io/helm-charts

Actualizar el Repositorio

    helm repo update

Instalar Grafana con Helm  

    helm install grafana grafana/grafana

Acceder a la Interfaz de Usuario de Grafana
Realice un port-forward para acceder a la interfaz de usuario de Grafana:

    kubectl port-forward service/grafana 3000:80

Para conectar la base de datos de Prometheus en Grafana, utilice la URL: http://host.docker.internal:9090
