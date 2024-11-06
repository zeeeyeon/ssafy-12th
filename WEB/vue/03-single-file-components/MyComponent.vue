<template>
  <div class="greeting">
    {{ mag }}
  </div>
</template>

<script setup>
import { ref } from 'vue'

const mag = ref('hello')

</script>

<style scoped>
.greeting {
  color: aqua;
}

</style>