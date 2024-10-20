from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views.decorators.cache import never_cache

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO
import base64
import zipfile

@never_cache
@login_required
def inicio(request):
    return render(request, 'encuestas/cargar_archivo.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')  # Redirige al nombre de la ruta 'login'


@never_cache
@login_required
def cargar_archivo(request):
    if request.method == 'POST':
        archivo = request.FILES['archivo_excel']
        df = pd.read_excel(archivo)
        # Lógica de procesamiento
        tablas = df.describe().to_html()
        # Generar gráficos
        plt.figure(figsize=(10,6))
        sns.countplot(x='columna_interes', data=df)
        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        imagen_png = base64.b64encode(buffer.getvalue()).decode('ascii')
        buffer.close()
        contexto = {'tablas': tablas, 'grafico': imagen_png}
        return render(request, 'encuestas/resultados.html', contexto)
    return render(request, 'encuestas/cargar_archivo.html')

@never_cache
@login_required
def descargar_zip(request):
    # Crear un archivo ZIP en memoria
    response = HttpResponse(content_type='application/zip')
    response['Content-Disposition'] = 'attachment; filename=resultados.zip'
    zip_file = zipfile.ZipFile(response, 'w')

    # Añadir archivos al ZIP
    # Por ejemplo, guardar el DataFrame como Excel y añadirlo
    excel_buffer = BytesIO()
    df.to_excel(excel_buffer, index=False)
    zip_file.writestr('resultados.xlsx', excel_buffer.getvalue())

    # Añadir gráfico
    # Aquí debes tener la imagen del gráfico guardada previamente
    zip_file.writestr('grafico.png', buffer_imagen_grafico.getvalue())

    zip_file.close()
    return response