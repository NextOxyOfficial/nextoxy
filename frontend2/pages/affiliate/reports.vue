<template>
    <section>

        <div class=" max-w-5xl mx-auto mb-5 p-1 mt-8">
            <p>Commissions History</p>
            <p v-if="list && !list.results" class="p-3 text-center">No History Found</p>
        </div>
        <div class="relative overflow-x-auto max-w-5xl mx-auto" v-if="list && list.results">
            <table class="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400">
                <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
                    <tr>
                        <th scope="col" class="px-6 py-3">
                            Date
                        </th>
                        <th scope="col" class="px-6 py-3">
                            Product
                        </th>
                        <th scope="col" class="px-6 py-3">
                            amount
                        </th>
                    </tr>
                </thead>
                <tbody>
                    <tr class="bg-white border-b dark:bg-gray-800 dark:border-gray-700" v-for="item in list.results" :key="item.id">
                        <th scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                            {{item.date}}
                        </th>
                        <td class="px-6 py-4">
                            <span v-if="item.product">{{item.product.name}}</span>
                            <span v-else>NA</span>
                        </td>
                        <td class="px-6 py-4">
                            ${{item.commission}}
                        </td>

                    </tr>
                </tbody>
            </table>
        </div>
    </section>
</template>

<script setup>
definePageMeta({
    layout: 'affiliate'
})
const Api = useApi()

const list = ref('')
async function getList() {
    const res = await Api.get('/api/affiliate/commission/')
    list.value = res.data
}
getList()

</script>

<style scoped></style>