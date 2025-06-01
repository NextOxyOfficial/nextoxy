<template>
  <BaseCard
    shape="rounded"
    class="py-8 my-4 rounded"
    v-if="menus.main_menu && menus.footer_menu"
  >
    <section class="relative z-10 overflow-hiddenpy-6">
      <div class="px-1 md:px-4">
        <div
          class="border-stroke mx-auto mb-8 w-full max-w-[770px] rounded-lg border"
        >
          <div
            class="border-stroke w-full border-b p-1 md:p-6 flex items-center justify-between"
          >
            <h3 class="text-lg md:text-2xl font-semibold">
              Header Navigation Menu
            </h3>

            <BaseButton
              color="primary"
              @click="saveAll"
              type="submit"
              class="inline-flex gap-2 justify-center rounded-md border border-transparent bg-gray-800 py-2 px-4 text-sm font-medium text-white -sm hover:bg-gray-900 focus:outline-none focus:ring-2 focus:ring-gray-900 focus:ring-offset-2"
            >
              <svg
                v-if="!loading9"
                xmlns="http://www.w3.org/2000/svg"
                width="22"
                height="22"
                viewBox="0 0 24 24"
              >
                <path
                  fill="currentColor"
                  d="M5 19V5h7v7h7v1c.7 0 1.37.13 2 .35V9l-6-6H5c-1.11 0-2 .89-2 2v14a2 2 0 0 0 2 2h8.35c-.22-.63-.35-1.3-.35-2H5m9-14.5l5.5 5.5H14V4.5m8.5 12.75L17.75 22L15 19l1.16-1.16l1.59 1.59l3.59-3.59l1.16 1.41Z"
                />
              </svg>
              <svg
                v-else
                xmlns="http://www.w3.org/2000/svg"
                width="22"
                height="22"
                viewBox="0 0 24 24"
              >
                <path
                  fill="currentColor"
                  d="M12,1A11,11,0,1,0,23,12,11,11,0,0,0,12,1Zm0,19a8,8,0,1,1,8-8A8,8,0,0,1,12,20Z"
                  opacity=".25"
                />
                <path
                  fill="currentColor"
                  d="M10.14,1.16a11,11,0,0,0-9,8.92A1.59,1.59,0,0,0,2.46,12,1.52,1.52,0,0,0,4.11,10.7a8,8,0,0,1,6.66-6.61A1.42,1.42,0,0,0,12,2.69h0A1.57,1.57,0,0,0,10.14,1.16Z"
                >
                  <animateTransform
                    attributeName="transform"
                    dur="0.75s"
                    repeatCount="indefinite"
                    type="rotate"
                    values="0 12 12;360 12 12"
                  />
                </path>
              </svg>
              Save
            </BaseButton>
          </div>
          <div>
            <div
              class="p-1 md:p-5 text-indigo-500 cursor-pointer"
              @click="addHereMain"
            >
              Add A Menu
            </div>
            <div
              v-for="menu in menus.main_menu"
              :key="menu.id"
              class="link-edit"
            >
              <div
                class="min-h-[80px] w-full gap-2 border-stroke hover:bg-primary flex flex-wrap items-center border-b px-1 md:px-7 py-2 hover:bg-opacity-[4%]"
                v-if="!menu.deleted"
              >
                <div
                  class="flex h-11 w-full max-w-[44px] items-center justify-center rounded-full text-base font-medium uppercase text-[#FFB52B] hidden"
                >
                  <svg
                    class="cursor-pointer -mt-1"
                    xmlns="http://www.w3.org/2000/svg"
                    width="32"
                    height="32"
                    viewBox="0 0 24 24"
                  >
                    <g fill="none" fill-rule="evenodd">
                      <path
                        d="M24 0v24H0V0h24ZM12.593 23.258l-.011.002l-.071.035l-.02.004l-.014-.004l-.071-.035c-.01-.004-.019-.001-.024.005l-.004.01l-.017.428l.005.02l.01.013l.104.074l.015.004l.012-.004l.104-.074l.012-.016l.004-.017l-.017-.427c-.002-.01-.009-.017-.017-.018Zm.265-.113l-.013.002l-.185.093l-.01.01l-.003.011l.018.43l.005.012l.008.007l.201.093c.012.004.023 0 .029-.008l.004-.014l-.034-.614c-.003-.012-.01-.02-.02-.022Zm-.715.002a.023.023 0 0 0-.027.006l-.006.014l-.034.614c0 .012.007.02.017.024l.015-.002l.201-.093l.01-.008l.004-.011l.017-.43l-.003-.012l-.01-.01l-.184-.092Z"
                      />
                      <path
                        fill="currentColor"
                        d="M10.7 3.148a1.5 1.5 0 0 1 2.599 0l8.634 14.954a1.5 1.5 0 0 1-1.299 2.25H3.366a1.5 1.5 0 0 1-1.299-2.25l8.634-14.954Z"
                      />
                    </g>
                  </svg>
                  <svg
                    class="cursor-pointer -mb-1"
                    xmlns="http://www.w3.org/2000/svg"
                    width="32"
                    height="32"
                    viewBox="0 0 24 24"
                  >
                    <g
                      fill="none"
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                    >
                      <path d="M0 0h24v24H0z" />
                      <path
                        fill="currentColor"
                        d="M19.007 3a3 3 0 0 1 2.828 3.94l-.068.185l-.062.126l-7.09 12.233a3 3 0 0 1-5.137.19l-.103-.173l-7.1-12.25l-.061-.125a3 3 0 0 1 2.625-4.125L4.897 3l.06.002L5 3h14.007z"
                      />
                    </g>
                  </svg>
                </div>
                <input
                  type="text"
                  v-model="menu.name"
                  class="rounded-md border border-gray-300 py-1 px-2 focus:border-gray-900 focus:outline-none sm :text-sm"
                />
                <div class="w-full flex-1 relative">
                  <input
                    type="text"
                    v-model="menu.link"
                    class="flex-1 w-full min-w-[100px] rounded-md border border-gray-300 py-1 px-2 focus:border-gray-900 focus:outline-none sm :text-sm"
                  />
                  <div class="suggest mt-1 w-full gap-1 hidden">
                    <select
                      @change="menu.link = $event.target.value"
                      id=""
                      class="flex-1 w-full min-w-[100px] rounded-md border border-gray-300 py-1 px-2 focus:border-gray-900 focus:outline-none sm :text-sm"
                    >
                      <option value="/signin">Sign In</option>
                      <option value="/signin">Start Free Trial</option>
                      <template v-if="pages && pages.results">
                        <option
                          :value="page.slug"
                          v-for="page in pages.results"
                          :key="page.id"
                        >
                          {{ page.title }}
                        </option>
                      </template>
                    </select>
                  </div>
                </div>
                <svg
                  @click="addHereMain(menu)"
                  class="cursor-pointer p-2 bg-rose-50 rounded"
                  xmlns="http://www.w3.org/2000/svg"
                  width="35"
                  height="35"
                  viewBox="0 0 24 24"
                >
                  <path
                    fill="currentColor"
                    d="M3 5a1 1 0 0 0 1 1h16a1 1 0 1 0 0-2H4a1 1 0 0 0-1 1Zm9 15a1 1 0 0 0 1-1v-3h3a1 1 0 1 0 0-2h-3v-3a1 1 0 1 0-2 0v3H8a1 1 0 1 0 0 2h3v3a1 1 0 0 0 1 1Z"
                  />
                </svg>
                <svg
                  @click="menu.deleted = true"
                  class="cursor-pointer p-2 bg-rose-50 rounded"
                  xmlns="http://www.w3.org/2000/svg"
                  width="32"
                  height="32"
                  viewBox="0 0 24 24"
                >
                  <path
                    fill="currentColor"
                    d="M7 21q-.825 0-1.413-.588T5 19V6q-.425 0-.713-.288T4 5q0-.425.288-.713T5 4h4q0-.425.288-.713T10 3h4q.425 0 .713.288T15 4h4q.425 0 .713.288T20 5q0 .425-.288.713T19 6v13q0 .825-.588 1.413T17 21H7ZM7 6v13h10V6H7Zm2 10q0 .425.288.713T10 17q.425 0 .713-.288T11 16V9q0-.425-.288-.713T10 8q-.425 0-.713.288T9 9v7Zm4 0q0 .425.288.713T14 17q.425 0 .713-.288T15 16V9q0-.425-.288-.713T14 8q-.425 0-.713.288T13 9v7ZM7 6v13V6Z"
                  />
                </svg>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="relative z-10 overflow-hiddenpy-6">
      <div class="mx-auto px-1 md:px-4 lg:container">
        <div
          class="border-stroke mx-auto mb-8 w-full max-w-[770px] rounded-lg border"
        >
          <div
            class="border-stroke w-full border-b p-1 md:p-6 flex items-center justify-between"
          >
            <h3 class="text-lg md:text-2xl font-semibold">
              Footer Navigation Menu
            </h3>

            <BaseButton
              color="primary"
              @click="saveAll"
              type="submit"
              class="inline-flex gap-2 justify-center rounded-md border border-transparent bg-gray-800 py-2 px-4 text-sm font-medium text-white -sm hover:bg-gray-900 focus:outline-none focus:ring-2 focus:ring-gray-900 focus:ring-offset-2"
            >
              <svg
                v-if="!loading9"
                xmlns="http://www.w3.org/2000/svg"
                width="22"
                height="22"
                viewBox="0 0 24 24"
              >
                <path
                  fill="currentColor"
                  d="M5 19V5h7v7h7v1c.7 0 1.37.13 2 .35V9l-6-6H5c-1.11 0-2 .89-2 2v14a2 2 0 0 0 2 2h8.35c-.22-.63-.35-1.3-.35-2H5m9-14.5l5.5 5.5H14V4.5m8.5 12.75L17.75 22L15 19l1.16-1.16l1.59 1.59l3.59-3.59l1.16 1.41Z"
                />
              </svg>
              <svg
                v-else
                xmlns="http://www.w3.org/2000/svg"
                width="22"
                height="22"
                viewBox="0 0 24 24"
              >
                <path
                  fill="currentColor"
                  d="M12,1A11,11,0,1,0,23,12,11,11,0,0,0,12,1Zm0,19a8,8,0,1,1,8-8A8,8,0,0,1,12,20Z"
                  opacity=".25"
                />
                <path
                  fill="currentColor"
                  d="M10.14,1.16a11,11,0,0,0-9,8.92A1.59,1.59,0,0,0,2.46,12,1.52,1.52,0,0,0,4.11,10.7a8,8,0,0,1,6.66-6.61A1.42,1.42,0,0,0,12,2.69h0A1.57,1.57,0,0,0,10.14,1.16Z"
                >
                  <animateTransform
                    attributeName="transform"
                    dur="0.75s"
                    repeatCount="indefinite"
                    type="rotate"
                    values="0 12 12;360 12 12"
                  />
                </path>
              </svg>
              Save
            </BaseButton>
          </div>
          <div>
            <div
              class="p-1 md:p-5 text-indigo-500 cursor-pointer"
              @click="addHereFooter"
            >
              Add A Menu
            </div>
            <div
              v-for="menu in menus.footer_menu"
              :key="menu.id"
              class="link-edit"
            >
              <div
                class="min-h-[80px] w-full gap-2 border-stroke hover:bg-primary flex flex-wrap items-center border-b p-1 md:p-7 hover:bg-opacity-[4%]"
                v-if="!menu.deleted"
              >
                <div
                  class="flex h-11 w-full max-w-[44px] items-center justify-center rounded-full text-base font-medium uppercase text-[#FFB52B] hidden"
                >
                  <svg
                    class="cursor-pointer -mt-1"
                    xmlns="http://www.w3.org/2000/svg"
                    width="32"
                    height="32"
                    viewBox="0 0 24 24"
                  >
                    <g fill="none" fill-rule="evenodd">
                      <path
                        d="M24 0v24H0V0h24ZM12.593 23.258l-.011.002l-.071.035l-.02.004l-.014-.004l-.071-.035c-.01-.004-.019-.001-.024.005l-.004.01l-.017.428l.005.02l.01.013l.104.074l.015.004l.012-.004l.104-.074l.012-.016l.004-.017l-.017-.427c-.002-.01-.009-.017-.017-.018Zm.265-.113l-.013.002l-.185.093l-.01.01l-.003.011l.018.43l.005.012l.008.007l.201.093c.012.004.023 0 .029-.008l.004-.014l-.034-.614c-.003-.012-.01-.02-.02-.022Zm-.715.002a.023.023 0 0 0-.027.006l-.006.014l-.034.614c0 .012.007.02.017.024l.015-.002l.201-.093l.01-.008l.004-.011l.017-.43l-.003-.012l-.01-.01l-.184-.092Z"
                      />
                      <path
                        fill="currentColor"
                        d="M10.7 3.148a1.5 1.5 0 0 1 2.599 0l8.634 14.954a1.5 1.5 0 0 1-1.299 2.25H3.366a1.5 1.5 0 0 1-1.299-2.25l8.634-14.954Z"
                      />
                    </g>
                  </svg>
                  <svg
                    class="cursor-pointer -mb-1"
                    xmlns="http://www.w3.org/2000/svg"
                    width="32"
                    height="32"
                    viewBox="0 0 24 24"
                  >
                    <g
                      fill="none"
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                    >
                      <path d="M0 0h24v24H0z" />
                      <path
                        fill="currentColor"
                        d="M19.007 3a3 3 0 0 1 2.828 3.94l-.068.185l-.062.126l-7.09 12.233a3 3 0 0 1-5.137.19l-.103-.173l-7.1-12.25l-.061-.125a3 3 0 0 1 2.625-4.125L4.897 3l.06.002L5 3h14.007z"
                      />
                    </g>
                  </svg>
                </div>
                <input
                  type="text"
                  v-model="menu.name"
                  class="rounded-md border border-gray-300 py-1 px-2 focus:border-gray-900 focus:outline-none sm :text-sm min-w-[100px]"
                />
                <div class="w-full flex-1 relative">
                  <input
                    type="text"
                    v-model="menu.link"
                    class="flex-1 w-full rounded-md border border-gray-300 py-1 px-2 focus:border-gray-900 focus:outline-none sm :text-sm min-w-[100px]"
                  />
                  <div class="suggest mt-1 w-full gap-1 hidden">
                    <select
                      @change="menu.link = $event.target.value"
                      id=""
                      class="flex-1 w-full rounded-md border border-gray-300 py-1 px-2 focus:border-gray-900 focus:outline-none sm :text-sm min-w-[100px]"
                    >
                      <option value="/signin">Sign In</option>
                      <option value="/signin">Register</option>
                      <template v-if="pages && pages.results">
                        <option
                          :value="page.slug"
                          v-for="page in pages.results"
                          :key="page.id"
                        >
                          {{ page.title }}
                        </option>
                      </template>
                    </select>
                  </div>
                </div>
                <svg
                  @click="addHereFooter(menu)"
                  class="cursor-pointer p-2 bg-rose-50 rounded"
                  xmlns="http://www.w3.org/2000/svg"
                  width="35"
                  height="35"
                  viewBox="0 0 24 24"
                >
                  <path
                    fill="currentColor"
                    d="M3 5a1 1 0 0 0 1 1h16a1 1 0 1 0 0-2H4a1 1 0 0 0-1 1Zm9 15a1 1 0 0 0 1-1v-3h3a1 1 0 1 0 0-2h-3v-3a1 1 0 1 0-2 0v3H8a1 1 0 1 0 0 2h3v3a1 1 0 0 0 1 1Z"
                  />
                </svg>
                <svg
                  @click="menu.deleted = true"
                  class="cursor-pointer p-2 bg-rose-50 rounded"
                  xmlns="http://www.w3.org/2000/svg"
                  width="32"
                  height="32"
                  viewBox="0 0 24 24"
                >
                  <path
                    fill="currentColor"
                    d="M7 21q-.825 0-1.413-.588T5 19V6q-.425 0-.713-.288T4 5q0-.425.288-.713T5 4h4q0-.425.288-.713T10 3h4q.425 0 .713.288T15 4h4q.425 0 .713.288T20 5q0 .425-.288.713T19 6v13q0 .825-.588 1.413T17 21H7ZM7 6v13h10V6H7Zm2 10q0 .425.288.713T10 17q.425 0 .713-.288T11 16V9q0-.425-.288-.713T10 8q-.425 0-.713.288T9 9v7Zm4 0q0 .425.288.713T14 17q.425 0 .713-.288T15 16V9q0-.425-.288-.713T14 8q-.425 0-.713.288T13 9v7ZM7 6v13V6Z"
                  />
                </svg>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </BaseCard>
</template>

<script setup>
const Api = useApi();
const menus = ref("");
const { notifs } = useAuth();
function getMenu() {
  Api.get("/api/ecommerce/dash/menus").then((res) => {
    menus.value = res.data;
  });
}
getMenu();
const loading9 = ref(false);
function saveAll() {
  loading9.value = true;
  Api.post("/api/ecommerce/dash/menus", menus.value).then((res) => {
    console.log(res);
    getMenu();
    loading9.value = false;
    notifs.value.push({ type: "success", message: "Menu saved" });
  });
}

function addHereMain(menu) {
  var index = menus.value.main_menu.indexOf(menu);
  var newId = Math.random().toString(36).substr(2, 9);
  menus.value.main_menu.splice(index + 1, 0, {
    name: "New Menu",
    link: "/home",
    new: true,
    id: newId,
  });
}

function addHereFooter(menu) {
  var index = menus.value.footer_menu.indexOf(menu);
  var newId = Math.random().toString(36).substr(2, 9);
  menus.value.footer_menu.splice(index + 1, 0, {
    name: "New Menu",
    link: "/home",
    new: true,
    id: newId,
  });
}

const pages = ref([]);
async function getPages() {
  const response = await Api.get("/api/ecommerce/dash/pages");
  pages.value = response.data;
}
getPages();
</script>

<style scoped>
.link-edit:hover .suggest {
  display: flex;
}
select {
  cursor: pointer;
}
</style>
