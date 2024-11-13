import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from "axios";

export const useCounterStore = defineStore('counter', () => {

  const articles = ref([])

  const API_URL = 'http://localhost:8000'

  //  DRF로 전체 게시글 요청을 보내고 응답을 받아 articles에 저장하는 함수
  //  비동기 요청이기 때문에 배열이 나중에 채워짐 => 그래서 미리 DOM에 채워야함
  //  상위 컴포넌트인 ArticleView에서 mount
  const getArticles = () => {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/articles/`
    })
        .then((response) => {
          // console.log(response.data)
          articles.value = response.data
        })
        .catch(err => console.log(err))
  }



  return { articles, getArticles, API_URL }
}, { persist: true })
