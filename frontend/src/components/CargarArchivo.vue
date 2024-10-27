<template>
  <v-container class="d-flex justify-center align-center fill-height">
    <v-card class="mx-auto my-5" max-width="600px" outlined>
      <v-card-title class="headline text-center">
        Subir Archivo de Encuesta
      </v-card-title>

      <v-card-text>
        <v-form @submit.prevent="processFile">
          <v-file-input
            label="Seleccione un archivo Excel"
            prepend-icon="mdi-upload"
            v-model="file"
            accept=".xls,.xlsx"
            outlined
            dense
            required
          ></v-file-input>
          <small class="text-caption grey--text">Formatos aceptados: .xlsx, .xls</small>

          <v-btn
            color="secondary"
            class="mt-4"
            block
            :disabled="!file"
            @click="processFile"
          >
            <v-icon left>mdi-cloud-upload</v-icon> Procesar Archivo
          </v-btn>
        </v-form>
      </v-card-text>

      <v-card-actions>
        <v-spacer></v-spacer>
        <v-icon color="grey">mdi-information-outline</v-icon>
        <span class="grey--text caption">Sube un archivo Excel para procesar los datos</span>
      </v-card-actions>
    </v-card>
  </v-container>
</template>

<script>
import axios from 'axios';  // Importa axios para manejar la solicitud

export default {
  data() {
    return {
      file: null,  // Almacena el archivo que el usuario selecciona
    };
  },
  methods: {
    getCookie(name) {
      // Función para obtener el valor del token CSRF de las cookies
      let cookieValue = null;
      if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
          const cookie = cookies[i].trim();
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
            break;
          }
        }
      }
      return cookieValue;
    },
    async processFile() {
      if (!this.file) {
        alert("Por favor selecciona un archivo primero.");
        return;
      }

      // Crear un objeto FormData para enviar el archivo
      let formData = new FormData();
      formData.append("archivo_excel", this.file);  // El nombre 'archivo_excel' debe coincidir con el del backend

      // Obtener el token CSRF
      const csrfToken = this.getCookie('csrftoken');

      try {
        // Realizar una solicitud POST al backend Django
        const response = await axios.post("http://localhost:8000/api/cargar_archivo/", formData, {
          headers: {
            "Content-Type": "multipart/form-data",  // Asegúrate de que las cabeceras estén correctas
            "X-CSRFToken": csrfToken,  // Enviar el token CSRF en la cabecera
            "withCredentials": true,  // Esto asegura que las cookies se envíen con la solicitud
          },
        });

        console.log("Respuesta del servidor:", response.data);
        alert("Archivo subido correctamente.");
      } catch (error) {
        console.error("Error al subir el archivo:", error.response ? error.response.data : error.message);
        alert("Error al subir el archivo.");
      }
    },
  },
};
</script>

<style scoped>
.fill-height {
  height: 100vh; /* Evita scroll innecesario */
}
</style>
