<template>
  <div>
    <Header></Header>
    <router-view></router-view>
    <Foot></Foot>
  </div>
</template>

<script>

import Header from './components/Header'
import Foot from './components/Foot'

export default {
  name: 'app',
  components: {
    Header,
    Foot
  },
  mounted () {
    const script = document.createElement('script')
    script.src = 'https://s4.cnzz.com/z_stat.php?id=1279225155&web_id=1279225155'
    script.language = 'JavaScript'
    document.body.appendChild(script)
  },
  watch: {
    '$route' () {
      if (window._czc) {
        let location = window.location
        let contentUrl = location.pathname + location.hash
        let refererUrl = '/'
        window._czc.push(['_trackPageview', contentUrl, refererUrl])
      }
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
