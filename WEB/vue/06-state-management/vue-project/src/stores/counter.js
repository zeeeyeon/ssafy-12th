import { ref, computed } from 'vue'
import { defineStore } from 'pinia'



// 공유하지 않는 private 한 상태값을 가지지 않는다
export const useCounterStore = defineStore('counter', () => {
  // 상태값
  const count = ref(0)
  // 계산된 값 === getters
  const doubleCount = computed(() => count.value * 2)
  // 메서드 === actions
  function increment() {
    count.value++
  }

  // 객체로 반드시 리턴이 필요함
  return { count, doubleCount, increment }
})
