<script setup>
// lifeCycle 생애 주기
// setup : 최초 세팅
// template : 어떤 그림을 그려야할지, 틀을 정하는 곳
// onMounted : 화면이 컴파일 후에 호충됨

// ex. api를 받아올때는 onMounted 에 설정해줘야함

import { RouterLink } from "vue-router";
</script>

<template>
  <nav>
    <RouterLink to="/">Home</RouterLink> |
    <RouterLink to="/cart">Cart</RouterLink>
  </nav>
</template>

<style scoped>

</style>