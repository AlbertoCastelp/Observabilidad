# Configuración y Personalización de Prometheus

# Instalación de Prometheus
Se ha utilizado el gestor de paquetes Helm para una configuración más sencilla de Prometheus y de todos los recursos necesarios de Kubernetes. Los Chart de Helm ofrecen más opciones de personalización, lo que permite un control detallado sobre el despliegue de Prometheus. El motor de plantillas de Helm también simplifica el proceso de actualización y gestión para implementaciones complejas que requieren una configuración compleja de la gestión de dependencias, versiones y soporte de rollback.

# Pasos para la instalación:
* Añadir el repositorio de Helm de Prometheus:

    helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
    
* Actualizar el repositorio:

    helm repo update
* Instalar Prometheus usando Helm:

    helm install prometheus prometheus-community/Prometheus
* Verificar la instalación en el clúster:
Port-Forwarding para acceder a la UI de Prometheus (Opcional)
Este paso es opcional y debe ser utilizado únicamente cuando quiere acceder/interactuar con el servidor de Prometheus que se ejecuta en un clúster de Kubernetes desde una máquina local.

* Pasos para realizar Port-Forwarding:
Ejecutar el comando:

    kubectl port-forward -n default prometheus-prometheus-0 9091:9090
# Interfaz de usuario de Prometheus
La interfaz de usuario (UI) de Prometheus proporciona las siguientes capacidades:

    -   Visualización de Métricas
    -   Consulta y Filtrado de Datos
    -   Creación de Gráficos Personalizados
    -   Configuración de Alertas
    -   Exploración de Métricas
    -   Análisis de Tendencias

# Configuración de rastreo de Prometheus
Al realizar la instalación de Prometheus mediante Helm, este crea un fichero ConfigMap llamado prometheus-server. Este archivo contiene la configuración de Prometheus para gestionar reglas de alerta, reglas de grabación y otras configuraciones relacionadas.
