import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import router from "@/router/index.js";

export const useCounterStore = defineStore('counter', () => {
  const articles = ref([])
  const API_URL = 'http://127.0.0.1:8000'
  const token = ref(null)
  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })

  // DRF로 전체 게시글 요청을 보내고 응답을 받아 articles에 저장하는 함수
  const getArticles = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/articles/`,
      headers: {
        Authorization: `Token ${token}`
      }
    })
      .then((res) => {
        // console.log(res.data)
        articles.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }

  // 회원가입 요청 액션
  const signUp = (payload) => {
    const {username, password1, password2} = payload
    // const username = payload.username
    // const password1 = payload.password1
    // const password2 = payload.password2

    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data: {
        username,
        password1,
        password2,
      }
    })
        .then((res) => {
          console.log(res)
          console.log('회원가입 성공')
          // 바로 회원가입 시, 바로 로그인 시켜줌
          const password = password1
          logIn({username, password})
        })
        .catch((err) => {
          console.log(err)
        })
  }

  const login =(payload) => {
    const {username, password} = payload

    axios.post(API_URL + '/accounts/login/', {username, password})
    .then((res) => {
      console.log(res)
      // 로그인 성공시 토큰값 채우기
      token.value = res.data.key
      // 메인 페이지로 바로 이동
      router.push({name: 'ArticlesView'})
    })
    .catch((err) => {
      console.log(err)
    })
  }
  
  return { articles, API_URL, getArticles, signUp, login, token, isLogin }
}, { persist: true })
