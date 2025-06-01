<script setup>
import {
  Dialog,
  DialogPanel,
  DialogTitle,
  TransitionChild,
  TransitionRoot,
} from "@headlessui/vue";
definePageMeta({
  layout: "dashboard",
});
const preloader = useState("preloader");
const people = [
  {
    name: "Lindsay Walton",
    title: "Front-end Developer",
    email: "lindsay.walton@example.com",
    role: "Everyone",
  },
];
const show = ref(false);
const Api = useApi();
const { shop } = useShop();

const coupons = ref("");
async function getCoupons() {
  const { data } = await Api.get("/api/ecommerce/dash/coupons");
  coupons.value = data;
}
getCoupons();

const newCoupon = ref({
  code: "",
  amount: "",
  type: "fixed",
  valid_till: "",
  error: "",
});
async function createCoupon() {
  if (!newCoupon.value.code) {
    newCoupon.value.error = "Please enter a coupon code";
    return;
  }
  if (!newCoupon.value.amount) {
    newCoupon.value.error = "Please enter a coupon amount";
    return;
  }
  if (!newCoupon.value.valid_till) {
    newCoupon.value.error = "Please enter a coupon valid till date";
    return;
  }
  const { data } = await Api.post(
    "/api/ecommerce/dash/coupons",
    newCoupon.value
  );
  console.log(data);
  getCoupons();
}
async function deleteCoupon(id) {
  const { data } = await Api.del("/api/ecommerce/dash/coupons?id=" + id);
  console.log(data);
  getCoupons();
}
</script>
<template>
  <div class="">
    <span>
      <div
        class="border-b border-gray-200 pb-4 flex my-3 sm:items-center justify-between"
      >
        <CommonTitleIcon
          :filename="'gift-and-coupon-min.png'"
          :title="'Coupons'"
        />
        <BaseButton @click="show = true" color="primary"
          >Create Coupon</BaseButton
        >
      </div>
      <BasePlaceload
        v-if="preloader"
        class="h-[50vh] w-full rounded opacity-35"
      />
      <BaseCard
        shape="rounded"
        class="mt-8 flex flex-col overflow-hidden p-1"
        v-else
      >
        <div class="-my-2 -mx-4 overflow-x-auto sm:-mx-6 lg:-mx-8">
          <div
            class="inline-block min-w-full py-2 align-middle md:px-6 lg:px-8"
          >
            <div class="overflow-hidden ring-opacity-5 md:rounded">
              <table class="min-w-full divide-y divide-gray-300">
                <thead class="">
                  <tr>
                    <th
                      scope="col"
                      class="py-3.5 pl-4 pr-3 text-left text-sm font-semibold sm:pl-6"
                    >
                      Code
                    </th>
                    <th
                      scope="col"
                      class="px-3 py-3.5 text-left text-sm font-semibold"
                    >
                      Value
                    </th>
                    <th
                      scope="col"
                      class="px-3 py-3.5 text-left text-sm font-semibold"
                    >
                      Expires
                    </th>
                    <th
                      scope="col"
                      class="px-3 py-3.5 text-left text-sm font-semibold"
                    >
                      Created
                    </th>
                    <th
                      scope="col"
                      class="px-3 py-3.5 text-left text-sm font-semibold"
                    >
                      Action
                    </th>
                  </tr>
                </thead>
                <tbody class="divide-y" v-if="coupons && shop">
                  <tr v-for="coupon in coupons.results" :key="coupon.id">
                    <td
                      class="whitespace-nowrap py-4 pl-4 pr-3 text-sm font-medium sm:pl-6"
                    >
                      {{ coupon.code }}
                    </td>
                    <td
                      class="whitespace-nowrap px-3 py-4 text-sm text-gray-500"
                    >
                      {{ coupon.amount }}
                      <span v-if="coupon.type == 'fixed'">{{
                        shop.currency
                      }}</span>
                      <span v-else>%</span>
                    </td>
                    <td
                      class="whitespace-nowrap px-3 py-4 text-sm text-gray-500"
                    >
                      {{ coupon.valid_till }}
                    </td>
                    <td
                      class="whitespace-nowrap px-3 py-4 text-sm text-gray-500"
                    >
                      {{ coupon.created_at }}
                    </td>
                    <td
                      class="relative whitespace-nowrap py-4 pl-3 pr-4 text-sm font-medium sm:pr-6"
                    >
                      <a
                        @click="deleteCoupon(coupon.id)"
                        class="text-indigo-600 hover:text-indigo-900 cursor-pointer"
                        >DELETE</a
                      >
                    </td>
                  </tr>
                </tbody>
              </table>
              <p
                v-if="coupons && coupons.results.length == 0"
                class="text-center text-gray-500 py-4"
              >
                No coupons found
              </p>
            </div>
          </div>
        </div>
      </BaseCard>
    </span>
    <CommonOver :show="show">
      <DialogPanel class="pointer-events-auto relative w-screen max-w-md">
        <div
          class="flex h-full flex-col text-muted-500 overflow-y-scroll-no custom-scroll bg-white dark:bg-slate-800 shadow-xl m-2 rounded-md"
        >
          <div class="flex justify-between items-center py-3 px-3">
            <h4 class="font-semibold leading-6">Create New Coupon</h4>
            <span
              type="button"
              class="rounded-md hover: cursor-pointer p-1 bg-slate-500/10"
              @click="show = false"
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
          <div class="bg-slate-400/10 p-2 m-2 sm:p-4 rounded-md">
            <label for="coupon-code" class="block text-sm font-medium"
              >Coupon Code</label
            >
            <div class="mt-1">
              <input
                v-model="newCoupon.code"
                id="coupon-code"
                name="coupon-code"
                type="text"
                autocomplete="text"
                required=""
                class="block w-full appearance-none rounded-md border border-gray-300 px-3 py-2 placeholder-gray-400 shadow-sm focus:border-indigo-500 focus:outline-none focus:ring-indigo-500 sm:text-sm"
              />
            </div>
          </div>
          <div class="relative flex-1 p-4 sm:p-6 !pt-2">
            <div class="space-y-3">
              <div class="space-y-1">
                <label for="password" class="block text-sm font-medium mb-2"
                  >Coupon Type</label
                >
                <div class="mt-1 flex gap-2 items-center justify-center">
                  <div
                    class="flex-1 border flex cursor-pointer rounded-md text-sm"
                  >
                    <input
                      v-model="newCoupon.type"
                      type="radio"
                      id="flat"
                      name="discount"
                      value="fixed"
                      checked
                      class="ml-3 text-indigo-600 cursor-pointer border-gray-300 focus:ring-indigo-500"
                    />
                    <label
                      for="flat"
                      class="outline-none cursor-pointer px-2 py-2 flex-1"
                      >Fixed Rate</label
                    >
                  </div>
                  <div
                    class="flex-1 border flex cursor-pointer rounded-md text-sm"
                  >
                    <input
                      v-model="newCoupon.type"
                      type="radio"
                      id="percentage"
                      name="discount"
                      value="percent"
                      class="ml-3 text-indigo-600 cursor-pointer border-gray-300 focus:ring-indigo-500"
                    />
                    <label
                      for="percentage"
                      class="cursor-pointer px-2 py-2 flex-1"
                      >Percentage</label
                    >
                  </div>
                </div>
              </div>
              <div class="flex gap-1">
                <div class="space-y-1" v-if="shop">
                  <label
                    for="password"
                    class="block text-sm font-medium"
                    v-if="newCoupon.type == 'fixed'"
                    >Value</label
                  >
                  <label for="password" class="block text-sm font-medium" v-else
                    >Coupon Percentage Value</label
                  >
                  <div class="mt-1">
                    <input
                      v-model="newCoupon.amount"
                      id="password"
                      name="password"
                      :placeholder="shop.currency"
                      type="number"
                      step="2"
                      autocomplete="current-password"
                      required=""
                      class="block w-full appearance-none rounded-md border border-gray-300 px-3 py-[9px] placeholder-gray-400 shadow-sm focus:border-indigo-500 focus:outline-none focus:ring-indigo-500 sm:text-sm"
                    />
                  </div>
                </div>
                <div class="space-y-1">
                  <label for="password" class="block text-sm font-medium"
                    >Expiration Date</label
                  >
                  <div class="mt-1">
                    <input
                      v-model="newCoupon.valid_till"
                      id="password"
                      name="password"
                      type="date"
                      step="2"
                      autocomplete="current-password"
                      required=""
                      class="block w-full appearance-none rounded-md border border-gray-300 px-3 py-2 placeholder-gray-400 shadow-sm focus:border-indigo-500 focus:outline-none focus:ring-indigo-500 sm:text-sm"
                    />
                  </div>
                </div>
              </div>

              <div>
                <p v-if="newCoupon.error" class="text-red-500 my-2">
                  {{ newCoupon.error }}
                </p>
                <BaseButton
                  color="primary"
                  @click="createCoupon"
                  type="submit"
                  class="flex w-full justify-center rounded-md border border-transparent bg-indigo-600 py-2 px-4 mt-6 text-sm font-medium shadow-sm hover:bg-indigo-700 focus:outline-none"
                  >Create Coupon</BaseButton
                >
              </div>
            </div>
          </div>
        </div>
      </DialogPanel>
    </CommonOver>
  </div>
</template>

<style scoped>
.finder + div {
  display: none;
}
.finder + div > * {
  cursor: pointer;
}
.finder:focus + div {
  display: block;
}
/* width */
.custom-scroll::-webkit-scrollbar {
  width: 6px;
}

/* Track */
.custom-scroll::-webkit-scrollbar-track {
  border-radius: 0px 6px 6px 0px;
}

/* Handle */
.custom-scroll::-webkit-scrollbar-thumb {
  background: rgb(114, 114, 114);
  border-radius: 0px 6px 6px 0px;
}

/* Handle on hover */
.custom-scroll::-webkit-scrollbar-thumb:hover {
  background: #888888;
}
</style>
