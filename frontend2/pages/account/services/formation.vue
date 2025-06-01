<script setup lang="ts">
import { debounce } from 'lodash'
import { Dialog, DialogPanel, DialogTitle, TransitionChild, TransitionRoot } from '@headlessui/vue'
import { CheckCircleIcon, ChevronRightIcon, EnvelopeIcon, PhoneIcon, CurrencyDollarIcon } from '@heroicons/vue/20/solid'
definePageMeta({
    layout: 'dashboard'
})

const Api = useApi()
const {shop}= useShop()


const orders = ref([])
const getOrders = async () => {
    const response = await Api.get('/api/account/service?type=FORMATION')
    orders.value = response.data
}
getOrders()
const loadMore = async (url) => {
    var url = url.split("/api/account/service");
    url = url[url.length - 1];
    const response = await Api.get('/api/account/service'+url)
    orders.value.results = orders.value.results.concat(response.data.results)
    orders.value.next = response.data.next
}
const search = ref('')
const searchOrder = async () => {
    const response = await Api.get('/api/account/service?search='+search.value)
    orders.value = response.data
}
const debouncedSearchOrder = debounce(searchOrder, 1000)


const manage = ref('')
async function setManage(order){
    manage.value = order
}

const usStates = ref([
  { name: 'Wyoming', fee: 102},
  { name: 'Colorado', fee: 50},
  { name: 'Kentucky', fee: 50},
])

const new_order = ref({
  active: false,
  type: 'FORMATION',
  method: 'stripe',
  title: 'Business Formation',
  company_type: "LTD",
  company_country: 'USA',
  company_state: { name: 'Wyoming', fee: 102},
  feature: 'business',
  company_name: '',
  company_name_alternative: '',
  owner1: {
    name: '',
    share: '',
  },
  owner2: {
    name: '',
    share: '',
  },
  owner3: {
    name: '',
    share: '',
  },
  owner4: {
    name: '',
    share: '',
  },
  email: '',
  full_name: '',
  gender: 'male',
  dob: '',
  phone: '',
  address: '',
  city: '',
  state: '',
  zip: '',
  country: '',
  amount: 299,
  amount2: 149,
  filled: true,
  error: '',
})
function getTotal() {
  if (new_order.value.company_country == 'USA'){
    var amt = new_order.value.amount + new_order.value.company_state.fee
  }else{
    var amt = new_order.value.amount2
  }

  return amt
}

async function placeOrder() {
  new_order.value.error = ''
  new_order.value.filled = true
  if(!new_order.value.company_name || !new_order.value.company_name_alternative
    || !new_order.value.email || !new_order.value.full_name || !new_order.value.dob || !new_order.value.phone
    || !new_order.value.address || !new_order.value.city || !new_order.value.state || !new_order.value.zip
    || !new_order.value.country
  ){
    new_order.value.error = 'All fields Are Requireds!'
    new_order.value.filled = false
    return
  }
  var data = JSON.parse(JSON.stringify(new_order.value))
  data.amount = getTotal()
  const response = await Api.post('/api/account/service', data)
  console.log(response.data);
  if (response.data){
    navigateTo('/account/checkout/'+response.data)
  }else{
    getOrders()
  }
  new_order.value.active = false
}

function payNow(order) {
    navigateTo('/account/checkout/'+order.invoice_id)
}


</script>

<template>
  <div>
    <div class="border-b border-gray-200/10 pb-5 sm:flex sm:items-center sm:justify-between">
      <CommonTitleIcon :filename="'pages-min.png'" title="USA/UK Business Formation"/>
    </div>
    <TairoContentWrapper>
     <template #left>
        <BaseInput
          v-model="search"
          icon="lucide:search"
          shape="full"
          placeholder="Find By Name Or Email..."
          :classes="{
            wrapper: 'w-full sm:w-auto',
          }"
          @keyup="debouncedSearchOrder"
        />
      </template>
      <template #right>
        <BaseButton @click="new_order.active = true" class="w-full sm:w-32" color="primary" shape="full">New Order</BaseButton>
      </template>
      <div>
        <div v-if="orders && orders.results &&  orders.results.length === 0">
          <BasePlaceholderPage
            title="No matching results"
            subtitle="Looks like we couldn't find any matching results for your search terms. Try other search terms."
          >
            <template #image>
              <img
                class="block dark:hidden"
                src="/static/img/illustrations/placeholders/flat/placeholder-search-4.svg"
                alt="Placeholder image"
              />
              <img
                class="hidden dark:block"
                src="/static/img/illustrations/placeholders/flat/placeholder-search-4-dark.svg"
                alt="Placeholder image"
              />
            </template>
          </BasePlaceholderPage>
        </div>
        <div v-else class="pt-6">
          <TransitionGroup
            enter-active-class="transform-gpu"
            enter-from-class="opacity-0 -translate-x-full"
            enter-to-class="opacity-100 translate-x-0"
            leave-active-class="absolute transform-gpu"
            leave-from-class="opacity-100 translate-x-0"
            leave-to-class="opacity-0 -translate-x-full"
          >
            <DemoFlexTableRow
              v-for="(order, index) in orders.results"
              :key="index"
              shape="straight"
              condensed
              spaced
            >
                <template #start>
                <DemoFlexTableCell
                  label="Order #"
                  :hide-label="index > 0"
                  tablet-hidden
                  class="w-full sm:w-[140px] whitespace-nowrap"
                >
                  <div class="text-xs">{{order.id}}</div>
                </DemoFlexTableCell>
                <DemoFlexTableCell
                  label="Order Date"
                  :hide-label="index > 0"
                  tablet-hidden
                  class="w-full sm:w-[140px] whitespace-nowrap"
                >
                  <div class="text-xs">{{order.created_at}}</div>
                </DemoFlexTableCell>
                <DemoFlexTableCell
                  label="Order Title"
                  class="w-full text-center"
                  :hide-label="index > 0"
                  type="stable"
                >
                  <span
                    class="text-muted-500 dark:text-muted-500 font-sans text-xs text-right md:text-left mb-1 md:mb-0"
                  >
                    <p class="font-medium truncate text-center">{{ order.title }}</p>
                  </span>
                </DemoFlexTableCell>
              </template>
              <template #end>
                <DemoFlexTableCell
                  label="status"
                  :hide-label="index > 0"
                  class="w-full sm:w-16"
                >
                  <BaseTag
                    color="success"
                    shape="full"
                    flavor="pastel"
                    size="sm"
                    class="capitalize whitespace-nowrap"
                    v-if="order.paid"
                  >
                    {{ order.status }}
                  </BaseTag>
                  <BaseTag
                    color="info"
                    shape="full"
                    flavor="pastel"
                    size="sm"
                    class="capitalize whitespace-nowrap"
                    v-else
                  >
                    Awaiting Payment
                  </BaseTag>
                </DemoFlexTableCell>
                
                <DemoFlexTableCell
                  label="Amount"
                  :hide-label="index > 0"
                  class="w-full sm:w-40"
                >
                  <span
                    class="text-muted-500 dark:text-muted-500 font-sans text-xs text-right md:text-left mb-1 md:mb-0"
                  >
                    <p class="font-medium truncate">USD ${{ order.amount }}</p>
                  </span>
                </DemoFlexTableCell>
                <DemoFlexTableCell label="action" :hide-label="index > 0">
                  <BaseButtonAction @click="setManage(order)" color="success">
                    <span>Details</span>
                  </BaseButtonAction>
                </DemoFlexTableCell>
                <DemoFlexTableCell
                  label="Payment"
                  :hide-label="index > 0"
                  class="w-full sm:w-28"
                >
                  <BaseTag
                    color="success"
                    shape="full"
                    flavor="pastel"
                    size="sm"
                    class="capitalize whitespace-nowrap"
                    v-if="order.paid"
                  >
                    Paid
                  </BaseTag>
                  <BaseTag
                    color="warning"
                    shape="full"
                    flavor="pastel"
                    size="sm"
                    class="capitalize whitespace-nowrap"
                    v-else
                  >
                    Draft/Unpaid
                  </BaseTag>
                </DemoFlexTableCell>
                <DemoFlexTableCell label="Action" :hide-label="index > 0" class="min-w-[120px]">
                  <BaseButton @click="payNow(order)" class="border border-muted-500 border-dashed !font-xs" size='sm' color="" flavor="outline" v-if="!order.paid">
                    <span class="text-xs">Pay Now</span>
                  </BaseButton>
                  <BaseTag
                    color="success"
                    shape="full"
                    flavor="pastel"
                    size="sm"
                    class="capitalize"
                    v-else
                  >
                    ----
                  </BaseTag>
                </DemoFlexTableCell>
              </template>
            </DemoFlexTableRow>
          </TransitionGroup>
        </div>
        <div class="flex items-center justify-center my-2">
            <BaseButton shape="rounded" class="flex w-[200px] justify-center" @click="loadMore(orders.next)" v-if="orders && orders.next">
              Load More
            </BaseButton>
        </div>
      </div>
    </TairoContentWrapper>

    <CommonOver :show="manage != ''">
            <DialogPanel class="pointer-events-auto relative w-screen max-w-3xl">
              <TransitionChild as="template" enter="ease-in-out duration-500" enter-from="opacity-0" enter-to="opacity-100" leave="ease-in-out duration-500" leave-from="opacity-100" leave-to="opacity-0">
                <div class="absolute top-0 md:-left-2 flex pt-1 z-[9] pr-2 sm:-ml-10 sm:pr-4">
                  <span type="button" class="rounded-full  shadow-xl bg-slate-100 dark:bg-slate-900 hover: cursor-pointer p-1" @click="manage = ''">
                    <span class="sr-only">Close panel</span>
                    <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><path fill="currentColor" d="M20 6.91L17.09 4L12 9.09L6.91 4L4 6.91L9.09 12L4 17.09L6.91 20L12 14.91L17.09 20L20 17.09L14.91 12L20 6.91Z"/></svg>
                  </span>
                </div>
              </TransitionChild>
              <div class="flex h-full flex-col overflow-y-scroll bg-white dark:bg-slate-900 py-6 shadow-xl" v-if="manage">
                <p class="p-2 w-full text-center border-b mb-3">{{manage.title}}</p>
                <div class="px-4 sm:px-6 flex flex-wrap gap-1 justify-center items-center">
                    <BaseTag shape="rounded" color="primary" flavor="outline">Amount: USD ${{ manage.amount }}</BaseTag>
                    <BaseTag shape="rounded" color="success" flavor="outline">Status: {{ manage.status }}</BaseTag>
                </div>
                <div class="relative mt-6 flex-1 px-4 sm:px-6">

                  <ul role="list" class="my-10 mx-auto">
                    <li >
                      <div class="relative pb-4">
                        <div class="relative flex space-x-3">
                          <div>
                            <span class="h-6 w-6 rounded-full flex items-center justify-center ring-6 ring-white bg-slate-400 ">
                              <TairoCheckAnimated class="h-6 w-6" />
                            </span>
                          </div>
                          <div class="flex min-w-0 flex-1 justify-between gap-2 pt-[2px] flex-wrap">
                            <div>
                              <p class="text-sm ">
                                Order Placed <a class="font-medium "></a>
                              </p>
                            </div>
                            <div class="whitespace-nowrap text-sm">
                               {{ manage.created_at }}
                            </div>
                          </div>
                        </div>
                          <BaseCard shape="rounded" class="p-1 md:p-6 mt-12 details-table text-muted-500">

                            <div class="flex gap-2 flex-wrap">
                                <p class="min-w-[20%]">Order</p>
                                <p class="min-w-[20%]">:</p>
                                <p class="flex-1">{{manage.data.title}}</p>
                            </div>
                            <div class="flex gap-2 flex-wrap">
                              <p class="min-w-[20%]">Phone</p>
                              <p class="min-w-[20%]">:</p>
                              <p class="flex-1">{{manage.data.phone}}</p>
                            </div>
                            <div class="flex gap-2 flex-wrap">
                                <p class="min-w-[20%]">Email</p>
                                <p class="min-w-[20%]">:</p>
                                <p class="flex-1">{{manage.data.email}}</p>
                            </div>


                            <div class="flex gap-2 flex-wrap">
                                <p class="min-w-[20%]">Company name</p>
                                <p class="min-w-[20%]">:</p>
                                <p class="flex-1">{{manage.data.company_name}}</p>
                            </div>
                            <div class="flex gap-2 flex-wrap">
                                <p class="min-w-[20%]">Alternative name</p>
                                <p class="min-w-[20%]">:</p>
                                <p class="flex-1">{{manage.data.company_name_alternative}}</p>
                            </div>
                            <div class="flex gap-2 flex-wrap">
                                <p class="min-w-[20%]">Company country</p>
                                <p class="min-w-[20%]">:</p>
                                <p class="flex-1">{{manage.data.company_country}}</p>
                            </div>

                            <div class="flex gap-2 flex-wrap" v-if="manage.data.company_country == 'USA'">
                                <p class="min-w-[20%]">Company State</p>
                                <p class="min-w-[20%]">:</p>
                                <p class="flex-1">{{manage.data.company_state.name}}</p>
                            </div>

                            <div class="flex gap-2 flex-wrap">
                                <p class="min-w-[20%]">Payment status</p>
                                <p class="min-w-[20%]">:</p>
                                <p class="flex-1" v-if="manage.paid">Paid</p>
                                <p class="flex-1" else>Unpaid</p>
                            </div>

                            <div class="flex gap-2 flex-wrap">
                                <p class="min-w-[20%]">Address</p>
                                <p class="min-w-[20%]">:</p>
                                <p class="flex-1">{{manage.data.address}}</p>
                            </div>
                            <div class="flex gap-2 flex-wrap">
                                <p class="min-w-[20%]">City</p>
                                <p class="min-w-[20%]">:</p>
                                <p class="flex-1">{{manage.data.city}}</p>
                            </div>
                            <div class="flex gap-2 flex-wrap">
                                <p class="min-w-[20%]">State</p>
                                <p class="min-w-[20%]">:</p>
                                <p class="flex-1">{{manage.data.state}}</p>
                            </div>
                            <div class="flex gap-2 flex-wrap">
                                <p class="min-w-[20%]">Zip</p>
                                <p class="min-w-[20%]">:</p>
                                <p class="flex-1">{{manage.data.zip}}</p>
                            </div>
                            <div class="flex gap-2 flex-wrap">
                                <p class="min-w-[20%]">Country</p>
                                <p class="min-w-[20%]">:</p>
                                <p class="flex-1">{{manage.data.country}}</p>
                            </div>

                            <div class="flex gap-2 flex-wrap">
                                <p class="min-w-[20%]">Amount</p>
                                <p class="min-w-[20%]">:</p>
                                <p class="flex-1">${{manage.data.amount}}</p>
                            </div>
                            <div class="flex gap-2 flex-wrap">
                                <p class="min-w-[20%]">Created At</p>
                                <p class="min-w-[20%]">:</p>
                                <p class="flex-1">{{manage.created_at}}</p>
                            </div>


                            <!-- Repeat the above structure for other data fields -->

                          </BaseCard>
                      </div>
                    </li>
                  </ul>

                </div>
              </div>
            </DialogPanel>
    </CommonOver>

    <TairoModal :open="new_order.active" size="xl" @close="new_order.active = false">
      <template #header>
        <!-- Header -->
        <div class="flex w-full items-center justify-between p-4 md:p-6 bg-slate-600/0 border-b">
        <span>
          <h3 class="font-heading text-muted-900 text-lg font-medium leading-6 dark:text-white">
            Place New Order
          </h3>
          <span class="flex gap-1 text-muted-500 justify-center mt-1">
            <Icon name="fluent:building-bank-28-regular" class="h-6 w-6" />
            <p>USA & UK Business Formation</p>
          </span>
        </span>

          <BaseButtonClose @click="new_order.active = false" />
        </div>
        <BaseMessage class="w-full x-4 flex !p-1" type="warning" message="Business bank account openings are subject to partner approval. NextOxy bears no responsibility. We ensure accurate and timely document submission." shape="" icon />
      </template>
      <!-- Body -->
      <div class="p-4 max-h-[65vh] overflow-y-scroll bf">
        <div class="mt-2">
            <p class="text-muted-500 dark:text-muted-500 mb-8 text-lg w-full text-center">
                Select Your Suitable Package
            </p>
            <BaseTabSlider
              v-model="new_order.company_country"
              :tabs="[
                  { label: 'USA', value: 'USA' },
                  { label: 'UK', value: 'UK' },
              ]"
              v-slot="{ activeValue }"
            >
              <div v-if="activeValue === 'USA'" class="font-sans text-sm text-gray-500 dark:text-gray-400">
                  <div class="bg-white">
                      <form
                      action=""
                      method="POST"
                      @submit.prevent
                      class="mx-auto max-w-7xl px-4"
                      >
                      <div>
                          <div>
                          <div class="w-full">
                              <div class="mx-auto w-full">
                              <div class="w-full">
                                  <div class="mx-auto mb-8 flex max-w-[350px]">
                                  <!-- <BaseRadioHeadless
                                      v-model="pricingMode"
                                      name="radio_custom"
                                      value="free"
                                  >
                                      <BaseCard
                                      shape="curved"
                                      class="peer-checked:!border-primary-500 relative border-2 p-8 opacity-60 grayscale peer-checked:opacity-100 peer-checked:grayscale-0 peer-checked:[&_.child]:!opacity-100"
                                      >
                                      <div class="flex flex-col text-center">
                                          <img
                                          src="/static/img/illustrations/onboarding/pricing-1.svg"
                                          alt="2 factor authentication with email"
                                          class="mx-auto mb-3 max-w-[160px]"
                                          />
                                          <BaseHeading size="md" weight="medium"
                                          >Free</BaseHeading
                                          >
                                          <BaseParagraph
                                          size="xs"
                                          lead="snug"
                                          class="text-muted-500 dark:text-muted-500 mb-3"
                                          >
                                          Start for free with most of our features. Get familiar
                                          with it and upgrade when you are ready.
                                          </BaseParagraph>
                                          <div class="my-1 text-left flex items-center gap-1">
                                              <Icon name="ph:check-circle-duotone" class="text-info-500 h-4 w-4 mt-[-2]" />
                                              <p>Close resubing pending tasks</p>
                                          </div>
                                          <div class="my-1 text-left flex items-center gap-1">
                                              <Icon name="ph:check-circle-duotone" class="text-info-500 h-4 w-4 mt-[-2]" />
                                              <p>Close resubing pending tasks</p>
                                          </div>
                                          <div class="my-1 text-left flex items-center gap-1">
                                              <Icon name="ph:check-circle-duotone" class="text-info-500 h-4 w-4 mt-[-2]" />
                                              <p>Close resubing pending tasks</p>
                                          </div>
                                          <div class="my-1 text-left flex items-center gap-1">
                                              <Icon name="ph:check-circle-duotone" class="text-info-500 h-4 w-4 mt-[-2]" />
                                              <p>Close resubing pending tasks</p>
                                          </div>
                                          <div
                                          class="flex items-center justify-center gap-2 pt-4"
                                          >
                                          <BaseText>
                                              <span>$0</span>
                                              <span class="text-muted-500 text-xs">
                                              /per month</span
                                              >
                                          </BaseText>
                                          </div>
                                      </div>
                                      <div class="child absolute end-2 top-3 opacity-0">
                                          <Icon
                                          name="ph:check-circle-duotone"
                                          class="text-primary-500 h-7 w-7"
                                          />
                                      </div>
                                      </BaseCard>
                                  </BaseRadioHeadless> -->
                                  <BaseRadioHeadless
                                      v-model="new_order.feature"
                                      name="radio_custom"
                                      value="business"
                                  >
                                      <BaseCard
                                      shape="curved"
                                      class="peer-checked:!border-primary-500 relative border-2 p-8 opacity-60 grayscale peer-checked:opacity-100 peer-checked:grayscale-0 peer-checked:[&_.child]:!opacity-100"
                                      >
                                      <div class="flex flex-col text-center">
                                          <img
                                          src="/static/img/illustrations/onboarding/pricing-3.svg"
                                          alt="2 factor authentication with app"
                                          class="mx-auto mb-3 max-w-[160px]"
                                          />
                                          <BaseHeading size="md" weight="medium"
                                          >Business</BaseHeading
                                          >
                                          <BaseParagraph
                                          size="xs"
                                          lead="snug"
                                          class="text-muted-500 dark:text-muted-500 mb-3"
                                          >
                                          An all-in-one plan for your business, with everything
                                          you need. Perfect for growing at large scale.
                                          </BaseParagraph>
                                          <div class="my-1 text-left flex items-center gap-1">
                                              <Icon name="ph:check-circle-duotone" class="text-info-500 h-4 w-4 mt-[-2]" />
                                              <p>Employer ID Number (EIN)</p>
                                          </div>
                                          <div class="my-1 text-left flex items-center gap-1">
                                              <Icon name="ph:check-circle-duotone" class="text-info-500 h-4 w-4 mt-[-2]" />
                                              <p>Open USA Business Bank Accounts</p>
                                          </div>
                                          <div class="my-1 text-left flex items-center gap-1">
                                              <Icon name="ph:check-circle-duotone" class="text-info-500 h-4 w-4 mt-[-2]" />
                                              <p>Articles Of Incorporation Certificate</p>
                                          </div>
                                          <div class="my-1 text-left flex items-center gap-1">
                                              <Icon name="ph:check-circle-duotone" class="text-info-500 h-4 w-4 mt-[-2]" />
                                              <p>ByLaw Documents</p>
                                          </div>
                                          <div class="my-1 text-left flex items-center gap-1">
                                              <Icon name="ph:check-circle-duotone" class="text-info-500 h-4 w-4 mt-[-2]" />
                                              <p>Registered USA Address</p>
                                          </div>
                                          <div class="my-1 text-left flex items-center gap-1">
                                              <Icon name="ph:check-circle-duotone" class="text-info-500 h-4 w-4 mt-[-2]" />
                                              <p>Registered Filing Agent</p>
                                          </div>
                                          <div
                                          class="flex items-center justify-center gap-2 pt-4"
                                          >
                                          <BaseText>
                                              <span>${{new_order.amount}}</span>
                                              <span class="text-muted-500 text-xs">
                                              (One Time)</span
                                              >
                                          </BaseText>
                                          </div>
                                      </div>
                                      <div class="child absolute end-2 top-3 opacity-0">
                                          <Icon
                                          name="ph:check-circle-duotone"
                                          class="text-primary-500 h-7 w-7"
                                          />
                                      </div>
                                      </BaseCard>
                                  </BaseRadioHeadless>
                                  </div>
                              </div>
                              </div>
                          </div>
                          </div>
                      </div>
                      </form>
                  </div>
              </div>

              <div
                  v-else-if="activeValue === 'UK'"
                  class="font-sans text-sm text-gray-500 dark:text-gray-400"
              >   
                  <div class="bg-white">
                      <form
                      action=""
                      method="POST"
                      @submit.prevent
                      class="mx-auto max-w-7xl px-4"
                      >
                      <div>
        

                          <div>
                          <div class="w-full">
                              <div class="mx-auto w-full">
                              <div class="w-full">
                                  <div class="mx-auto mb-8 flex max-w-[350px]">
                                  <!-- <BaseRadioHeadless
                                      v-model="pricingMode"
                                      name="radio_custom"
                                      value="free"
                                  >
                                      <BaseCard
                                      shape="curved"
                                      class="peer-checked:!border-primary-500 relative border-2 p-8 opacity-60 grayscale peer-checked:opacity-100 peer-checked:grayscale-0 peer-checked:[&_.child]:!opacity-100"
                                      >
                                      <div class="flex flex-col text-center">
                                          <img
                                          src="/static/img/illustrations/onboarding/pricing-1.svg"
                                          alt="2 factor authentication with email"
                                          class="mx-auto mb-3 max-w-[160px]"
                                          />
                                          <BaseHeading size="md" weight="medium"
                                          >Free</BaseHeading
                                          >
                                          <BaseParagraph
                                          size="xs"
                                          lead="snug"
                                          class="text-muted-500 dark:text-muted-500 mb-3"
                                          >
                                          Start for free with most of our features. Get familiar
                                          with it and upgrade when you are ready.
                                          </BaseParagraph>
                                          <div class="my-1 text-left flex items-center gap-1">
                                              <Icon name="ph:check-circle-duotone" class="text-info-500 h-4 w-4 mt-[-2]" />
                                              <p>Close resubing pending tasks</p>
                                          </div>
                                          <div class="my-1 text-left flex items-center gap-1">
                                              <Icon name="ph:check-circle-duotone" class="text-info-500 h-4 w-4 mt-[-2]" />
                                              <p>Close resubing pending tasks</p>
                                          </div>
                                          <div class="my-1 text-left flex items-center gap-1">
                                              <Icon name="ph:check-circle-duotone" class="text-info-500 h-4 w-4 mt-[-2]" />
                                              <p>Close resubing pending tasks</p>
                                          </div>
                                          <div class="my-1 text-left flex items-center gap-1">
                                              <Icon name="ph:check-circle-duotone" class="text-info-500 h-4 w-4 mt-[-2]" />
                                              <p>Close resubing pending tasks</p>
                                          </div>
                                          <div
                                          class="flex items-center justify-center gap-2 pt-4"
                                          >
                                          <BaseText>
                                              <span>$0</span>
                                              <span class="text-muted-500 text-xs">
                                              /per month</span
                                              >
                                          </BaseText>
                                          </div>
                                      </div>
                                      <div class="child absolute end-2 top-3 opacity-0">
                                          <Icon
                                          name="ph:check-circle-duotone"
                                          class="text-primary-500 h-7 w-7"
                                          />
                                      </div>
                                      </BaseCard>
                                  </BaseRadioHeadless> -->
                                  <BaseRadioHeadless
                                      v-model="new_order.feature"
                                      name="radio_custom"
                                      value="business"
                                  >
                                      <BaseCard
                                      shape="curved"
                                      class="peer-checked:!border-primary-500 relative border-2 p-8 opacity-60 grayscale peer-checked:opacity-100 peer-checked:grayscale-0 peer-checked:[&_.child]:!opacity-100"
                                      >
                                      <div class="flex flex-col text-center">
                                          <img
                                          src="/static/img/illustrations/onboarding/pricing-3.svg"
                                          alt="2 factor authentication with app"
                                          class="mx-auto mb-3 max-w-[160px]"
                                          />
                                          <BaseHeading size="md" weight="medium"
                                          >Business</BaseHeading
                                          >
                                          <BaseParagraph
                                          size="xs"
                                          lead="snug"
                                          class="text-muted-500 dark:text-muted-500 mb-3"
                                          >
                                          An all-in-one plan for your business, with everything
                                          you need. Perfect for growing at large scale.
                                          </BaseParagraph>
                                          <div class="my-1 text-left flex items-center gap-1">
                                            <Icon
                                              name="ph:check-circle-duotone"
                                              class="text-info-500 h-4 w-4 mt-[-2]"
                                            />
                                            <p>Business Registration Certificate</p>
                                          </div>
                                          <div class="my-1 text-left flex items-center gap-1">
                                            <Icon
                                              name="ph:check-circle-duotone"
                                              class="text-info-500 h-4 w-4 mt-[-2]"
                                            />
                                            <p>Business Wise</p>
                                          </div>
                                          <div class="my-1 text-left flex items-center gap-1">
                                            <Icon
                                              name="ph:check-circle-duotone"
                                              class="text-info-500 h-4 w-4 mt-[-2]"
                                            />
                                            <p>Business PayPal</p>
                                          </div>
                                          <div class="my-1 text-left flex items-center gap-1">
                                            <Icon
                                              name="ph:check-circle-duotone"
                                              class="text-info-500 h-4 w-4 mt-[-2]"
                                            />
                                            <p>Bank Account By Wise</p>
                                          </div>
                                          <div class="my-1 text-left flex items-center gap-1">
                                            <Icon
                                              name="ph:check-circle-duotone"
                                              class="text-info-500 h-4 w-4 mt-[-2]"
                                            />
                                            <p>Registered Filing Agent</p>
                                          </div>
                                          <div class="my-1 text-left flex items-center gap-1">
                                            <Icon
                                              name="ph:check-circle-duotone"
                                              class="text-info-500 h-4 w-4 mt-[-2]"
                                            />
                                            <p>UK Registered Address</p>
                                          </div>
                                          <div
                                          class="flex items-center justify-center gap-2 pt-4"
                                          >
                                          <BaseText>
                                              <span>$149</span>
                                              <span class="text-muted-500 text-xs">
                                              /per month</span
                                              >
                                          </BaseText>
                                          </div>
                                      </div>
                                      <div class="child absolute end-2 top-3 opacity-0">
                                          <Icon
                                          name="ph:check-circle-duotone"
                                          class="text-primary-500 h-7 w-7"
                                          />
                                      </div>
                                      </BaseCard>
                                  </BaseRadioHeadless>
                                  </div>
                              </div>
                              </div>
                          </div>
                          </div>
                      </div>
                      </form>
                  </div>
              </div>
            </BaseTabSlider>
          <div class="grid grid-cols-12 gap-4">

            <div class="col-span-12 sm:col-span-6 rounded p-[2px]"  :class="{'bg-red-400/20':!new_order.filled && !new_order.company_type}">
              <div name="type">
                <BaseSelect v-model="new_order.company_type" shape="rounded" label="Company Name Ending">
                  <option value="LIMITED">Limited</option>
                  <option value="LTD">LTD</option>
                </BaseSelect>
              </div>
            </div>
            <div class="col-span-12 sm:col-span-6 rounded p-[2px]"  :class="{'bg-red-400/20':!new_order.filled && !new_order.company_state}" v-if="new_order.company_country == 'USA'">
              <div name="type">
                <BaseSelect v-model="new_order.company_state" shape="rounded" label="Registering State">
                  <option v-for="st in usStates" :key="st.name" :value="st">{{st.name}} (State Fee ${{st.fee}})</option>
                </BaseSelect>
              </div>
            </div>
            
            
            <div class="col-span-12 sm:col-span-6 rounded p-[2px]" :class="{'bg-red-400/20':!new_order.filled && !new_order.company_name}">
              <div name="firstName">
                <BaseInput
                  label="Company Name"
                  placeholder="ex: NextOxy Technology LTD"
                  v-model="new_order.company_name"
                  type="text"
                />
              </div>
            </div>
            <div class="col-span-12 sm:col-span-6 rounded p-[2px]" :class="{'bg-red-400/20':!new_order.filled && !new_order.company_name_alternative}">
              <div name="firstName">
                <BaseInput
                  label="Chose alternative company name if the first one isn't available"
                  placeholder="ex: NextOxy Technology Limited"
                  v-model="new_order.company_name_alternative"
                  type="text"
                />
              </div>
            </div>
            <p class="text-muted-500 pb-2 border-b mb-2 col-span-12 mt-7 rounded p-[2px]">Business Owners/Directors</p>
            <div class="col-span-12 sm:col-span-6 rounded p-[2px]" :class="{'bg-red-400/20':!new_order.filled && !new_order.owner1}">
              <div name="firstName">
                <BaseInput
                  label="1. Owner name"
                  placeholder="ex: John"
                  v-model="new_order.owner1.name"
                  type="text"
                />
              </div>
            </div>
            <div class="col-span-12 sm:col-span-6 rounded p-[2px]" :class="{'bg-red-400/20':!new_order.filled && !new_order.owner1}">
              <div name="firstName">
                <BaseInput
                  label="1. Owner Share"
                  placeholder="ex: 25%"
                  v-model="new_order.owner1.share"
                  type="text"
                />
              </div>
            </div>

            <div class="col-span-12 sm:col-span-6 rounded p-[2px]" >
              <div name="firstName">
                <BaseInput
                  label="2. Owner name"
                  placeholder="ex: John"
                  v-model="new_order.owner2.name"
                  type="text"
                />
              </div>
            </div>
            <div class="col-span-12 sm:col-span-6 rounded p-[2px]">
              <div name="firstName">
                <BaseInput
                  label="2. Owner Share"
                  placeholder="ex: 25%"
                  v-model="new_order.owner2.share"
                  type="text"
                />
              </div>
            </div>
            
            <div class="col-span-12 sm:col-span-6 rounded p-[2px]" >
              <div name="firstName">
                <BaseInput
                  label="3. Owner name"
                  placeholder="ex: John"
                  v-model="new_order.owner3.name"
                  type="text"
                />
              </div>
            </div>
            <div class="col-span-12 sm:col-span-6 rounded p-[2px]">
              <div name="firstName">
                <BaseInput
                  label="3. Owner Share"
                  placeholder="ex: 25%"
                  v-model="new_order.owner3.share"
                  type="text"
                />
              </div>
            </div>

            <div class="col-span-12 sm:col-span-6 rounded p-[2px]" >
              <div name="firstName">
                <BaseInput
                  label="4. Owner name"
                  placeholder="ex: John"
                  v-model="new_order.owner4.name"
                  type="text"
                />
              </div>
            </div>
            <div class="col-span-12 sm:col-span-6 rounded p-[2px]">
              <div name="firstName">
                <BaseInput
                  label="4. Owner Share"
                  placeholder="ex: 25%"
                  v-model="new_order.owner4.share"
                  type="text"
                />
              </div>
            </div>


             



            <p class="text-muted-500 pb-2 border-b mb-2 col-span-12 mt-7 rounded p-[2px]">Personal Information</p>
            <div class="col-span-12 sm:col-span-6" :class="{'bg-red-400/20':!new_order.filled && !new_order.email}">
              <div name="lastName">
                <BaseInput
                  label="Business Email"
                  placeholder=""
                  v-model="new_order.email"
                  type="text"
                />
              </div>
            </div>
            <div class="col-span-12 sm:col-span-6" :class="{'bg-red-400/20':!new_order.filled && !new_order.full_name}">
              <div name="lastName">
                <BaseInput
                  label="Full Name"
                  placeholder="Eg: John Doe"
                  v-model="new_order.full_name"
                  type="text"
                />
              </div>
            </div>
             <div class="col-span-12 sm:col-span-6 flex gap-3 pt-[35px] relative rounded p-[2px]">
              <label for="" class="nui-input-label absolute top-[10px] left-0 text-xs">Gender</label>
              <BaseRadio
                v-model="new_order.gender"
                name="checkbox_base"
                value="male"
                label="Male"
                color="success"
              />
              <BaseRadio
                v-model="new_order.phone"
                name="checkbox_base"
                value="female"
                label="Female"
                color="success"
              />
            </div>
            <div class="col-span-12 sm:col-span-6" :class="{'bg-red-400/20':!new_order.filled && !new_order.dob}">
              <div name="lastName">
                <BaseInput
                  label="Date Of Birth"
                  placeholder="Eg: 01/01/1997"
                  v-model="new_order.dob"
                  type="date"
                />
              </div>
            </div>
            <div class="col-span-12 sm:col-span-6" :class="{'bg-red-400/20':!new_order.filled && !new_order.phone}">
              <div name="lastName">
                <BaseInput
                  label="Phone Number"
                  placeholder="Eg: +12312313"
                  v-model="new_order.phone"
                  type="text"
                />
              </div>
            </div>

            
           
            

            <p class="text-muted-500 pb-2 border-b mb-2 col-span-12 mt-7 rounded p-[2px]">Your Local Address</p>
            <div class="col-span-12 sm:col-span-6" :class="{'bg-red-400/20':!new_order.filled && !new_order.address}">
              <div name="lastName">
                <BaseInput
                  label="Address"
                  placeholder=""
                  v-model="new_order.address"
                  type="text"
                />
              </div>
            </div>
            <div class="col-span-12 sm:col-span-6" :class="{'bg-red-400/20':!new_order.filled && !new_order.city}">
              <div name="lastName">
                <BaseInput
                  label="City"
                  placeholder=""
                  v-model="new_order.city"
                  type="text"
                />
              </div>
            </div>
            <div class="col-span-12 sm:col-span-6" :class="{'bg-red-400/20':!new_order.filled && !new_order.state}">
              <div name="lastName">
                <BaseInput
                  label="State"
                  placeholder=""
                  v-model="new_order.state"
                  type="text"
                />
              </div>
            </div>
            <div class="col-span-12 sm:col-span-6" :class="{'bg-red-400/20':!new_order.filled && !new_order.zip}">
              <div name="lastName">
                <BaseInput
                  label="Zip Code"
                  placeholder=""
                  v-model="new_order.zip"
                  type="text"
                />
              </div>
            </div>
            <div class="col-span-12 sm:col-span-6" :class="{'bg-red-400/20':!new_order.filled && !new_order.country}">
              <div name="lastName">
                <BaseInput
                  label="Country"
                  placeholder=""
                  v-model="new_order.country"
                  type="text"
                />
              </div>
            </div>

          </div>
        </div>
      </div>

      <template #footer>
        <!-- Footer -->
        <div class="p-4 md:p-6 flex-1 border-t">
        <p class="w-full text-center text-rose-500 p-1 pb-2" v-if="new_order.error">{{new_order.error}}</p>
          <div class="flex gap-x-2 justify-center items-center">
            <span class="text-slate-800 font-bold ">Total ${{getTotal()}} </span>
            <BaseButton @click="new_order.active = false">Close</BaseButton>
            <BaseButton color="primary" flavor="solid" @click="placeOrder">
              Create Order
            </BaseButton>
          </div>
        </div>
      </template>
    </TairoModal>
  </div>
</template>


<style>
.bf .nui-tab-slider-track{
    margin: auto !important;
}
</style>

<style scoped>
.details-table > div{
  margin-bottom: 10px;
}
</style>