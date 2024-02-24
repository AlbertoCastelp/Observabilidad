# arquitectura
1. Instalar Helm

   Instrucciones de instalación de Helm

2. Instalar kubectl

   Instrucciones de instalación de kubectl

3. Instalar Kind

   Siga las instrucciones detalladas en el siguiente enlace
   3.1 Cree el clúster utilizando el archivo config.yaml y especifique el número de workers.
   3.2 Aplique la configuración.
   3.3 Descargue e instale el repositorio del dashboard con Helm:

   css

helm upgrade --install kubernetes-dashboard kubernetes-dashboard/kubernetes-dashboard --create-namespace --namespace kubernetes-dashboard

3.4 Realice un port-forward para acceder a la interfaz de usuario de Kubernetes:

bash

kubectl -n kubernetes-dashboard port-forward svc/kubernetes-dashboard 8443:443

3.5 Cree y aplique en el clúster el archivo de configuración de los SA y CRBinding:

lua

kubectl create -f k8s-dashboard-account.yaml

3.6 Genere la contraseña de administrador:

sql

    kubectl -n kube-system create token admin-user

    3.7 Introduzca el token obtenido en el punto 3.6 en la interfaz de usuario.
    3.8 Abra la interfaz en el navegador utilizando la ruta: https://localhost:8443/

4. Instalar Prometheus

   4.1 Cree el namespace.
   4.2 Instale Prometheus usando Helm:

   arduino

helm install prometheus prometheus-community/kube-prometheus-stack --namespace default

4.3 Realice un port-forward para acceder a la interfaz de usuario de Prometheus:

bash

    kubectl port-forward service/prometheus-server 9090:80

    4.4 Cree el ConfigMap aplicando el archivo prometheus-config.yaml generado en el namespace de instalación.
    4.5 Cree los Services aplicando el archivo correspondiente.

5. Instalar Grafana

   5.1 Añada el repositorio de Grafana:

   csharp

helm repo add grafana https://grafana.github.io/helm-charts

5.2 Actualice el repositorio:

sql

helm repo update

5.3 Instale Grafana con Helm:

bash

helm install grafana grafana/grafana

5.4 Realice un port-forward:

bash

    kubectl port-forward service/grafana 3000:80

    5.5 Para conectar la base de datos de Prometheus en Grafana, utilice la URL: http://host.docker.internal:9090

6. Instalar Mailhog

   6.1 Descargue el repositorio de charts:

   csharp

helm repo add codecentric https://codecentric.github.io/helm-charts

6.2 Instale el chart de Mailhog:

bash

helm install mailhog codecentric/mailhog

6.3 Para acceder a la Web UI, ejecute:

arduino

export POD_NAME=$(kubectl get pods --namespace email -l "app.kubernetes.io/name=mailhog,app.kubernetes.io/instance=mailhog" -o jsonpath="{.items[0].metadata.name}")
kubectl port-forward --namespace email $POD_NAME 8025

6.4 Para acceder al servidor SMTP, ejecute:

arduino

    export POD_NAME=$(kubectl get pods --namespace email -l "app.kubernetes.io/name=mailhog,app.kubernetes.io/instance=mailhog" -o jsonpath="{.items[0].metadata.name}")
    kubectl port-forward --namespace email $POD_NAME 1025

7. Configurar alertas en Grafana

   Siga las instrucciones aquí para configurar alertas en Grafana.
