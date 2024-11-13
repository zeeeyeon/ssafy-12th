<template>
  <div>
    <h1>Article Page</h1>
    <RouterLink :to="{ name: 'CreateView'}">Create</RouterLink>
    <ArticleList />
  </div>
</template>

<script setup>

import {useCounterStore} from "@/stores/counter.js";
import {onMounted} from "vue";
import ArticleList from "@/components/ArticleList.vue";

const store = useCounterStore()

// 호출되는 시점을 컨트롤하는 것이 아님
onMounted(() => {
  // mount 되기 전 store에 있는 전체 게시글 요청 함수를 호출
  store.getArticles()
})
</script>

<style>

</style>
