
Aquí tienes un README para el código proporcionado:

Generador de Informes Diarios
Este script Python automatiza la generación de informes diarios a partir de archivos CSV que contienen datos relevantes para el monitoreo y análisis de sistemas. El informe incluye gráficos y descripciones que ayudan a comprender mejor las métricas registradas.

Requisitos
Python 3.x
Bibliotecas Python:
os
pandas
matplotlib
reportlab
shutil
tempfile
smtplib
email
Uso
Preparación de los archivos CSV: Asegúrate de tener los archivos CSV con los datos que deseas incluir en el informe en el mismo directorio que este script.
Ejecución del script: Ejecuta el script proporcionando los nombres de los archivos CSV como argumentos. Por ejemplo:
bash
Copy code
python generar_informe.py
Resultados: El script generará un informe en formato PDF con los gráficos correspondientes a los datos de los archivos CSV proporcionados. Además, enviará el informe por correo electrónico al destinatario especificado.
Funcionalidades
Limpieza de datos: El script limpia los archivos CSV eliminando espacios en blanco, comas y convirtiendo los datos en el formato adecuado para su análisis.
Generación de gráficos: Crea gráficos de barras o de líneas dependiendo de la estructura de los datos. También genera gráficos de torta para las cinco métricas más altas.
Descripciones personalizadas: Las descripciones de los gráficos se generan automáticamente a partir de los nombres de los archivos CSV, pero pueden ser personalizadas según sea necesario.
Envío de informes por correo electrónico: El informe generado se envía automáticamente por correo electrónico al destinatario especificado.
Configuración del Correo Electrónico
Para utilizar la función de envío de correo electrónico, asegúrate de configurar correctamente los siguientes parámetros en el script:

sender_email: Dirección de correo electrónico del remitente.
sender_password: Contraseña de la cuenta de correo electrónico del remitente.
recipient_email: Dirección de correo electrónico del destinatario.
smtp_server: Servidor SMTP para el envío de correos electrónicos (se utiliza Gmail en este ejemplo).
smtp_port: Puerto SMTP para la conexión al servidor.
Nota: Es recomendable utilizar una cuenta de correo electrónico de prueba para evitar exponer credenciales sensibles.

Contribuciones
Si deseas contribuir a este proyecto, ¡siéntete libre de enviar pull requests!