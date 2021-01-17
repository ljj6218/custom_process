<template>
  <div>
    <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" >

      <el-menu-item v-for="(menuItem, idx) in menuList" :index="idx.toString()" :key="idx">
        <a :href="menuItem.router">      
          {{ menuItem.name }}
        </a>
      </el-menu-item>

    </el-menu>
  </div>
</template>

<script>
var menuList = [
  {
    'router':'#/JsonToStruct',
    'name':'Json 转 Go Struct',
  },
  {
    'router':'#/Thank',
    'name':'感谢',
  },
]
export default {
  data() {
    return {
      activeIndex: '0',
      menuList: menuList,
    }
  }
}
</script>
