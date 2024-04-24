# Configuración y personalización de Grafana. 

# Instalación de Grafana
Para hacer más fácil la configuración de Grafana en Kubernetes, se ha optado por utilizar plantillas de Helm, como en el caso de Prometheus. Los Chart de Helm simplifican la gestión de actualizaciones y dependencias en despliegues complicados gracias a su motor de plantillas.
Para este proyecto, se ha realizado la instalación de Grafana en el namespace “default”, para realizar dicha instalación se ha lanzado el siguiente comando. 

* Se añade el repositorio de Helm de Grafana

    helm repo add grafana https://grafana.github.io/helm-charts
* Se actualiza el repositorio de Helm. 

    helm repo update
* Se instala Grafana usando Helm
    
    helm install grafana grafana/grafana
* Verificar que Grafana está corriendo 
    
    kubectl port-forward service/grafana 3000:80

# Port-Forwarding para acceder a la UI de Grafana
Para poder configurar Dashboards personalizados en Grafana, se deberá realizar un port-forward del servicio de Grafana para acceder a su interfaz de usuario desde la máquina local. Esto nos permite interactuar con Grafana y realizar configuraciones o visualizar datos sin tener que acceder directamente al clúster de Kubernetes donde está desplegado. De esta forma, se facilita la configuración, visualización de datos y cualquier otra tarea relacionada con Grafana desde fuera del entorno de Kubernetes.

    kubectl port-forward service/grafana 3000:80
# Interfaz de usuario de Grafana 
La interfaz de Grafana proporciona un entorno intuitivo para visualizar y analizar datos a través de dashboard y tablas. Permite la creación de paneles personalizados para monitorear el rendimiento y comportamiento de sistemas y servicios. Se pueden realizar consultas y filtrar datos utilizando PromQL, configurar reglas de alerta, explorar métricas disponibles y analizar tendencias a lo largo del tiempo. Para acceder a la UI de Grafana. 

    http://localhost:3000

# Añadir un Data Source de Prometheus en Grafana
Se deberá de configurar el Data Source de Prometheus en Grafana para que Grafana pueda acceder y visualizar las métricas recopiladas por Prometheus. Esto permite a Grafana mostrar gráficos y tablas basados en las métricas almacenadas en Prometheus, lo que facilita el monitoreo y análisis de sistemas y servicios en entornos de infraestructura.
Para configurar el Data Source en Grafana se deberán seguir los siguientes pasos
* Se deberá desplazar por el menú de la izquierda hasta llegar a la opción Connections y hacer “click” en Data Source. 
* Una vez accedido se deberá de hacer “click” en Add data source.
* Del catálogo de Data Source que ofrece Grafana, se deberá seleccionar el de Prometheus.
* Se abrirá una nueva ventana de configuración, en la cual se deberá de configurar la URL en la que está expuesto el Servidor de Prometheus. 
* La URL se configurará para este proyecto usando la siguiente URL http://host.docker.internal:9090. 
* El resto de los campos se pueden dejar como están por defecto, por lo que solo quedará hacer “click” en Save&Test.
* Se deberá realizar una comprobación prestando especial atención a la conexión con el Servidor de Prometheus, verificando que la conexión se haya establecido correctamente para poder exportar las métricas de Prometheus a Grafana. Si la conexión es correcta deberá aparecer en la parte inferior un “check” de color verde acompañado del texto “Successfully queried the Prometheus API”
#	Creación del dashboard salud de clúster. 
Se ha diseñado un panel de control que permite visualizar de manera integrada los aspectos más relevantes del estado y el rendimiento del clúster. Este panel se compone de varias secciones, cada una enfocada en aspectos clave como la utilización de la CPU, la memoria y el consumo de los nodos. Estos datos son fundamentales para mantener un control efectivo sobre el clúster, permitiendo monitorear su salud y optimizar su funcionamiento.
Para la implementación de este dashboard, se deberá de seguir los siguientes pasos. 
* Se deberá desplazar al menú de la izquierda y hacer “click” en Dashboard y posteriormente hará “click” en Create Dashboard.
* Seleccionará import dashboard
* Deberá seleccionar el fichero que contiene el dashboard que quiere importar y arrastrarlo hacia la zona indicada para ello. 
* Seleccionará el Data Source del que será usado para exportar las métricas de Prometheus y posteriormente serán usadas en los dashboard de Grafana.
Por último, al hacer “click” en create, automáticamente Grafana empezará a representar los datos en el dashboard. 
Para una información más detallada se puede dirigir al ANEXO B. Grafana. 
