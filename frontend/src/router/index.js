import { createRouter, createWebHistory } from 'vue-router';
import LoginPage from '@/components/Login.vue';
import CargarArchivoPage from '@/components/CargarArchivo.vue';

const routes = [
  {
    path: '/login',
    name: 'Login',
    component: LoginPage,
  },
  {
    path: '/cargar',
    name: 'CargarArchivo',
    component: CargarArchivoPage, // Definimos CargarArchivoPage como la vista principal
    meta: { requiresAuth: true },
  },
  {
    path: '/',
    redirect: '/cargar', // Redirigir a Cargar Archivo como vista principal
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

// Guard para proteger rutas
router.beforeEach((to, from, next) => {
  const publicPages = ['/login'];
  const authRequired = !publicPages.includes(to.path);
  const loggedIn = localStorage.getItem('access_token');

  if (authRequired && !loggedIn) {
    return next('/login');
  }
  next();
});

export default router;
