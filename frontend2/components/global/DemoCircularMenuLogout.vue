<template>
  <NuxtLink
    @click="logOutUser"
    class="inline-flex h-9 w-9 items-center justify-center rounded-full transition-all duration-300 cursor-pointer"
  >
    <span
      class="bg-primary-700 flex h-9 w-9 items-center justify-center rounded-full"
    >
      <Icon name="ion:ios-log-out" class="h-5 w-5 text-white" />
    </span>
  </NuxtLink>
</template>

<script setup>
const { user, logout } = useAuth()
function logOutUser() {
  logout()
  navigateTo('/')  
}
</script>
