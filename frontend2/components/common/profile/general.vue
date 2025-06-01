<template>
    <div>
        <div class="space-y-6 sm:px-6 lg:col-span-9 lg:px-0 mt-4">
            <section aria-labelledby="payment-details-heading">
                <div>
                    <div class="shadow sm:overflow-hidden sm:rounded-md">
                    <div class="bg-white py-6 px-4 sm:p-6">
                        <div class="bg-slate-50 p-2 rounded">
                            <h2 id="payment-details-heading" class="text-lg font-medium leading-6 text-gray-900">Personal Info</h2>
                            <p class="mt-1 text-sm text-gray-500">Update your billing information. Please note that updating your location could affect your tax rates.</p>
                        </div>

                        <div class="mt-6 grid grid-cols-4 gap-6">
                        <div class="col-span-4 sm:col-span-2">
                            <label for="first-name" class="block text-sm font-medium text-gray-700">First name</label>
                            <input v-model="account.first_name" type="text" name="first-name" id="first-name" autocomplete="cc-given-name" class="mt-1 block w-full rounded-md border border-gray-300 py-2 px-3 shadow-sm focus:border-gray-900 focus:outline-none focus:ring-gray-900 sm:text-sm" />
                        </div>

                        <div class="col-span-4 sm:col-span-2">
                            <label for="last-name" class="block text-sm font-medium text-gray-700">Last name</label>
                            <input v-model="account.last_name" type="text" name="last-name" id="last-name" autocomplete="cc-family-name" class="mt-1 block w-full rounded-md border border-gray-300 py-2 px-3 shadow-sm focus:border-gray-900 focus:outline-none focus:ring-gray-900 sm:text-sm" />
                        </div>

                        <div class="col-span-4 sm:col-span-2">
                            <label for="email-address" class="block text-sm font-medium text-gray-700">Email address</label>
                            <input v-model="account.email" type="text" name="email-address" id="email-address" autocomplete="email" class="mt-1 block w-full rounded-md border border-gray-300 py-2 px-3 shadow-sm focus:border-gray-900 focus:outline-none focus:ring-gray-900 sm:text-sm" />
                        </div>

                        <div class="col-span-4 sm:col-span-2">
                            <label for="expiration-date" class="block text-sm font-medium text-gray-700">Phone number</label>
                            <input v-model="account.phone_number" type="text" class="mt-1 block w-full rounded-md border border-gray-300 py-2 px-3 shadow-sm focus:border-gray-900 focus:outline-none focus:ring-gray-900 sm:text-sm" />
                        </div>

                        <div class="col-span-4 sm:col-span-2">
                            <label for="expiration-date" class="block text-sm font-medium text-gray-700">Address</label>
                            <input v-model="account.address" type="text" class="mt-1 block w-full rounded-md border border-gray-300 py-2 px-3 shadow-sm focus:border-gray-900 focus:outline-none focus:ring-gray-900 sm:text-sm" />
                        </div>
                        <div class="col-span-4 sm:col-span-2">
                            <label for="expiration-date" class="block text-sm font-medium text-gray-700">City</label>
                            <input v-model="account.city" type="text" class="mt-1 block w-full rounded-md border border-gray-300 py-2 px-3 shadow-sm focus:border-gray-900 focus:outline-none focus:ring-gray-900 sm:text-sm" />
                        </div>
                        <div class="col-span-4 sm:col-span-2">
                            <label for="expiration-date" class="block text-sm font-medium text-gray-700">State</label>
                            <input v-model="account.state" type="text" class="mt-1 block w-full rounded-md border border-gray-300 py-2 px-3 shadow-sm focus:border-gray-900 focus:outline-none focus:ring-gray-900 sm:text-sm" />
                        </div>


                        <div class="col-span-4 sm:col-span-2">
                            <label for="country" class="block text-sm font-medium text-gray-700">Country</label>
                            <select v-model="account.country" id="country" name="country" autocomplete="country-name" class="mt-1 block w-full rounded-md border border-gray-300 bg-white py-2 px-3 shadow-sm focus:border-gray-900 focus:outline-none focus:ring-gray-900 sm:text-sm">
                                <option value="">Select Country</option>
                                <option v-for="con in countries" :value="con.code2">{{ con.name }}</option>
                            </select>
                        </div>

                        <div class="col-span-4 sm:col-span-2">
                            <label for="postal-code" class="block text-sm font-medium text-gray-700">ZIP / Postal code</label>
                            <input v-model="account.zip_code" type="text" name="postal-code" id="postal-code" autocomplete="postal-code" class="mt-1 block w-full rounded-md border border-gray-300 py-2 px-3 shadow-sm focus:border-gray-900 focus:outline-none focus:ring-gray-900 sm:text-sm" />
                        </div>
                        </div>
                    </div>
                    <div class="bg-white py-6 px-4 sm:p-6">
                        <div class="bg-slate-50 p-2 rounded">
                            <h2 id="payment-details-heading" class="text-lg font-medium leading-6 text-gray-900">Billing Info</h2>
                            <p class="mt-1 text-sm text-gray-500">Update your billing information. Please note that updating your location could affect your tax rates.</p>
                        </div>

                        <div class="mt-6 grid grid-cols-4 gap-6">
                        <div class="col-span-4 sm:col-span-2">
                            <label for="first-name" class="block text-sm font-medium text-gray-700">First name</label>
                            <input v-model="account.billing_first_name" type="text" name="first-name" id="first-name" autocomplete="cc-given-name" class="mt-1 block w-full rounded-md border border-gray-300 py-2 px-3 shadow-sm focus:border-gray-900 focus:outline-none focus:ring-gray-900 sm:text-sm" />
                        </div>

                        <div class="col-span-4 sm:col-span-2">
                            <label for="last-name" class="block text-sm font-medium text-gray-700">Last name</label>
                            <input v-model="account.billing_last_name" type="text" name="last-name" id="last-name" autocomplete="cc-family-name" class="mt-1 block w-full rounded-md border border-gray-300 py-2 px-3 shadow-sm focus:border-gray-900 focus:outline-none focus:ring-gray-900 sm:text-sm" />
                        </div>


                        <div class="col-span-4 sm:col-span-2">
                            <label for="expiration-date" class="block text-sm font-medium text-gray-700">Phone number</label>
                            <input v-model="account.billing_phone_number" type="text" class="mt-1 block w-full rounded-md border border-gray-300 py-2 px-3 shadow-sm focus:border-gray-900 focus:outline-none focus:ring-gray-900 sm:text-sm" />
                        </div>


                        <div class="col-span-4 sm:col-span-2">
                            <label for="expiration-date" class="block text-sm font-medium text-gray-700">Address</label>
                            <input v-model="account.billing_address" type="text" class="mt-1 block w-full rounded-md border border-gray-300 py-2 px-3 shadow-sm focus:border-gray-900 focus:outline-none focus:ring-gray-900 sm:text-sm" />
                        </div>
                        <div class="col-span-4 sm:col-span-2">
                            <label for="expiration-date" class="block text-sm font-medium text-gray-700">City</label>
                            <input v-model="account.billing_city" type="text" class="mt-1 block w-full rounded-md border border-gray-300 py-2 px-3 shadow-sm focus:border-gray-900 focus:outline-none focus:ring-gray-900 sm:text-sm" />
                        </div>
                        <div class="col-span-4 sm:col-span-2">
                            <label for="expiration-date" class="block text-sm font-medium text-gray-700">State</label>
                            <input v-model="account.billing_state" type="text" class="mt-1 block w-full rounded-md border border-gray-300 py-2 px-3 shadow-sm focus:border-gray-900 focus:outline-none focus:ring-gray-900 sm:text-sm" />
                        </div>


                        <div class="col-span-4 sm:col-span-2">
                            <label for="country" class="block text-sm font-medium text-gray-700">Country</label>
                            <select v-model="account.billing_country" id="country" name="country" autocomplete="country-name" class="mt-1 block w-full rounded-md border border-gray-300 bg-white py-2 px-3 shadow-sm focus:border-gray-900 focus:outline-none focus:ring-gray-900 sm:text-sm">
                                <option value="">Select Country</option>
                                <option v-for="con in countries" :value="con.code2">{{ con.name }}</option>
                            </select>
                        </div>

                        <div class="col-span-4 sm:col-span-2">
                            <label for="postal-code" class="block text-sm font-medium text-gray-700">ZIP / Postal code</label>
                            <input v-model="account.billing_zip_code" type="text" name="postal-code" id="postal-code" autocomplete="postal-code" class="mt-1 block w-full rounded-md border border-gray-300 py-2 px-3 shadow-sm focus:border-gray-900 focus:outline-none focus:ring-gray-900 sm:text-sm" />
                        </div>
                        </div>
                    </div>
                    <div class="bg-gray-50 px-4 py-3 text-right sm:px-6">
                        <button @click="saveAccount" type="submit" class="inline-flex justify-center rounded-md border border-transparent bg-gray-800 py-2 px-4 text-sm font-medium text-white shadow-sm hover:bg-gray-900 focus:outline-none focus:ring-2 focus:ring-gray-900 focus:ring-offset-2">Save</button>
                    </div>
                    </div>
                </div>
            </section>
        </div>
    </div>
</template>

<script setup>
    const { account, getAccount } = useAccount()
    const Api = useApi()
    const countries = ref([])
    function getCountries(){
        Api.get('/api/utils/countries/').then(res => {
            countries.value = res.data
        })
    }
    getCountries()

    function saveAccount(){
        Api.post('/api/account/profile', account.value).then(res => {
            getAccount()
            console.log(res)
        })
    }
</script>

<style scoped>

</style>