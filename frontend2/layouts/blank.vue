<template>
  <slot />
</template>

<script setup>
const {shop, getShop}= useShop()
getShop()
</script>

<style scoped>
</style>