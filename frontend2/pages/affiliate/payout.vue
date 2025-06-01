<template>
    <section>
        <!-- ====== Call To Action Section Start -->
        <section class="relative z-10 overflow-hidden bg-primary py-20 lg:py-[110px]">
            <div class="container mx-auto">
                <div class="relative overflow-hidden">
                    <div class="-mx-4 flex flex-wrap items-stretch">
                        <div class="w-full px-4">
                            <div class="mx-auto max-w-[570px] text-center">
                                <h2 class="mb-6 text-3xl font-semibold leading-snug text-slate-900 md:text-[40px] flex flex-col">
                                    <span class=""> USD ${{ overview.current_balance }} </span>
                                    <span class="font-light pr-0.5">Current Balance</span>
                                </h2>
                                <p class="mb-8 text-base leading-relaxed">
                                    You do not have any withdrawable balance. To withdraw, you must have at least USD $100 in your account.
                                </p>
                                <button @click="newW.active=true" class="inline-block rounded bg-[#13C296] py-3 px-7 text-base font-medium text-white transition hover:bg-opacity-90">
                                    Withdraw Now
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <div>
                <span class="absolute left-0 top-0">
                    <svg width="495" height="470" viewBox="0 0 495 470" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <circle cx="55" cy="442" r="138" stroke="white" stroke-opacity="0.04" stroke-width="50" />
                        <circle cx="446" r="39" stroke="white" stroke-opacity="0.04" stroke-width="20" />
                        <path d="M245.406 137.609L233.985 94.9852L276.609 106.406L245.406 137.609Z" stroke="white"
                            stroke-opacity="0.08" stroke-width="12" />
                    </svg>
                </span>
                <span class="absolute right-0 bottom-0">
                    <svg width="493" height="470" viewBox="0 0 493 470" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <circle cx="462" cy="5" r="138" stroke="white" stroke-opacity="0.04" stroke-width="50" />
                        <circle cx="49" cy="470" r="39" stroke="white" stroke-opacity="0.04" stroke-width="20" />
                        <path d="M222.393 226.701L272.808 213.192L259.299 263.607L222.393 226.701Z" stroke="white"
                            stroke-opacity="0.06" stroke-width="13" />
                    </svg>
                </span>
            </div>
        </section>
        <!-- ====== Call To Action Section End -->

        <!-- ====== Modal Section Start -->
        <section v-if="newW.active">
            <div class="dark:bg-dark fixed left-0 top-0 h-screen w-full overflow-y-scroll bg-white/10 py-10 z-40">
                <div class="dark:bg-dark-2 shadow-xl border dark:shadow-three mx-auto max-w-[465px] rounded-[10px] bg-white p-8">
                    <div class="border-stroke dark:border-dark-3 mb-9 overflow-hidden rounded-md border">
                        <img src="https://cdn.tailgrids.com/2.0/image/application/images/modals/image-01.svg" alt="modal image" class="w-full" />
                    </div>
                    <div class="text-center">
                        <h3 class="text-dark mb-2.5 text-2xl font-semibold dark:text-white sm:text-[28px]">Payout</h3>
                        <p class="text-body-color dark:text-dark-6 mb-6 text-sm">Payments are disbursed within a 48-hour timeframe. However, it is important to note that potential delays may arise on account of bank holidays.</p>
                        <div class="mb-9 flex items-center justify-center mx-auto relative w-[200px]">
                            <div class="absolute left-2 text-muted-500">USD $</div>
                            <input class="p-2 border pl-16 w-full rounded" type="text" v-model="newW.amount">
                        </div>
                        <p class="text-center mb-5" v-if="newW.error">{{newW.error}}</p>
                        <div class="flex items-center space-x-4">
                            <button @click="newW.active = false" class="text-body-color shadow-1 hover:bg-gray-2 dark:shadow-3 h-12 w-full rounded-md bg-white text-center text-base font-medium dark:bg-white/5 dark:text-white dark:hover:bg-white/10">Cancel</button>
                            <button class="bg-[#13C296] h-12 w-full rounded-md text-center text-base font-medium text-white hover:bg-opacity-90" @click="submitW">Submit Request</button>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <!-- ====== Modal Section End -->

        <div class=" max-w-5xl mx-auto mb-5 p-1">
            <p>Withdrawal History</p>
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
                            amount
                        </th>
                        <th scope="col" class="px-6 py-3">
                            Status
                        </th>
                    </tr>
                </thead>
                <tbody>
                    <tr class="bg-white border-b dark:bg-gray-800 dark:border-gray-700" v-for="item in list.results" :key="item.id">
                        <th scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                            {{item.date}}
                        </th>
                        <td class="px-6 py-4">
                            ${{item.amount}}
                        </td>

                        <td class="px-6 py-4">
                            {{item.status}}
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
const overview = ref('')
async function getOverview() {
    const res = await Api.get('/api/affiliate/overview/')
    overview.value = res.data
}
getOverview()
const list = ref('')
async function getList() {
    const res = await Api.get('/api/affiliate/withdraw/')
    list.value = res.data
}
getList()

const newW = ref({
    active: false,
    amount: 25,
    error: "",
})
async function submitW() {
    newW.value.error = ""
    if(!newW.value.amount || newW.value.amount < 25){
        newW.value.error = "Minimum withdrawal amount is $25."
        return;
    }
    if(newW.value.amount > overview.value.current_balance){
        newW.value.error = "Insufficient balance"
        return;
    }
    const res = await Api.post('/api/affiliate/withdraw/', newW.value)
    list.value = res.data
    newW.value.active = false
}
</script>

<style scoped></style>