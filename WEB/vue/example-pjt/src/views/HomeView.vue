<script setup>
import {useCartStore} from "@/stores/cart.js";
import {onMounted} from "vue";
import {useRouter} from "vue-router";

// api 로 데이터를 다운로드 받아야한다.
// setup 에서 호출하는 게 맞을까?
// 무슨 문제점이 발생할 수 있을까?
// -> DOM 입장에서는 없는 데이터로 화면을 그리려고 시도할 수 있음
// -> 데이터 다운로드보다 DOM을 그리는게 더 느리다.
const store = useCartStore()
// setup : DOM이 그려지기 전에 호출
// 데이터 다운로드는 DOM이 그려지고 난 후에 가져오는 걸 권장
onMounted(() => {
  store.getProducts()
})

// 라우터를 이동시켜주는 기능
// 클릭했을 때 보내야함 => router

const router = useRouter()
const goDetail = (product) => {
  router.push(`/${product.id}`)
}

const addToCart = (product) => {
  store.addToCart(product)
  // 경로말고 name으로 바꿔주기
  router.push("/cart")
}
</script>

<template>
  <h1>상품 목록 리스트</h1>
  <div class="product_list">
    <div v-for="product in store.products" :key="product.id" class="product_card">
      <img :src="product.image" alt="" class="product_image">
      <div class="product_detail">
        <h3>{{ product.title }}</h3>
        <p>가격: ${{ product.price }}</p>
        <button @click="goDetail(product)">상세페이지로 이동</button>
        <button @click="addToCart(product)">장바구니로 이동</button>
      </div>
    </div>
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