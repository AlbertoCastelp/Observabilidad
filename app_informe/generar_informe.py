import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
from reportlab.lib.pagesizes import letter, landscape
from reportlab.platypus import SimpleDocTemplate, Paragraph, Image, PageBreak, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
import shutil
import tempfile
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


def limpiar_csv(nombre_csv):
    # Leer el archivo CSV y cargarlo en un DataFrame, omitiendo la primera fila
    df = pd.read_csv(nombre_csv, skiprows=[0])

    if df.empty:
        print(f"El DataFrame está vacío para el archivo {nombre_csv}.")
        return None

    # Renombrar las columnas eliminando los espacios en blanco y reemplazando las comas con guiones bajos
    df.columns = [col.strip().replace(' ', '_').replace(',', '') for col in df.columns]

    # Convertir valores de las columnas de la 1 en adelante a tipo numérico si es necesario
    for col in df.columns[1:]:
        if df[col].dtype == 'object':  # Verificar si la columna contiene valores de tipo string
            if '%' in df[col].iloc[0]:  # Verificar si el primer valor contiene '%'
                df[col] = df[col].str.replace(',', '.').str.replace('%', '').astype(float)
            else:
                df[col] = df[col].str.replace(',', '').astype(float)

    # Reemplazar las comas y los puntos y convertir a tipo numérico si la columna 'Count' contiene valores de tipo string
    if 'Count' in df.columns and df['Count'].dtype == 'object':
        df['Count'] = df['Count'].str.replace(',', '').str.replace('.', '').astype(int)

    # Guardar el DataFrame modificado de nuevo en un archivo CSV
    nombre_csv_modificado = 'modificado_' + nombre_csv
    df.to_csv(nombre_csv_modificado, index=False)

    # Imprimir la tabla después de la limpieza
    print(f"Tabla después de la limpieza para {nombre_csv}:")
    print(df)

    # Retornar tanto el nombre del archivo modificado como el DataFrame
    return nombre_csv_modificado


def generar_grafico(nombre_archivo, columna_indice=None):
    # Leer el archivo (CSV o XLSX)
    if nombre_archivo.endswith('.csv'):
        df = pd.read_csv(nombre_archivo)
    elif nombre_archivo.endswith('.xlsx'):
        df = pd.read_excel(nombre_archivo)
    else:
        print("Formato de archivo no compatible.")
        return None

    # Convertir la primera columna a tipo de datos de cadena si es necesario
    if not isinstance(df.iloc[:, 0].iloc[0], str):
        df.iloc[:, 0] = df.iloc[:, 0].astype(str)

    # Verificar si la columna de índice está presente en el DataFrame
    if columna_indice and columna_indice not in df.columns:
        print(f"No se puede generar el gráfico. La columna {columna_indice} no está presente en el archivo.")
        return None

    # Convertir valores de las columnas a números
    for columna in df.columns[1:]:
        if df[columna].dtype == 'object':
            if '%' in df[columna].iloc[0]:
                df[columna] = df[columna].str.replace(',', '.').str.replace('%', '').astype(float)

    # Determinar qué tipo de gráfico generar según los datos
    if 'Time' not in df.columns:

        columna_valor = df.columns[1]  # Tomar la segunda columna como valores
        columna_indice = df.columns[0]  # Tomar la primera columna como índice

        df.set_index(columna_indice, inplace=True)
        plt.figure(figsize=(16, 10))
        plt.bar(df.index, df[columna_valor])
        plt.xlabel(columna_indice)
        plt.ylabel(columna_valor)
        plt.title('Gráfico de barras')
        plt.xticks(rotation=45)
        plt.yticks(fontsize=8)
        plt.gca().xaxis.set_major_locator(plt.MaxNLocator(15))
        nombre_grafico = os.path.join(tempfile.mkdtemp(), f'{os.path.splitext(os.path.basename(nombre_archivo))[0]}.png')
        plt.savefig(nombre_grafico, dpi=400)
        plt.close()
        if os.path.exists(nombre_grafico):
            return nombre_grafico, columna_valor
        else:
            print(f"No se pudo generar el gráfico para {nombre_archivo}.")
            return None

    else:
        columnas_datos = df.columns[1:]
        df_sorted = df.sort_values(by=df.columns[1], ascending=True)

        plt.figure(figsize=(20, 14))
        for columna in columnas_datos:
            plt.plot(df.iloc[:, 0], df[columna], label=columna, linewidth=2)

        plt.xlabel('Tiempo')
        plt.ylabel('Valor')
        plt.title('Gráfico de líneas')
        plt.xticks(rotation=45)
        plt.yticks(fontsize=8)
        plt.gca().xaxis.set_major_locator(plt.MaxNLocator(10))
        plt.legend()
        nombre_grafico = os.path.join(tempfile.mkdtemp(), f'{os.path.splitext(os.path.basename(nombre_archivo))[0]}.png')
        plt.savefig(nombre_grafico, dpi=400)
        plt.close()
        if os.path.exists(nombre_grafico):
            return nombre_grafico, None
        else:
            print(f"No se pudo generar el gráfico para {nombre_archivo}.")
            return None


def generar_descripcion_grafico(nombre_archivo):
    # Función para generar la descripción del gráfico basada en el nombre del archivo CSV
    nombre_sin_extension = os.path.splitext(nombre_archivo)[0]
    palabras = nombre_sin_extension.split('_')
    palabras_capitalizadas = [palabra.capitalize() for palabra in palabras]
    descripcion = ' '.join(palabras_capitalizadas)
    if not descripcion:
        descripcion = "Descripción genérica para el gráfico."
    return descripcion

def generar_informe_pdf(nombre_informe, author_name, archivos_csv):
    doc = SimpleDocTemplate(nombre_informe, pagesize=letter) #pagesize=landscape(letter))  # Página apaisada
    width, height = letter
    contenido = []
    estilos = getSampleStyleSheet()

    imagenes_temporales = []

    # Portada
    portada = Image('portada.png', width=450, height=550)
    #portada = Image('portada.png', width=width, height=height)
    contenido.append(portada)
    autor_info = Paragraph(f"Autor: {author_name}", estilos['Normal'])
    contenido.append(autor_info)
    contenido.append(PageBreak())
    

    descripcion_graficos = {}

    for archivo_csv in archivos_csv:
        descripcion_graficos[archivo_csv] = generar_descripcion_grafico(archivo_csv)

    for archivo_csv in archivos_csv:
        archivo_limpiado = limpiar_csv(archivo_csv)
        resultado_grafico = generar_grafico(archivo_limpiado)

        if resultado_grafico:
            grafico, columna_valor = resultado_grafico
            imagenes_temporales.append(grafico)  # Agregar el nombre del archivo de imagen a la lista de imágenes temporales

            descripcion = descripcion_graficos.get(archivo_csv, "Descripción genérica para el gráfico.")

            estilo_titulo = estilos['Title']
            titulo = Paragraph(f"<b>Gráfico {os.path.splitext(os.path.basename(archivo_csv))[0]}</b>", style=estilo_titulo)
            imagen = Image(grafico, width=500, height=300)
            parrafo = Paragraph(descripcion, style=estilos['Normal'])
            mas_descripcion = f"El gráfico generado a partir del archivo '{archivo_csv}' muestra las métricas registradas a intervalos regulares, ofreciendo una representación visual de los datos recopilados. Proporciona una visión detallada de [métrica específica] a lo largo del tiempo, lo que permite analizar tendencias, identificar patrones y tomar decisiones informadas basadas en los datos. Estas métricas son fundamentales para monitorear el rendimiento del sistema, identificar posibles problemas y optimizar la eficiencia operativa."
            parrafo = Paragraph(f"{descripcion}<br/><br/>{mas_descripcion}", style=estilos['Normal'])

            contenido.extend([titulo, imagen, parrafo])
            contenido.append(PageBreak())

            if columna_valor:
                df = pd.read_csv(archivo_limpiado)
                columna_para_torta = columna_valor
                if not df.empty:
                    valores_torta = df[columna_para_torta].tolist()
                    etiquetas_torta = df.iloc[:, 0].tolist()

                    valores_torta_ordenados = sorted(valores_torta, reverse=True)[:5]
                    etiquetas_torta_ordenadas = [etiquetas_torta[valores_torta.index(valor)] for valor in valores_torta_ordenados]

                    plt.figure(figsize=(8, 8))
                    plt.pie(valores_torta_ordenados, labels=etiquetas_torta_ordenadas, autopct='%1.1f%%', startangle=140)
                    plt.axis('equal')
                    plt.title('Gráfico de torta de los 5 más altos')
                    nombre_grafico_torta = os.path.join(tempfile.mkdtemp(), f'torta_{os.path.splitext(os.path.basename(archivo_csv))[0]}.png')
                    plt.savefig(nombre_grafico_torta, dpi=400)
                    plt.close()
                    plt.legend()
                    if os.path.exists(nombre_grafico_torta):
                        imagen_torta = Image(nombre_grafico_torta, width=400, height=400)
                        contenido.extend([imagen_torta])
                        contenido.append(PageBreak())
                    else:
                        print(f"No se pudo generar el gráfico de torta para {archivo_csv}.")

        else:
            print("No se generó ningún gráfico.")

    doc.title = "Informe Diario"
    doc.build(contenido)

    for imagen_temporal in imagenes_temporales:
        os.remove(imagen_temporal)
    shutil.rmtree(os.path.dirname(imagenes_temporales[0]))
    for archivo_csv in archivos_csv:
        os.remove(f'modificado_{archivo_csv}')

    # Llamada a la función para enviar el correo electrónico con el informe adjunto
    sender_email = "observabilidad.giss@gmail.com"
    sender_password = "xxx xxxx xxx xxxx"
    recipient_email = "albertocastellanoslimon@gmail.com"
    subject = "Informe Diario"
    body = "Adjunto encontrará el informe diario."
    attachment_path = nombre_informe  # El informe generado es el archivo adjunto

    enviar_correo_smtp(sender_email, sender_password, recipient_email, subject, body, attachment_path)

def enviar_correo_smtp(sender_email, sender_password, recipient_email, subject, body, attachment_path=None):
    # Configuración de SMTP
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    # Crear el mensaje de correo electrónico
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = recipient_email
    msg["Subject"] = subject

    # Agregar el cuerpo del correo electrónico si está disponible
    if body:
        msg.attach(MIMEText(body, "plain"))

    # Adjuntar el archivo si está disponible
    if attachment_path:
        with open(attachment_path, "rb") as attachment:
            part = MIMEApplication(attachment.read(), Name=os.path.basename(attachment_path))
        part['Content-Disposition'] = f'attachment; filename="{os.path.basename(attachment_path)}"'
        msg.attach(part)

    # Conectar al servidor SMTP y enviar el correo electrónico
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, msg.as_string())

generar_informe_pdf('informe.pdf', 'Alberto Castellanos', ['Cpu Usage per Node.csv', 'Memory Usage per Node.csv', 'CPU Used.csv', 'MEMORY Used.csv', 'Consumos por Namespace.csv', 'API.csv', 'Errores Integracion policia 504.csv', 'Errores más comunes.csv', 'Peticiones erroneas vs Total.csv'])
