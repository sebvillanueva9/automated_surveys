<template>
  <v-app>
    <!-- Mostrar el menú lateral solo si el usuario está autenticado -->
    <v-navigation-drawer v-if="isAuthenticated" app v-model="drawer" permanent color="accent">
      <v-list dense>
        <v-list-item>
          <v-list-item-content>
            <v-list-item-title class="title">Menú</v-list-item-title>
          </v-list-item-content>
        </v-list-item>

        <v-divider></v-divider>

        <v-list-item v-for="item in menuItems" :key="item.title" :to="item.route" router>
          <v-list-item-icon>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-icon>

          <v-list-item-content>
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <!-- Barra superior con el botón de cerrar sesión -->
    <v-app-bar app color="primary" dark>
      <v-app-bar-nav-icon v-if="isAuthenticated" @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
      <v-toolbar-title>Automatización de Procesos</v-toolbar-title>
      <v-spacer></v-spacer>
      <div v-if="isAuthenticated">
        <v-btn icon @click="logout">
          <v-icon color="white">mdi-logout</v-icon>
        </v-btn>
      </div>
    </v-app-bar>

    <v-main>
      <v-container>
        <router-view></router-view>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: 'App',
  data() {
    return {
      drawer: false,
      menuItems: [
        { title: 'Cargar Archivo', icon: 'mdi-upload', route: '/cargar' },
        { title: 'Otro Proceso', icon: 'mdi-cog', route: '/otro-proceso' },
      ],
      isAuthenticated: false,
    };
  },
  computed: {
    isUserAuthenticated() {
      return !!localStorage.getItem('access_token');
    },
  },
  watch: {
    isUserAuthenticated(newVal) {
      this.isAuthenticated = newVal;
    },
  },
  mounted() {
    // Actualizar el estado de autenticación al cargar el componente
    this.isAuthenticated = !!localStorage.getItem('access_token');
    if (this.isAuthenticated && this.$router.currentRoute.path === '/') {
      this.$router.push('/cargar');
    }
  },
  methods: {
    logout() {
      localStorage.removeItem('access_token');
      this.isAuthenticated = false;
      this.$router.push('/login');
    },
  },
};
</script>
