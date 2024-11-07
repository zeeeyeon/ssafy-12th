<script setup>
defineProps({
  myProp: Object
})
</script>

<template>
  <p>{{ myProp.id }}</p>
  <p>{{ myProp.name }}</p>
</template>

<style scoped>

</style>