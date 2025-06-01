<script setup lang="ts">
const navigation = [
  {
    name: 'Account Management',
    children: [
      {
        name: 'Services',
        icon: 'solar:soundwave-square-broken',
        icon2: 'noto-v1:fire',
        to: '/account',
        exact: true,
      },
      {
        name: 'Billing',
        icon: 'solar:card-2-broken',
        to: '/account/billing',
      },
      {
        name: 'General Info',
        icon: 'solar:user-id-broken',
        to: '/account/settings',
      },
      {
        name: 'Password Settings',
        icon: 'solar:key-minimalistic-square-2-broken',
        to: '/account/password',
      },
      // {
      //   name: 'Access Management',
      //   icon: 'solar:users-group-two-rounded-broken',
      //   to: '/account/access',
      // },
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
