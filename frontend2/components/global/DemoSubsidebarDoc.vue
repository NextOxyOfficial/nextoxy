<script setup lang="ts">
const navigation = [
  {
    name: "Coming soon",
    children: [
      {
        name: "Api Notice",
        icon: "solar:soundwave-square-broken",
        to: "/documentation",
        exact: true,
      },
    ],
  },
];
</script>

<template>
  <TairoSubsidebar>
    <template #header>
      <TairoSubsidebarHeader />
    </template>

    <TairoSubsidebarMenu :navigation="navigation" />
  </TairoSubsidebar>
</template>
