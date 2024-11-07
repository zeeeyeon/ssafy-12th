<template>
  <ParentChild
      my-msg="message"
      :dynamic-props="name"
      @some-event="someCallback"
      @emit-args="getNumbers"
      @update-name="updateName"
  />
  <ParentItem
      v-for="item in items"
      :key="item.id"
      :my-prop="item"
  />
</template>

<script setup>
import ParentChild from "@/components/ParentChild.vue";
import {ref} from "vue";
import ParentItem from "@/components/ParentItem.vue";

const name = ref('zeeyeon')
const items = ref([
  {id: 1, name: '사과'},
  {id: 2, name: '바나나'},
  {id: 3, name: '딸기'},
])

const someCallback = () => {
  console.log('자식 컴포넌트에서 발신한 이벤트를 수신했어용')
}

const getNumbers = (...args) => {
  console.log(args)
  console.log(`자식 컴포넌트로 부터 데이터를 ${args}를 받았습니다.`)
}

// 반응형 변수 name 을 변경하기 위해 호출하는 method
const updateName = () => {
  name.value = 'edit zeeyeon'
  console.log(name)
}

</script>

<style scoped>

</style>