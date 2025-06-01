<script setup lang="ts">
const year = new Date().getFullYear()
</script>

<template>
  <footer
    class="dark:bg-muted-900 border-muted-200 dark:border-muted-700 relative border-t bg-white"
  >
    <NuxtLink
      to="/"
      class="dark:bg-muted-900 absolute inset-x-0 -top-4 mx-auto flex h-9 w-14 items-center justify-center bg-white"
    >
      <img class="h-10 md:h-12 object-contain" src="https://nextoxy.com/static/frontend/images/home/logo.png" alt="" srcset="">
    </NuxtLink>
    <div
      class="ltablet:flex-row mx-auto flex max-w-7xl flex-col items-center justify-between px-6 py-8 lg:flex-row"
    >
      <NuxtLink
        to="/"
        aria-label="Go to Tairo homepage"
        class="ltablet:w-1/5 block w-full lg:w-1/5"
      >
        <img class="h-10 md:h-12 object-contain" src="https://nextoxy.com/static/frontend/images/home/logo.png" alt="" srcset="">
      </NuxtLink>
      <div
        class="ltablet:mt-0 ltablet:gap-6 mt-6 flex flex-wrap items-center justify-center gap-4 lg:mt-0 lg:gap-6"
      >
        <NuxtLink
          to="/privacy-policy"
          class="text-muted-600 hover:text-primary-500 dark:text-muted-200 dark:hover:text-primary-400 text-sm transition-colors duration-300"
        >
          Privacy Policy
        </NuxtLink>

        <NuxtLink
          to="/terms-of-service"
          class="text-muted-600 hover:text-primary-500 dark:text-muted-200 dark:hover:text-primary-400 text-sm transition-colors duration-300"
        >
          Terms & Condition
        </NuxtLink>
        <NuxtLink
          to="/faq"
          rel="noopener"
          class="text-muted-600 hover:text-primary-500 dark:text-muted-200 dark:hover:text-primary-400 text-sm transition-colors duration-300"
        >
          FAQ
        </NuxtLink>
        <NuxtLink
          to="/aboutus"
          rel="noopener"
          class="text-muted-600 hover:text-primary-500 dark:text-muted-200 dark:hover:text-primary-400 text-sm transition-colors duration-300"
        >
          About Us
        </NuxtLink>
        <NuxtLink
          to="/affiliate"
          rel="noopener"
          class="text-muted-600 hover:text-primary-500 dark:text-muted-200 dark:hover:text-primary-400 text-sm transition-colors duration-300"
        >
          Affiliate
        </NuxtLink>
        <NuxtLink
          to="/business-formation"
          rel="noopener"
          class="text-muted-600 hover:text-primary-500 dark:text-muted-200 dark:hover:text-primary-400 text-sm transition-colors duration-300"
        >
          Business Formation
        </NuxtLink>
        <NuxtLink
          to="/contactus"
          rel="noopener"
          class="text-muted-600 hover:text-primary-500 dark:text-muted-200 dark:hover:text-primary-400 text-sm transition-colors duration-300"
        >
          Contact Us
        </NuxtLink>
      </div>
    </div>
      <div class="text-muted-500 text-center dark:text-muted-400 flex w-full items-center justify-center text-sm mb-12" >
        <span>
          © NextOxy
          <NuxtLink
            to="/"
            rel="noopener"
            class="text-muted-600 hover:text-primary-500 dark:text-muted-200 dark:hover:text-primary-400 text-sm transition-colors duration-300"
          >
          . All rights reserved 
          </NuxtLink>
          2022-{{ year }}.
        </span>
      </div>
  </footer>
</template>
