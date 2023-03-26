import { createApp } from 'vue';
import { createPinia } from 'pinia';
import App from './App.vue';

import './assets/main.css';
import './assets/fonts.css';
import './assets/fontawesome.css';
const pinia = createPinia();
const app = createApp(App);

app.use(pinia);

app.mount('#app');
