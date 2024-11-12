<script setup>
import {ref} from "vue";
import {useCounterStore} from "@/stores/counter.js";

const store = useCounterStore()
const todoText = ref('')
const formElem = ref(null)

// 중앙 저장소에 addTodo 액션을 직접 호출해도 되지만
// 굳이 createTodo를 만들어서 호출하는 이유는
// addTodo 호출 전후로 추가 로직을 작성할 수 있기 때문
const createTodo = (todoText) => {
  store.addTodo(todoText)
  // 할 일 삽입 후 빈칸으로 만들기
  formElem.value.reset()
}
</script>

<template>
  <div>
<!--  ref: form 을 선택한 것  -->
    <form @submit.prevent="createTodo(todoText)" ref="formElem">
      <input type="text" v-model="todoText">
      <input type="submit">
    </form>
  </div>
</template>

<style scoped>

</style>