<script setup lang="ts">
const Api = useApi()
const route = useRoute()
const router = useRouter()
const page = computed(() => parseInt((route.query.page as string) ?? '1'))

const filter = ref('')
const perPage = ref(25)

const search = ref('')
const data = ref('')
async function getData() {
  var url = '/api/ecommerce/home/plugins'
    if(search.value){
      url += '?search=' + search.value;
    }
    const res = await Api.get(url)
    data.value = res.data
}
getData()
</script>

<template>
  <div v-if="data">
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
            @keypress.enter="getData"
          />
          <BaseButton @click="getData" color="primary">Search</BaseButton>
        </div>
      </template>
      <template #right>
        <BaseButton to="/account" class="w-full sm:w-32" shape="curved">Manage</BaseButton>
        <BaseButton data-nui-tooltip="Contact us to publish your plugin." data-nui-tooltip-position="down" to="/support/new" color="primary" class="w-full sm:w-32" shape="curved">
          <Icon name="lucide:plus" class="h-4 w-4" />
          <span>Upload</span>
        </BaseButton>
      </template>
      <div>
        <div v-if="data?.results.length === 0">
          <BasePlaceholderPage
            title="No matching results"
            subtitle="Looks like we couldn't find any matching results for your search terms. Try other search terms."
          >
            <template #image>
              <img
                class="block dark:hidden"
                src="/static/img/illustrations/placeholders/flat/placeholder-search-5.svg"
                alt="Placeholder image"
              />
              <img
                class="hidden dark:block"
                src="/static/img/illustrations/placeholders/flat/placeholder-search-5-dark.svg"
                alt="Placeholder image"
              />
            </template>
          </BasePlaceholderPage>
        </div>
        <div
          v-else
          class="ltablet:grid-cols-3 grid gap-4 sm:grid-cols-2 lg:grid-cols-3 pb-40"
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
              v-for="(item, index) in data?.results"
              :key="index"
              shape="curved"
              class="p-3"
            >
              <div class="flex w-full items-center gap-2">
                <img :src="Api.baseURL + item.image" :alt="item.name" class="max-w-[46px]" />
                <div>
                  <BaseHeading tag="h3" size="sm" weight="medium">
                    {{ item.name }}
                  </BaseHeading>
                  <BaseParagraph size="xs" class="text-muted-400">
                    <span>Ecommerce</span>
                    <span class="px-1 text-base leading-tight">&middot;</span>
                    <span>v1.00</span>
                  </BaseParagraph>
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
                      to="/account"
                      title="Details"
                      text="More about this plugin"
                    >
                      <template #start>
                        <Icon
                          name="ic:outline-remove-red-eye"
                          class="me-2 block h-5 w-5"
                        />
                      </template>
                    </BaseDropdownItem>
                    <BaseDropdownItem
                      to="/account"
                      title="Install"
                      text="Use this plugin"
                    >
                      <template #start>
                        <Icon
                          name="solar:download-minimalistic-linear"
                          class="me-2 block h-5 w-5"
                        />
                      </template>
                    </BaseDropdownItem>
                    
                  </BaseDropdown>
                </div>
              </div>
            </BaseCard>
          </TransitionGroup>
        </div>
        <div v-if="data?.results.length !== 0" class="mt-4">
          
        </div>
      </div>
    </TairoContentWrapper>
  </div>
</template>
