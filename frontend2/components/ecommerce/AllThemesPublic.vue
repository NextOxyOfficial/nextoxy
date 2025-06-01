<template>
  <div class="w-full pb-20">
    <TairoContentWrapper>
      <template #left>
        <div class="flex gap-[2px] items-center">
          <BaseInput
            v-model="search"
            icon="lucide:search"
            shape="rounded"
            type="search"
            placeholder="Find theme..."
            :classes="{
              wrapper: 'w-full sm:w-auto',
            }"
            @keypress.enter="getAllThemes"
          />
          <BaseButton @click="getAllThemes" color="primary">Search</BaseButton>
        </div>
      </template>
      <template #right>
        <BaseSelect
          v-model="filter"
          @change="getAllThemes"
          shape="rounded"
          label="Select a subscription"
          icon="ri:verified-badge-line"
          label-float
        >
          <option value="all">All Packages</option>
          <option :value="pack.id" v-for="pack in packages" :key="pack.id">
            {{ pack.name }}
          </option>
        </BaseSelect>
      </template>
      <div>
        <div v-if="!pending && allThemes && allThemes.results.length === 0">
          <BasePlaceholderPage
            title="No matching results"
            subtitle="Looks like we couldn't find any matching results for your search terms. Try other search terms."
          >
            <template #image>
              <img
                class="block dark:hidden"
                src="/static/img/illustrations/placeholders/flat/placeholder-search-7.svg"
                alt="Placeholder image"
              />
              <img
                class="hidden dark:block"
                src="/static/img/illustrations/placeholders/flat/placeholder-search-7-dark.svg"
                alt="Placeholder image"
              />
            </template>
          </BasePlaceholderPage>
        </div>
        <div v-else>
          <div
            class="ltablet:grid-cols-3 grid w-full gap-4 sm:grid-cols-2 lg:grid-cols-3"
          >
            <TransitionGroup
              enter-active-class="transform-gpu"
              enter-from-class="opacity-0 -translate-x-full"
              enter-to-class="opacity-100 translate-x-0"
              leave-active-class="absolute transform-gpu"
              leave-from-class="opacity-100 translate-x-0"
              leave-to-class="opacity-0 -translate-x-full"
            >
              <BaseCard
                v-for="item in allThemes.results"
                :key="item.id"
                shape="curved"
                class="p-4 shadow-lg"
              >
                <div class="mb-3 flex items-center gap-3">
                  <div class="leading-none">
                    <h4
                      class="text-muted-800 dark:text-muted-100 font-sans text-sm font-medium capitalize"
                    >
                      {{ item.name }}
                    </h4>
                    <div class="text-muted-400 font-sans text-xs">
                      <Icon
                        name="ic:sharp-stars"
                        class="block h-4 w-4 text-yellow-500"
                        v-if="item.rating > 0"
                      />
                      <Icon
                        name="ic:sharp-stars"
                        class="block h-4 w-4 text-yellow-500"
                        v-if="item.rating > 1"
                      />
                      <Icon
                        name="ic:sharp-stars"
                        class="block h-4 w-4 text-yellow-500"
                        v-if="item.rating > 2"
                      />
                      <Icon
                        name="ic:sharp-stars"
                        class="block h-4 w-4 text-yellow-500"
                        v-if="item.rating > 3"
                      />
                      <Icon
                        name="ic:sharp-stars"
                        class="block h-4 w-4 text-yellow-500"
                        v-if="item.rating > 4"
                      />
                      <Icon
                        name="ic:sharp-stars"
                        class="block h-4 w-4 text-yellow-500"
                        v-if="item.rating > 5"
                      />
                      <Icon
                        name="ic:sharp-stars"
                        class="block h-4 w-4 text-slate-500/60"
                        v-if="item.rating < 5"
                      />
                      <Icon
                        name="ic:sharp-stars"
                        class="block h-4 w-4 text-slate-500/60"
                        v-if="item.rating < 4"
                      />
                      <Icon
                        name="ic:sharp-stars"
                        class="block h-4 w-4 text-slate-500/60"
                        v-if="item.rating < 3"
                      />
                      <Icon
                        name="ic:sharp-stars"
                        class="block h-4 w-4 text-slate-500/60"
                        v-if="item.rating < 2"
                      />
                      <Icon
                        name="ic:sharp-stars"
                        class="block h-4 w-4 text-slate-500/60"
                        v-if="item.rating < 1"
                      />
                    </div>
                  </div>
                  <div class="ms-auto">
                    <BaseDropdown
                      flavor="context"
                      label="Dropdown"
                      orientation="end"
                      size="md"
                      class="z-20"
                      shape="curved"
                    >
                      <BaseDropdownItem
                        to="#"
                        title="Edit"
                        text="Edit this project"
                      >
                        <template #start>
                          <Icon
                            name="ph:pencil-duotone"
                            class="me-2 block h-5 w-5"
                          />
                        </template>
                      </BaseDropdownItem>
                      <BaseDropdownDivider />
                      <BaseDropdownItem
                        to="#"
                        title="Permissions"
                        text="Manage permissions"
                      >
                        <template #start>
                          <Icon
                            name="ph:lock-duotone"
                            class="me-2 block h-5 w-5"
                          />
                        </template>
                      </BaseDropdownItem>
                      <BaseDropdownItem
                        to="#"
                        title="Share"
                        text="Share this project"
                      >
                        <template #start>
                          <Icon
                            name="ph:share-duotone"
                            class="me-2 block h-5 w-5"
                          />
                        </template>
                      </BaseDropdownItem>
                      <BaseDropdownDivider />
                      <BaseDropdownItem
                        to="#"
                        title="Delete"
                        text="Delete this project"
                      >
                        <template #start>
                          <Icon
                            name="ph:trash-duotone"
                            class="me-2 block h-5 w-5"
                          />
                        </template>
                      </BaseDropdownItem>
                    </BaseDropdown>
                  </div>
                </div>
                <div>
                  <img
                    :src="Api.baseURL + item.image"
                    :alt="item.name"
                    class="rounded-lg w-full h-[275px] object-cover"
                  />
                </div>
                <hr class="mt-6" />
                <div class="my-4 flex items-center justify-between">
                  <div>
                    <div
                      class="flex items-center gap-1"
                      :class="item.package.color"
                      v-if="item.package"
                    >
                      <Icon :name="item.package.icon" class="h-4 w-4" />
                      <p class="font-sans text-sm">
                        Subscription: {{ item.package.name }}
                      </p>
                    </div>
                    <div class="text-green-500 flex items-center gap-1" v-else>
                      <Icon name="teenyicons:gift-outline" class="h-4 w-4" />
                      <p class="font-sans text-sm">Subscription: FREE</p>
                    </div>
                  </div>
                  <div>
                    <!-- <BaseAvatarGroup
                      size="xs"
                      :limit="2"
                      :avatars="item.team"
                    /> -->
                  </div>
                </div>
                <div
                  class="flex items-center gap-2 justify-between w-full"
                  v-if="shop"
                >
                  <nuxt-link
                    :to="'https://' + item.path + '.nextoxy.com'"
                    target="_blank"
                    class="w-full max-w-[40%]"
                  >
                    <BaseButton
                      shape="rounded"
                      color="success"
                      flavor="pastel"
                      class="w-full"
                    >
                      <span>Preview</span>
                      <Icon name="lucide:arrow-right" class="me-1 h-4 w-4" />
                    </BaseButton>
                  </nuxt-link>
                  <BaseButton
                    shape="rounded"
                    color="success"
                    disabled
                    class="w-full max-w-[40%]"
                    v-if="
                      !shop.package ||
                      !item.package ||
                      shop.package.id == item.package.id
                    "
                  >
                    <Icon name="ph:checks-duotone" class="me-1 h-4 w-4" />
                    Owned
                  </BaseButton>
                  <nuxt-link to="/ecommerce/subscription" class="w-14" v-else>
                    <BaseButton
                      data-nui-tooltip-position="down"
                      :data-nui-tooltip="'Upgrade Plan'"
                      color="success"
                      shape="rounded"
                      shadow="flat"
                      class="!rounded-full !h-14 !w-14 shadow-xl !p-1 relative"
                    >
                      <Icon
                        name="ph:crown-duotone"
                        class="h-6 w-6 text-yellow-400 absolute top-1"
                      />
                      <span class="font-bold pt-2">Get</span>
                      <Icon name="mdi:plus-thick" class="h-6 w-6 !m-0 pt-2" />
                    </BaseButton>
                  </nuxt-link>
                </div>
                <div
                  class="flex items-center gap-2 justify-between w-full"
                  v-else
                >
                  <nuxt-link
                    :to="'https://' + item.path + '.nextoxy.com'"
                    target="_blank"
                    class="w-full max-w-[40%]"
                  >
                    <BaseButton
                      shape="rounded"
                      color="success"
                      flavor="pastel"
                      class="w-full"
                    >
                      <span>Preview</span>
                      <Icon name="lucide:arrow-right" class="me-1 h-4 w-4" />
                    </BaseButton>
                  </nuxt-link>
                  <nuxt-link to="/auth/login" class="w-14">
                    <BaseButton
                      color="success"
                      shape="rounded"
                      shadow="flat"
                      class="!rounded-full !h-14 !w-14 shadow-xl !p-1"
                    >
                      <span>Get</span>
                      <Icon name="mdi:plus-thick" class="h-4 w-4 !m-0" />
                    </BaseButton>
                  </nuxt-link>
                </div>
              </BaseCard>
            </TransitionGroup>
          </div>
          <div class="mt-6">
            <BasePagination
              :total-items="data?.total ?? 0"
              :item-per-page="perPage"
              :current-page="page"
              shape="curved"
            />
          </div>
        </div>
      </div>
    </TairoContentWrapper>
  </div>
</template>

<script setup>
const Api = useApi();
const allThemes = ref("");
const filter = ref("all");
const search = ref("");
async function getAllThemes() {
  var url = "/api/ecommerce/home/themes?package=" + filter.value;
  if (search.value) {
    url += "&search=" + search.value;
  }
  const res = await Api.get(url);
  allThemes.value = res.data;
}
getAllThemes();

const packages = ref("");
async function getPackages() {
  const { data } = await Api.get("/api/ecommerce/home/packages");
  packages.value = data;
}
getPackages();
</script>

<style scoped></style>
