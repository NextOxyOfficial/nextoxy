<template>
    <div>
        <h5 class="my-2 font-bold">What do you want to sell?</h5>
        <p>By identifying the item of interest, the registration process can be tailored to suit the specific needs and preferences of the seller, facilitating a seamless and personalized onboarding experience. </p>
        <div class="checkboxes my-3 mt-8 flex flex-wrap gap-1 flex-col text-sm sm:flex-row">
            <div class="border pl-6 flex gap-1 justify-start items-center cursor-pointer rounded" :class="{'border-purple-500':productType.own}">
                <input v-model="productType.own" type="checkbox" name="type" id="own" class="">
                <label for="own" class="cursor-pointer p-3 md:p-6 w-full">Own Products</label>
            </div>
            <div class="border pl-6 flex gap-1 justify-start items-center cursor-pointer rounded" :class="{'border-purple-500':productType.digital}">
                <input v-model="productType.digital" type="checkbox" name="type" id="digital" class="">
                <label for="digital" class="cursor-pointer p-3 md:p-6 w-full">Digital Products</label>
            </div>
            <div class="border pl-6 flex gap-1 justify-start items-center cursor-pointer rounded" :class="{'border-purple-500':productType.dropshipping}">
                <input v-model="productType.dropshipping" type="checkbox" name="type" id="dropshipping">
                <label for="dropshipping" class="cursor-pointer p-3 md:p-6 w-full">Dropshipping Products</label>
            </div>
            <div class="border pl-6 flex gap-1 justify-start items-center cursor-pointer rounded" :class="{'border-purple-500':productType.services}">
                <input v-model="productType.services" type="checkbox" name="type" id="services" class="">
                <label for="services" class="cursor-pointer p-3 md:p-6 w-full">Services</label>
            </div>
            <div class="border pl-6 flex gap-1 justify-start items-center cursor-pointer rounded" :class="{'border-purple-500':productType.other}">
                <input v-model="productType.other" type="checkbox" name="type" id="other" class="">
                <label for="other" class="cursor-pointer p-3 md:p-6 w-full">Other</label>
            </div>
        </div>
    </div>
</template>

<script setup>
    const productType = ref({
        own: false,
        digital: false,
        dropshipping: false,
        services: false,
        other: false,
    })
</script>

<style scoped>
    .checkboxes > *{
        flex:1;
        min-width: 48%;
    }
    .radio-item input[type=radio]:checked + label:after {
      border-radius: 11px;
      width: 12px;
      height: 12px;
      position: absolute;
      top: 9px;
      left: 10px;
      content: " ";
      display: block;
      background: #749cc4;
    }
</style>