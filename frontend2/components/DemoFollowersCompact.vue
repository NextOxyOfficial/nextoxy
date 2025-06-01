<script setup lang="ts">
const followers = [
  {
    "data-nui-tooltip": "Clarke Smith",
    src: "/static/img/avatars/3.svg",
  },
  {
    "data-nui-tooltip": "John Rowner",
    src: "/static/img/avatars/6.svg",
  },
  {
    "data-nui-tooltip": "Maggie Pitts",
    src: "/static/img/avatars/9.svg",
  },
];
</script>

<template>
  <div>
    <div class="mb-4 flex items-center justify-between">
      <BaseHeading
        as="h3"
        size="sm"
        weight="semibold"
        lead="tight"
        class="text-muted-800 dark:text-white"
      >
        <span>Latest Reviews</span>
      </BaseHeading>
      <BaseAvatarGroup :avatars="followers" size="xs" :limit="3" />
    </div>
    <div>
      <BaseParagraph size="xs">
        <span class="text-muted-400">
          Great News!
          <NuxtLink
            to="#"
            class="text-primary-500 underline-offset-2 hover:underline"
          >
            Clarke
          </NuxtLink>
          ,
          <NuxtLink
            to="#"
            class="text-primary-500 underline-offset-2 hover:underline"
          >
            John
          </NuxtLink>
          and
          <NuxtLink
            to="#"
            class="text-primary-500 underline-offset-2 hover:underline"
          >
            Maggie
          </NuxtLink>
          think that NextOxy is an exceptional ecommerce online shop builder
          that offers stunning templates, an intuitive interface, and robust
          ecommerce functionalities.
        </span>
      </BaseParagraph>
    </div>
  </div>
</template>
