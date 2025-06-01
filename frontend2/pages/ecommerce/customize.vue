<template>
  <section
    class="w-full dark:bg-slate-800 text-slate-700 dark:text-white text-xs"
  >
    <!-- topbar  -->
    <div
      class="w-full flex justify-between items-center py-4 px-3 h-[60px] border-b border-slate-200 bg-slate-50 dark:bg-slate-900"
    >
      <div
        class="flex gap-1 justify-center items-center pb-2"
        style="width: 180px"
      >
        <nuxt-link to="/ecommerce/">
          <img
            src="/static/frontend/images/logo.png"
            alt=""
            srcset=""
            vertical-align="middle"
            class="h-6"
          />
        </nuxt-link>
        <h5 class="text-center my-1 text-xl">Oxy Editor</h5>
      </div>
      <div class="flex gap-1">
        <button class="px-2 py-1 bg-slate-100 dark:bg-slate-950">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="22"
            height="22"
            viewBox="0 0 24 24"
          >
            <path
              fill="currentColor"
              d="M21 2H3c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h7v2H9c-.55 0-1 .45-1 1s.45 1 1 1h6c.55 0 1-.45 1-1s-.45-1-1-1h-1v-2h7c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2zm-1 14H4c-.55 0-1-.45-1-1V5c0-.55.45-1 1-1h16c.55 0 1 .45 1 1v10c0 .55-.45 1-1 1z"
            />
          </svg>
        </button>
        <button
          @click="over = true"
          class="px-2 py-1 bg-slate-100 dark:bg-slate-950"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="22"
            height="22"
            viewBox="0 0 36 36"
          >
            <path
              fill="currentColor"
              d="M30 2H6a2 2 0 0 0-2 2v28a2 2 0 0 0 2 2h24a2 2 0 0 0 2-2V4a2 2 0 0 0-2-2ZM19 32h-2v-2h2ZM6 28V4h24v24Z"
              class="clr-i-solid clr-i-solid-path-1"
            />
            <path fill="none" d="M0 0h36v36H0z" />
          </svg>
        </button>
        <button class="px-2 py-1 bg-slate-100 dark:bg-slate-950">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="22"
            height="22"
            viewBox="0 0 24 24"
          >
            <path
              fill="currentColor"
              d="M17 1.01L7 1c-1.1 0-2 .9-2 2v18c0 1.1.9 2 2 2h10c1.1 0 2-.9 2-2V3c0-1.1-.9-1.99-2-1.99zM17 19H7V5h10v14z"
            />
          </svg>
        </button>
      </div>
      <div class="right">
        <nuxt-link to="/ecommerce/">
          <BaseButton color="primary">Close</BaseButton>
        </nuxt-link>
      </div>
    </div>

    <div class="w-full h-full flex">
      <!-- sidebar -->
      <div class="tools py-4 px-6" style="width: 250px">
        <nuxt-link to="/ecommerce/" class="w-full">
          <BaseButton class="w-full" color="primary"
            >Back to Dashboard</BaseButton
          >
        </nuxt-link>
        <div
          class="shop-pages whitespace-nowrap text-muted-500 dark:text-muted-300"
          v-if="shop?.package && shop?.package.id == 5"
        >
          <button
            @click="initiate('?edit=true')"
            :class="
              page === '?edit=true'
                ? 'text-primary'
                : 'text-[#374151] dark:text-white'
            "
            class="bg-transparent w-full shadow-none text-sm h-9 flex gap-2 items-center ml-4 mt-3"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="20"
              height="20"
              viewBox="0 0 24 24"
            >
              <path
                fill="currentColor"
                d="M12 3L1 11.4l1.21 1.59L4 11.62V21h16v-9.38l1.79 1.36L23 11.4L12 3zm6 16H6v-8.9l6-4.58l6 4.58V19zm-9-5c0 .55-.45 1-1 1s-1-.45-1-1s.45-1 1-1s1 .45 1 1zm3-1c.55 0 1 .45 1 1s-.45 1-1 1s-1-.45-1-1s.45-1 1-1zm3 1c0-.55.45-1 1-1s1 .45 1 1s-.45 1-1 1s-1-.45-1-1z"
              />
            </svg>
            Home Page
          </button>

          <button
            @click="initiate('/details/1?edit=true')"
            :class="
              page == '/details/1?edit=true'
                ? 'text-primary'
                : 'text-[#374151] dark:text-white'
            "
            class="bg-transparent w-full shadow-none text-sm h-9 flex gap-2 items-center ml-4"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="17"
              height="17"
              viewBox="0 0 48 48"
            >
              <g
                fill="none"
                stroke="currentColor"
                stroke-linejoin="round"
                stroke-width="4"
              >
                <rect width="36" height="36" x="6" y="6" rx="3" />
                <path d="M13 13h8v8h-8z" />
                <path
                  stroke-linecap="round"
                  d="M27 13h8m-8 7h8m-22 8h22m-22 7h22"
                />
              </g>
            </svg>
            Product Details Page
          </button>
          <button
            @click="initiate('/wishlist?edit=true')"
            :class="
              page == '/wishlist?edit=true'
                ? 'text-primary'
                : 'text-[#374151] dark:text-white'
            "
            class="bg-transparent w-full shadow-none text-sm h-9 flex gap-2 items-center ml-4"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="20"
              height="20"
              viewBox="0 0 24 24"
            >
              <path
                fill="currentColor"
                d="M16.5 3c-1.74 0-3.41.81-4.5 2.09C10.91 3.81 9.24 3 7.5 3C4.42 3 2 5.42 2 8.5c0 3.78 3.4 6.86 8.55 11.54L12 21.35l1.45-1.32C18.6 15.36 22 12.28 22 8.5C22 5.42 19.58 3 16.5 3zm-4.4 15.55l-.1.1l-.1-.1C7.14 14.24 4 11.39 4 8.5C4 6.5 5.5 5 7.5 5c1.54 0 3.04.99 3.57 2.36h1.87C13.46 5.99 14.96 5 16.5 5c2 0 3.5 1.5 3.5 3.5c0 2.89-3.14 5.74-7.9 10.05z"
              />
            </svg>
            Wishlist Page
          </button>
          <button
            @click="initiate('/cart?edit=true')"
            :class="
              page == '/cart?edit=true'
                ? 'text-primary'
                : 'text-[#374151] dark:text-white'
            "
            class="bg-transparent w-full shadow-none text-sm h-9 flex gap-2 items-center ml-4"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="20"
              height="20"
              viewBox="0 0 24 24"
            >
              <path
                fill="currentColor"
                d="M17 18a2 2 0 0 1 2 2a2 2 0 0 1-2 2a2 2 0 0 1-2-2c0-1.11.89-2 2-2M1 2h3.27l.94 2H20a1 1 0 0 1 1 1c0 .17-.05.34-.12.5l-3.58 6.47c-.34.61-1 1.03-1.75 1.03H8.1l-.9 1.63l-.03.12a.25.25 0 0 0 .25.25H19v2H7a2 2 0 0 1-2-2c0-.35.09-.68.24-.96l1.36-2.45L3 4H1V2m6 16a2 2 0 0 1 2 2a2 2 0 0 1-2 2a2 2 0 0 1-2-2c0-1.11.89-2 2-2m9-7l2.78-5H6.14l2.36 5H16Z"
              />
            </svg>
            Cart Page
          </button>
          <button
            @click="initiate('/my_account?edit=true')"
            :class="
              page == '/my_account?edit=true'
                ? 'text-primary'
                : 'text-[#374151] dark:text-white'
            "
            class="bg-transparent w-full shadow-none text-sm h-9 flex gap-2 items-center ml-4"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="20"
              height="20"
              viewBox="0 0 24 24"
            >
              <path
                fill="currentColor"
                d="M5 17.85q1.35-1.325 3.138-2.087T12 15q2.075 0 3.863.763T19 17.85V5H5v12.85ZM12 13q1.45 0 2.475-1.025T15.5 9.5q0-1.45-1.025-2.475T12 6q-1.45 0-2.475 1.025T8.5 9.5q0 1.45 1.025 2.475T12 13Zm-7 8q-.825 0-1.413-.588T3 19V5q0-.825.588-1.413T5 3h14q.825 0 1.413.588T21 5v14q0 .825-.588 1.413T19 21H5Zm2-2h10v-.25q-1.05-.875-2.325-1.313T12 17q-1.4 0-2.675.438T7 18.75V19Zm5-8q-.625 0-1.063-.438T10.5 9.5q0-.625.438-1.063T12 8q.625 0 1.063.438T13.5 9.5q0 .625-.438 1.063T12 11Zm0 .425Z"
              />
            </svg>
            Account Page
          </button>
          <button
            @click="initiate('/contact_us?edit=true')"
            :class="
              page == '/contact_us?edit=true'
                ? 'text-primary'
                : 'text-[#374151] dark:text-white'
            "
            class="bg-transparent w-full shadow-none text-sm h-9 flex gap-2 items-center ml-4"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="20"
              height="20"
              viewBox="0 0 24 24"
            >
              <g fill="none" stroke="currentColor" stroke-width="1.5">
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  d="M7 12h10M7 8h6"
                />
                <path
                  d="M3 20.29V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2H7.961a2 2 0 0 0-1.561.75l-2.331 2.914A.6.6 0 0 1 3 20.29Z"
                />
              </g>
            </svg>
            Contact Page
          </button>
          <button
            @click="initiate('/tracking?edit=true')"
            :class="
              page == '/tracking?edit=true'
                ? 'text-primary'
                : 'text-[#374151] dark:text-white'
            "
            class="bg-transparent w-full shadow-none text-sm h-9 flex gap-2 items-center ml-4"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="20"
              height="20"
              viewBox="0 0 24 24"
            >
              <path
                fill="currentColor"
                d="M20 8h-3V4H3c-1.1 0-2 .9-2 2v11h2c0 1.66 1.34 3 3 3s3-1.34 3-3h6c0 1.66 1.34 3 3 3s3-1.34 3-3h2v-5l-3-4zm-.5 1.5l1.96 2.5H17V9.5h2.5zM6 18c-.55 0-1-.45-1-1s.45-1 1-1s1 .45 1 1s-.45 1-1 1zm2.22-3c-.55-.61-1.33-1-2.22-1s-1.67.39-2.22 1H3V6h12v9H8.22zM18 18c-.55 0-1-.45-1-1s.45-1 1-1s1 .45 1 1s-.45 1-1 1z"
              />
            </svg>
            Tracking Page
          </button>
          <button
            @click="initiate('/signin?edit=true')"
            :class="
              page == '/signin?edit=true'
                ? 'text-primary'
                : 'text-[#374151] dark:text-white'
            "
            class="bg-transparent w-full shadow-none text-sm h-9 flex gap-2 items-center ml-4"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="20"
              height="20"
              viewBox="0 0 24 24"
            >
              <path
                fill="currentColor"
                d="M12 13q1.45 0 2.475-1.025Q15.5 10.95 15.5 9.5q0-1.45-1.025-2.475Q13.45 6 12 6q-1.45 0-2.475 1.025Q8.5 8.05 8.5 9.5q0 1.45 1.025 2.475Q10.55 13 12 13Zm0-2q-.625 0-1.062-.438q-.438-.437-.438-1.062t.438-1.062Q11.375 8 12 8t1.062.438q.438.437.438 1.062t-.438 1.062Q12.625 11 12 11Zm0 11.5L3 17V7l9-5.5L21 7v10Zm0-2.35l3.675-2.25q-.825-.425-1.75-.662Q13 17 12 17t-1.925.238q-.925.237-1.75.662Zm-5.6-3.425q1.2-.825 2.613-1.275Q10.425 15 12 15q1.575 0 2.988.45q1.412.45 2.612 1.275l1.4-.85v-7.75L12 3.85L5 8.125v7.75Zm5.6-6.45Z"
              />
            </svg>
            Signin/Signup Page
          </button>
        </div>
      </div>
      <!-- shop view  -->
      <div class="relative flex-1" style="height: calc(100vh - 60px)">
        <iframe
          class="border-[1px] border-t-0"
          :src="url"
          frameborder="0"
          style="
            overflow: hidden;
            overflow-x: hidden;
            overflow-y: hidden;
            height: 100%;
            width: 100%;
            position: relative;
            top: 0px;
            left: 0;
            right: 0px;
            bottom: 0px;
          "
          height="100%"
          width="100%"
        ></iframe>
        <div
          class="absolute z-10 top-40 left-[50%] translate-x-[-50%]"
          v-if="loading_iframe"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="32"
            height="32"
            viewBox="0 0 24 24"
          >
            <circle cx="12" cy="3" r="0" fill="currentColor">
              <animate
                id="svgSpinners6DotsScaleMiddle0"
                attributeName="r"
                begin="0;svgSpinners6DotsScaleMiddle2.end-0.5s"
                calcMode="spline"
                dur="0.6s"
                keySplines=".27,.42,.37,.99;.53,0,.61,.73"
                values="0;2;0"
              />
            </circle>
            <circle cx="16.5" cy="4.21" r="0" fill="currentColor">
              <animate
                id="svgSpinners6DotsScaleMiddle1"
                attributeName="r"
                begin="svgSpinners6DotsScaleMiddle0.begin+0.1s"
                calcMode="spline"
                dur="0.6s"
                keySplines=".27,.42,.37,.99;.53,0,.61,.73"
                values="0;2;0"
              />
            </circle>
            <circle cx="7.5" cy="4.21" r="0" fill="currentColor">
              <animate
                id="svgSpinners6DotsScaleMiddle2"
                attributeName="r"
                begin="svgSpinners6DotsScaleMiddle4.begin+0.1s"
                calcMode="spline"
                dur="0.6s"
                keySplines=".27,.42,.37,.99;.53,0,.61,.73"
                values="0;2;0"
              />
            </circle>
            <circle cx="19.79" cy="7.5" r="0" fill="currentColor">
              <animate
                id="svgSpinners6DotsScaleMiddle3"
                attributeName="r"
                begin="svgSpinners6DotsScaleMiddle1.begin+0.1s"
                calcMode="spline"
                dur="0.6s"
                keySplines=".27,.42,.37,.99;.53,0,.61,.73"
                values="0;2;0"
              />
            </circle>
            <circle cx="4.21" cy="7.5" r="0" fill="currentColor">
              <animate
                id="svgSpinners6DotsScaleMiddle4"
                attributeName="r"
                begin="svgSpinners6DotsScaleMiddle6.begin+0.1s"
                calcMode="spline"
                dur="0.6s"
                keySplines=".27,.42,.37,.99;.53,0,.61,.73"
                values="0;2;0"
              />
            </circle>
            <circle cx="21" cy="12" r="0" fill="currentColor">
              <animate
                id="svgSpinners6DotsScaleMiddle5"
                attributeName="r"
                begin="svgSpinners6DotsScaleMiddle3.begin+0.1s"
                calcMode="spline"
                dur="0.6s"
                keySplines=".27,.42,.37,.99;.53,0,.61,.73"
                values="0;2;0"
              />
            </circle>
            <circle cx="3" cy="12" r="0" fill="currentColor">
              <animate
                id="svgSpinners6DotsScaleMiddle6"
                attributeName="r"
                begin="svgSpinners6DotsScaleMiddle8.begin+0.1s"
                calcMode="spline"
                dur="0.6s"
                keySplines=".27,.42,.37,.99;.53,0,.61,.73"
                values="0;2;0"
              />
            </circle>
            <circle cx="19.79" cy="16.5" r="0" fill="currentColor">
              <animate
                id="svgSpinners6DotsScaleMiddle7"
                attributeName="r"
                begin="svgSpinners6DotsScaleMiddle5.begin+0.1s"
                calcMode="spline"
                dur="0.6s"
                keySplines=".27,.42,.37,.99;.53,0,.61,.73"
                values="0;2;0"
              />
            </circle>
            <circle cx="4.21" cy="16.5" r="0" fill="currentColor">
              <animate
                id="svgSpinners6DotsScaleMiddle8"
                attributeName="r"
                begin="svgSpinners6DotsScaleMiddlea.begin+0.1s"
                calcMode="spline"
                dur="0.6s"
                keySplines=".27,.42,.37,.99;.53,0,.61,.73"
                values="0;2;0"
              />
            </circle>
            <circle cx="16.5" cy="19.79" r="0" fill="currentColor">
              <animate
                id="svgSpinners6DotsScaleMiddle9"
                attributeName="r"
                begin="svgSpinners6DotsScaleMiddle7.begin+0.1s"
                calcMode="spline"
                dur="0.6s"
                keySplines=".27,.42,.37,.99;.53,0,.61,.73"
                values="0;2;0"
              />
            </circle>
            <circle cx="7.5" cy="19.79" r="0" fill="currentColor">
              <animate
                id="svgSpinners6DotsScaleMiddlea"
                attributeName="r"
                begin="svgSpinners6DotsScaleMiddleb.begin+0.1s"
                calcMode="spline"
                dur="0.6s"
                keySplines=".27,.42,.37,.99;.53,0,.61,.73"
                values="0;2;0"
              />
            </circle>
            <circle cx="12" cy="21" r="0" fill="currentColor">
              <animate
                id="svgSpinners6DotsScaleMiddleb"
                attributeName="r"
                begin="svgSpinners6DotsScaleMiddle9.begin+0.1s"
                calcMode="spline"
                dur="0.6s"
                keySplines=".27,.42,.37,.99;.53,0,.61,.73"
                values="0;2;0"
              />
            </circle>
          </svg>
        </div>
      </div>
    </div>

    <!-- Right Side Over -->
    <CommonOver :show="over">
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
          <div class="absolute top-0 -left-2 flex pt-4 pr-2 sm:-ml-10 sm:pr-4">
            <span
              type="button"
              class="rounded-full text-slate-600 shadow-xl bg-white cursor-pointer p-1"
              @click="over = false"
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
          class="flex h-full flex-col overflow-y-scroll bg-white py-6 shadow-xl"
        >
          <div class="px-4 sm:px-6">
            <DialogTitle class="text-base font-semibold leading-6 text-gray-900"
              >Panel title</DialogTitle
            >
          </div>
          <div class="relative mt-6 flex-1 px-4 sm:px-6">
            <!-- Your content -->
          </div>
        </div>
      </DialogPanel>
    </CommonOver>
  </section>
</template>

<script setup>
definePageMeta({
  layout: "editor",
});
import {
  Dialog,
  DialogPanel,
  DialogTitle,
  TransitionChild,
  TransitionRoot,
} from "@headlessui/vue";
const { shop, getShop } = useShop();
const Api = useApi();
const url = ref("");
const page = ref("?edit=true");
const loading_iframe = ref(true);
async function initiate(pg = "?edit=true") {
  loading_iframe.value = true;
  if (!shop.value || !shop.value.name) {
    await getShop();
  }
  if (Api.baseURL == "http://127.0.0.1:8000") {
    url.value = "http://" + shop.value.name + ".localhost:8000";
  } else {
    url.value = "https://" + shop.value.name + ".nextoxy.com";
  }
  page.value = pg;
  url.value += pg;
  setTimeout(() => {
    loading_iframe.value = false;
  }, 2000);
}
initiate();
const over = ref(false);
</script>

<style scoped>
.shop-pages button svg {
  opacity: 0.8;
}
</style>
