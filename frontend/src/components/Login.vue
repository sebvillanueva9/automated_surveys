<template>
  <v-main class="fill-height">
    <v-container>
      <v-row justify="center" align="center" class="login-card">
        <v-col cols="12" sm="8" md="4">
          <v-card>
            <v-card-title class="text-h5">Iniciar Sesión</v-card-title>
            <v-card-text>
              <v-form @submit.prevent="login">
                <v-text-field
                  label="Usuario"
                  v-model="username"
                  required
                ></v-text-field>
                <v-text-field
                  label="Contraseña"
                  v-model="password"
                  type="password"
                  required
                ></v-text-field>
                <v-btn type="submit" color="secondary" block>Ingresar</v-btn>
              </v-form>
              <v-alert v-if="error" type="error">{{ error }}</v-alert>
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </v-main>
</template>

<script>
import axios from 'axios';

export default {
  name: 'LoginPage',
  data() {
    return {
      username: '',
      password: '',
      error: '',
    };
  },
  methods: {
    async login() {
      try {
        const response = await axios.post('/api/login/', {
          username: this.username,
          password: this.password,
        });
        const token = response.data.access_token;
        localStorage.setItem('access_token', token);

        // Actualiza el estado de autenticación inmediatamente después de iniciar sesión
        this.$root.isAuthenticated = true;
        this.$router.push('/');
      } catch (error) {
        this.error = 'Usuario o contraseña incorrectos.';
      }
    },
  },
};
</script>

<style scoped>
.fill-height {
  height: 100vh;
}
.login-card {
  margin-top: 50px;
}
</style>
