<template>

    <CommonModal>
        <div class="absolute right-[10px] top-[12px]">
            <div @click="closeModal" class="mx-auto cursor-pointer flex h-10 w-10 p-2 flex-shrink-0 items-center justify-center rounded-full bg-white border text-rose-800 hover:shadow-lg">
              <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><path fill="currentColor" d="M18.3 5.71a.996.996 0 0 0-1.41 0L12 10.59L7.11 5.7A.996.996 0 1 0 5.7 7.11L10.59 12L5.7 16.89a.996.996 0 1 0 1.41 1.41L12 13.41l4.89 4.89a.996.996 0 1 0 1.41-1.41L13.41 12l4.89-4.89c.38-.38.38-1.02 0-1.4z"/></svg>
            </div>
          </div>
        <div class="flex-1 mt-3 border-l text-center sm:mt-0 sm:text-left w-full">
            <h3 class="text-slate-800 p-4 bg-slate-100">Please Provide Billing Information</h3>
            <div class="flex flex-1 flex-col justify-center p-5 w-full">
              <div class="md:col-span-2 md:mt-0">
                <div class="bg-white py-6 px-4 sm:p-6">
                    <div class="bg-slate-50 p-2 rounded">
                        <p class="mt-1 text-sm text-gray-500">Update your billing information. Please note that updating your location could affect your tax rates.</p>
                    </div>

                    <div class="mt-6 grid grid-cols-4 gap-6">
                    <div class="col-span-4 sm:col-span-2">
                        <label for="first-name" class="block text-sm font-medium text-gray-700">First name <span class="text-rose-500">*</span> </label>
                        <input v-model="account.billing_first_name" type="text" name="first-name" id="first-name" autocomplete="cc-given-name" class="mt-1 block w-full rounded-md border border-gray-300 py-2 px-3 shadow-sm focus:border-gray-900 focus:outline-none focus:ring-gray-900 sm:text-sm" />
                    </div>

                    <div class="col-span-4 sm:col-span-2">
                        <label for="last-name" class="block text-sm font-medium text-gray-700">Last name <span class="text-rose-500">*</span> </label>
                        <input v-model="account.billing_last_name" type="text" name="last-name" id="last-name" autocomplete="cc-family-name" class="mt-1 block w-full rounded-md border border-gray-300 py-2 px-3 shadow-sm focus:border-gray-900 focus:outline-none focus:ring-gray-900 sm:text-sm" />
                    </div>


                    <div class="col-span-4 sm:col-span-2">
                        <label for="expiration-date" class="block text-sm font-medium text-gray-700">Phone number <span class="text-rose-500">*</span> </label>
                        <input v-model="account.billing_phone_number" type="text" class="mt-1 block w-full rounded-md border border-gray-300 py-2 px-3 shadow-sm focus:border-gray-900 focus:outline-none focus:ring-gray-900 sm:text-sm" />
                    </div>


                    <div class="col-span-4 sm:col-span-2">
                        <label for="expiration-date" class="block text-sm font-medium text-gray-700">Address <span class="text-rose-500">*</span> </label>
                        <input v-model="account.billing_address" type="text" class="mt-1 block w-full rounded-md border border-gray-300 py-2 px-3 shadow-sm focus:border-gray-900 focus:outline-none focus:ring-gray-900 sm:text-sm" />
                    </div>
                    <div class="col-span-4 sm:col-span-2">
                        <label for="expiration-date" class="block text-sm font-medium text-gray-700">City <span class="text-rose-500">*</span> </label>
                        <input v-model="account.billing_city" type="text" class="mt-1 block w-full rounded-md border border-gray-300 py-2 px-3 shadow-sm focus:border-gray-900 focus:outline-none focus:ring-gray-900 sm:text-sm" />
                    </div>
                    <div class="col-span-4 sm:col-span-2">
                        <label for="expiration-date" class="block text-sm font-medium text-gray-700">State <span class="text-rose-500">*</span> </label>
                        <input v-model="account.billing_state" type="text" class="mt-1 block w-full rounded-md border border-gray-300 py-2 px-3 shadow-sm focus:border-gray-900 focus:outline-none focus:ring-gray-900 sm:text-sm" />
                    </div>


                    <div class="col-span-4 sm:col-span-2">
                        <label for="country" class="block text-sm font-medium text-gray-700">Country <span class="text-rose-500">*</span> </label>
                        <select v-model="account.billing_country" id="country" name="country" autocomplete="country-name" class="mt-1 block w-full rounded-md border border-gray-300 bg-white py-2 px-3 shadow-sm focus:border-gray-900 focus:outline-none focus:ring-gray-900 sm:text-sm">
                            <option value="">Select Country</option>
                            <option v-for="con in countries" :value="con.code2">{{ con.name }}</option>
                        </select>
                    </div>

                    <div class="col-span-4 sm:col-span-2">
                        <label for="postal-code" class="block text-sm font-medium text-gray-700">ZIP / Postal code <span class="text-rose-500">*</span> </label>
                        <input v-model="account.billing_zip_code" type="text" name="postal-code" id="postal-code" autocomplete="postal-code" class="mt-1 block w-full rounded-md border border-gray-300 py-2 px-3 shadow-sm focus:border-gray-900 focus:outline-none focus:ring-gray-900 sm:text-sm" />
                    </div>
                    </div>
                </div>
              </div>

              <div class="methods px-6" v-if="account.billing_country">
                <div class="flex items-center justify-start gap-4 flex-wrap">
                  <div class="flex items-center relative">
                    <input v-model="account.payment_method" id="default-radio-1" type="radio" value="stripe" name="default-radio" class="payment-option absolute -z-10 opacity-0 pointer-events-none w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 cursor-pointer">
                    <label for="default-radio-1" class="p-2 relative border rounded text-sm font-medium text-gray-900 dark:text-gray-300 cursor-pointer">
                        <svg class="absolute left-1 top-1 bg-lime-600 p-1 rounded text-white" :class="{'opacity-30':account.payment_method=='sp'}" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path fill="currentColor" d="M11 8H6V6h5V4H8.5V3h-2v1H4v6h5v2H4v2h2.5v1h2v-1H11zm8.59 4.52l-5.66 5.65l-2.83-2.83l-1.41 1.42L13.93 21L21 13.93z"/></svg>
                        <img src="/static/frontend/images/stripe.png" class="h-14" alt="" srcset="">
                    </label>
                  </div>
                  <div class="flex items-center relative" v-if="account.billing_country == 'BD'">
                    <input v-model="account.payment_method" id="default-radio-2" type="radio" value="sp" name="default-radio" class="payment-option absolute -z-10 opacity-0 pointer-events-none w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 cursor-pointer">
                    <label for="default-radio-2" class="p-2 relative border rounded text-sm font-medium text-gray-900 dark:text-gray-300 cursor-pointer">
                        <svg class="absolute left-1 top-1 bg-lime-600 p-1 rounded text-white" :class="{'opacity-30':account.payment_method=='stripe'}" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path fill="currentColor" d="M11 8H6V6h5V4H8.5V3h-2v1H4v6h5v2H4v2h2.5v1h2v-1H11zm8.59 4.52l-5.66 5.65l-2.83-2.83l-1.41 1.42L13.93 21L21 13.93z"/></svg>
                        <img src="/static/frontend/images/sp.png" class="h-14" alt="" srcset="">
                    </label>
                  </div>
                </div>
              </div>

              <div class="flex justify-end my-4 gap-1">
                <button v-if="!status" @click="saveAccount" class="btn px-3 py-2">Save & Continue</button>
                <button v-if="status == 'saving'" class="flex items-center gap-2 btn px-8 py-2">
                    <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24"><path fill="currentColor" d="M12,1A11,11,0,1,0,23,12,11,11,0,0,0,12,1Zm0,19a8,8,0,1,1,8-8A8,8,0,0,1,12,20Z" opacity=".25"/><path fill="currentColor" d="M10.14,1.16a11,11,0,0,0-9,8.92A1.59,1.59,0,0,0,2.46,12,1.52,1.52,0,0,0,4.11,10.7a8,8,0,0,1,6.66-6.61A1.42,1.42,0,0,0,12,2.69h0A1.57,1.57,0,0,0,10.14,1.16Z"><animateTransform attributeName="transform" dur="0.75s" repeatCount="indefinite" type="rotate" values="0 12 12;360 12 12"/></path></svg>
                </button>
                <button v-if="status == 'saved'" class="flex items-center gap-2 btn px-3 py-2">
                    <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24"><path fill="currentColor" d="M9 16.17L4.83 12l-1.42 1.41L9 19L21 7l-1.41-1.41L9 16.17z"/></svg>
                    <span>Saved</span>
                </button>
              </div>
            </div>
          </div>
    </CommonModal>
  
</template>

<script setup>
    const { account, getAccount } = useAccount()
    const { notifs } = useAuth()
    const emit = defineEmits(['continueNext', 'closeModal'])

    function closeModal(){
        emit('closeModal')
    }

    const Api = useApi()
    const countries = ref([])
    function getCountries(){
        Api.get('/api/utils/countries/').then(res => {
            countries.value = res.data
        })
    }
    getCountries()

    const status = ref('')
    function saveAccount(){
        console.log(account.value.billing_zip_code == '');
        if(!account.value.billing_first_name || !account.value.billing_last_name || !account.value.billing_address || !account.value.billing_city || !account.value.billing_state || !account.value.billing_zip_code || !account.value.billing_country || !account.value.billing_phone_number){
            notifs.value.push({
                type: 'error',
                message: 'Please fill all the fields'
            })
            status.value = ''
            return
        }
        status.value = 'saving'
        Api.post('/api/account/profile', account.value).then(res => {
            console.log(res, account.value)
            notifs.value.push({
                type: 'success',
                message: 'Account updated successfully'
            })
            status.value = 'saved'
            setTimeout(() => {
                status.value = ''
            }, 2000)
            getAccount()
            emit('continueNext')
        })
    }
    // account.billing_country
    watchEffect(() => {
        if(account.value.billing_country == 'BD'){
            account.value.payment_method = 'sp'
        }else{
            account.value.payment_method = 'stripe'
        }
    })
</script>

<style scoped>
    .payment-option:checked + label {
        background-color: #3b83f625;
        border-radius: 5px;
        border: 1px solid teal;
        color: #fff;
    }
</style>