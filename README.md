
# Guía de Instalación y Configuración del Entorno Kubernetes
Esta guía proporciona instrucciones detalladas para la instalación y configuración de un entorno Kubernetes, incluyendo herramientas como Helm, kubectl, Kind, Prometheus, Grafana. Estas herramientas son fundamentales para la gestión, supervisión y operación eficiente de clústeres Kubernetes.

# 1. Instalación de Helm
Helm es un gestor de paquetes para Kubernetes que facilita la instalación, actualización y gestión de aplicaciones en el clúster. Helm ahora tiene un script de instalación que automáticamente obtiene la última versión de Helm e instala localmente. Puedes descargar ese script y luego ejecutarlo localmente. Está bien documentado para que puedas leerlo y entender qué está haciendo antes de ejecutarlo.

# 1.1. Instrucciones de Instalación de Helm
Siga las instrucciones específicas para la instalación de Helm en su sistema.

    $ curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3
    $ chmod 700 get_helm.sh
    $ ./get_helm.sh

Sí, puedes usar curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash si deseas estar en la vanguardia.
# A través de Administradores de Paquetes
La comunidad de Helm proporciona la capacidad de instalar Helm a través de administradores de paquetes de sistemas operativos. Estos no son compatibles con el proyecto Helm y no se consideran terceros de confianza.
Desde Homebrew (macOS)
Miembros de la comunidad de Helm han contribuido con una fórmula de Helm para Homebrew. Esta fórmula generalmente está actualizada.

    rew install Helm

(Nota: También hay una fórmula para emacs-helm, que es un proyecto diferente).

Desde Chocolatey (Windows)
Miembros de la comunidad de Helm han contribuido con una compilación de paquetes de Helm para Chocolatey. Este paquete generalmente está actualizado.

    choco install kubernetes-helm

Desde Scoop (Windows)
Miembros de la comunidad de Helm han contribuido con una compilación de paquetes de Helm para Scoop. Este paquete generalmente está actualizado.

    scoop install helm

Desde Winget (Windows)
Miembros de la comunidad de Helm han contribuido con una compilación de paquetes de Helm para Winget. Este paquete generalmente está actualizado.

    winget install Helm.Helm

Desde Apt (Debian/Ubuntu)
Miembros de la comunidad de Helm han contribuido con un paquete de Helm para Apt. Este paquete generalmente está actualizado.

    $ curl https://baltocdn.com/helm/signing.asc | gpg --dearmor | sudo tee /usr/share/keyrings/helm.gpg > /dev/null
    $ sudo apt-get install apt-transport-https --yes
    $ echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/helm.gpg] https://baltocdn.com/helm/stable/debian/ all main" | $ sudo tee /etc/apt/sources.list.d/helm-stable-debian.list
    $ sudo apt-get update
    $ sudo apt-get install helm

Desde dnf/yum (Fedora)
Desde Fedora 35, Helm está disponible en el repositorio oficial. Puedes instalar Helm con el siguiente comando:
    
    $ sudo dnf install helm

Desde Snap
La comunidad de Snapcrafters mantiene la versión Snap del paquete Helm. Puedes instalarlo con el siguiente comando:

    $ sudo snap install helm --classic

Desde pkg (FreeBSD)
Miembros de la comunidad de FreeBSD han contribuido con la construcción de un paquete Helm para la Colección de Puertos de FreeBSD. Este paquete generalmente está actualizado. Puedes instalarlo con el siguiente comando:

    $ pkg install helm

Compilaciones de Desarrollo
Además de las versiones publicadas, puedes descargar o instalar instantáneas de desarrollo de Helm.

Desde Compilaciones Canary

Las compilaciones "Canary" son versiones del software Helm que se compilan a partir de la última rama principal. No son versiones oficiales y pueden no ser estables. Sin embargo, ofrecen la oportunidad de probar las características más avanzadas.
Las binarias de Canary Helm se almacenan en get.helm.sh. Aquí tienes enlaces a las compilaciones comunes:
* Linux AMD64
* macOS AMD64
* Windows AMD64 experimental
* Desde el Código Fuente (Linux, macOS)
Compilar Helm desde el código fuente requiere un poco más de trabajo, pero es la mejor opción si deseas probar la última versión (pre-lanzamiento) de Helm. Debes tener un entorno de Go funcional.

    $ git clone https://github.com/helm/helm.git
    $ cd helm
    $ make
    
Si es necesario, descargará las dependencias y las cacheará, y validará la configuración. Luego, compilará Helm y lo colocará en bin/helm.

# 2. Instalación de kubectl
Instalar kubectl en Linux
Existen los siguientes métodos para instalar kubectl en Linux:
*	Instalar el binario de kubectl con curl en Linux
*	Instalar usando la gestión de paquetes nativa
*	Instalar usando otra gestión de paquetes
*	Instalar el binario de kubectl con curl en Linux

# 2.1. Instrucciones de Instalación de kubectl
Siga las instrucciones específicas para la instalación de kubectl en su sistema.
Descarga la última versión con el siguiente comando:

    $ curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
Nota: Para descargar una versión específica, reemplaza la parte $(curl -L -s https://dl.k8s.io/release/stable.txt) del comando con la versión específica.
Por ejemplo, para descargar la versión 1.30.0 en Linux x86-64, escribe:
    
    $ curl -LO https://dl.k8s.io/release/v1.30.0/bin/linux/amd64/kubectl
Y para Linux ARM64, escribe:

    $ curl -LO https://dl.k8s.io/release/v1.30.0/bin/linux/arm64/kubectl
Valida el binario (opcional)
Descarga el archivo de suma de comprobación de kubectl:

    $ curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl.sha256"
Valida el binario de kubectl contra el archivo de suma de comprobación:

    $ echo "$(cat kubectl.sha256)  kubectl" | sha256sum --check
Si es válido, la salida es:

    $ kubectl: OK
Si la comprobación falla, sha256 sale con un estado no nulo e imprime una salida similar a:

    $ kubectl: FAILED
sha256sum: WARNING: 1 computed checksum did NOT match
Nota: Descarga la misma versión del binario y la suma de comprobación.
Instalar kubectl

    $ sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
Nota: Si no tienes acceso de root en el sistema de destino, aún puedes instalar kubectl en el directorio ~/.local/bin:

    $ chmod +x kubectl
    $ mkdir -p ~/.local/bin
    $ mv ./kubectl ~/.local/bin/kubectl

Luego añade (o prepend) ~/.local/bin a $PATH
Prueba para asegurarte de que la versión que instalaste esté actualizada:

    $ kubectl version --client
O usa esto para obtener una vista detallada de la versión:

    $ kubectl version --client --output=yaml

# 3. Instalación de Kind
Kind (Kubernetes in Docker) es una herramienta para ejecutar clústeres Kubernetes locales utilizando contenedores Docker como nodos.

# 3.1. Instalación
NOTA: kind no requiere kubectl, pero no podrás realizar algunos de los ejemplos en nuestra documentación sin él. Para instalar kubectl, consulta la documentación de instalación upstream de kubectl.

Si eres desarrollador de Go, es posible que encuentres conveniente la opción de instalación go install.

De lo contrario, ofrecemos binarios de release descargables, paquetes mantenidos por la comunidad y una guía de instalación desde código fuente.

Se recomiendan encarecidamente las versiones estables etiquetadas (actualmente v0.22.0) para el uso en CI en particular.

Es posible que necesites instalar el código más reciente desde el origen en HEAD si estás desarrollando Kubernetes en sí mismo en HEAD / las fuentes más recientes.

# 3.2 Instalación con un Gestor de Paquetes
La comunidad de kind ha habilitado la instalación a través de los siguientes gestores de paquetes.

En macOS a través de Homebrew:

    brew install kind

En macOS a través de MacPorts:

    sudo port selfupdate && sudo port install kind

En Windows a través de Chocolatey (https://chocolatey.org/packages/kind):

    choco install kind

# 3.3 Instalación desde Binarios de Release
Los binarios precompilados están disponibles en nuestra página de releases.

Para instalar, descarga el binario para tu plataforma desde "Assets", luego renómbralo a kind (o tal vez kind.exe en Windows) y colócalo en tu $PATH en tu directorio de instalación de binarios preferido.

En Linux:

Para AMD64 / x86_64

    [ $(uname -m) = x86_64 ] && curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.22.0/kind-linux-amd64

Para ARM64

    $(uname -m) = aarch64 ] && curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.22.0/kind-linux-arm64
    chmod +x ./kind
    sudo mv ./kind /usr/local/bin/kind

En macOS:

Para Macs Intel

    [ $(uname -m) = x86_64 ] && curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.22.0/    kind-darwin-amd64
Para Macs M1 / ARM

    [ $(uname -m) = arm64 ] && curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.22.0/kind-darwin-arm64
    chmod +x ./kind
    mv ./kind /some-dir-in-your-PATH/kind

En Windows en PowerShell:

    curl.exe -Lo kind-windows-amd64.exe https://kind.sigs.k8s.io/dl/v0.22.0/kind-windows-amd64
    Move-Item .\kind-windows-amd64.exe c:\some-dir-in-your-PATH\kind.exe

# 3.4 Creación de un Clúster
Crear un clúster de Kubernetes es tan simple como 

    kind create cluster.

Esto inicializará un clúster de Kubernetes utilizando una imagen de nodo preconstruida. Las imágenes preconstruidas están alojadas en kindest/node, pero para encontrar imágenes adecuadas para una versión dada actualmente debes verificar las notas de la versión para tu versión de kind (verifica con kind version), donde encontrarás una lista completa de imágenes creadas para una versión de kind.

Para especificar otra imagen, usa el indicador --image – kind create cluster --image=....

El uso de una imagen diferente te permite cambiar la versión de Kubernetes del clúster creado.

Si deseas construir la imagen de nodo tú mismo con una versión personalizada, consulta la sección de construcción de imágenes.

Por defecto, el clúster recibirá el nombre kind. Usa el indicador --name para asignar al clúster un nombre de contexto diferente.

Si deseas que el comando create cluster bloquee hasta que el plano de control alcance un estado listo, puedes usar el indicador --wait y especificar un tiempo de espera. Para usar --wait, debes especificar las unidades de tiempo para esperar. Por ejemplo, para esperar 30 segundos, usa --wait 30s, para 5 minutos usa --wait 5m, etc.

Puedes descubrir más uso con kind create cluster --help.

kind puede detectar automáticamente si tienes instalado Docker, Podman o Nerdctl y elegirá el que esté disponible. Si deseas desactivar la detección automática, usa la variable de entorno KIND_EXPERIMENTAL_PROVIDER=docker, KIND_EXPERIMENTAL_PROVIDER=podman o KIND_EXPERIMENTAL_PROVIDER=nerdctl para seleccionar el tiempo de ejecución.

# 3.5 Interactuar con tu Clúster
Después de crear un clúster, puedes usar kubectl para interactuar con él utilizando el archivo de configuración generado por kind.

Por defecto, la configuración de acceso al clúster se almacena en ${HOME}/.kube/config si la variable de entorno $KUBECONFIG no está establecida.

Si la variable de entorno $KUBECONFIG está establecida, entonces se usa como una lista de rutas (reglas normales de delimitación de ruta para tu sistema). Estas rutas se fusionan. Cuando se modifica un valor, se modifica en el archivo que define la sección. Cuando se crea un valor, se crea en el primer archivo que existe. Si no existen archivos en la cadena, entonces crea el último archivo de la lista.

Puedes usar el indicador --kubeconfig al crear el clúster, luego solo se carga ese archivo. El indicador solo se puede establecer una vez y no se realiza ninguna fusión.

Para ver todos los clústeres que has creado, puedes usar el comando get clusters.

Por ejemplo, digamos que creas dos clústeres:

    kind create cluster # El nombre de contexto del clúster predeterminado es `kind`.
    ...
    kind create cluster --name kind-2

Cuando enumeras tus clústeres kind, verás algo como lo siguiente:

    kind get clusters
    kind
    kind-2

Para interactuar con un clúster específico, solo necesitas especificar el nombre del clúster como un contexto en kubectl:

    kubectl cluster-info --context kind-kind
    kubectl cluster-info --context kind-kind-2

# 3.6 Eliminar un Clúster
Si creaste un clúster con kind create cluster entonces eliminarlo es igualmente simple:

    kind delete cluster

Si no se especifica el indicador --name, kind usará el nombre de contexto de clúster predeterminado kind y eliminará ese clúster.

Nota: Por diseño, solicitar eliminar un clúster que no existe no devolverá un error. Esto es intencional y es un medio para tener una forma idempotente de limpiar los recursos.

# 3.7 Cargar una Imagen en tu Clúster
Las imágenes de Docker se pueden cargar en los nodos de tu clúster con:

    kind load docker-image my-custom-image-0 my-custom-image-1

Nota: Si usas un clúster nombrado, deberás especificar el nombre del clúster en el que deseas cargar las imágenes: 

    kind load docker-image my-custom-image-0 my-custom-image-1 --name kind-2.

Además, los archivos de imágenes se pueden cargar con: 

    kind load image-archive /my-image-archive.tar.

Esto permite un flujo de trabajo como:

    docker build -t my-custom-image:unique-tag ./my-image-dir
    kind load docker-image my-custom-image:unique-tag
    kubectl apply -f my-manifest-using-my-image:unique-tag

NOTA: Puedes obtener una lista de imágenes presentes en un nodo del clúster usando docker exec:

    docker exec -it my-node-name crictl images

Donde my-node-name es el nombre del contenedor Docker (por ejemplo, kind-control-plane).

NOTA: La política de extracción predeterminada de Kubernetes es IfNotPresent a menos que la etiqueta de la imagen sea :latest o esté omitida (e implícitamente :latest), en cuyo caso la política predeterminada es Always. IfNotPresent hace que el Kubelet omita la extracción de una imagen si ya existe. Si deseas que esas imágenes cargadas en el nodo funcionen como se espera, por favor:

No uses una etiqueta :latest
Y / o:Especifica imagePullPolicy: IfNotPresent o imagePullPolicy: Never en tu(s) contenedor(es).
Consulta la política de extracción de imágenes de Kubernetes para más información.

Consulta también: Usar kind con Registros Privados.

# 3.8 Configuraciones para Docker Desktop
Si estás construyendo Kubernetes (por ejemplo, kind build node-image) en macOS o Windows, entonces necesitas un mínimo de 6GB de RAM dedicados a la máquina virtual (VM) que ejecuta el motor Docker. Se recomiendan 8GB.

Para cambiar los límites de recursos para Docker en Mac, necesitarás abrir el menú de Preferencias.

Ahora, ve a la página de configuraciones avanzadas y cambia las configuraciones allí, consulta cómo cambiar los límites de recursos de Docker. Configuración de 8 GB de memoria en Docker para Mac.

Para cambiar los límites de recursos para Docker en Windows, necesitarás hacer clic derecho en el icono de Moby en la barra de tareas y elegir "Configuración". Si ves "Cambiar a contenedores de Linux", entonces primero necesitarás hacer eso antes de abrir "Configuración".

Ahora, ve a la página de configuraciones avanzadas y cambia las configuraciones allí, consulta cómo cambiar los límites de recursos de Docker.

Configuración de 8 GB de memoria en Docker para Windows.

También puedes intentar eliminar cualquier dato no utilizado dejado por el motor Docker, por ejemplo, docker system prune.

# 3.9 Avanzado
Configuración de tu Clúster kind
Para un archivo de configuración kind de muestra, consulta kind-example-config. Para especificar un archivo de configuración al crear un clúster, usa el indicador --config:

    kind create cluster --config kind-example-config.yaml

# 3.10 Clústeres Multi-nodo
En particular, muchos usuarios pueden estar interesados en clústeres multi-nodo. Una configuración simple para esto se puede lograr con el siguiente contenido de archivo de configuración:

Configuración del clúster de tres nodos (dos trabajadores)

    kind: Cluster
    apiVersion: kind.x-k8s.io/v1alpha4
    nodes:
    - role: control-plane
    - role: worker
    - role: worker

# 3.11 Alta Disponibilidad del Plano de Control
También puedes tener un clúster con varios nodos de plano de control:

Un clúster con 3 nodos de plano de control y 3 trabajadores

    kind: Cluster
    apiVersion: kind.x-k8s.io/v1alpha4
    nodes:
    - role: control-plane
    - role: control-plane
    - role: control-plane
    - role: worker
    - role: worker
    - role: worker

# 3.12 Asignación de Puertos a la Máquina Anfitriona
Puedes asignar puertos adicionales desde los nodos a la máquina anfitriona con extraPortMappings:

    kind: Cluster
    apiVersion: kind.x-k8s.io/v1alpha4
    nodes:
    - role: control-plane
    extraPortMappings:
    - containerPort: 80
        hostPort: 80
        listenAddress: "0.0.0.0" # Opcional, por defecto es "0.0.0.0"
        protocol: udp # Opcional, por defecto es tcp

Esto puede ser útil si estás usando servicios NodePort o demonios que exponen puertos del anfitrión.

Nota: Vincular la dirección de escucha a 127.0.0.1 puede afectar tu capacidad para acceder al servicio.

Es posible que desees consultar la Guía de Ingreso y la Guía de Balanceo de Carga.

# 3.13 Exportar Registros del Clúster
kind tiene la capacidad de exportar todos los registros relacionados con kind para que los explores. Para exportar todos los registros del clúster predeterminado (nombre de contexto kind):

    kind export logs

Registros exportados a: /tmp/396758314

Al igual que con todos los demás comandos, si deseas realizar la acción en un clúster con un nombre de contexto diferente, usa el indicador --name.

Como puedes ver, kind colocó todos los registros del clúster kind en un directorio temporal. Si deseas especificar una ubicación, simplemente agrega la ruta al directorio después del comando:

    kind export logs ./somedir

Registros exportados a: ./somedir

La estructura de los registros se verá más o menos así:

    .
    ├── docker-info.txt
    └── kind-control-plane/
        ├── containers
        ├── docker.log
        ├── inspect.json
        ├── journal.log
        ├── kubelet.log
        ├── kubernetes-version.txt
        └── pods/
