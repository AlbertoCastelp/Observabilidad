INSTALACION DE PROMETHEUS EN KUBERNETES

1. Add the Prometheus Helm repository: helm repo add prometheus-community https://prometheus-community.github.io/helm-charts

2. Update the Helm repository: helm repo update

3. Install Prometheus using Helm: helm install prometheus prometheus-community/prometheus

4. Verify that Prometheus is running: kubectl port-forward service/prometheus-server 9090:80

Open a web browser and go to http://localhost:9090. You should see the Prometheus web interface.