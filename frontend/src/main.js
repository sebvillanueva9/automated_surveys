// main.js

import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import vuetify from './plugins/vuetify';

// Importa los estilos de Vuetify y los íconos
import 'vuetify/styles';
import '@mdi/font/css/materialdesignicons.css';

const app = createApp(App);

app.use(router);
app.use(vuetify);

app.mount('#app');
