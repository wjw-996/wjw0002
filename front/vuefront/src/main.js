import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

Vue.config.productionTip = false

//引入请求Http模块
import Axios from 'axios'
//将Axios注册入Vue原型 随后即可使用this.$http 
Vue.prototype.$http = Axios

//导入自定义的API模块（及api文件夹内的内容)并注册到Vue原型中，以后即可使用this.$api
import * as api from './api'
Vue.prototype.$api = api

import jsCookie from 'js-cookie'
Vue.prototype.$jsCookie = jsCookie


new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
