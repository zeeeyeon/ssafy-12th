<template>
  <div>
    <h1>LogIn Page</h1>
    <form @submit.prevent="login">
      <label for="username">username : </label>
      <input type="text" id="username" v-model.trim="username"><br>

      <label for="password">password : </label>
      <input type="password" id="password" v-model.trim="password"><br>

      <input type="submit" value="logIn">
    </form>
  </div>
</template>

<script setup>
import {ref} from "vue";
import {useCounterStore} from "@/stores/counter.js";

const store = useCounterStore()

const username = ref(null)
const password = ref(null)

const login = () => {
  const payload = {
    username: username.value,
    password: password.value
  }
  store.login(payload)
}
</script>

<style>

</style>
