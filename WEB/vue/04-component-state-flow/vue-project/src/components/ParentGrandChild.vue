<script setup>
defineProps({
  myMsg: String,
})

// 상위 객체로 보낼 때 여기서 맞춰줘야함
const emit = defineEmits(['updateName'])

const edit = () => {
  // 상위 객체로 보낼 때 여기서 맞춰줘야함
  emit('updateName')
}
</script>

<template>
  <p>{{ myMsg }}</p>
  <button @click="edit">이름 변경</button>
</template>

<style scoped>

</style>