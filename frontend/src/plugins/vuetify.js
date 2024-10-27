// plugins/vuetify.js

import { createVuetify } from 'vuetify';
import 'vuetify/styles';

import * as components from 'vuetify/components';
import * as directives from 'vuetify/directives';
import { VDataTable } from 'vuetify/labs/components'; 
const vuetify = createVuetify({
  components: {
    ...components,
    VDataTable, // Añade VDataTable a los componentes
  },
  directives,
  theme: {
    defaultTheme: 'myCustomTheme',
    themes: {
      myCustomTheme: {
        dark: false,
        colors: {
          primary: '#46009b',
          secondary: '#ff7d00',
          accent: '#e2e2e2',
        },
      },
    },
  },
});

export default vuetify;
