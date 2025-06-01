<template>
    <div>
        <h5 class="my-6 font-bold">Enter your shop name</h5>
        <p class="text-sm">Please provide the name of your shop for account registration. Your shop name will serve as your unique identifier within our software platform.  </p>
        <div class="py-5 flex max-w-sm flex-wrap whitespace-nowrap gap-2">
            <input @keyup="checkAvailability" v-model="shopName" type="text" name="type" id="ec" class="border border-purple-500 rounded rounded-r-none px-2 py-2 flex-1 max-w-[200px]" placeholder="ShopName">
            <button class="p-2 rounded border border-purple-500 bg-purple-600 text-white" @click="emitRegisterWithShopName()">Create Shop</button>
        </div>
        <p class="text-rose-500 flex gap-1 items-center" v-if="error">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 32 32"><path fill="currentColor" d="M16 23a1.5 1.5 0 1 0 1.5 1.5A1.5 1.5 0 0 0 16 23zm-1-11h2v9h-2z"/><path fill="currentColor" d="M29 30H3a1 1 0 0 1-.887-1.461l13-25a1 1 0 0 1 1.774 0l13 25A1 1 0 0 1 29 30ZM4.65 28h22.7l.001-.003L16.002 6.17h-.004L4.648 27.997Z"/></svg>
            {{ error }}
        </p>


          <!-- terms  -->
        <div class="my-12">
            <p class="mt-2 text-center text-sm text-gray-600">
            <span class="font-medium text-gray-500 dark:text-gray-400">By signing up, you agree to our</span>
            <a href="/terms-of-service" target="_blank" class="text-orange-600 hover:text-orange-500">
                Terms & Conditions
            </a>
            <span class="font-medium text-gray-500 dark:text-gray-400"> ,</span>
            <a href="/privacy-policy" target="_blank" class="text-orange-600 hover:text-orange-500">
                Privacy Policy
            </a>
            <span class="font-medium text-gray-500 dark:text-gray-400"> and</span>
            <a href="/privacy-policy" target="_blank" class="text-orange-600 hover:text-orange-500">
                Cookie Policy
            </a>
            <span class="font-medium text-gray-500 dark:text-gray-400">.</span>
            </p>
        </div>
    </div>
</template>

<script setup>
    const Api = useApi()
    defineComponent({
      name: 'ChildCmp',
      emits: [ 'registerWithShopName' ],
    });
    const emit = defineEmits(['registerWithShopName'])
    const shopName = ref('')
    const error = ref('')

    async function emitRegisterWithShopName() {
        if (shopName.value.length > 0) {
            error.value = ''
        } else {
            error.value = 'Shop name is required!'
            return
        }
        shopName.value = shopName.value.replace(/[^a-zA-Z0-9-]/g, '').toLowerCase();
        const {data} = await Api.get('/api/account/ecommerce/?check='+shopName.value)
        if(data != 'not exists'){
            error.value = 'Shop name already exists!'
            return
        }
        emit('registerWithShopName', shopName.value)
    }
    function checkAvailability(){
        // remove all except a to z, Ato Z , 0 to 9 and hyphen, also lowercase everything
        shopName.value = shopName.value.replace(/[^a-zA-Z0-9-]/g, '').toLowerCase();
    }

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