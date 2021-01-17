import Vue from 'vue'
import axios from 'axios'

axios.defaults.baseURL = '/api';
Vue.prototype.$axios = axios
