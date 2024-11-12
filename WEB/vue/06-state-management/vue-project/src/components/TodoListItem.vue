<script setup>
import {useCounterStore} from "@/stores/counter.js";

defineProps({
  todo: Object
})
const store = useCounterStore()
</script>

<template>
  <div>
    <span @click="store.updateTodo(todo.id)" :class="{ 'is-done': todo.isDone }">
      {{ todo.text }}
    </span>
    <button @click="store.deleteTodo(todo.id)">삭제</button>
  </div>
</template>

<style scoped>
.is-done {
  text-decoration: line-through;
}
</style>