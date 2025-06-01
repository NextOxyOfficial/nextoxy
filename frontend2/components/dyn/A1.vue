<template>
  <section>a1 comps {{item}}</section>
</template>

<script setup>
const Api = useApi()
const item = ref('')
async function getItem() {
    const res = await Api.get('https://jsonplaceholder.typicode.com/todos/'+Math.floor(Math.random() * 10) )
    item.value = res.data
}
getItem()
</script>

<style scoped>
</style>