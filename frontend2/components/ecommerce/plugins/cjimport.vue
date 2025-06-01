<template>
  <div class="">
    <img @click="open=true" src="/static/frontend/images/ecommerce/cj.png" alt="" srcset="" class="h-12 border p-2 cursor-pointer rounded active">
    <CommonModal v-if="open">
        <div class="absolute right-[10px] top-[12px]">
            <div @click="open = false" class="mx-auto cursor-pointer flex h-10 w-10 p-2 flex-shrink-0 items-center justify-center rounded-full bg-white border text-rose-800 hover:shadow-lg">
              <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><path fill="currentColor" d="M18.3 5.71a.996.996 0 0 0-1.41 0L12 10.59L7.11 5.7A.996.996 0 1 0 5.7 7.11L10.59 12L5.7 16.89a.996.996 0 1 0 1.41 1.41L12 13.41l4.89 4.89a.996.996 0 1 0 1.41-1.41L13.41 12l4.89-4.89c.38-.38.38-1.02 0-1.4z"/></svg>
            </div>
          </div>
          <div class="mt-3 text-center sm:mt-0 sm:text-left w-full">
            <h3 class="text-slate-100 p-4 bg-purple-600">Import From CJ Dropshipping</h3>
            <div class="px-4 py-8 pb-12 relative">
                <div class="my-1">
                    <label class="block text-sm font-medium text-gray-500 my-2">Product SKU</label>
                    <div class="flex">
                        <input v-model="sku" type="text" class="border px-3 py-2 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-l">
                        <button @click="importNow" class="px-3 py-2 rounded-none rounded-r  bg-purple-600 text-white">Import</button>
                    </div>
                </div>
                <div v-if="loading" class="mt-4 flex justify-center w-full h-full absolute left-0 top-0 bg-white">
                    <div class="animate-spin rounded-full h-20 w-20 border-t-2 border-b-2 border-purple-500"></div>
                </div>
                <div v-if="result" class="mt-4">
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
const sku = ref('CJLS1068782')
const open = ref(false)
const loading = ref(false)
const result = ref('')
function importNow(){
    loading.value = true
    Api.get('/api/ecommerce/dash/cjimport?sku='+sku.value).then(res => {
        loading.value = false
        console.log(res.data.success);
        if (res.data.success){
            notifs.value.push({
                title: 'Product Imported Successfully',
                type: 'success'
            })
            result.value = "Product Imported Successfully"
            manageData(res.data.data)
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
    console.log(cjData);
    newProduct.value.name = cjData.productNameEn;
    newProduct.value.cj_pid = cjData.pid;
    newProduct.value.sku = cjData.productSku;
    newProduct.value.short_description = cjData.productNameEn;
    newProduct.value.description = cjData.description;
    newProduct.value.material = cjData.materialNameEnSet[0];
    newProduct.value.origin = 'CN';
    newProduct.value.productWeight = cjData.productWeight;
    newProduct.value.packingWeight = cjData.packingWeight;
    newProduct.value.newUrlImages = cjData.productImageSet;
    newProduct.value.productvariant_set = []
    // jhamela here 
    var key = 'color'
    if(cjData.variants.length > 0){
        newProduct.value.has_variants = true;
        let firstVar = cjData.variants[0]
        let variantKey = firstVar.variantKey.split('-');
        if(variantKey.length == 1){
            newProduct.value.size_variant = false;
        }else if(variantKey.length == 2){
            newProduct.value.size_variant = true;
            const colorRegex = /^(\d|.)$/;
            console.log(colorRegex.test(variantKey[0]), variantKey[0]);
            if (colorRegex.test(variantKey[0])) {
              key = 'size'
            }
        }
    }
    for (let index = 0; index < cjData.variants.length; index++) {
        const cjVar = cjData.variants[index];
        var newVariation = {
            buy_price: '',
            sale_price: '',
            stock: 10,
            color: '',
            size: '',
            weight: '',
            model: '',
            material: '',
            new: true,
            id: ''
        }
        console.log(cjVar.variantKey)
        newVariation.buy_price = cjVar.variantSellPrice;
        newVariation.sale_price = cjVar.variantSellPrice;
        newVariation.id = cjVar.vid;
        let variantKey = cjVar.variantKey.split('-');
        if(variantKey.length == 1){
            newVariation.color = variantKey[0];
        }else if(variantKey.length == 2){
            if (key=='size'){
                newVariation.color = variantKey[1];
                newVariation.size = variantKey[0];
            }else{
                newVariation.color = variantKey[0];
                newVariation.size = variantKey[1];
            }
        }
        
        newProduct.value.productvariant_set.push(newVariation)
    }
    emits("setCJData", newProduct.value);
}

</script>

<style>
.cj .active{
    background-color: rgba(201, 239, 255, 0.178);
    border: 1px solid teal;
}
</style>