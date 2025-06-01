<template>
    <div class="flex flex-col justify-center items-center" v-if="!success">
        <h5 class="my-2 font-bold text-center">Creating Your Store!</h5>
        <div class="py-2 flex gap-5 flex-col max-w-sm mx-auto text-center">
            Please Wait A Few Seconds..
        </div>
        <img src="/static/frontend/images/ecommerce/website.gif" alt="" srcset="" class="rounded shadow w-[300px]">
    </div>
    <div class="flex flex-col justify-center items-center" v-else>
        <h5 class="my-2 font-bold text-center text-green-500">Congratulations, Your Store Is Now Ready!</h5>
        <div class="py-2 flex gap-5 flex-col max-w-sm mx-auto text-center">
            Your store is ready to launch, you can visit your store by clicking the "Complete" button below.
        </div>
        <img src="/static/frontend/images/ecommerce/success.gif" alt="" srcset="" class="rounded shadow w-[300px]">
    </div>
</template>

<script setup>
    const success = ref(false)
    setTimeout(() => {
        success.value = true
    }, 5000)
</script>

<style scoped>
    .radio-item input[type=radio]:checked + label:after {
      border-radius: 11px;
      width: 12px;
      height: 12px;
      position: absolute;
      top: 9px;
      left: 10px;
      content: " aaa";
      display: block;
      background: #749cc4;
    }
</style>