<template>
    <div>
        <h5 class="my-2 font-bold">Where do you want to sell your products?</h5>
        <p>During software account registration, you'll be asked, "Where do you want to sell your products?" This question seeks to understand your intended marketplaces for product distribution. Specify your target platforms or regions to effectively reach your customers and expand your business reach. </p>
        <div class="checkboxes my-3 mt-8 flex flex-wrap gap-1 flex-col text-sm sm:flex-row">
            <div class="border pl-6 flex gap-1 justify-start items-center cursor-pointer rounded" :class="{'border-purple-500':productType.facebook}">
                <input v-model="productType.facebook" type="checkbox" name="type" id="facebook" class="">
                <label for="facebook" class="cursor-pointer p-3 md:p-6 w-full">Facebook</label>
            </div>
            <div class="border pl-6 flex gap-1 justify-start items-center cursor-pointer rounded" :class="{'border-purple-500':productType.instagram}">
                <input v-model="productType.instagram" type="checkbox" name="type" id="instagram" class="">
                <label for="instagram" class="cursor-pointer p-3 md:p-6 w-full">Instagram</label>
            </div>
            <div class="border pl-6 flex gap-1 justify-start items-center cursor-pointer rounded" :class="{'border-purple-500':productType.twitter}">
                <input v-model="productType.twitter" type="checkbox" name="type" id="twitter" class="">
                <label for="twitter" class="cursor-pointer p-3 md:p-6 w-full">Twitter</label>
            </div>
            <div class="border pl-6 flex gap-1 justify-start items-center cursor-pointer rounded" :class="{'border-purple-500':productType.pinterest}">
                <input v-model="productType.pinterest" type="checkbox" name="type" id="pinterest" class="">
                <label for="pinterest" class="cursor-pointer p-3 md:p-6 w-full">Pinterest</label>
            </div>
            <div class="border pl-6 flex gap-1 justify-start items-center cursor-pointer rounded" :class="{'border-purple-500':productType.youtube}">
                <input v-model="productType.youtube" type="checkbox" name="type" id="youtube" class="">
                <label for="youtube" class="cursor-pointer p-3 md:p-6 w-full">Youtube</label>
            </div>
            <div class="border pl-6 flex gap-1 justify-start items-center cursor-pointer rounded" :class="{'border-purple-500':productType.tiktok}">
                <input v-model="productType.tiktok" type="checkbox" name="type" id="tiktok" class="">
                <label for="tiktok" class="cursor-pointer p-3 md:p-6 w-full">Tiktok</label>
            </div>
            <div class="border pl-6 flex gap-1 justify-start items-center cursor-pointer rounded" :class="{'border-purple-500':productType.reddit}">
                <input v-model="productType.reddit" type="checkbox" name="type" id="reddit" class="">
                <label for="reddit" class="cursor-pointer p-3 md:p-6 w-full">Reddit</label>
            </div>
            <div class="border pl-6 flex gap-1 justify-start items-center cursor-pointer rounded" :class="{'border-purple-500':productType.blog}">
                <input v-model="productType.blog" type="checkbox" name="type" id="blog" class="">
                <label for="blog" class="cursor-pointer p-3 md:p-6 w-full">Blog</label>
            </div>
            <div class="border pl-6 flex gap-1 justify-start items-center cursor-pointer rounded" :class="{'border-purple-500':productType.snapchat}">
                <input v-model="productType.snapchat" type="checkbox" name="type" id="snapchat" class="">
                <label for="snapchat" class="cursor-pointer p-3 md:p-6 w-full">Snapchat</label>
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
        facebook: false,
        instagram: false,
        twitter: false,
        pinterest: false,
        youtube: false,
        tiktok: false,
        reddit: false,
        blog: false,
        snapchat: false,
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