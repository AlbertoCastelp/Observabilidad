NODOS UNSCHEDULABLE 
sum(kube_node_spec_unschedulable)

CPU USAGE

(1 - sum(avg by (mode) (rate(node_cpu_seconds_total{job="node-exporter", mode=~"idle|iowait|steal", cluster="""}[5m]))))*100

MEMORY USAGE    
(1 - sum(node_memory_MemAviable_bytes:sum{cluster=""})/ sum(node_memory_MemTotal_bytes{job="node-exporter", cluster""}))*100

CPU TOTAL
sum(machine_cpu_cores{kubernetes_io_hostname=~"$node"})

MEMORY TOTAL
sum(machine_memory_bytes{kubernetes_io_hostname=~"$node"})

CPU USAGE PER NODE
(100 - (avg by(instance) (rate(node_cpu_seconds_total{mode=~"idle", instance!=" "}[2m]))*100))

MEMORY USAGE PER NODE
(node_memory_MemTotal_bytes{instance!=" "} - node_memory_MemAviable_bytes{instance!=" "}) / node_memory_MemTotal_bytes{instante!=" "}*100

CONTAINER RESTART 
incrase(kube_pod_container_status_restarts_toatl[5m]) > 0

POD BASED CPU USAGE
sum(rate(container_cpu_usage_total{image!="", name=~"^k8s_.*", kubernetes_io_hostname=~"$node", namespace=~"$namespace", container=~"$application"}[5m])) by (pod)

POD BASES MEMORY USAGE
sum(container_memory_working_set_bytes{container!="", namespace=~"$namespace", container=~"$application", container!="POD"}) by (pod)