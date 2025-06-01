<script setup lang="ts">
import { debounce } from "lodash";
definePageMeta({
  layout: "dashboard",
});
const preloader = useState("preloader");

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

const Api = useApi();
const leads = ref([]);
const getLeads = async () => {
  const { data } = await Api.get("/api/ecommerce/dash/leads");
  leads.value = data;
};
getLeads();
const loadMore = async (url) => {
  var url = url.split("/api/ecommerce/dash/leads");
  url = url[url.length - 1];
  const response = await Api.get("/api/ecommerce/dash/leads" + url);
  leads.value.results = leads.value.results.concat(response.data.results);
  leads.value.next = response.data.next;
};
const search = ref("");
const searchOrder = async () => {
  const response = await Api.get(
    "/api/ecommerce/dash/leads?search=" + search.value
  );
  leads.value = response.data;
  filter.value = true;
};
const debouncedSearchOrder = debounce(searchOrder, 1000);

function statusColor(itemStatus: string) {
  switch (itemStatus) {
    case "online":
      return "success";
    case "working":
      return "info";
    case "suspended":
      return "warning";
    default:
      break;
  }
}

const selected = ref("");
const isModalOpen = ref(false);
function closeModal() {
  isModalOpen.value = false;
}

function openModal(item) {
  isModalOpen.value = true;
  selected.value = JSON.parse(JSON.stringify(item));
}

async function DeleteLead() {
  selected.value.message = "";
  const { data } = await Api.del(
    "/api/ecommerce/dash/leads?id=" + selected.value.id
  );
  selected.value.class = data.class;
  selected.value.message = data.message;
  closeModal();
  getLeads();
}
async function updateItemStatus(id, status) {
  console.log(id, status);
  const { data } = await Api.get(
    "/api/ecommerce/dash/leads?id=" + id + "&status=" + status
  );
}
</script>

<template>
  <div>
    <!-- Modal component -->
    <TairoModal :open="isModalOpen" size="lg" @close="closeModal">
      <template #header>
        <!-- Header -->
        <div
          class="flex w-full items-center justify-between p-4 md:p-6 mb-0 !pb-0"
        >
          <div class="">
            <h3
              class="font-heading text-muted-900 text-lg font-medium leading-6 dark:text-white"
            >
              Are you sure?
            </h3>
            <h3
              class="font-heading text-muted-900 text-lg font-medium leading-6 dark:text-white text-center"
            >
              Leads will be deleted forever.
            </h3>
          </div>

          <BaseButtonClose @click="closeModal" />
        </div>
      </template>

      <!-- Body -->

      <template #footer>
        <!-- Footer -->
        <div class="p-4 md:p-6 w-full">
          <div class="flex w-full gap-x-2 justify-between items-center">
            <BaseButton color="danger" flavor="pastel" @click="DeleteLead"
              >Delete</BaseButton
            >
            <span class="flex gap-2 items-center hidden">
              <BaseButton @click="closeModal">Close</BaseButton>
              <BaseButton color="primary" flavor="solid">Update</BaseButton>
            </span>
          </div>
        </div>
      </template>
    </TairoModal>

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
          >Manage</BaseButton
        >
        <BaseButton color="primary" shape="full" class="w-full sm:w-32 hidden">
          <Icon name="lucide:plus" class="h-4 w-4" />
          <span>Add User</span>
        </BaseButton>
      </template>
      <BasePlaceload
        v-if="preloader"
        class="h-[50vh] w-full rounded opacity-35"
      />
      <div v-else>
        <div
          v-if="leads && leads.results && leads.results.length === 0"
          class="mt-28"
        >
          <BasePlaceholderPage
            title="The list of your leads will be appeared here"
          >
            <template #image>
              <img
                class="block dark:hidden"
                src="/static/frontend/images/no-customer.png"
                alt="Placeholder image"
              />
              <img
                class="hidden dark:block"
                src="/static/frontend/images/no-customer.png"
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
              v-for="(item, index) in leads.results"
              :key="index"
              shape="straight"
              condensed
              spaced
            >
              <template #start>
                <DemoFlexTableStart
                  label="user"
                  :hide-label="index > 0"
                  :title="'#' + item.id"
                  :subtitle="item.created_at"
                />
              </template>
              <template #end>
                <DemoFlexTableCell
                  label="Name"
                  :hide-label="index > 0"
                  class="w-full sm:w-40"
                >
                  <p
                    class="text-muted-500 dark:text-muted-400 font-sans text-sm"
                  >
                    {{ item.name }}
                  </p>
                </DemoFlexTableCell>

                <DemoFlexTableCell
                  label="Email"
                  :hide-label="index > 0"
                  class="w-full sm:w-40"
                >
                  <span
                    class="text-muted-500 dark:text-muted-400 font-sans text-sm"
                  >
                    {{ item.email }}
                  </span>
                </DemoFlexTableCell>
                <DemoFlexTableCell
                  label="Phone"
                  :hide-label="index > 0"
                  class="w-full sm:w-40"
                >
                  <span
                    class="text-muted-500 dark:text-muted-400 font-sans text-sm"
                  >
                    {{ item.phone }}
                  </span>
                </DemoFlexTableCell>
                <DemoFlexTableCell
                  label="Message"
                  :hide-label="index > 0"
                  class="w-full sm:w-40"
                >
                  <p
                    class="text-muted-500 dark:text-muted-400 font-sans text-sm"
                  >
                    {{ item.message }}
                  </p>
                </DemoFlexTableCell>
                <DemoFlexTableCell
                  label="Join"
                  :hide-label="index > 0"
                  class="w-full sm:w-16 hidden"
                >
                  <BaseTag color="success" flavor="pastel" shape="full"
                    >Active</BaseTag
                  >
                </DemoFlexTableCell>

                <DemoFlexTableCell label="Status" :hide-label="index > 0">
                  <BaseSelect
                    v-model="item.status"
                    rounded="none"
                    size="sm"
                    @change="updateItemStatus(item.id, item.status)"
                  >
                    <option value="No Status">No Status</option>
                    <option value="Returning Customer">
                      Returning Customer
                    </option>
                    <option value="Customer">Customer</option>
                  </BaseSelect>
                </DemoFlexTableCell>
                <DemoFlexTableCell label="action" :hide-label="index > 0">
                  <BaseButtonAction
                    color="danger"
                    flavor="pastel"
                    @click="openModal(item)"
                  >
                    <span>Delete</span>
                  </BaseButtonAction>
                </DemoFlexTableCell>
              </template>
            </DemoFlexTableRow>
          </TransitionGroup>
        </div>
        <div class="flex items-center justify-center my-2">
          <BaseButton
            shape="rounded"
            class="flex w-[200px] justify-center"
            @click="loadMore(leads.next)"
            v-if="leads && leads.next"
          >
            Load More
          </BaseButton>
        </div>
      </div>
    </TairoContentWrapper>
  </div>
</template>
