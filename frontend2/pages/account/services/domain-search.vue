<template>
  <section>
    <BaseCard shape="rounded" class="px-2 md:px-6 py-4 md:py-12 w-full min-h-[50vh] flex flex-col justify-center items-center relative">
        <nuxt-link to="/account/services/domains" class="absolute top-1 left-1">
            <BaseButton color="primary" flavor="pastel" size="sm">My Domains</BaseButton>
        </nuxt-link>
      <BaseHeading
        as="h4"
        size="lg"
        weight="base"
        lead="tight"
        class="text-muted-800 mb-4 dark:text-white"
      >
        Domain Search..
      </BaseHeading>
    <div class="relative flex gap-1">
      <BaseInput
        v-model="search.query"
        type="email"
        label=""
        placeholder="Enter domain name..."
        icon="ph:magnifying-glass-thin"
        :error="search.error"
        @keypress.enter="getRes()"
        @keyup="search.result = ''"
      />
        <BaseButton v-if="search.loading" color="success" disabled>Search</BaseButton>
        <BaseButton v-else @click="getRes()" color="success">Search</BaseButton>
    </div>
    <div class="flex items-center justify-center my-5 gap-3" v-if="search.loading">
        <Icon name="svg-spinners:ring-resize" class="text-success-500 h-7 w-7" />
        <p>Please wait while we're checking domain's availability...</p>
    </div>

    <div class="my-4 w-full max-w-xl" v-if="search.result">
        <div class="w-full" v-if="search.result == 404">
            <BaseMessage type="warning" class="w-full">
                Sorry, <span>"{{search.query}}"</span> is not available!
            </BaseMessage>
        </div>
        <div class="" v-else>
            <BaseMessage type="info" class="w-full">
                <span>"{{search.query}}"</span> is available!
            </BaseMessage>
            <template  v-for="rate in search.result.rates">
                <div class="p-1 my-4 rounded flex flex-wrap gap-2 md:gap-3" v-if="rate['@Name'] == 'register'" :key="rate">
                    <BaseCard @click="setOrder(price['@Duration'], price['@Price'])" shape="curved" class="hover:shadow-lg cursor-pointer px-3 py-2 border border-dashed flex-1 w-full min-w-[200px] text-xs" :class="{'!border-success-500 shadow-lg dark:shadow-white/40':price['@Duration'] == search.duration}" v-for="price in rate['Product']['Price']" :key="price">
                        <div class="flex w-full items-center gap-2">
                        <Icon name="ph:shopping-cart" class="text-success-500 h-12 w-12 bg-slate-500/10 rounded-full p-2" />
                
                        <div>
                        <BaseHeading
                            tag="h6"
                            size="xs"
                            weight="medium"
                            class="text-muted-700 dark:text-muted-100"
                        >
                            Price USD ${{price['@Price']}}
                        </BaseHeading>
                        <div
                            class="flex items-center justify-center gap-6 sm:justify-start sm:gap-0"
                        >
                            Buy for {{price['@Duration']}} year <span v-if="price['@Duration'] > 1">s</span>
                        </div>
                        </div>
                
                    </div>
                    </BaseCard>
                </div>
            </template>
            <div class="w-full flex justify-end items-center">
                <BaseButton @click="createInvoice()" color="success">Checkout
                <Icon name="ic:baseline-arrow-right-alt" class="h-7 w-7" />
                </BaseButton>
            </div>
        </div>
    </div>
    </BaseCard>
  </section>
</template>

<script setup>
definePageMeta({
    layout: 'dashboard'
})
const Api = useApi()

const search = ref({
    query: '',
    result: '',
    loading: false,
    error: '',
    duration: '',
    amount: '',
})


async function getRes() {
    search.value.loading = false
    search.value.duration = ''
    search.value.error = ''
    if (!search.value.query){
        search.value.error = 'Please enter domain name'
        return
    }
    let domain = search.value.query
    domain = domain.replace(/^(https?:\/\/)?/, '');
    domain = domain.replace(/^www\./, '');

    const tldMatch = domain.match(/\.[^.]{2,}$/);
    const tld = tldMatch ? tldMatch[0].substr(1) : '';
    console.log(tld, domain);
    if (!tld){
        search.value.error = 'Please enter valid domain name. Eg: .com, .net, .org etc...'
        return
    }
    search.value.loading = true
    const res = await Api.get('/api/account/domains?tld='+tld+'&domain='+domain)
    console.log(res)
    search.value.result = res.data
    search.value.loading = false
}

function setOrder(duration, amount) {
    search.value.duration = duration;
    search.value.amount = amount;
}
async function createInvoice() {
    const res = await Api.post('/api/account/domains', {
        'domain': search.value.query,
        'duration': search.value.duration,
        'amount': search.value.amount,
    })
    console.log(res)
    navigateTo('/account/checkout/'+res.data)
}
</script>

<style scoped>
</style>