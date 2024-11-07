

<template>
  <p>{{ myMsg }}</p>
  <p>{{ dynamicProps }}</p>

  // @update-name이 하위 객체에서 받아올 이름
  <ParentGrandChild
    :my-msg="myMsg"
    @update-name="updateName"
  />

<!--  <button @click="$emit('someEvent')">출력</button>-->
  <button @click="buttonClick">클릭</button>
  <button @click="emitArgs">추가 인자 전달</button>
  <button @click="updateName">추가 인자 전달</button>

</template>

<script setup>
import ParentGrandChild from "@/components/ParentGrandChild.vue";

// 내려받은 props 선언
// 1. 배열 선언 방식
// defineProps(['myMsg'])
// 2. 객체 선언 방식
defineProps({
  myMsg: String,
  dynamicProps: String,
})

// props 데이터를 활용해야하는 경우
// const props = defineProps({ myMsg });
// console.log(props)
// console.log(props.myMsg)

// emit 이벤트 선언(배열, 객체방식)
const emit = defineEmits(['someEvent', 'emitArgs', 'updateName'])

const buttonClick = () => {
  emit('someEvent')
}

const emitArgs = () => {
  emit('emitArgs', 1, 2, 3)
}

const updateName = () => {
  emit('updateName')
}


</script>

<style scoped>

</style>