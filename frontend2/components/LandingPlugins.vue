<template>
  <section class="mx-auto w-full max-w-7xl px-4 relative mt-32">
    <div
      class="grid max-w-screen-xl p-8 mx-auto lg:gap-8 xl:gap-0 lg:p-16 lg:grid-cols-12 !rounded-3xl !bg-[#faf5ff] dark:!bg-[#1B1B36] relative"
      shape="rounded-6xl"
    >
      <span
        class="px-4 py-3 border border-slate-700/20 rounded-xl absolute bg-[#ffffff] dark:bg-[#222244] left-[10%] top-0 translate-y-[-50%]"
        >Start Today
        <Icon name="openmoji:ok-hand" class="me-2 h-5 w-5" />
      </span>
      <div class="mr-auto place-self-center lg:col-span-7 max-w-[580px]">
        <p
          class="max-w-2xl mb-2 text-primary-500 lg:mb-3 text-sm md:text-base font-semibold"
        >
          INTRODUCING PLUGINS
        </p>
        <h1
          class="max-w-2xl mb-4 text-2xl font-semibold tracking-tight leading-tight md:text-3xl text-muted-700 dark:text-muted-300"
        >
          Explore, Choose, and Transform with NextOxys' Robust Plugin System
        </h1>
        <p
          class="max-w-2xl mb-6 font-light lg:mb-8 text-muted-600 dark:text-muted-400"
        >
          Our Plugin Hub is designed to empower your online presence, offering a
          myriad of plugins to cater to every aspect of your website. From
          seamless payment gateways to insightful site analysis and a plethora
          of useful tools
        </p>
        <nuxt-link
          to="/plugins"
          class="max-w-2xl mb-2 text-primary-500 lg:mb-3 text-sm md:text-base font-semibold flex gap-2 items-center hover:gap-3"
        >
          <span> Learn more about plugins</span>
          <Icon
            name="material-symbols:line-end-arrow-notch-rounded"
            class="me-2 h-5 w-5"
          />
        </nuxt-link>
      </div>
      <div class="mt-12 lg:mt-0 lg:col-span-5 lg:flex">
        <img
          class="dark:hidden"
          src="/static/frontend/images/landing-plugins.png"
          alt="mockup"
        />
        <img
          class="hidden dark:block"
          src="/static/frontend/images/landing-plugins-dark.png"
          alt="mockup"
        />
      </div>
    </div>
  </section>
</template>

<script setup></script>

<style scoped></style>
