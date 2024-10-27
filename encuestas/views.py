from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import ensure_csrf_cookie

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status

from .serializers import ResultadosSerializer

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO
import base64
import zipfile
import sys
import logging

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

class CargarArchivoAPI(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    @ensure_csrf_cookie
    def post(self, request, format=None):
        print("Iniciando el método POST", flush=True)

        # Verifica si el archivo fue enviado
        archivo = request.FILES.get('archivo_excel')
        if not archivo:
            print("No se proporcionó ningún archivo", flush=True)
            return Response({'error': 'No se proporcionó ningún archivo'}, status=status.HTTP_400_BAD_REQUEST)

        print("Archivo detectado", flush=True)

        # Solo para prueba, imprime el nombre del archivo
        print(f"Archivo recibido: {archivo.name}", flush=True)

        # Respuesta temporal para confirmar recepción
        return Response({'message': f"Archivo recibido: {archivo.name}"}, status=status.HTTP_200_OK)

        # Procesa el archivo Excel
        # try:
        #     df = pd.read_excel(archivo)
        # except Exception as e:
        #     return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        # # Lógica de procesamiento
        # tablas = df.describe().to_html()

        # # Generar gráficos
        # plt.figure(figsize=(10,6))
        # sns.countplot(x='columna_interes', data=df)
        # buffer = BytesIO()
        # plt.savefig(buffer, format='png')
        # buffer.seek(0)
        # imagen_png = base64.b64encode(buffer.getvalue()).decode('ascii')
        # buffer.close()

        # # Serializar los resultados
        # data = {
        #     'tablas': tablas,
        #     'grafico': imagen_png,
        # }
        # serializer = ResultadosSerializer(data=data)
        # if serializer.is_valid():
        #     return Response(serializer.data, status=status.HTTP_200_OK)
        # else:
        #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)