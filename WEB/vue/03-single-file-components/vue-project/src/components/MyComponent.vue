<script setup>
import MyComponentItem from "@/components/MyComponentItem.vue";

// const input = ref(null);

</script>

<template>
  <div>
    <h2>MyComponent</h2>
    <MyComponentItem/>
    <MyComponentItem/>
    <MyComponentItem/>
    <input ref="input"></input>

<!--    onMounted(() => {-->
<!--      console.log(input)-->
<!--    })-->
  </div>
</template>

<style scoped>

</style>