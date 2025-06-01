<template>
  <section class="max-w-xl mx-auto bg-slate-50 p-4 md:p-16 my-6 text-muted-700">
        <p class="w-full text-xl mb-2 text-center uppercase">Bank Account Information</p>
        <p class="w-full text-center">Please provide your bank account information in order to receive contactless payouts</p>
        <hr class="my-4">
        <!-- <div class="mb-6">
            <label for="email" class="block mb-2 text-sm font-medium">Full Name</label>
            <input v-model="overview.name" type="text" id="name" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Full Name" required>
        </div>
        <div class="mb-6">
            <label for="email" class="block mb-2 text-sm font-medium">Your email</label>
            <input v-model="overview.email" type="email" id="email" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Email Address" required>
        </div>
        <div class="mb-6">
            <label for="email" class="block mb-2 text-sm font-medium">Your phone</label>
            <input v-model="overview.phone" type="email" id="email" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Email Address" required>
        </div> -->
        <div class="mb-6">
            <label for="email" class="block mb-2 text-sm font-medium">Bank Name</label>
            <input v-model="overview.bank_name" type="text" id="name" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="" required>
        </div>
        <div class="mb-6">
            <label for="email" class="block mb-2 text-sm font-medium">Account Number</label>
            <input v-model="overview.bank_account" type="email" id="email" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="" required>
        </div>
        <div class="mb-6">
            <label for="email" class="block mb-2 text-sm font-medium">Routing Number</label>
            <input v-model="overview.bank_routing" type="email" id="email" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="" required>
        </div>
        <div class="mb-6">
            <label for="email" class="block mb-2 text-sm font-medium">Bank Address</label>
            <input v-model="overview.bank_address" type="email" id="email" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="" required>
        </div>

        <button @click="saveData" type="submit" class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">Save</button>
  </section>
</template>

<script setup>
definePageMeta({
    layout: 'affiliate'
})
const Api = useApi()
const overview = ref('')
async function getOverview() {
    const res = await Api.get('/api/affiliate/overview/')
    overview.value = res.data
}
getOverview()
async function saveData() {
    const res = await Api.post('/api/affiliate/overview/', overview.value)
    overview.value = res.data
}
</script>

<style scoped>
</style>