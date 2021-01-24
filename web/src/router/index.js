import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

// 无需权限控制
export const constantRoutes = [
  {
    path: '/',
    name: 'index',
    redirect: '/CustomProcessBase',
    hidden: true,
    meta: { title: 'Json 转 Struct' }
  },
  {
    path: '/CustomProcessBase',
    name: 'CustomProcessBase',
    hidden: true,
    component: () => import('@/view/CustomProcessBase.vue'),
    meta: { title: '管理 详情页' }
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
