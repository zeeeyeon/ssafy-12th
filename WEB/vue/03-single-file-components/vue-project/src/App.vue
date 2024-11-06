<template>
  <h1>App.Vue</h1>
  <MyComponent/>
</template>

<script setup>
// @ - src 경로를 뜻하는 약어
import MyComponent from "@/components/MyComponent.vue";
</script>

<style scoped>
// 하위 컴포넌트의 최상위 태그까지는 영향을 끼친다.
// 태그 선택자를 선택하지보다 클래스 선택자를 사용하여 클래스를 지정해 주는 것이 좋음.
div {
  border: 1px solid black;
}
</style>
