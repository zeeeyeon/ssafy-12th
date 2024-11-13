<template>
  <div>
    <h1>Detail</h1>
    <div v-if="article !== null">
<!--   데이터를 받아오는 것 보다 먼저 그리기 시작하여 error, 그래서 v-if 조건 달아주기   -->
      <p>게시글 번호: {{ article.id }}</p>
      <p>게시글 제목: {{ article.title }}</p>
      <p>게시글 내용: {{ article.content }}</p>
      <p>게시글 작성일: {{ article.created_at }}</p>
      <p>게시글 수정일: {{ article.updated_at }}</p>
    </div>
  </div>
</template>

<script setup>
import axios from "axios";
import {onMounted, ref} from "vue";
import {useCounterStore} from "@/stores/counter.js";
import {useRoute} from "vue-router";

const store = useCounterStore()
const route = useRoute()
// 여기에 데이터를 채워줌
const article = ref(null)

// detail 그려지기(마운트) 전에 미리 데이터를 받아와야 함
onMounted(() => {
  axios({
    method: "get",
    // route 정보의 파라미터에서 가져와서 객체 연결해주기
    url: `${store.API_URL}/api/v1/articles/${route.params.id}`,
  })
      .then(response => {
        console.log(response.data);
        article.value = response.data;
      })
      .catch(error => {
        console.log(error);
      })
})


</script>

<style>

</style>
