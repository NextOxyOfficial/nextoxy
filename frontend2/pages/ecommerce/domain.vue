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

const toaster = useToaster();
const { notifs } = useAuth();
const { $swal } = useNuxtApp();
const Api = useApi();
const domains = ref([]);
const getDomains = async () => {
  const res = await Api.get("/api/ecommerce/dash/domains");
  domains.value = res.data;
};
onMounted(() => {
  getDomains();
});

const show = ref(false);
const newDomainLoading = ref(false);
const newDomainError = ref("");
const newDomain = ref("");
const addNewDomain = async () => {
  newDomainLoading.value = true;
  newDomainError.value = "";
  const res = await Api.post("/api/ecommerce/dash/domains", {
    domain: newDomain.value,
  });
  console.log(res);
  if (res.data && res.data.code == "400") {
    newDomainError.value = res.data.msg;
    newDomainLoading.value = false;
    notifs.value.push({
      type: "error",
      message: res.data.msg,
    });
    return;
  }
  notifs.value.push({
    type: "success",
    message: "Domain added successfully",
  });
  getDomains();
  show.value = false;
  newDomainLoading.value = false;
};
const deleteDomain = async (domain) => {
  $swal
    .fire({
      title: "Are you sure?",
      text: "You won't be able to revert this!",
      icon: "warning",
      showCancelButton: true,
      confirmButtonColor: "#3085d6",
      cancelButtonColor: "#d33",
      confirmButtonText: "Yes, delete it!",
    })
    .then(async (result) => {
      if (result.isConfirmed) {
        const res = await Api.del(
          "/api/ecommerce/dash/domains?id=" + domain.id
        );
        getDomains();
        notifs.value.push({
          type: "success",
          message: "Page deleted successfully",
        });
      }
    });
};
const dnsManagement = ref(null);
const showDns = ref(false);
const records = ref([]);
async function setDnsManagement(domain) {
  showDns.value = true;
  dnsManagement.value = domain;
  const res = await Api.get(
    `/api/ecommerce/dash/records?domain=${dnsManagement.value.id}`
  );
  records.value = res.data;
}

const newRecord = ref({
  type: "a",
  name: "",
  value: "",
  ttl: 1,
  error: "",
});

async function addNewRecord() {
  console.log(newRecord.value);
  const res = await Api.post(
    `/api/ecommerce/dash/records?domain=${dnsManagement.value.id}`,
    newRecord.value
  );
  console.log(res);
  if (res.data.code == 400) {
    newRecord.value.error = res.data.msg;
  } else {
    records.value = res.data;
  }
}

function copyNameserver(e, ns) {
  e.target.innerHTML = "Copied!";
  navigator.clipboard.writeText(ns);
  setTimeout(() => {
    e.target.innerHTML = "Copy";
  }, 2000);
}
function copyUrl(text) {
  navigator.clipboard.writeText(text);
  toaster.show({
    title: "Copied!",
    message: "",
    color: "info",
    icon: "lucide:check",
    closable: true,
  });
}
</script>
<template>
  <div class="">
    <section>
      <div class="pb-4 sm:flex sm:items-center justify-between my-4">
        <CommonTitleIcon :filename="'web-min.png'" :title="'Domains & Dns'" />
        <div class="mt-4 sm:mt-0 sm:ml-16 sm:flex-none relative">
          <button
            @click="show = true"
            type="button"
            class="inline-flex items-center justify-center rounded-md border border-transparent bg-primary-500 px-4 py-2 text-sm text-white -sm hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2 sm:w-auto"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="18"
              height="18"
              viewBox="0 0 24 24"
            >
              <path
                fill="currentColor"
                d="M19 12.998h-6v6h-2v-6H5v-2h6v-6h2v6h6z"
              />
            </svg>
            Add New Domain
          </button>
        </div>
      </div>
      <BasePlaceload
        v-if="preloader"
        class="h-[50vh] w-full rounded opacity-35"
      />
      <TairoContentWrapper v-else>
        <div>
          <div
            v-if="domains && domains.results && domains.results.length === 0"
          >
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
          <div v-else class="pt-1">
            <TransitionGroup
              enter-active-class="transform-gpu"
              enter-from-class="opacity-0 -translate-x-full"
              enter-to-class="opacity-100 translate-x-0"
              leave-active-class="absolute transform-gpu"
              leave-from-class="opacity-100 translate-x-0"
              leave-to-class="opacity-0 -translate-x-full"
            >
              <DemoFlexTableRow
                v-for="(domain, index) in domains.results"
                :key="index"
                shape="straight"
                condensed
                spaced
              >
                <template #start>
                  <DemoFlexTableCell
                    label=""
                    :hide-label="index > 0"
                    class="w-full"
                  >
                    <div class="w-full">
                      <p class="w-full">
                        {{ domain.domain
                        }}<span v-if="domain.subdomain">.nextoxy.com</span>
                      </p>
                    </div>
                  </DemoFlexTableCell>
                  <DemoFlexTableCell
                    label="dns server"
                    :hide-label="index > 0"
                    tablet-hidden
                    class="w-full sm:w-[260px]"
                  >
                    <div class="text-xs">
                      <p
                        class="text-xs mb-1 flex items-center justify-center"
                        v-if="domain.ns1"
                      >
                        <span>{{ domain.ns1 }}</span>
                        <BaseButton
                          color="success"
                          size="xs"
                          class="text-xs px-1 py-[2px] ml-1"
                          @click="copyNameserver($event, domain.ns1)"
                          >Copy</BaseButton
                        >
                      </p>
                      <p
                        class="text-xs mb-1 flex items-center justify-center"
                        v-if="domain.ns2"
                      >
                        <span>{{ domain.ns2 }}</span>
                        <BaseButton
                          color="success"
                          size="xs"
                          class="text-xs px-1 py-[2px] ml-1"
                          @click="copyNameserver($event, domain.ns2)"
                          >Copy</BaseButton
                        >
                      </p>
                    </div>
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
                      class="capitalize"
                    >
                      Active
                    </BaseTag>
                  </DemoFlexTableCell>
                  <DemoFlexTableCell
                    label="domain Date"
                    :hide-label="index > 0"
                    tablet-hidden
                    class="w-full sm:w-[160px]"
                  >
                    <div class="text-xs">{{ domain.created_at }}</div>
                  </DemoFlexTableCell>
                  <DemoFlexTableCell label="action" :hide-label="index > 0">
                    <BaseButtonAction
                      @click="setDnsManagement(domain)"
                      color="muted"
                    >
                      <span>Manage</span>
                    </BaseButtonAction>
                  </DemoFlexTableCell>
                  <DemoFlexTableCell label="Delete" :hide-label="index > 0">
                    <BaseButtonAction
                      @click="deleteDomain(domain)"
                      color="muted"
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
              @click="loadMore(domains.next)"
              v-if="domains && domains.next"
            >
              Load More
            </BaseButton>
          </div>
        </div>
      </TairoContentWrapper>
    </section>

    <CommonOver :show="show">
      <DialogPanel class="pointer-events-auto relative w-screen max-w-md">
        <TransitionChild
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
          ></div>
        </TransitionChild>
        <div
          class="flex h-full flex-col text-muted-500 overflow-y-scroll-no custom-scroll bg-white dark:bg-slate-800 shadow-xl m-2 rounded-md"
        >
          <div class="flex justify-between items-center py-3 px-3">
            <DialogTitle class="leading-6">Add New Domain</DialogTitle>
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
          <div class="relative mt-6 flex-1 px-4 sm:px-6">
            <div class="space-y-6">
              <div>
                <label for="email" class="block text-sm">Domain Name</label>
                <div class="mt-1">
                  <input
                    @keydown.enter="addNewDomain()"
                    v-model="newDomain"
                    id="email"
                    name="email"
                    type="text"
                    autocomplete="email"
                    required=""
                    class="block w-full appearance-none rounded-md border border-gray-300 px-3 py-2 placeholder-gray-400 -sm focus:border-indigo-500 focus:outline-none focus:ring-indigo-500 sm:text-sm"
                  />
                </div>
              </div>
              <p class="my-4 text-rose-700" v-if="newDomainError">
                {{ newDomainError }}
              </p>
              <div v-if="!newDomainLoading">
                <button
                  @click="addNewDomain"
                  type="submit"
                  class="flex w-full justify-center rounded-md border border-transparent bg-indigo-600 py-2 px-4 text-sm text-white -sm hover:bg-indigo-700 focus:outline-none"
                >
                  Add Domain
                </button>
              </div>
              <div v-else>
                <button
                  type="submit"
                  class="flex w-full justify-center rounded-md border border-transparent bg-indigo-600 py-2 px-4 text-sm text-white -sm hover:bg-indigo-700 focus:outline-none"
                >
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    width="32"
                    height="32"
                    viewBox="0 0 24 24"
                  >
                    <g>
                      <circle
                        cx="12"
                        cy="2.5"
                        r="1.5"
                        fill="currentColor"
                        opacity=".14"
                      />
                      <circle
                        cx="16.75"
                        cy="3.77"
                        r="1.5"
                        fill="currentColor"
                        opacity=".29"
                      />
                      <circle
                        cx="20.23"
                        cy="7.25"
                        r="1.5"
                        fill="currentColor"
                        opacity=".43"
                      />
                      <circle
                        cx="21.5"
                        cy="12"
                        r="1.5"
                        fill="currentColor"
                        opacity=".57"
                      />
                      <circle
                        cx="20.23"
                        cy="16.75"
                        r="1.5"
                        fill="currentColor"
                        opacity=".71"
                      />
                      <circle
                        cx="16.75"
                        cy="20.23"
                        r="1.5"
                        fill="currentColor"
                        opacity=".86"
                      />
                      <circle cx="12" cy="21.5" r="1.5" fill="currentColor" />
                      <animateTransform
                        attributeName="transform"
                        calcMode="discrete"
                        dur="0.75s"
                        repeatCount="indefinite"
                        type="rotate"
                        values="0 12 12;30 12 12;60 12 12;90 12 12;120 12 12;150 12 12;180 12 12;210 12 12;240 12 12;270 12 12;300 12 12;330 12 12;360 12 12"
                      />
                    </g>
                  </svg>
                </button>
              </div>
            </div>
          </div>
        </div>
      </DialogPanel>
    </CommonOver>

    <CommonOver :show="showDns">
      <DialogPanel
        class="pointer-events-auto relative w-screen max-w-5xl bg-white dark:bg-slate-700"
        v-if="dnsManagement"
      >
        <TransitionChild
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
              @click="showDns = false"
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
        </TransitionChild>
        <div
          class="flex h-full flex-col overflow-y-scroll py-6 -xl text-muted-600 px-3"
        >
          <div class="px-4 sm:px-6">
            <DialogTitle class="leading-6 uppercase text-center"
              >Update Dns Records</DialogTitle
            >
            <hr class="my-2" />
            <BaseMessage class="max-w-sm" type="info" shape="rounded" icon>
              <div class="flex gap-2 items-center justify-between w-full">
                <a
                  class="flex gap-2 items-center"
                  target="_blank"
                  :href="'https://' + dnsManagement.domain"
                >
                  <p class="">{{ dnsManagement.domain }}</p>
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    width="18"
                    height="18"
                    viewBox="0 0 24 24"
                  >
                    <path
                      fill="none"
                      stroke="currentColor"
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6m4-3h6v6m-11 5L21 3"
                    />
                  </svg>
                </a>
                <BaseButtonIcon
                  @click="copyUrl('https://' + dnsManagement.domain)"
                  shape="curved"
                  size="sm"
                  flavor="pastel"
                  color="info"
                >
                  <Icon
                    name="material-symbols:content-copy-outline-rounded"
                    class="h-4 w-4"
                  />
                </BaseButtonIcon>
              </div>
            </BaseMessage>
          </div>

          <div class="p-4 px-6 space-y-6">
            <div class="flex gap-4 flex-wrap">
              <div class="flex-0 min-w-[120px]">
                <label for="email" class="block text-sm mb-2">Type</label>
                <select
                  v-model="newRecord.type"
                  name=""
                  id=""
                  class="block w-full rounded-md border border-gray-300 px-3 py-2 placeholder-gray-400 -sm focus:border-indigo-500 focus:outline-none focus:ring-indigo-500 sm:text-sm"
                >
                  <option value="a">A</option>
                  <option value="aaaa">AAAA</option>
                  <option value="cname">CNAME</option>
                  <option value="mx">MX</option>
                  <option value="ns">NS</option>
                  <option value="ptr">PTR</option>
                  <option value="srv">SRV</option>
                  <option value="spf">SPF</option>
                  <option value="txt">TXT</option>
                </select>
              </div>
              <div class="flex-1 max-w-[300px] min-w-[120px]">
                <label for="email" class="block text-sm mb-2">Name</label>
                <input
                  v-model="newRecord.name"
                  id="email"
                  name="email"
                  type="text"
                  autocomplete="email"
                  required=""
                  class="block w-full appearance-none rounded-md border border-gray-300 px-3 py-2 placeholder-gray-400 -sm focus:border-indigo-500 focus:outline-none focus:ring-indigo-500 sm:text-sm"
                />
              </div>
              <div class="flex-1 min-w-[190px]">
                <label
                  for="email"
                  class="block text-sm mb-2"
                  v-if="newRecord.type == 'a'"
                  >IPv4 address (Required)</label
                >
                <label
                  for="email"
                  class="block text-sm mb-2"
                  v-else-if="newRecord.type == 'aaaa'"
                  >IPv6 address (Required)</label
                >
                <label
                  for="email"
                  class="block text-sm mb-2"
                  v-else-if="newRecord.type == 'cname'"
                  >Target (Required)</label
                >
                <label
                  for="email"
                  class="block text-sm mb-2"
                  v-else-if="newRecord.type == 'ptr'"
                  >Domain name (Required)</label
                >
                <label
                  for="email"
                  class="block text-sm mb-2"
                  v-else-if="newRecord.type == 'mx'"
                  >Target (Required)</label
                >
                <label
                  for="email"
                  class="block text-sm mb-2"
                  v-else-if="newRecord.type == 'ns'"
                  >Domain name (Required)</label
                >
                <label
                  for="email"
                  class="block text-sm mb-2"
                  v-else-if="newRecord.type == 'srv'"
                  >Target (Required)</label
                >
                <label
                  for="email"
                  class="block text-sm mb-2"
                  v-else-if="newRecord.type == 'spf'"
                  >Text (Required)</label
                >
                <label
                  for="email"
                  class="block text-sm mb-2"
                  v-else-if="newRecord.type == 'txt'"
                  >Text (Required)</label
                >
                <span v-if="newRecord.type == 'txt'">
                  <textarea
                    v-model="newRecord.value"
                    class="w-full border rounded"
                    name=""
                    id=""
                    cols="30"
                    rows="3"
                  ></textarea>
                </span>
                <span v-else>
                  <input
                    v-model="newRecord.value"
                    id="email"
                    name="email"
                    type="text"
                    autocomplete="email"
                    required=""
                    class="block w-full appearance-none rounded-md border border-gray-300 px-3 py-2 placeholder-gray-400 -sm focus:border-indigo-500 focus:outline-none focus:ring-indigo-500 sm:text-sm"
                  />
                </span>
              </div>
              <div class="min-w-[120px]">
                <label for="email" class="block text-sm mb-2">TTL</label>
                <select
                  v-model="newRecord.ttl"
                  name=""
                  id=""
                  class="block w-full rounded-md border border-gray-300 px-3 py-2 placeholder-gray-400 -sm focus:border-indigo-500 focus:outline-none focus:ring-indigo-500 sm:text-sm"
                >
                  <option value="1">1 Min</option>
                  <option value="2">2 Min</option>
                  <option value="5">5 Min</option>
                  <option value="10">10 Min</option>
                  <option value="15">15 Min</option>
                  <option value="30">30 Min</option>
                  <option value="60">1 Hour</option>
                  <option value="120">2 Hour</option>
                  <option value="300">5 Hour</option>
                  <option value="720">12 Hour</option>
                  <option value="1440">24 Hour</option>
                </select>
              </div>
            </div>
            <div>
              {{ newRecord.value }}
              <p class="text-rose-600 mb-4" v-if="newRecord.error">
                {{ newRecord.error }}
              </p>
              <button
                @click="addNewRecord"
                type="submit"
                class="flex justify-center rounded-md border border-transparent bg-indigo-600 py-2 px-4 text-sm text-white -sm hover:bg-indigo-700 focus:outline-none"
              >
                Add Record
              </button>
            </div>
          </div>

          <hr class="my-2" />

          <table class="p-4 px-6 min-w-full divide-y divide-gray-200 my-5">
            <thead class="">
              <tr>
                <th
                  scope="col"
                  class="px-6 py-3 text-left text-xs text-gray-500 uppercase tracking-wider"
                >
                  Type
                </th>
                <th
                  scope="col"
                  class="px-6 py-3 text-left text-xs text-gray-500 uppercase tracking-wider"
                >
                  Name
                </th>
                <th
                  scope="col"
                  class="px-6 py-3 text-left text-xs text-gray-500 uppercase tracking-wider"
                >
                  Value
                </th>
                <th
                  scope="col"
                  class="px-6 py-3 text-left text-xs text-gray-500 uppercase tracking-wider"
                >
                  TTL
                </th>
                <th scope="col" class="relative px-6 py-3">
                  <span class="sr-only">Edit</span>
                </th>
              </tr>
            </thead>
            <tbody class="divide-y divide-gray-200">
              <tr class="stripe" v-for="dns in records" :key="dns.id">
                <td class="px-6 py-4 whitespace-nowrap">
                  <div class="text-sm">A</div>
                </td>
                <td class="px-6 py-4 whitespace-nowrap">
                  <div class="text-sm">{{ dns.name }}</div>
                </td>
                <td class="px-6 py-4 whitespace-nowrap">
                  <div class="text-sm">{{ dns.content }}</div>
                </td>
                <td class="px-6 py-4 whitespace-nowrap">
                  <div class="text-sm">{{ dns.ttl }}</div>
                </td>
                <td class="px-6 py-4 whitespace-nowrap text-right text-sm">
                  <a href="#" class="text-indigo-600 hover:text-indigo-900"
                    >Edit</a
                  >
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </DialogPanel>
    </CommonOver>
  </div>
</template>

<style scoped>
.stripe:nth-child(odd) {
  background-color: rgba(0, 0, 0, 0.05);
}
</style>
