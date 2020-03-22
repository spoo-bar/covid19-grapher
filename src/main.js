import Vue from 'vue'
import App from './App.vue'
import './registerServiceWorker'
import router from './router'
import store from './store'
import HighchartsVue from 'highcharts-vue'
import "bootswatch/dist/minty/bootstrap.min.css";

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
Vue.use(HighchartsVue);
