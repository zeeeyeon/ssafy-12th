<script setup>
import {useCartStore} from "@/stores/cart.js";
import {useRouter} from "vue-router";


const store = useCartStore();
const router = useRouter();

const goDetail = (product) => {
  router.push(`/${product.id}`)
}

const deleteToCart = (product) => {
  store.deleteToCart(product.id)
}
</script>

<template>
  <h1>장바구니</h1>

  <div v-if="store.carts.length > 0">
    <div class="product_list">
      <div v-for="product in store.carts" :key="product.id" class="product_card">
        <img :src="product.image" alt="" class="product_image">
        <div class="product_detail">
          <h3>{{ product.title }}</h3>
          <p>가격: ${{ product.price }}</p>
          <button @click="goDetail(product)">상세페이지로 이동</button>
          <button @click="deleteToCart(product)">장바구니에서 제거</button>
        </div>
      </div>
    </div>
  </div>

  <div v-else>
    <p>장바구니가 비어있습니다.</p>
  </div>
</template>

<style scoped>
.product_list {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
}

.product_card {
  border: 1px solid #ddd;
  width: 200px;
  padding: 15px;
}

.product_image {
  width: 100%;
}

.product_detail {
  text-align: center;
}
</style>