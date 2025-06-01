<template>
  <section class="bg-[#050b0c] text-white mt-16 py-16 px-2 md:px-4">
    <img
      class="w-full h-full max-w-5xl left-[50%] translate-x-[-50%] object-contain absolute z-[1] opacity-50"
      src="/static/frontend/landing/map.svg"
      alt="mockup"
    />
    <div
      class="grid max-w-7xl mx-auto lg:gap-8 xl:gap-0 lg:grid-cols-12 relative z-10"
    >
      <div class="mr-auto place-self-center lg:col-span-7 max-w-[580px] z-10">
        <p
          class="max-w-2xl mb-2 text-primary-500 lg:mb-3 md:text-base font-semibold"
        >
          Trusted by Diverse Businesses
        </p>
        <h1
          class="max-w-2xl mb-4 text-2xl font-semibold tracking-tight leading-tight md:text-3xl"
        >
          Our global footprint is a testament to the trust bestowed upon us by a
          diverse range of businesses.
        </h1>
        <p class="max-w-2xl mb-6 font-light lg:mb-8 text-slate-400">
          From startups to established enterprises, NextOxy Cloud has earned the
          confidence of businesses across industries, attesting to the
          adaptability and reliability ingrained in our services.
        </p>
        <nuxt-link
          to="/plugins"
          class="max-w-2xl mb-2 text-primary-500 lg:mb-3 md:text-base font-semibold flex gap-2 items-center hover:gap-3"
        >
          <span> Learn more</span>
          <Icon
            name="material-symbols:line-end-arrow-notch-rounded"
            class="me-2 h-5 w-5"
          />
        </nuxt-link>
      </div>
      <div class="mt-12 lg:mt-0 lg:col-span-5 lg:flex">
        <img
          class=""
          src="/static/frontend/landing/overview-image.webp"
          alt="mockup"
        />
      </div>
    </div>
    <div class="max-w-7xl mx-auto mt-8 z-10 relative">
      <hr class="mb-16" />
      <p
        class="max-w-3xl mb-2 text-primary-500 lg:mb-3 md:text-base font-semibold"
      >
        Global Reach, Local Impact
      </p>
      <h1
        class="max-w-3xl mb-4 text-2xl font-semibold tracking-tight leading-tight md:text-3xl"
      >
        NextOxy Cloud transcends borders, fostering a global presence that
        resonates with businesses worldwide.
      </h1>
      <p class="max-w-3xl mb-6 font-light lg:mb-8 text-slate-400">
        Our platform's adaptability ensures that whether a business operates in
        bustling metropolises or remote corners of the world, NextOxy Cloud's
        seamless services remain a reliable foundation for success.
      </p>
      <div
        class="w-full flex flex-col md:flex-row flex-wrap gap-3"
        ref="target"
      >
        <div class="flex-1">
          <h2 class="text-3xl md:text-5xl font-bold my-3">{{ users }}K+</h2>
          <p>Of global users</p>
        </div>
        <div class="flex-1">
          <h2 class="text-3xl md:text-5xl font-bold my-3">${{ sales }}M+</h2>
          <p>Of annual sales processed</p>
        </div>
        <div class="flex-1">
          <h2 class="text-3xl md:text-5xl font-bold my-3">{{ countries }}+</h2>
          <p>Countries covered</p>
        </div>
        <div class="flex-1">
          <h2 class="text-3xl md:text-5xl font-bold my-2">
            <Icon
              name="ph:infinity-bold"
              class="text-white h-10 md:h-14 w-10 md:w-14"
            />
          </h2>
          <p>Unlimited theme access</p>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
const target = ref(null);
const users = ref(0);
const sales = ref(0);
const countries = ref(0);
const targetIsVisible = ref(false);
const { stop } = useIntersectionObserver(
  target,
  ([{ isIntersecting }], observerElement) => {
    targetIsVisible.value = isIntersecting;
    if (!isIntersecting) {
      users.value = 0;
      sales.value = 0;
      countries.value = 0;
    } else {
      startIncrement();
    }
  }
);
async function startIncrement() {
  incrementValue(users, 250, 3000);
  incrementValue(sales, 16, 3000);
  incrementValue(countries, 193, 3000);
}

async function incrementValue(valueRef, targetValue, duration) {
  const incrementAmount = 1;
  const totalIncrements = targetValue / incrementAmount;
  const incrementInterval = duration / totalIncrements;

  return new Promise((resolve) => {
    const intervalId = setInterval(() => {
      valueRef.value += incrementAmount;

      if (valueRef.value >= targetValue) {
        clearInterval(intervalId);
        resolve();
      }
    }, incrementInterval);
  });
}
</script>

<style scoped></style>
