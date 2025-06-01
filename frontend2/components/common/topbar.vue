<template>
  <div class="w-full bg-gradient-to-r from-slate-900 to-slate-800 py-[7px]">
    <div class="container mx-auto">
        <div class="relative w-full">
        <p class="text-center text-xs md:text-base font-medium text-white">For support or any kind of suggestion/opinion please reach us to <span class="text-blue-200">support@nextoxy.com</span> & win a free t-shirt :)</p>
        <button @click="showAlert = false" class="absolute right-0 top-1/2 -translate-y-1/2 hidden">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <g opacity="0.8">
                <path d="M17 7L7 17" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
                <path fill-rule="evenodd" clip-rule="evenodd" d="M7 7L17 17L7 7Z" fill="white" />
                <path d="M7 7L17 17" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
            </g>
            </svg>
        </button>
        </div>
    </div>
  </div>
</template>

<script setup>

</script>

<style scoped>
</style>