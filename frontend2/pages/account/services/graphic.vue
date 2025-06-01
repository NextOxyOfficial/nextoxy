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
    const response = await Api.get('/api/account/service?type=GRAPHIC')
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
    const response = await Api.get('/api/ecommerce/dash/orders?search='+search.value)
    orders.value = response.data
}
const debouncedSearchOrder = debounce(searchOrder, 1000)


const manage = ref('')
async function setManage(order){
    manage.value = order
}

const new_order = ref({
  active: false,
  name: '',
  phone: '',
  email: '',
  title: 'Logo Design',
  detail: '',
  deadline: '',
  amount: '',
  message: '',
  type: 'GRAPHIC',
  method: 'stripe',
  error: '',
  filled: true,
})

async function placeOrder() {
  new_order.value.error = ''
  new_order.value.filled = true
  if(!new_order.value.name || !new_order.value.phone || !new_order.value.email || !new_order.value.title 
   || !new_order.value.amount || !new_order.value.message || !new_order.value.deadline || !new_order.value.detail
  ){
    new_order.value.error = 'All fields Are Requireds!'
    new_order.value.filled = false
    return
  }
  const response = await Api.post('/api/account/service', new_order.value)
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
      <CommonTitleIcon :filename="'pages-min.png'" title="Graphic Design"/>
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
                    ---
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
                          <BaseCard shape="rounded" class="p-1 md:p-6 mt-12">
                            <div class="flex gap-2 flex-wrap">
                              <p class="min-w-[20%]">Name</p>
                              <p class="min-w-[20%]">:</p>
                              <p class="flex-1">{{manage.data.name}}</p>
                            </div>
                            <div class="flex gap-2 flex-wrap">
                              <p class="min-w-[20%]">Phone</p>
                              <p class="min-w-[20%]">:</p>
                              <p class="flex-1">{{manage.data.phone}}</p>
                            </div>
                            <div class="flex gap-2 flex-wrap">
                              <p class="min-w-[20%]">Order Type</p>
                              <p class="min-w-[20%]">:</p>
                              <p class="flex-1">{{manage.data.title}}</p>
                            </div>
                            <div class="flex gap-2 flex-wrap">
                              <p class="min-w-[20%]">Order Detail</p>
                              <p class="min-w-[20%]">:</p>
                              <p class="flex-1">{{manage.data.detail}}</p>
                            </div>
                            <div class="flex gap-2 flex-wrap">
                              <p class="min-w-[20%]">Message</p>
                              <p class="min-w-[20%]">:</p>
                              <p class="flex-1">{{manage.data.message}}</p>
                            </div>
                            <div class="flex gap-2 flex-wrap">
                              <p class="min-w-[20%]">Deadline</p>
                              <p class="min-w-[20%]">:</p>
                              <p class="flex-1">{{manage.data.deadline}}</p>
                            </div>
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
            <Icon name="game-icons:pencil-brush" class="h-6 w-6" />
            <p>Graphic Design Service</p>
          </span>
        </span>

          <BaseButtonClose @click="new_order.active = false" />
        </div>
      </template>
      <!-- Body -->
      <div class="p-4 md:p-6 lg:p-12 lg:pt-2 max-h-[65vh] overflow-y-scroll">
        <div class="mt-2">
          <div class="grid grid-cols-12 gap-4">
            
            <div class="col-span-12 sm:col-span-6 rounded p-[2px]" :class="{'bg-red-400/20':!new_order.filled && !new_order.name}">
              <div name="firstName">
                <BaseInput
                  label="Business Name"
                  placeholder="ex: John"
                  v-model="new_order.name"
                  type="text"
                />
              </div>
            </div>

            <div class="col-span-12 sm:col-span-6 rounded p-[2px]" :class="{'bg-red-400/20':!new_order.filled && !new_order.phone}">
              <div name="lastName">
                <BaseInput
                  label="Contact Number"
                  placeholder="ex: Doe"
                  v-model="new_order.phone"
                  type="text"
                />
              </div>
            </div>
            <div class="col-span-12 sm:col-span-6 rounded p-[2px]" :class="{'bg-red-400/20':!new_order.filled && !new_order.email}">
              <div name="lastName">
                <BaseInput
                  label="Email"
                  placeholder="Eg: example@mail.com"
                  v-model="new_order.email"
                  type="text"
                />
              </div>
            </div>
             
            <div class="col-span-12 sm:col-span-6 rounded p-[2px]"  :class="{'bg-red-400/20':!new_order.filled && !new_order.title}">
              <div name="type">
                <BaseSelect v-model="new_order.title" shape="rounded" label="Design Type">
                  <option value="Logo Design">Logo Design</option>
                  <option value="Banner Design">Banner Design</option>
                  <option value="Mockup">Mockup</option>
                  <option value="Other">Other</option>
                </BaseSelect>
              </div>
            </div>
             <br>
             <div class="col-span-12 rounded p-[2px]" :class="{'bg-red-400/20':!new_order.filled && !new_order.detail}">
              <div name="message">
                <BaseTextarea
                  label="Order Detail"
                  placeholder="write about your order..."
                  v-model="new_order.detail"
                />
              </div>
            </div>
            <div class="col-span-12 sm:col-span-6 rounded p-[2px]" :class="{'bg-red-400/20':!new_order.filled && !new_order.amount}">
              <div name="budget">
                <BaseInput
                  type="number"
                  label="Your Budget (USD)"
                  placeholder="$200"
                  v-model="new_order.amount"
                />
              </div>
            </div>

            <div class="col-span-12 sm:col-span-6" :class="{'bg-red-400/20':!new_order.filled && !new_order.deadline}">
              <div name="lastName">
                <BaseInput
                  label="Deadline"
                  placeholder=""
                  v-model="new_order.deadline"
                  type="date"
                />
              </div>
            </div>

            <div class="col-span-12 rounded p-[2px]" :class="{'bg-red-400/20':!new_order.filled && !new_order.message}">
              <div name="message">
                <BaseTextarea
                  label="Message"
                  placeholder="write your message..."
                  v-model="new_order.message"
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
            <span class="text-slate-800 font-bold " v-if="new_order.amount">Total ${{ new_order.amount }} </span>
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
