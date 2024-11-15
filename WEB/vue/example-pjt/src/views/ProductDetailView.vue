<script setup>
// 이 페이지를 들어왔을 때 알 수 있는 것 : product의 id 값
import {useRoute, useRouter} from "vue-router";
import {useCartStore} from "@/stores/cart.js";

const route = useRoute();
// route 설정값이랑 맞는지 확인하기
const productId = route.params.product_id;

const store = useCartStore();

// axios를 써도 상관없지만 store에 데이터가 저장되어 있기 때문에 꺼내서 쓰면 됨
const product = store.getProductById(productId);
console.log(product);
</script>

<template>
  <h1>상세 페이지</h1>
<!--  새로고침했을때는 pinia 데이터가 다 날아감 => 랜더링이 안됨 -->
<!--  그래서 div에 조건문을 걸어줘야함-->
  {{ product }}
  <div v-if="product">
    <img :src="product.image" alt="" class="product_image">
    <h3>{{ product.title }}</h3>
    <p>가격: ${{ product.price }}</p>
    <p>카테고리: {{ product.category }}</p>
  </div>
</template>

<style scoped>

</style>