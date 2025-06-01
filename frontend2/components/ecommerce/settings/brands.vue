<template>
  <section class="pb-16">
    <div class="container mx-auto">
      <div class="py-3 px-4 mb-4 sm:flex sm:items-center sm:justify-between">
        <h3 class="text-lg font-medium leading-6">Brands</h3>
        <div class="mt-3 sm:mt-0 sm:ml-4">
          <BaseButton
            color="primary"
            @click="form = true"
            type="submit"
            class="inline-flex gap-2 justify-center rounded-md border border-transparent bg-gray-800 py-2 px-4 text-sm font-medium text-white -sm hover:bg-gray-900 focus:outline-none focus:ring-2 focus:ring-gray-900 focus:ring-offset-2"
          >
            + Add
          </BaseButton>
        </div>
      </div>
      <div
        v-if="form"
        class="border-b bg-slate-50 dark:bg-slate-700 dark:border-slate-950 border-gray-200 py-3 px-4 mb-4 sm:flex sm:items-center justify-start gap-2"
      >
        <span v-if="newBrand.image" class="relative">
          <svg
            @click="newBrand.image = ''"
            class="absolute -top-1 -left-1 text-rose-400 bg-rose-50 p-1 shadow-lg hover:shadow-xl cursor-pointer"
            xmlns="http://www.w3.org/2000/svg"
            width="22"
            height="22"
            viewBox="0 0 24 24"
          >
            <path
              fill="currentColor"
              d="m9.4 16.5l2.6-2.6l2.6 2.6l1.4-1.4l-2.6-2.6L16 9.9l-1.4-1.4l-2.6 2.6l-2.6-2.6L8 9.9l2.6 2.6L8 15.1ZM5 21V6H4V4h5V3h6v1h5v2h-1v15Zm2-2h10V6H7ZM7 6v13Z"
            />
          </svg>
          <img
            :src="newBrand.image"
            alt=""
            srcset=""
            class="w-12 h-12 object-cover rounded"
          />
        </span>
        <span v-else>
          <input
            type="file"
            class="hidden"
            id="fileUploader"
            @change="uploadBrandImage"
          />
          <label
            for="fileUploader"
            class="w-12 h-10 border border-slate-400 text-slate-500 flex flex-col gap-1 justify-center items-center text-sm p-1 rounded cursor-pointer"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="20"
              height="20"
              class="text-slate-500"
              viewBox="0 0 48 48"
            >
              <g fill="none">
                <path
                  fill="#000"
                  d="M44 24C44 22.8954 43.1046 22 42 22C40.8954 22 40 22.8954 40 24H44ZM24 8C25.1046 8 26 7.10457 26 6C26 4.89543 25.1046 4 24 4V8ZM39 40H9V44H39V40ZM8 39V9H4V39H8ZM40 24V39H44V24H40ZM9 8H24V4H9V8ZM9 40C8.44772 40 8 39.5523 8 39H4C4 41.7614 6.23857 44 9 44V40ZM39 44C41.7614 44 44 41.7614 44 39H40C40 39.5523 39.5523 40 39 40V44ZM8 9C8 8.44772 8.44771 8 9 8V4C6.23858 4 4 6.23857 4 9H8Z"
                />
                <path
                  stroke="#000"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="4"
                  d="M6 35L16.6931 25.198C17.4389 24.5143 18.5779 24.4953 19.3461 25.1538L32 36"
                />
                <path
                  stroke="#000"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="4"
                  d="M28 31L32.7735 26.2265C33.4772 25.5228 34.5914 25.4436 35.3877 26.0408L42 31"
                />
                <path
                  stroke="#000"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="4"
                  d="M37 18L37 6"
                />
                <path
                  stroke="#000"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="4"
                  d="M32 11L37 6L42 11"
                />
              </g>
            </svg>
          </label>
        </span>
        <input
          v-model="newBrand.name"
          type="text"
          class="block max-w-xs w-full border border-gray-300 dark:text-slate-200 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
          placeholder="Brand Name"
        />

        <BaseButton
          color="primary"
          @click="addBrand"
          type="submit"
          class="inline-flex gap-2 justify-center rounded-md border border-transparent bg-gray-800 py-2 px-4 text-sm font-medium text-white -sm hover:bg-gray-900 focus:outline-none focus:ring-2 focus:ring-gray-900 focus:ring-offset-2"
        >
          + Add
        </BaseButton>
        <button
          @click="form = false"
          type="button"
          class="inline-flex items-center rounded-md border shadow bg-slate-100 px-4 py-2 text-sm font-medium text-slate-700 hover:bg-slate-200 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2"
        >
          Cancel
        </button>
      </div>
      <p v-if="showError" class="text-red-500">Fill both the fields</p>
      <div class="mx-auto flex flex-wrap items-center justify-start p-4 gap-2">
        <div
          class="flex h-[110px] w-[188px] items-center justify-center px-5 pb-4 shadow relative cursor-pointer all-brand"
          v-for="brand in brands"
          :key="brand.id"
        >
          <img
            :src="Api.baseURL + brand.image"
            alt="image"
            class="h-10 max-w-full"
          />
          <span
            class="edit-btn hidden absolute bottom-0 right-0 w-full h-full z-50 justify-center gap-3 bg-slate-50/60"
          >
            <span
              @click="updatingBrand(brand)"
              class="flex justify-center items-center font-bold text-slate-800 text-sm hover:text-shadow"
            >
              <svg
                class="p-2 bg-lime-100 hover:shadow rounded"
                xmlns="http://www.w3.org/2000/svg"
                width="34"
                height="34"
                viewBox="0 0 24 24"
              >
                <path
                  fill="currentColor"
                  d="M5 19h1.4l8.625-8.625l-1.4-1.4L5 17.6ZM19.3 8.925l-4.25-4.2l1.4-1.4q.575-.575 1.413-.575q.837 0 1.412.575l1.4 1.4q.575.575.6 1.388q.025.812-.55 1.387ZM4 21q-.425 0-.712-.288Q3 20.425 3 20v-2.825q0-.2.075-.387q.075-.188.225-.338l10.3-10.3l4.25 4.25l-10.3 10.3q-.15.15-.337.225q-.188.075-.388.075ZM14.325 9.675l-.7-.7l1.4 1.4Z"
                />
              </svg>
            </span>
            <span
              @click="deleteBrand(brand)"
              class="flex justify-center items-center font-bold text-slate-800 text-sm hover:text-shadow"
            >
              <svg
                v-if="!loading5"
                class="p-2 bg-rose-100 hover:shadow rounded"
                xmlns="http://www.w3.org/2000/svg"
                width="34"
                height="34"
                viewBox="0 0 24 24"
              >
                <path
                  fill="currentColor"
                  d="M6 19c0 1.1.9 2 2 2h8c1.1 0 2-.9 2-2V7H6v12zM8 9h8v10H8V9zm7.5-5l-1-1h-5l-1 1H5v2h14V4h-3.5z"
                />
              </svg>
              <svg
                v-else
                class="p-2 bg-rose-100 hover:shadow rounded"
                xmlns="http://www.w3.org/2000/svg"
                width="34"
                height="34"
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
            </span>
          </span>
          <span
            class="absolute bottom-0 right-0 w-full px-2 py-0 bg-slate-300/25 text-center"
            >{{ brand.name }}</span
          >
        </div>
      </div>
    </div>
    <CommonOver :show="update != ''">
      <DialogPanel
        class="pointer-events-auto relative w-screen max-w-lg bg-slate-50 dark:bg-slate-700"
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
          <div class="absolute top-0 -left-2 flex pt-4 pr-2 sm:-ml-10 sm:pr-4">
            <span
              type="button"
              class="bg-slate-50 dark:bg-slate-700 rounded-full text-slate-600 dark:text-slate-100 shadow-xl hover:text-slate-500 cursor-pointer p-1"
              @click="update = false"
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
          class="flex h-full flex-col overflow-y-scroll py-6 shadow-xl"
          v-if="update"
        >
          <div class="px-4 sm:px-6">
            <DialogTitle class="text-base font-semibold leading-6 text-center"
              >Update Brand: {{ update.name }}</DialogTitle
            >
          </div>
          <div class="relative mt-6 flex-1 px-4 sm:px-6">
            <div
              class="py-3 px-2 mb-4 flex sm:items-center justify-start gap-2 rounded"
            >
              <span v-if="update.newimage" class="relative px-4">
                <svg
                  @click="update.newimage = ''"
                  class="absolute -top-1 left-3 text-rose-400 bg-rose-50 p-1 shadow-lg hover:shadow-xl cursor-pointer"
                  xmlns="http://www.w3.org/2000/svg"
                  width="22"
                  height="22"
                  viewBox="0 0 24 24"
                >
                  <path
                    fill="currentColor"
                    d="m9.4 16.5l2.6-2.6l2.6 2.6l1.4-1.4l-2.6-2.6L16 9.9l-1.4-1.4l-2.6 2.6l-2.6-2.6L8 9.9l2.6 2.6L8 15.1ZM5 21V6H4V4h5V3h6v1h5v2h-1v15Zm2-2h10V6H7ZM7 6v13Z"
                  />
                </svg>
                <img
                  :src="update.newimage"
                  alt=""
                  srcset=""
                  class="w-12 h-12 object-cover rounded"
                />
              </span>
              <span v-else-if="update.image" class="relative px-4">
                <svg
                  @click="update.image = ''"
                  class="absolute -top-1 left-3 text-rose-400 bg-rose-50 p-1 shadow-lg hover:shadow-xl cursor-pointer"
                  xmlns="http://www.w3.org/2000/svg"
                  width="22"
                  height="22"
                  viewBox="0 0 24 24"
                >
                  <path
                    fill="currentColor"
                    d="m9.4 16.5l2.6-2.6l2.6 2.6l1.4-1.4l-2.6-2.6L16 9.9l-1.4-1.4l-2.6 2.6l-2.6-2.6L8 9.9l2.6 2.6L8 15.1ZM5 21V6H4V4h5V3h6v1h5v2h-1v15Zm2-2h10V6H7ZM7 6v13Z"
                  />
                </svg>
                <img
                  :src="Api.baseURL + update.image"
                  alt=""
                  srcset=""
                  class="w-12 h-12 object-cover rounded"
                />
              </span>
              <span v-else>
                <input
                  type="file"
                  class="hidden"
                  id="fileUploader2"
                  @change="updateBrandImage"
                />
                <label
                  for="fileUploader2"
                  @click="uploader = true"
                  class="w-12 h-12 flex flex-col gap-1 justify-center items-center text-sm p-1 rounded text-slate-400 cursor-pointer"
                >
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    width="32"
                    height="22"
                    viewBox="0 0 2048 2048"
                  >
                    <path
                      fill="currentColor"
                      d="M1408 576q0-26 19-45t45-19q26 0 45 19t19 45q0 26-19 45t-45 19q-26 0-45-19t-19-45zm640 960v128h-256v256h-128v-256h-256v-128h256v-256h128v256h256zM922 1216l358 357v91H0V256h1792v896h-128V384H128v421l192-191l512 512l256-256l448 447v91h-91l-357-358l-166 166zM320 794L128 987v549h933L320 794z"
                    />
                  </svg>
                </label>
              </span>
              <input
                v-model="update.name"
                type="text"
                class="block max-w-xs w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                placeholder="Main Category"
              />
            </div>
            <div class="flex gap-1 mt-7">
              <BaseButton @click="saveBrand" color="primary"
                >Save Changes</BaseButton
              >
              <BaseButton @click="update = ''" color="danger"
                >Cancel</BaseButton
              >
            </div>
          </div>
        </div>
      </DialogPanel>
    </CommonOver>
  </section>
</template>

<script setup>
import {
  Dialog,
  DialogPanel,
  DialogTitle,
  TransitionChild,
  TransitionRoot,
} from "@headlessui/vue";
const { $swal } = useNuxtApp();
const { notifs } = useAuth();
const Api = useApi();
const form = ref(false);
const newBrand = ref({
  name: "",
  image: "",
});
const brands = ref([]);
const showError = ref(false);
function getBrands() {
  Api.get("/api/ecommerce/dash/brands").then((res) => {
    brands.value = res.data;
  });
}
getBrands();
const uploadBrandImage = (e) => {
  const file = e.target.files[0];
  const reader = new FileReader();
  reader.readAsDataURL(file);
  reader.onload = () => {
    newBrand.value.image = reader.result;
  };
};
const addBrand = () => {
  console.log(newBrand.value);
  if (!newBrand.value.name || !newBrand.value.image) {
    showError.value = true;
    notifs.value.push({
      type: "error",
      title: "Fill all fields",
      message: "Please fill brand name and brand image",
    });
    return;
  }
  Api.post("/api/ecommerce/dash/brands", newBrand.value).then((res) => {
    form.value = false;
    newBrand.value = {
      name: "",
      image: "",
    };
    showError.value = false;
    notifs.value.push({
      type: "success",
      message: "Brand added successfully",
    });
    getBrands();
  });
};
const update = ref("");
function updatingBrand(brand) {
  update.value = JSON.parse(JSON.stringify(brand));
}
function updateBrandImage(e) {
  const file = e.target.files[0];
  const reader = new FileReader();
  reader.readAsDataURL(file);
  reader.onload = () => {
    update.value.newimage = reader.result;
  };
}
function saveBrand() {
  Api.put("/api/ecommerce/dash/brands", update.value).then((res) => {
    getBrands();
    update.value = "";
    notifs.value.push({
      type: "success",
      message: "Brand updated successfully",
    });
  });
}

const loading5 = ref(false);
function deleteBrand(brand) {
  loading5.value = true;
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
    .then((result) => {
      if (result.isConfirmed) {
        Api.del("/api/ecommerce/dash/brands?id=" + brand.id).then((res) => {
          loading5.value = false;
          notifs.value.push({
            type: "success",
            message: "Brand deleted successfully",
          });
          getBrands();
        });
      }
    });
}
</script>

<style scoped>
.all-brand:hover .edit-btn {
  display: flex;
}
</style>
