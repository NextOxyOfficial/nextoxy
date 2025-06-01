<script setup lang="ts">
const navigation = [
  {
    name: 'Account Management',
    children: [
      {
        name: 'New Ticket',
        icon: 'solar:card-2-broken',
        to: '/support/new',
      },
      {
        name: 'Tickets',
        icon: 'solar:card-2-broken',
        to: '/support',
      },
    ],
  },
]
</script>

<template>
  <TairoSubsidebar>
    <template #header>
      <TairoSubsidebarHeader />
    </template>

    <TairoSubsidebarMenu :navigation="navigation" />
  </TairoSubsidebar>
</template>
