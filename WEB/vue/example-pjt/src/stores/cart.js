import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from "axios";

export const useCartStore = defineStore('cart', () => {

  // 실행했을 때 데이터를 받아온 순간 문제가 안생기는 이유 : localstorage 에 데이터가 들어가게 됨. (pinia 사용시)
  // 컴포넌트에 들어가면
  // 위에 저장된 userId로 서버에 요철하도록 구현하는 경우가 많음
  // user 객체를 넣으면 모든 데이터가 다 넘어가게 됨. (유의)
  // let loginUser = ref({'userId': userId})


  // 여러 개의 컴포넌트에서 활용하는 데이터만 store 로 관리해야 한다. !
  // 여러 명이 작업할 때 체감이 될 것 @
  let products = ref([])
  let carts = ref([])

  // 데이터 다운로드
  const getProducts = () => {
    // promise(비동기) 객체와 동일하게 활용
    // 성공했을 때 .then, 실패했을 때 .catch
    axios.get('https://fakestoreapi.com/products')
        .then(res => {
          console.log(res.data)
          products.value = res.data
        })
        .catch(err => {
          console.log(err)
        })
  }

  // 상세 페이지 상품 조회
  const getProductById = (id) => {
    const product = products.value.find((element) => {
          console.log(element, id)
          return element.id == id
    }
    )
    return product
  }

  // 1. 장바구니에 추가하기
  const addToCart = (product) => {
  // 장바구니에 포함되어 있지 않다면 추가
    const index = carts.value.findIndex((element) => element.id === product.id)

    if (index === -1) {
      alert('장바구니 페이지로 이동합니다.')
      carts.value.push(product);
    }else {
      alert('이미 추가된 상품입니다.')
    }
  }


  // 2. 장바구니에서 삭제하기
  const deleteToCart = (productId) => {
    // 1. id를 통해서 해당 상품의 index를 찾는다.
  //   2. 해당 index를 기준으로 하나를 제거한다. (splice)
    const index = carts.value.findIndex((element) => element.id === productId)
    if (index !== -1) {
      carts.value.splice(index, 1)
    }
  }




  return { products, carts, getProducts, getProductById, addToCart, deleteToCart }
}, {persis: true})
// 실행했을 때 데이터를 받아온 순간 문제가 안생기는 이유 : localstorage 에 데이터가 들어가게 됨.
