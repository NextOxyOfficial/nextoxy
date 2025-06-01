<template>
  <section>
    <div class="w-full" v-if="preloader">
      <div class="flex flex-wrap gap-1">
        <BaseCard shape="rounded" class="p-6 md:p-12 mb-2 w-full max-w-[400px]">
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
          <div class="flex items-center">
            <BasePlaceload class="h-10 w-10 rounded-full" />

            <div class="ms-3 grow space-y-2">
              <BasePlaceload class="h-3 w-full rounded" />

              <BasePlaceload class="h-3 w-[85%] rounded" />
            </div>
          </div>
        </BaseCard>
        <BaseCard shape="rounded" class="p-6 md:p-12 mb-2 flex-1">
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
          <div class="flex items-center">
            <BasePlaceload class="h-10 w-10 rounded-full" />

            <div class="ms-3 grow space-y-2">
              <BasePlaceload class="h-3 w-full rounded" />

              <BasePlaceload class="h-3 w-[85%] rounded" />
            </div>
          </div>
          <div class="flex items-center mt-8">
            <BasePlaceload class="h-10 w-10 rounded-full" />

            <div class="ms-3 grow space-y-2">
              <BasePlaceload class="h-3 w-full rounded" />

              <BasePlaceload class="h-3 w-[85%] rounded" />
            </div>
          </div>
        </BaseCard>
      </div>
      <div class="flex gap-6 mt-12 flex-wrap pb-[20vh]">
        <BaseCard
          shape="rounded"
          class="px-6 md:px-12 py-16 mb-2 flex-1 max-w-[350px] min-w-[290px]"
          v-for="i in 8"
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
    </div>
    <div class="my-5" v-else>
      <div class="pb-5 my-4 sm:flex sm:items-center sm:justify-between">
        <CommonTitleIcon
          :filename="'plug-in-min.png'"
          weight="bold"
          :title="'Plugins'"
        />
      </div>
      <div
        class="bg-primary dark:bg-slate-700 flex p-4 text-white items-center gap-4 mb-6"
      >
        <UIcon name="i-heroicons-information-circle-solid" class="text-4xl" />
        <p class="text-xl">
          If you need a custom plugin please contact with us
          <span class="text-blue-500 font-semibold">support@nextoxy.com</span>
        </p>
      </div>

      <Swiper
        v-if="featuredPlugins && featuredPlugins.results"
        :modules="[SwiperAutoplay, SwiperEffectCreative]"
        :slides-per-view="1"
        :loop="true"
        :effect="'creative'"
        :autoplay="{
          delay: 3000,
          disableOnInteraction: true,
        }"
        :creative-effect="{
          prev: {
            shadow: false,
            translate: ['-20%', 0, -1],
          },
          next: {
            translate: ['100%', 0, 0],
          },
        }"
      >
        <SwiperSlide
          v-for="plugin in featuredPlugins.results"
          :key="plugin.id"
          class="bg-slate-50 border dark:bg-slate-800 rounded"
        >
          <div class="relative flex justify-between rounded overflow-hidden">
            <img
              class="h-[400px] w-[500px] flex-1 object-cover"
              :src="Api.baseURL + plugin.feature_image"
              alt=""
              v-if="plugin.feature_image"
            />
            <img
              class="h-[400px] w-[500px] flex-1 object-cover"
              src="https://via.placeholder.com/500"
              alt=""
              v-else
            />

            <div class="flex-1 relative p-4 flex justify-center items-center">
              <div class="max-w-[400px]">
                <p class="mt-2 text-3xl font-bold tracking-tight sm:text-4xl">
                  {{ plugin.title }}
                  <span class="text-sm bg-slate-200 px-1 rounded relative"
                    >v1.0.0
                    <span
                      class="absolute -top-2 -right-3 cursor-pointer z-10 bg-indigo-300 h-4 flex justify-center items-center w-4 text-center rounded-full text-xs text-white"
                      >!</span
                    >
                  </span>
                </p>
                <p class="mt-2">{{ plugin.instruction }}</p>
                <div class="mt-5">
                  <div class="inline-flex rounded-md shadow">
                    <button
                      v-if="plugin.installed"
                      @click="uninstallPlugin($event, plugin.id)"
                      class="inline-flex items-center justify-center rounded-md border border-muted-500 px-5 py-2 text-base font-medium"
                    >
                      Installed
                    </button>
                    <button
                      v-else
                      @click="installPlugin($event, plugin.id)"
                      class="inline-flex items-center justify-center rounded-md border border-muted-500 px-5 py-2 text-base font-medium"
                    >
                      Install Plugin
                    </button>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </SwiperSlide>
      </Swiper>
      <hr class="my-4" />
      <BaseCard class="p-4">
        <h4 class="text-slate-500 text-xl font-semibold">Installed Plugins</h4>
        <div class="rounded overflow-hidden">
          <BaseCard
            shape="curved"
            class="p-6 flexs justify-between flex-wrap items-center hidden"
          >
            <h4 class="text-slate-500">Installed Plugins</h4>
            <div class="flex relative w-full max-w-[300px]">
              <input
                v-model="nonInstalledSearchQ"
                class="border h-[40px] px-2 py-1 rounded-xl w-full"
                type="search"
                placeholder="Search Here.."
              />
              <button
                @click="nonInstalledSearch"
                class="absolute right-1 top-0 h-full rounded-l text-slate-500"
              >
                <svg
                  class="p-1 bg-white/0 rounded-xl"
                  xmlns="http://www.w3.org/2000/svg"
                  width="32"
                  height="32"
                  viewBox="0 0 256 256"
                >
                  <path
                    fill="currentColor"
                    d="m229.66 218.34l-50.07-50.06a88.11 88.11 0 1 0-11.31 11.31l50.06 50.07a8 8 0 0 0 11.32-11.32ZM40 112a72 72 0 1 1 72 72a72.08 72.08 0 0 1-72-72Z"
                  />
                </svg>
              </button>
            </div>
          </BaseCard>
          <div
            class="flex gap-1 flex-wrap mb-6 mt-3 lg:grid lg:grid-cols-5"
            v-if="shopPlugins.results"
          >
            <BaseCard
              shape="curved"
              class="p-4 max-w-[100vw] md:max-w-[250px] lg:w-full"
              v-for="spl in shopPlugins.results"
              :key="spl.id"
            >
              <div class="flex gap-2 justify-end">
                <svg
                  @click="activation = spl"
                  class="w-4 cursor-pointer"
                  xmlns="http://www.w3.org/2000/svg"
                  width="32"
                  height="32"
                  viewBox="0 0 24 24"
                >
                  <path
                    fill="#242424"
                    d="m19.44 12.99l-.01.02c.04-.33.08-.67.08-1.01c0-.34-.03-.66-.07-.99l.01.02l2.44-1.92l-2.43-4.22l-2.87 1.16l.01.01c-.52-.4-1.09-.74-1.71-1h.01L14.44 2H9.57l-.44 3.07h.01c-.62.26-1.19.6-1.71 1l.01-.01l-2.88-1.17l-2.44 4.22l2.44 1.92l.01-.02c-.04.33-.07.65-.07.99c0 .34.03.68.08 1.01l-.01-.02l-2.1 1.65l-.33.26l2.43 4.2l2.88-1.15l-.02-.04c.53.41 1.1.75 1.73 1.01h-.03L9.58 22h4.85s.03-.18.06-.42l.38-2.65h-.01c.62-.26 1.2-.6 1.73-1.01l-.02.04l2.88 1.15l2.43-4.2s-.14-.12-.33-.26l-2.11-1.66zM12 15.5c-1.93 0-3.5-1.57-3.5-3.5s1.57-3.5 3.5-3.5s3.5 1.57 3.5 3.5s-1.57 3.5-3.5 3.5z"
                  />
                </svg>
              </div>
              <div class="flex justify-between items-center">
                <img
                  class="h-16 w-16 object-contain cursor-pointer"
                  :src="Api.baseURL + spl.plugin.image"
                  alt=""
                />
                <div class="flex gap-1 items-center text-green-700">
                  <p class="text-sm">Installed</p>
                </div>
              </div>
              <div class="my-4 cursor-pointer">
                <h4 class="text-base font-medium">{{ spl.plugin.name }}</h4>
                <p class="text-xs font-normal">{{ spl.plugin.title }}</p>
              </div>
              <div class="flex justify-between items-center">
                <div
                  @click="uninstallPlugin($event, spl.id)"
                  class="flex gap-1 items-center border rounded-md px-2 py-1 cursor-pointer"
                >
                  <p class="text-xs">Uninstall</p>
                </div>
                <div
                  class="flex gap-1 justify-between items-center"
                  v-if="spl.activated"
                >
                  <p class="text-xs text-green-700">Active</p>
                  <div
                    @click="deActivatePlugin(spl.id)"
                    class="flex bg-slate-100 text-slate-800 gap-1 items-center border rounded-md px-2 py-1 cursor-pointer"
                  >
                    <p class="text-xs">Deactivate</p>
                  </div>
                </div>
                <div class="flex gap-1 justify-between items-center" v-else>
                  <p class="text-xs text-rose-700">Inactive</p>
                  <div
                    @click="activation = spl"
                    class="flex bg-green-700 text-white gap-1 items-center border rounded-md px-2 py-1 cursor-pointer"
                  >
                    <p class="text-xs">Activate</p>
                  </div>
                </div>
              </div>
            </BaseCard>
          </div>
          <div
            v-if="shopPlugins.results && shopPlugins.results.length == 0"
            class="text-center pb-8"
          >
            <p class="text-sm text-gray-500">No Installed Plugin Found</p>
          </div>
        </div>
      </BaseCard>
      <hr class="my-4" />
      <div class="">
        <BaseCard shape="curved" class="p-4">
          <div class="flex justify-between flex-wrap items-center">
            <h4 class="text-slate-500 text-xl font-semibold">All Plugins</h4>
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
                @keypress.enter="getPlugins"
              />
              <BaseButton @click="getPlugins" color="primary"
                >Search</BaseButton
              >
            </div>
          </div>

          <div class="grids-container mt-3">
            <div
              class="grids-wapper grid gap-4 grid-cols-3 md:grid-cols-4"
              v-if="plugins.results"
            >
              <BaseCard
                shape="curved"
                class="p-4"
                v-for="pl in plugins.results"
                :key="pl.id"
              >
                <div class="flex justify-between items-center">
                  <img
                    @click="viewPlugin(pl)"
                    class="h-16 w-16 object-contain cursor-pointer"
                    :src="Api.baseURL + pl.image"
                    alt=""
                  />
                  <div class="">
                    <div
                      class="flex gap-1 items-center text-green-700 justify-center"
                      v-if="pl.installed"
                    >
                      <p class="text-sm">Installed</p>
                    </div>
                    <div
                      @click="installPlugin($event, pl.id)"
                      class="text-white bg-slate-900 flex gap-1 items-center border rounded-md px-2 cursor-pointer"
                      v-else
                    >
                      <p class="text-xs px-2 py-1">Install</p>
                    </div>
                    <div
                      @click="viewPlugin(pl)"
                      class="flex gap-1 items-center border rounded-md px-2 cursor-pointer mt-2"
                    >
                      <p class="text-xs px-2 py-1">View Details</p>
                    </div>
                  </div>
                </div>
                <div @click="viewPlugin(pl)" class="my-4 cursor-pointer">
                  <h4 class="text-base font-medium">{{ pl.name }}</h4>
                  <p class="text-xs font-normal">{{ pl.title }}</p>
                </div>
              </BaseCard>
            </div>
          </div>
        </BaseCard>
      </div>

      <!-- activation  -->
      <CommonModal v-if="activation">
        <div class="absolute right-[10px] top-[9px]">
          <div
            @click="activation = ''"
            class="mx-auto cursor-pointer flex h-10 w-10 p-2 flex-shrink-0 items-center justify-center rounded-full bg-white border text-rose-800 hover:shadow-lg"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="32"
              height="32"
              viewBox="0 0 24 24"
            >
              <path
                fill="currentColor"
                d="M18.3 5.71a.996.996 0 0 0-1.41 0L12 10.59L7.11 5.7A.996.996 0 1 0 5.7 7.11L10.59 12L5.7 16.89a.996.996 0 1 0 1.41 1.41L12 13.41l4.89 4.89a.996.996 0 1 0 1.41-1.41L13.41 12l4.89-4.89c.38-.38.38-1.02 0-1.4z"
              />
            </svg>
          </div>
        </div>
        <div class="text-center sm:mt-0 sm:text-left w-full">
          <h3 class="text-slate-100 p-4 bg-purple-600">Plugin Setup</h3>
          <div class="flex justify-center flex-col md:flex-row w-full">
            <div class="my-5 pt-2 px-4 flex-1 max-w-[350px] text-sm">
              <h2 class="text-xl font-semibold mb-3">Instruction</h2>
              <p>
                {{ activation.plugin.instruction }}
              </p>
            </div>
            <div
              class="flex flex-1 flex-col justify-center p-5 w-full max-w-sm"
            >
              <div class="md:col-span-2 md:mt-0">
                <div
                  class="my-2"
                  v-for="fl in activation.data.fields"
                  :key="fl"
                >
                  <label class="block font-bold text-gray-700">
                    {{ fl.help }}
                    <span class="text-rose-700 font-bold" v-if="fl.required"
                      >*</span
                    >
                  </label>
                  <textarea
                    v-if="fl.type == 'textarea'"
                    v-model="fl.value"
                    name=""
                    id=""
                    cols="30"
                    rows="8"
                    class="mt-1 border px-3 py-2 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md"
                  ></textarea>
                  <input
                    v-else
                    v-model="fl.value"
                    :placeholder="fl.help"
                    :type="fl.type"
                    class="mt-1 border px-3 py-2 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md"
                  />
                </div>
              </div>
              <div class="flex justify-end my-4 gap-2">
                <BaseButton @click="activatePlugin" color="primary" size="sm"
                  >Save & Activate</BaseButton
                >
              </div>
              <p v-if="activation.error" class="test-rose-500">
                {{ activation.error }}
              </p>
            </div>
          </div>
        </div>
      </CommonModal>
      <!-- common  -->
      <CommonModal v-if="preview">
        <div class="absolute right-[10px] top-[12px]">
          <div
            @click="preview = ''"
            class="mx-auto cursor-pointer flex h-10 w-10 p-2 flex-shrink-0 items-center justify-center rounded-full bg-white border text-rose-800 hover:shadow-lg"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="32"
              height="32"
              viewBox="0 0 24 24"
            >
              <path
                fill="currentColor"
                d="M18.3 5.71a.996.996 0 0 0-1.41 0L12 10.59L7.11 5.7A.996.996 0 1 0 5.7 7.11L10.59 12L5.7 16.89a.996.996 0 1 0 1.41 1.41L12 13.41l4.89 4.89a.996.996 0 1 0 1.41-1.41L13.41 12l4.89-4.89c.38-.38.38-1.02 0-1.4z"
              />
            </svg>
          </div>
        </div>
        <div class="mt-3 text-center sm:mt-0 sm:text-left w-full">
          <h3 class="text-slate-100 p-4 bg-purple-600">Plugin Details</h3>
          <div class="flex flex-1 flex-col justify-center p-5 w-full">
            <div class="md:col-span-2 md:mt-0">
              <div class="bg-white rounded-lg shadow-lg overflow-hidden">
                <div class="p-6">
                  <h2 class="text-lg font-medium text-gray-900">
                    {{ preview.title }}
                  </h2>
                  <p class="text-sm text-gray-500">{{ preview.instruction }}</p>
                </div>
                <img
                  class="w-full max-h-[500px] object-cover object-center"
                  :src="Api.baseURL + preview.image"
                  alt=""
                />
                <div class="p-6">
                  <div class="flex items-center">
                    <span class="mr-3 text-gray-700 font-medium">Type:</span>
                    <span
                      class="px-2 py-1 bg-gray-200 text-gray-800 text-xs rounded-full uppercase"
                      >{{ preview.type }}</span
                    >
                  </div>
                  <div class="flex items-center mt-4">
                    <span class="mr-3 text-gray-700 font-medium">Price:</span>
                    <span class="text-gray-900 font-semibold"
                      >USD ${{ preview.price }}</span
                    >
                  </div>
                  <div class="mt-4 border p-4">
                    <span class="text-gray-700 font-medium">Data Fields:</span>
                    <ul class="pl-4 mt-2 text-sm text-gray-500">
                      <li
                        v-for="(field, key) in preview.data.fields"
                        :key="key"
                      >
                        {{ key }} - {{ field.help }}
                      </li>
                    </ul>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </CommonModal>
    </div>
  </section>
</template>
<!-- shop-plugins
plugins -->
<script setup>
definePageMeta({
  layout: "dashboard",
});
const preloader = useState("preloader");
const { notifs } = useAuth();
const Api = useApi();
const { shop, getShop } = useShop();

const plugins = ref("");
const search = ref("");
async function getPlugins() {
  const { data } = await Api.get(
    "/api/ecommerce/dash/plugins?search=" + search.value
  );
  plugins.value = data;
}
getPlugins();

const featuredPlugins = ref("");
async function getFeaturedPlugins() {
  const { data } = await Api.get("/api/ecommerce/dash/plugins?featured=1");
  featuredPlugins.value = data;
}
getFeaturedPlugins();

const shopPlugins = ref("");
async function getShopPlugins() {
  const { data } = await Api.get("/api/ecommerce/dash/shop-plugins");
  shopPlugins.value = data;
}
getShopPlugins();

async function installPlugin(e, pid) {
  e.target.innerHTML = "Installing...";
  const { data } = await Api.get(
    "/api/ecommerce/dash/shop-plugins?install=" + pid
  );
  console.log(data);
  shopPlugins.value = data;
  e.target.innerHTML = "Install";
  notifs.value.push({
    type: "success",
    message: "Plugin installed successfully",
  });
  getPlugins();
}
async function uninstallPlugin(e, pid) {
  e.target.innerHTML = "Uninstalling...";
  const { data } = await Api.get(
    "/api/ecommerce/dash/shop-plugins?uninstall=" + pid
  );
  console.log(data);
  shopPlugins.value = data;
  e.target.innerHTML = "Uninstall";
  getPlugins();
  getShop();
}

const activation = ref("");
async function activatePlugin(e) {
  e.target.innerHTML = "Please wait..";
  const { data } = await Api.put(
    "/api/ecommerce/dash/shop-plugins",
    activation.value
  );
  console.log(data);
  e.target.innerHTML = "Save And Activate";
  if (data == 200) {
    activation.value = "";
    getShopPlugins();
    notifs.value.push({
      type: "success",
      message: "Plugin activated successfully",
    });
  } else {
    notifs.value.push({
      type: "error",
      message: "Plugin activation failed",
    });
  }
  getShop();
}

async function deActivatePlugin(id) {
  const { data } = await Api.get(
    "/api/ecommerce/dash/shop-plugins?deactivate=" + id
  );
  console.log(data);
  shopPlugins.value = data;
  getShop();
}

// search
const nonInstalledSearchQ = ref("");
const installedSearchQ = ref("");
const nonInstalledSearch = () => {
  Api.get(
    "/api/ecommerce/dash/plugins?search=" + nonInstalledSearchQ.value
  ).then(({ data }) => {
    plugins.value = data;
  });
};
const installedSearch = () => {
  Api.get(
    "/api/ecommerce/dash/shop-plugins?search=" + installedSearchQ.value
  ).then(({ data }) => {
    shopPlugins.value = data;
  });
};
// view
const preview = ref("");
const viewPlugin = (plugin) => {
  console.log(plugin);
  preview.value = plugin;
};
</script>

<style scoped>
.plugin-box:hover .plugin-avtivation {
  display: block;
}
@media (max-width: 914px) {
  .grids-wapper {
    grid-template-columns: repeat(3, 1fr);
  }
}
@media (max-width: 550px) {
  .grids-wapper {
    grid-template-columns: repeat(2, 1fr);
  }
}
@media (max-width: 400px) {
  .grids-wapper {
    grid-template-columns: repeat(1, 1fr);
  }
  .grid-box {
    max-width: 100%;
  }
}
</style>
