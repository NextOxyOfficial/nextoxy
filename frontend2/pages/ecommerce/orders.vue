<script setup lang="ts">
import { debounce } from "lodash";
import {
  Dialog,
  DialogPanel,
  DialogTitle,
  TransitionChild,
  TransitionRoot,
} from "@headlessui/vue";
import {
  CheckCircleIcon,
  ChevronRightIcon,
  EnvelopeIcon,
  PhoneIcon,
  CurrencyDollarIcon,
} from "@heroicons/vue/20/solid";
const preloader = useState("preloader");
definePageMeta({
  layout: "dashboard",
});

const Api = useApi();
const { shop } = useShop();

const route = useRoute();
const router = useRouter();
const page = computed(() => parseInt((route.query.page as string) ?? "1"));

const filter = ref("");
const perPage = ref(10);

watch([filter, perPage], () => {
  router.push({
    query: {
      page: undefined,
    },
  });
});

const query = computed(() => {
  return {
    filter: filter.value,
    perPage: perPage.value,
    page: page.value,
  };
});

const orders = ref([]);
const getOrders = async () => {
  const response = await Api.get("/api/ecommerce/dash/orders");
  orders.value = response.data;
};
getOrders();
const loadMore = async (url) => {
  var url = url.split("/api/ecommerce/dash/orders");
  url = url[url.length - 1];
  const response = await Api.get("/api/ecommerce/dash/orders" + url);
  orders.value.results = orders.value.results.concat(response.data.results);
  orders.value.next = response.data.next;
};
const search = ref("");
const searchOrder = async () => {
  const response = await Api.get(
    "/api/ecommerce/dash/orders?search=" + search.value
  );
  orders.value = response.data;
};
const debouncedSearchOrder = debounce(searchOrder, 1000);

async function setManage(order) {
  const response = await Api.get("/api/ecommerce/dash/orders?oid=" + order.id);
  manage.value = response.data;
}

const manage = ref("");
const addStatus = ref(false);
const savedStatus = ref([]);
const newStatus = ref({
  name: "",
  note: "",
  review: false,
});

const submitNewStatus = () => {
  console.log(newStatus.value.name);
  if (!newStatus.value.name) {
    return;
  }
  newStatus.value.order_id = manage.value.id;
  Api.post("/api/ecommerce/dash/orderstatus", newStatus.value)
    .then(function (response) {
      getSavedStatus();
      setManage(manage.value);
      // set the status in orders list
      const order = orders.value.results.find(
        (order) => order.id === manage.value.id
      );
      order.status = newStatus.value.name;
      newStatus.value = {
        name: "",
        note: "",
      };
      addStatus.value = false;
    })
    .catch(function (error) {
      console.log(error);
    });
};

const getSavedStatus = async () => {
  const response = await Api.get("/api/ecommerce/dash/orderstatus");
  savedStatus.value = response.data;
};
getSavedStatus();
const setNewStatus = (e) => {
  newStatus.value = e.target.value;
  if (!newStatus.value) {
    newStatus.value = {
      name: "",
      note: "",
    };
  }
  const selected = savedStatus.value.filter(
    (status) => status.id == newStatus.value
  );
  newStatus.value = {
    name: selected[0].name,
    note: selected[0].note,
  };
};
</script>

<template>
  <div>
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
        <BaseButton class="w-full sm:w-32 hidden" shape="full"
          >Filter</BaseButton
        >
      </template>
      <BasePlaceload
        v-if="preloader"
        class="h-[50vh] w-full rounded opacity-35"
      />
      <div v-else>
        <div
          v-if="orders && orders.results && orders.results.length === 0"
          class="mt-28"
        >
          <BasePlaceholderPage title="Here you can see your orders">
            <template #image>
              <img
                class="block dark:hidden"
                src="/static/frontend/images/no-order.png"
                alt="Placeholder image"
              />
              <img
                class="hidden dark:block"
                src="/static/frontend/images/no-order.png"
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
            <template v-for="(order, index) in orders.results">
              <DemoFlexTableRow
                :key="index"
                shape="straight"
                condensed
                spaced
                v-if="order.address"
              >
                <template #start>
                  <DemoFlexTableStart
                    label="Customer"
                    :hide-label="index > 0"
                    :title="
                      order.address.first_name + ' ' + order.address.last_name
                    "
                    :subtitle="order.address.street_address"
                    :avatar="order.src"
                    :badge="orders.badge"
                    :initials="orders.initials"
                  />
                  <DemoFlexTableCell
                    label="Contact"
                    :hide-label="index > 0"
                    class="w-full sm:w-40"
                  >
                    <div
                      class="text-muted-500 dark:text-muted-400 font-sans text-xs flex flex-col text-right md:text-left mb-1 md:mb-0"
                      v-if="order.address"
                    >
                      <span class="truncate">{{ order.address.phone }}</span>
                      <span class="truncate">{{ order.address.email }}</span>
                    </div>
                  </DemoFlexTableCell>
                  <DemoFlexTableCell
                    label="Amount"
                    :hide-label="index > 0"
                    class="w-full sm:w-40"
                  >
                    <div
                      class="text-muted-500 dark:text-muted-400 font-sans text-xs text-right md:text-left mb-1 md:mb-0"
                    >
                      <p class="font-bold truncate text-indigo-600">
                        Total: {{ shop.currency }}
                        {{ order.total - order.discount }}
                      </p>
                    </div>
                  </DemoFlexTableCell>

                  <DemoFlexTableCell
                    label="Order Date"
                    :hide-label="index > 0"
                    tablet-hidden
                    class="w-full sm:w-[160px]"
                  >
                    <div class="text-xs">{{ order.created_at }}</div>
                  </DemoFlexTableCell>
                  <DemoFlexTableCell
                    label="status"
                    :hide-label="index > 0"
                    class="w-full sm:w-16"
                  >
                    <BaseTag
                      color="success"
                      shape="full"
                      flavor="pastel"
                      size="md"
                      class="capitalize font-semibold"
                    >
                      {{ order.status }}
                    </BaseTag>
                  </DemoFlexTableCell>
                  <DemoFlexTableCell label="action" :hide-label="index > 0">
                    <BaseButtonAction @click="setManage(order)" color="muted">
                      <span>Manage</span>
                    </BaseButtonAction>
                  </DemoFlexTableCell>
                </template>
              </DemoFlexTableRow>
            </template>
          </TransitionGroup>
        </div>
        <div class="flex items-center justify-center my-2">
          <BaseButton
            shape="rounded"
            class="flex w-[200px] justify-center"
            @click="loadMore(orders.next)"
            v-if="orders && orders.next"
          >
            Load More
          </BaseButton>
        </div>
      </div>
    </TairoContentWrapper>
    <CommonOver :show="manage != ''">
      <DialogPanel class="pointer-events-auto relative w-screen max-w-3xl">
        <!-- <TransitionChild
          as="template"
          enter="ease-in-out duration-500"
          enter-from="opacity-0"
          enter-to="opacity-100"
          leave="ease-in-out duration-500"
          leave-from="opacity-100"
          leave-to="opacity-0"
        >
          <div
            class="absolute top-0 md:-left-2 flex pt-1 z-[9] pr-2 sm:-ml-10 sm:pr-4"
          >
            <span
              type="button"
              class="rounded-full shadow-xl bg-slate-100 dark:bg-slate-900 hover: cursor-pointer p-1"
              @click="manage = ''"
            >
              <span class="sr-only">Close panel</span>
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="32"
                height="32"
                viewBox="0 0 24 24"
              >
                <path
                  fill="currentColor"
                  d="M20 6.91L17.09 4L12 9.09L6.91 4L4 6.91L9.09 12L4 17.09L6.91 20L12 14.91L17.09 20L20 17.09L14.91 12L20 6.91Z"
                />
              </svg>
            </span>
          </div>
        </TransitionChild> -->
        <div
          class="flex h-full flex-col text-muted-500 overflow-y-scroll-no custom-scroll bg-white dark:bg-slate-800 shadow-xl m-2 rounded-md"
          v-if="manage"
        >
          <!-- {{ orders.results[0] }} -->
          <div class="flex justify-between items-center py-3 px-3 mb-2">
            <h4 class="font-semibold leading-6">Manage Order</h4>
            <span
              type="button"
              class="rounded-md hover: cursor-pointer p-1 bg-slate-500/10"
              @click="manage = ''"
            >
              <span class="sr-only">Close panel</span>
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="22"
                height="22"
                viewBox="0 0 24 24"
              >
                <path
                  fill="currentColor"
                  d="M19 6.41L17.59 5L12 10.59L6.41 5L5 6.41L10.59 12L5 17.59L6.41 19L12 13.41L17.59 19L19 17.59L13.41 12z"
                />
              </svg>
            </span>
          </div>
          <div
            class="px-4 sm:px-6 flex flex-wrap gap-1 justify-center items-center"
          >
            <BaseTag shape="rounded" color="primary" flavor="outline"
              >SubTotal: {{ shop.currency }}{{ manage.total }}</BaseTag
            >

            <BaseTag shape="rounded" color="success" flavor="outline"
              >Discount: {{ shop.currency }}{{ manage.discount }}</BaseTag
            >

            <BaseTag shape="rounded" color="info" flavor="outline"
              >Total: {{ shop.currency
              }}{{ manage.total - manage.discount }}</BaseTag
            >

            <nuxt-link :to="'/ecommerce/invoice?oid=' + manage.id"
              ><BaseTag shape="rounded" color="success"
                >Download Invoice</BaseTag
              ></nuxt-link
            >
          </div>
          <div class="relative mt-6 flex-1 px-4 sm:px-6">
            <TairoFlexTable>
              <template #header>
                <TairoFlexTableHeading type="grow"
                  >Product</TairoFlexTableHeading
                >

                <TairoFlexTableHeading type="stable"
                  >Quantity</TairoFlexTableHeading
                >

                <TairoFlexTableHeading type="stable"
                  >Price</TairoFlexTableHeading
                >
              </template>

              <TairoFlexTableRow
                v-for="product in manage.items"
                :key="product.id"
                shape="rounded"
              >
                <TairoFlexTableCell type="grow" data-content="Product">
                  <div class="flex items-center">
                    <BaseAvatar
                      :src="Api.baseURL + product.productimage_set[0].thumbnail"
                      size="sm"
                      v-if="
                        product.productimage_set && product.productimage_set[0]
                      "
                    />
                    <div class="ms-3 leading-none">
                      <h4 class="font-sans text-sm font-medium">
                        {{ product.name }}
                      </h4>
                      <p class="text-muted-400 font-sans text-xs font-normal">
                        {{ product.role }}
                      </p>
                    </div>
                  </div>
                </TairoFlexTableCell>
                <TairoFlexTableCell type="stable" data-content="Quantity" light>
                  {{ product.quantity }}
                </TairoFlexTableCell>
                <TairoFlexTableCell type="stable" data-content="Price">
                  <span class="font-medium"
                    >{{ shop.currency }}{{ product.sale_price }}</span
                  >
                </TairoFlexTableCell>
              </TairoFlexTableRow>
            </TairoFlexTable>
            <div class="flex justify-between my-4 mx-auto">
              <h6>Order Status</h6>
              <button @click="addStatus = true" class="btn px-3 py-1">
                <BaseTag shape="rounded" color="success">+ Add Status</BaseTag>
              </button>
            </div>

            <div class="form my-10 mx-auto" v-if="addStatus">
              <div class="container mx-auto my-8 pb-4 shadow">
                <div
                  class="flex justify-between items-center rounded-t p-2 px-3"
                >
                  <p>Add Order Status</p>
                  <div class="flex gap-2 items-center">
                    <label for="select" class="block whitespace-nowrap"
                      >Saved Option:</label
                    >
                    <select
                      @change="setNewStatus"
                      id="select"
                      class="mt-1 w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                    >
                      <option value="">Unset</option>
                      <option
                        :value="status.id"
                        v-for="status in savedStatus"
                        :key="status.id"
                      >
                        {{ status.name }}
                      </option>
                    </select>
                  </div>
                </div>
                <div class="flex gap-1 p-3">
                  <div class="mb-2">
                    <label for="order-status" class="block">Order Status</label>
                    <input
                      v-model="newStatus.name"
                      placeholder="eg: Completed"
                      type="text"
                      id="order-status"
                      class="mt-1 w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                    />
                  </div>
                  <div class="mb-2 flex-1">
                    <label for="title-note" class="block">Title Note</label>
                    <input
                      v-model="newStatus.note"
                      placeholder="eg: Your order has been completed"
                      type="text"
                      id="title-note"
                      class="mt-1 w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                    />
                  </div>
                </div>
                <div class="flex gap-2 px-4 pb-2">
                  <input
                    v-model="newStatus.review"
                    type="checkbox"
                    name="notify"
                    id="notify"
                    class=""
                  />
                  <label for="notify" class="block"
                    >Allow to Write Review</label
                  >
                </div>
                <button
                  @click="submitNewStatus"
                  type="submit"
                  class="ml-3 bg-blue-500 text-white px-4 py-2 rounded-md hover:bg-blue-700"
                >
                  Submit
                </button>
                <button
                  @click="addStatus = false"
                  type="submit"
                  class="ml-3 bg-slate-100 dark:bg-slate-600 px-4 py-2 rounded-md hover:bg-slate-200"
                >
                  Cancel
                </button>
              </div>
            </div>

            <ul role="list" class="my-10 mx-auto">
              <li v-for="status in manage.statuses" :key="status.id">
                <div class="relative pb-6">
                  <span
                    class="absolute top-3 left-3 -ml-px h-full w-0.5 bg-gray-200"
                    aria-hidden="true"
                  />
                  <div class="relative flex space-x-3">
                    <div>
                      <span
                        class="h-6 w-6 rounded-full flex items-center justify-center ring-6 ring-white bg-slate-400"
                      >
                        <TairoCheckAnimated class="h-6 w-6" />
                      </span>
                    </div>
                    <BaseCard
                      shape="rounded"
                      color="success"
                      class="flex flex-wrap min-w-0 flex-1 justify-between space-y-2 p-3"
                    >
                      <div>
                        <div class="text-sm">
                          <p class="capitalize whitespace-nowrap">
                            {{ status.name }}
                          </p>
                          <p class="font-normal text-sm text-muted-500">
                            {{ status.note }}
                          </p>
                        </div>
                      </div>
                      <div class="whitespace-nowrap text-right text-sm">
                        <i class="text-xs">{{ status.date }}</i>
                      </div>
                    </BaseCard>
                  </div>
                </div>
              </li>
              <li>
                <div class="relative pb-6">
                  <div class="relative flex space-x-3">
                    <div>
                      <span
                        class="h-6 w-6 rounded-full flex items-center justify-center ring-6 ring-white bg-slate-400"
                      >
                        <TairoCheckAnimated class="h-6 w-6" />
                      </span>
                    </div>
                    <div
                      class="flex min-w-0 flex-1 justify-between space-x-4 pt-1.5"
                    >
                      <div>
                        <p class="text-sm">
                          Order Placed <a class="font-medium"></a>
                        </p>
                      </div>
                      <div class="whitespace-nowrap text-right text-sm">
                        <span>{{ manage.created_at }}</span>
                      </div>
                    </div>
                  </div>
                </div>
              </li>
            </ul>
          </div>
        </div>
      </DialogPanel>
    </CommonOver>
  </div>
</template>
