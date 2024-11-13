<template>
  <div>
    <h1>게시글 작성</h1>
    <form @submit.prevent="createArticle">
      <label for="title">제목: </label>
      <input type="text" id="title" v-model="title">
      <br>
      <label for="content">내용: </label>
      <textarea id="content" v-model="content"></textarea>
      <input type="submit">
    </form>
  </div>
</template>


<script setup>
import {ref} from "vue";
import axios from "axios";
import {useCounterStore} from "@/stores/counter.js";
import {useRouter} from "vue-router";
import ArticleView from "@/views/ArticleView.vue";

const store = useCounterStore()

const title = ref(null)
const content = ref(null)
const router = useRouter();

// 장고가 제공하지 않는 페이지에서 가짜 데이터를 보내는것을 방지하는 것이었음 => csrf 토큰 검사 ㄴㄴ
const createArticle = () => {
  axios.post(`${store.API_URL}/api/v1/articles/`, {
    title: title.value,
    content: content.value
  })
      .then(response => {
        console.log('게시글 작성 성공');
        router.push({name: 'ArticleView'});
      })
      .catch(error => {
        console.log(error);
      })
}
</script>

<style>

</style>
