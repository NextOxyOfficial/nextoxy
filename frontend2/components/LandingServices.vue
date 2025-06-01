<template>
  <section class="mx-auto w-full max-w-7xl px-4 relative mt-32">
    <div class="mr-auto place-self-center lg:col-span-7 max-w-[780px] mx-auto">
      <p
        class="max-w-2xl mb-2 text-primary-500 lg:mb-3 md:text-base font-semibold w-full text-center"
      >
        All-in-One Management
      </p>
      <h1
        class="max-w-5xl mb-4 text-2xl font-semibold tracking-tight leading-tight md:text-5xl md:leading-tight text-muted-700 dark:text-muted-300 w-full text-center"
      >
        A comprehensive suite covering sales, profiling, and loss accounts,
        NextOxy Cloud simplifies business management.
      </h1>
    </div>
    <div
      class="w-full flex flex-col justify-center md:flex-row gap-4 md:gap-56 mt-12 items"
    >
      <div class="flex-1 max-w-[420px] mt-0 md:mt-12">
        <span
          class="p-5 !rounded-xl cursor-pointer block item"
          :class="{ 'active-item': active == 1 }"
          @click="active = 1"
        >
          <div class="flex items-center gap-3">
            <img
              class="w-10"
              src="/static/frontend/icons/abs-1.svg"
              alt="mockup"
            />
            <p class="font-bold text-muted-600 dark:text-muted-400">
              Ecommerce Simplified
            </p>
          </div>
          <div class="text text-muted-500 py-1">
            NextOxy Cloud streamlines ecommerce, dropshipping, and business
            operations for optimal efficiency.Real-time analytics empower
            businesses to make data-driven decisions for sustained and strong
            growth.
          </div>
        </span>
        <span
          class="p-5 !rounded-xl cursor-pointer block item"
          :class="{ 'active-item': active == 2 }"
          @click="active = 2"
        >
          <div class="flex items-center gap-3">
            <img
              class="w-10"
              src="/static/frontend/icons/abs-2.svg"
              alt="mockup"
            />
            <p class="font-bold text-muted-600 dark:text-muted-400">
              AI-Powered Precision
            </p>
          </div>
          <div class="text text-muted-500 py-1">
            NextOxy Cloud leverages AI for unparalleled precision in
            decision-making. From predictive analytics optimizing sales
            strategies to intelligent inventory management, businesses unlock
            new dimensions of efficiency and strategic insight.
          </div>
        </span>
        <span
          class="p-5 !rounded-xl cursor-pointer block item"
          :class="{ 'active-item': active == 3 }"
          @click="active = 3"
        >
          <div class="flex items-center gap-3">
            <img
              class="w-10"
              src="/static/frontend/icons/abs-3.svg"
              alt="mockup"
            />
            <p class="font-bold text-muted-600 dark:text-muted-400">
              Boosted Sales Performance
            </p>
          </div>
          <div class="text text-muted-500 py-1">
            Dynamic tools and AI-driven insights empower businesses to track,
            analyze, and enhance sales performance. Predictive analytics enable
            businesses to forecast trends, optimize pricing, and boost revenue.
          </div>
        </span>
        <span
          class="p-5 !rounded-xl cursor-pointer block item"
          :class="{ 'active-item': active == 4 }"
          @click="active = 4"
        >
          <div class="flex items-center gap-3">
            <img
              class="w-10"
              src="/static/frontend/icons/abs-4.svg"
              alt="mockup"
            />
            <p class="font-bold text-muted-600 dark:text-muted-400">
              Secure Profiling
            </p>
          </div>
          <div class="text text-muted-500 py-1">
            NextOxy Cloud ensures secure and scalable profile and loss
            management for confident, growth-focused decisions.It provides the
            financial clarity necessary for making informed decisions and
            steering the business towards long-term success.
          </div>
        </span>
      </div>
      <div
        class="flex-1 max-w-[550px] min-h-[300px] xs:min-h-[350px] sm:min-h-[550px] relative"
      >
        <span
          class="opacity-0 absolute"
          :class="{ '!opacity-100': active == 1 }"
        >
          <img
            class="dark:hidden max-w-[530px] w-full max-h-[450px] md:max-h-[550px]"
            src="/static/frontend/landing/services-light/1-min.png"
            alt="mockup"
          />
          <img
            class="hidden dark:block max-w-[530px] w-full max-h-[450px] md:max-h-[550px]"
            src="/static/frontend/landing/services-dark/1-min.png"
            alt="mockup"
          />
        </span>
        <span
          class="opacity-0 absolute"
          :class="{ '!opacity-100': active == 2 }"
        >
          <img
            class="dark:hidden max-w-[530px] w-full max-h-[450px] md:max-h-[550px]"
            src="/static/frontend/landing/services-light/2-min.png"
            alt="mockup"
          />
          <img
            class="hidden dark:block max-w-[530px] w-full max-h-[450px] md:max-h-[550px]"
            src="/static/frontend/landing/services-dark/2-min.png"
            alt="mockup"
          />
        </span>
        <span
          class="opacity-0 absolute"
          :class="{ '!opacity-100': active == 3 }"
        >
          <img
            class="dark:hidden max-h-[450px] md:max-h-[550px]"
            src="/static/frontend/landing/services-light/3-min.png"
            alt="mockup"
          />
          <img
            class="hidden dark:block max-w-[530px] w-full max-h-[450px] md:max-h-[550px]"
            src="/static/frontend/landing/services-dark/3-min.png"
            alt="mockup"
          />
        </span>
        <span
          class="opacity-0 absolute"
          :class="{ '!opacity-100': active == 4 }"
        >
          <img
            class="dark:hidden max-w-[530px] w-full max-h-[450px] md:max-h-[550px]"
            src="/static/frontend/landing/services-light/4-min.png"
            alt="mockup"
          />
          <img
            class="hidden dark:block max-w-[530px] w-full max-h-[450px] md:max-h-[550px]"
            src="/static/frontend/landing/services-dark/4-min.png"
            alt="mockup"
          />
        </span>
      </div>
    </div>
  </section>
</template>

<script setup>
const active = ref(1);
</script>

<style scoped>
.items .item {
  overflow: hidden;
  max-height: 65px;
  transition: all 0.2s ease-in-out;
  border: 1px solid rgba(128, 128, 128, 0);
}
.items .item img {
  filter: grayscale(1);
  transition: all 1s ease-in-out;
}
.items .active-item {
  border: 1px solid rgba(128, 128, 128, 0.1);
  max-height: 500px !important;
  margin: 10px 5px;
  box-shadow: 0px 0px 5px rgba(128, 128, 128, 0.1);
}
.items .active-item img {
  filter: grayscale(0) !important;
}
.items .active-item .text {
  display: block !important;
}
</style>
