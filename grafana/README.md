# Overview
Instalamos de Grafana

# Prequesite
You have a kubernetes cluster configured and are using the proper context with `kubectl`.

# Process

1. Añadimos el repositorio de grafana --> helm repo add grafana https://grafana.github.io/helm-charts
2. Realizamos un upgrade --> helm repo update
3. Instalamos con Helm el repositorio de grafana --> helm install grafana grafana/grafana. You should see some output like this:
   ![alt text](Installing-Kubernetes-Dashboard.png.webp)
4. Realizamos un port-forward --> kubectl port-forward service/grafana 3000:80
5. Abrir el navegador añadiendo http://localhost:3000. Deberías de ver la página de Login de Grafana.
6. Introduces las claves de acceso y usuario para acceder a Grafana (en caso de no ser admin/admin buscar secret que indica user/pass)
7. Añadimos el Datasource de prometheus. (añadiendo en Prometheus Server --> http://prometheus-kube-prometheus-prometheus.monitoring:9090)
8. Guardamos y realiza un Test de conexión. 
9. Creamos un nuevo Dashboard. 
10. Guardamos y aplicamos el Dashboard creado. 

# Deployment
For fun let's just deploy nginx to our cluster:
1. Run `kubectl apply -f https://k8s.io/examples/application/deployment.yaml`.
2. Run `kubectl get pods -o wide`. You should see something like this:
   ![alt text](get-pods.png)
3. Now let's expose our nging deployment. Run `kubectl expose deployment nginx-deployment --type NodePort`.
4. Through port forwarding we can access our application. First run `kubectl get svc`. You should see this:
   ![alt text](get-svc.png)
   Now run `kubectl port-forward service/nginx-deployment 8000:80`.
   (Assuming nothing else is running on port 8000)
5. In your browser, go to http://localhost:8000.
   You should see the default nginx page.

# Clean up
You can honeslty just run `kind delete cluster` and it'll delete the default cluster by the name of `kind`. If you gave your cluster a name just run `kind delete cluster --name <name of cluster>`.

Enjoy!
