import { ref, computed } from 'vue'
import { defineStore } from 'pinia'



// 공유하지 않는 private 한 상태값을 가지지 않는다
// store에 state를 정의하지 않았다면 컴포넌트에서 새로 추가할 수 없음
export const useCounterStore = defineStore('counter', () => {

  let id = 0
  const todos = ref([])

  // state를 조작하는 actions 만들기
  const addTodo = (Todotext) => {
    todos.value.push({
      id: id++,
      text: Todotext,
      isDone: false
    })
  }

  const deleteTodo = (selectedId) => {
    const index = todos.value.findIndex((todo) => todo.id === selectedId);
    todo.value.splice(index, 1)
  }

  const updateTodo = (selectedId) => {
    console.log('update')
    todos.value = todos.value.map((todo) => {
      if (todo.id === selectedId) {
        todo.isDone = !todo.isDone
      }
      return todo
    })
  }

  const doneTodosCount = computed(() => {
    const doneTodos = todos.value.filter((todo) => todo.isDone);
    return doneTodos.length
  })

  return { todos, addTodo, deleteTodo, updateTodo, doneTodosCount }





  /*
  // 상태값, ref()
  const count = ref(0)

  // 계산된 값 === getters, computed()
  //  state 자체를 변경하는 것이 아닌 그것을 의존하는 값을 감지하는 것
  const doubleCount = computed(() => count.value * 2)

  // 메서드 === actions, function()
  // state를 조작할 수 있는 것은 actions
  function increment() {
    count.value++
  }

  // 객체로 반드시 리턴이 필요함
  return { count, doubleCount, increment }

   */

},{persist: true})
