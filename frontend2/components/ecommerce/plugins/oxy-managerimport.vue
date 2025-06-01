<template>
    <div class="">
      <img @click="open=true" src="/static/frontend/images/ecommerce/oxymanager.svg" alt="" srcset="" class="h-12 border p-2 cursor-pointer rounded active">
      <CommonModal v-if="open">
          <div class="absolute right-[10px] top-[12px]">
              <div @click="open = false" class="mx-auto cursor-pointer flex h-10 w-10 p-2 flex-shrink-0 items-center justify-center rounded-full bg-white border text-rose-800 hover:shadow-lg">
                <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><path fill="currentColor" d="M18.3 5.71a.996.996 0 0 0-1.41 0L12 10.59L7.11 5.7A.996.996 0 1 0 5.7 7.11L10.59 12L5.7 16.89a.996.996 0 1 0 1.41 1.41L12 13.41l4.89 4.89a.996.996 0 1 0 1.41-1.41L13.41 12l4.89-4.89c.38-.38.38-1.02 0-1.4z"/></svg>
              </div>
            </div>
            <div class="mt-3 text-center sm:mt-0 sm:text-left w-full">
              <h3 class="text-slate-100 p-4 bg-purple-600">Import From OxyManager</h3>
              <div class="px-4 py-8 pb-12 relative">
                  <div class="my-1">
                      <label class="block text-sm font-medium text-gray-500 my-2">Product ID</label>
                      <div class="flex">
                          <input v-model="sku" type="text" class="border px-3 py-2 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-l">
                          <button @click="importNow" class="px-3 py-2 rounded-none rounded-r bg-purple-600 text-white">Import</button>
                      </div>
                  </div>
                  <div v-if="loading" class="mt-4 flex justify-center w-full h-full absolute left-0 top-0 bg-white">
                      <div class="animate-spin rounded-full h-20 w-20 border-t-2 border-b-2 border-purple-500"></div>
                  </div>
                  <div v-if="result" class="mt-4 text-green-600">
                      {{result}}
                  </div>
              </div>
            </div>
      </CommonModal>
    </div>
  </template>
  
  <script setup>
  const {notifs} = useAuth()
  const emits = defineEmits(["setCJData"])
  const Api = useApi()
  const sku = ref('')
  const open = ref(false)
  const loading = ref(false)
  const result = ref('')
  function importNow(){
      loading.value = true
      Api.get('/api/ecommerce/dash/oxymanagerimport?sku='+sku.value).then(res => {
          loading.value = false
          console.log(res.data), res.data.success;
          if (res.data.error){
                result.value = res.data.error
                notifs.value.push({
                    title: res.data.error,
                    type: 'error'
                })

          }else if (res.data.success){
              notifs.value.push({
                  title: 'Product Imported Successfully',
                  type: 'success'
              })
              result.value = "Product Imported Successfully"
              manageData(res.data)
          }else{
              result.value = res.data.message
              notifs.value.push({
                  title: res.data.message,
                  type: 'error'
              })
          }
      })
  }
  
  
  const newProduct = ref({
      name: '',
      buy_price:'0.00',
      sale_price:'',
      sku: '',
      short_description: '',
      description: '',
      highlight: 'new',
      material: '',
      origin: '',
      model: '',
      brandname: '',
      productWeight: '',
      packingWeight: '',
      shipping: '',
      categories: [],
      productvariant_set: [],
      has_variants: false,
      color_variant: true,
      size_variant: true,
      weight_variant: false,
      model_variant: false,
      material_variant: false,
      tags: [],
      newImages: [],
      draft: false,
      error: '',
      loading1: false,
      loading2: false,
      cj_pid: '',
      newUrlImages:[]
  })
  
  function manageData(cjData){
      open.value = false;
      newProduct.value.name = cjData.name;
      newProduct.value.oxymanager_id = cjData.id;
      newProduct.value.short_description = cjData.description;
      newProduct.value.description = cjData.description;
      newProduct.value.sale_price = cjData.price;
      newProduct.value.buy_price = cjData.buyrate;
      newProduct.value.stock = cjData.instock;
      newProduct.value.origin = 'CN';
      emits("setCJData", newProduct.value);
  }
  
  </script>
  
  <style>
  .cj .active{
      background-color: rgba(201, 239, 255, 0.178);
      border: 1px solid teal;
  }
  </style>