<script setup lang="ts">
definePageMeta({
  title: 'The Nuxt & Tailwind CSS dashboard system',
  description:
    'Nuxt & Tailwind CSS dashboard system template that comes with 100+ prebuilt pages and 40+ custom UI components.',
  breadcrumb: {
    label: 'Tairo',
  },
  layout: 'landing',
})
const Api = useApi()
</script>

<template>
  <div class="mx-auto w-full max-w-7xl px-4 pt-24 md:pt-36">
    <EcommerceAllThemesPublic />
  </div>
</template>
