<script setup lang="ts">
definePageMeta({
  layout: "dashboard",
});
const preloader = useState("preloader");

const Api = useApi();
const { shop, getShop } = useShop();

const packages = ref("");
async function getPackages() {
  const { data } = await Api.get("/api/ecommerce/dash/packages");
  packages.value = data;
}
getPackages();

function yearlySave(price, yearly) {
  return parseFloat(yearly - price * 12).toFixed(2);
}

const customRadio = ref("1");
const selectedPlan = computed(() => {
  if (!packages.value) {
    return false;
  }
  return packages.value.find((plan) => plan.level == customRadio.value);
});
const method = ref("stripe");
const period = ref("yearly");

async function makePayment() {
  const data = {
    planId: selectedPlan.value.id,
    method: method.value,
    period: period.value,
  };
  console.log(data);
  const res = await Api.post("/api/ecommerce/dash/shopthemes", data);
  if (res.data) {
    console.log(res.data);
    navigateTo("/account/checkout/" + res.data);
  }
}
</script>

<template>
  <section>
    <div class="w-full max-w-4xl mx-auto" v-if="preloader">
      <BaseCard shape="rounded" class="px-4 md:px-6 py-12 mb-2 flex-1 w-full">
        <div class="flex items-center">
          <BasePlaceload class="h-10 w-10 rounded-full" />

          <div class="ms-3 grow space-y-2">
            <BasePlaceload class="h-3 w-full rounded" />

            <BasePlaceload class="h-3 w-[85%] rounded" />
          </div>
        </div>
      </BaseCard>
      <div class="flex gap-1">
        <div class="flex gap-1 flex-wrap">
          <BaseCard
            shape="rounded"
            class="px-4 md:px-6 py-12 mb-2 flex-1 max-w-[350px] min-w-[150px]"
            v-for="i in 4"
            :key="i"
          >
            <div class="flex items-center">
              <BasePlaceload class="h-10 w-10 rounded-full" />

              <div class="ms-3 grow space-y-2">
                <BasePlaceload class="h-3 w-full rounded" />

                <BasePlaceload class="h-3 w-[85%] rounded" />
              </div>
            </div>
          </BaseCard>
        </div>
        <BaseCard shape="rounded" class="px-6 md:px-10 mb-2 py-12">
          <div class="flex justify-between">
            <BaseCard
              shape="rounded"
              class="p-3 md:p-4 mb-2 max-w-[150px]"
              v-for="i in 2"
              :key="i"
            >
              <div class="flex items-center">
                <div class="ms-3 grow space-y-2">
                  <BasePlaceload class="h-3 w-[85%] rounded" />
                </div>
              </div>
            </BaseCard>
          </div>
          <div class="flex items-center mb-2">
            <BasePlaceload class="h-10 w-10 rounded-full" />

            <div class="ms-3 grow space-y-2">
              <BasePlaceload class="h-3 w-full rounded" />

              <BasePlaceload class="h-3 w-[85%] rounded" />
            </div>
          </div>
          <div class="flex items-center">
            <BasePlaceload class="h-10 w-10 rounded-full" />

            <div class="ms-3 grow space-y-2">
              <BasePlaceload class="h-3 w-full rounded" />

              <BasePlaceload class="h-3 w-[85%] rounded" />
            </div>
          </div>
        </BaseCard>
      </div>
    </div>
    <span v-else>
      <BaseCard
        v-if="shop && shop.package"
        shape="rounded"
        color="info"
        class="p-6 mx-auto w-full max-w-4xl mb-3"
      >
        <BaseHeading
          as="h4"
          size="lg"
          weight="semibold"
          lead="tight"
          class="text-muted-800 mb-2 dark:text-white"
        >
          Your Current Plan
        </BaseHeading>
        <div
          class="flex gap-2 md:gap-4 items-center"
          :class="shop.package.color"
        >
          <Icon :name="shop.package.icon" class="h-12 w-12 text-current" />
          <section>
            <BaseParagraph
              size="lg"
              lead="tight"
              class="flex items-center gap-1"
            >
              <span>{{ shop.package?.name }}</span>
            </BaseParagraph>
            <BaseParagraph
              size="sm"
              lead="tight"
              class="text-muted-600 mt-2"
              v-if="shop.package_validity"
            >
              Your subscription is expiring in
              <b>{{ shop.package_validity_days }} days</b>, as of
              <b>{{ shop.package_validity }}</b>
            </BaseParagraph>
          </section>
        </div>
      </BaseCard>
      <BaseCard
        v-else
        shape="rounded"
        color="info"
        class="p-6 mx-auto w-full max-w-4xl mb-3"
      >
        <BaseHeading
          as="h4"
          size="sm"
          weight="semibold"
          lead="tight"
          class="text-muted-800 mb-2 dark:text-white"
        >
          Current Plan
        </BaseHeading>

        <BaseParagraph size="sm" lead="tight" class="text-muted-400">
          Your Do Not Have Any Plan.
        </BaseParagraph>
      </BaseCard>
      <div
        action=""
        method="POST"
        @submit.prevent
        class="mx-auto w-full max-w-4xl pb-1"
      >
        <!-- plans -->
        <div
          class="dark:border-muted-800 mb-10 grid gap-4 md:grid-cols-2 xl:gap-8"
        >
          <div class="grid grid-cols-2 gap-2 xl:gap-3">
            <BaseRadioHeadless
              v-model="customRadio"
              name="radio_custom"
              :value="pack.level"
              v-for="pack in packages"
              :key="pack.id"
            >
              <BaseCard
                shape="rounded"
                class="text-muted-400/50 peer-checked:!border-success-500 peer-checked:text-success-500 group relative p-6 text-center peer-checked:[&_.child]:!opacity-100"
              >
                <div
                  class="child border-muted-200 dark:border-muted-700 dark:bg-muted-800 absolute left-1 top-1 flex h-7 px-2 text-xs items-center justify-center rounded-full border bg-white"
                  v-if="pack.name == shop.package?.name"
                >
                  Current Plan
                </div>
                <div
                  class="child border-muted-200 dark:border-muted-700 dark:bg-muted-800 absolute end-3 top-3 flex h-7 w-7 items-center justify-center rounded-full border bg-white opacity-0"
                >
                  <Icon
                    :class="pack.color"
                    name="lucide:check"
                    class="h-3 w-3"
                  />
                </div>
                <Icon :name="pack.icon" :class="pack.color" class="h-10 w-10" />
                <BaseHeading
                  as="h4"
                  size="sm"
                  weight="medium"
                  class="text-muted-800 dark:text-white"
                >
                  {{ pack.name }}
                </BaseHeading>
                <BaseText
                  size="sm"
                  lead="tight"
                  class="my-1"
                  :class="pack.color"
                  >{{ pack.title }}</BaseText
                >
                <BaseText size="xs" lead="tight" class="text-muted-400"
                  >USD ${{ pack.price }}/month</BaseText
                >
              </BaseCard>
            </BaseRadioHeadless>
          </div>
          <div v-if="selectedPlan">
            <BaseCard shape="rounded" class="p-6">
              <BaseSelect v-model="period" shape="rounded" label="Select Plan">
                <option value="monthly">Monthly</option>
                <option value="yearly">Yearly</option>
              </BaseSelect>
              <div class="flex gap-6 my-3">
                <Icon
                  :name="selectedPlan?.icon"
                  :class="selectedPlan?.color"
                  class="h-12 w-12"
                />
                <div>
                  <template v-if="period == 'monthly'">
                    <BaseText size="md" lead="tight" weight="semibold">
                      ${{ selectedPlan?.price }}
                      <span class="text-muted-400 font-normal">/1 month</span>
                    </BaseText>
                    <BaseText
                      size="xs"
                      lead="tight"
                      class="mb-2"
                      :class="selectedPlan.color"
                    >
                      <span
                        >Subscribe for 1 year to save: USD ${{
                          parseFloat(
                            selectedPlan.price * 12 - selectedPlan.yearly
                          ).toFixed(2)
                        }}</span
                      >
                    </BaseText>
                  </template>
                  <template v-else>
                    <BaseText size="md" lead="tight" weight="semibold">
                      ${{ selectedPlan?.yearly }}
                      <span class="text-muted-400 font-normal">/12 months</span>
                    </BaseText>
                    <BaseText
                      size="xs"
                      lead="tight"
                      class="mb-2"
                      :class="selectedPlan.color"
                    >
                      <span
                        >You saved USD ${{
                          yearlySave(selectedPlan.price, selectedPlan.yearly)
                        }}</span
                      >
                    </BaseText>
                  </template>
                </div>
              </div>
              <div class="my-4">
                <BaseParagraph
                  size="sm"
                  lead="tight"
                  class="text-muted-500 dark:text-muted-400"
                >
                  {{ selectedPlan?.description }}
                </BaseParagraph>
              </div>
              <div class="grid grid-cols-2 gap-6 font-sans text-xs">
                <div>
                  <ul>
                    <li
                      class="flex items-center gap-2"
                      :class="selectedPlan?.color"
                    >
                      <Icon name="lucide:check" class="h-3 w-3 text-current" />
                      <span class="text-muted-400">{{
                        selectedPlan.feature1
                      }}</span>
                    </li>
                    <li
                      class="flex items-center gap-2"
                      :class="selectedPlan?.color"
                    >
                      <Icon name="lucide:check" class="h-3 w-3 text-current" />
                      <span class="text-muted-400">{{
                        selectedPlan.feature2
                      }}</span>
                    </li>
                    <li
                      class="flex items-center gap-2"
                      :class="selectedPlan?.color"
                    >
                      <Icon name="lucide:check" class="h-3 w-3 text-current" />
                      <span class="text-muted-400">{{
                        selectedPlan.feature3
                      }}</span>
                    </li>
                  </ul>
                </div>
                <div>
                  <ul>
                    <li
                      class="flex items-center gap-2"
                      :class="selectedPlan.color"
                    >
                      <Icon name="lucide:check" class="h-3 w-3 text-current" />
                      <span class="text-muted-400">{{
                        selectedPlan.feature4
                      }}</span>
                    </li>
                    <li
                      class="flex items-center gap-2"
                      :class="selectedPlan.color"
                    >
                      <Icon name="lucide:check" class="h-3 w-3 text-current" />
                      <span class="text-muted-400">{{
                        selectedPlan.feature5
                      }}</span>
                    </li>
                    <li
                      class="flex items-center gap-2"
                      :class="selectedPlan.color"
                    >
                      <Icon name="lucide:check" class="h-3 w-3 text-current" />
                      <span class="text-muted-400">{{
                        selectedPlan.feature6
                      }}</span>
                    </li>
                  </ul>
                </div>
              </div>
            </BaseCard>
          </div>
        </div>
      </div>
      <div
        shape="curved"
        class="border-t pt-6 max-w-4xl mx-auto flex flex-col items-end justify-end my-2 gap-2 text-sm"
        v-if="selectedPlan && selectedPlan.name != shop.package?.name"
      >
        <BaseButton v-if="selectedPlan" @click="makePayment" color="success"
          >Continue To Checkout</BaseButton
        >
        <BaseButton class="opacity-50" v-else color="success"
          >Continue To Checkout</BaseButton
        >
      </div>
      <p
        class="text-center w-full"
        v-if="selectedPlan?.name == shop?.package?.name"
      >
        This is your current plan.
      </p>
    </span>
  </section>
</template>
