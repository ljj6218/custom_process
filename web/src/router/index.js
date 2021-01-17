import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

// 无需权限控制
export const constantRoutes = [
  {
    path: '/',
    name: 'index',
    redirect: '/JsonToStruct',
    hidden: true,
    meta: { title: 'Json 转 Struct' }
  },
  {
    path: '/JsonToStruct',
    name: 'JsonToStruct',
    hidden: true,
    component: () => import('@/view/JsonToStruct.vue'),
    meta: { title: 'Json 转 Struct' }
  },
  {
    path: '/Thank',
    name: 'Thank',
    hidden: true,
    component: () => import('@/view/Thank.vue'),
    meta: { title: '感谢' }
  },
]

const router = new Router({
  routes: constantRoutes
})

export default router
