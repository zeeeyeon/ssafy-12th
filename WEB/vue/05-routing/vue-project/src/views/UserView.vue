<script setup>
import {useRoute, useRouter, onBeforeRouteLeave, onBeforeRouteUpdate } from "vue-router";

const route = useRoute();
const userId = ref(route.params.id);

const router = useRouter()
const goHome = () => {
  router.push({ name: "home" });
  router.replace({ name: "home" });

onBeforeRouteLeave((to, from) => {
  const answer = window.confirm('정말 떠나실 건가요?')
  if (answer === false) {
    return false
  }
})
}

// 같은 라우트 내의 다른 사용자로 이동할 때
// 반응형 변수는 업데이트 되지않음(최소한으로 그리려하기 때문)
const routeUpdate = (to, from) => {
  router.push({ name: "user", params: { id: 100 } });
}

// 특정한 주소는 유지인데 파라미터가 변경될때 주소는 변경해서 보내지만 같이 보내는 반응형 변수의 값은 그대로임
// 그래서 값을 다시 할당 해 줘야 함.
onBeforeRouteUpdate((to, from) => {
  userId.value = to.params.id;
})
</script>

<template>
  <h1>UserView</h1>

  <RouterLink :to="{ name: 'user-profile' }">Profile</RouterLink>
  <RouterLink :to="{ name: 'user-posts' }">Posts</RouterLink>

  <h2> {{ $route.params }} 유저 프로필 페이지 </h2>
  <h2> {{ $route.params.id }} 유저 프로필 페이지 </h2>
  <h2> {{ userId }} 유저 프로필 페이지 </h2>
  <button @click="goHome">goHome</button>
  <button @click="routeUpdate">100번 유저 페이지로 이동</button>
  <hr>
  <RouterView />
</template>

<style scoped>


</style>