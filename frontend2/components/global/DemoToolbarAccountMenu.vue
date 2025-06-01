<script setup lang="ts">
import { Menu, MenuButton, MenuItem, MenuItems } from '@headlessui/vue'
const { user, logout } = useAuth()
function logOutUser() {
  logout()
  navigateTo('/')  
}
</script>

<template>
  <div class="group inline-flex items-center justify-center text-right" v-if="user">
    <Menu as="div" class="relative h-9 w-9 text-left" v-slot="{ close }">
      <MenuButton as="template">
        <button
          type="button"
          class="bg-white dark:bg-slate-700/50 border border-slate-300/30 ring-muted-200 dark:ring-muted-700 dark:ring-offset-muted-900 inline-flex h-9 w-9 items-center justify-center rounded-full ring-1 ring-transparent transition-all duration-300 ring-offset-4"
        >
          <div
            class="relative inline-flex h-9 w-9 items-center justify-center rounded-full"
          >
            <Icon name="ic:twotone-manage-accounts" class="text-muted-400 h-5 w-5" />
          </div>
        </button>
      </MenuButton>

      <Transition
        enter-active-class="transition duration-100 ease-out"
        enter-from-class="transform scale-95 opacity-0"
        enter-to-class="transform scale-100 opacity-100"
        leave-active-class="transition duration-75 ease-in"
        leave-from-class="transform scale-100 opacity-100"
        leave-to-class="transform scale-95 opacity-0"
      >
        <MenuItems
          class="divide-muted-100 border-muted-200 dark:divide-muted-700 dark:border-muted-700 dark:bg-muted-800 absolute end-0 mt-2 w-64 origin-top-right divide-y rounded-md border bg-white shadow-lg focus:outline-none"
        >
          <div class="p-6 text-center">
            <div
              class="relative mx-auto flex h-20 w-20 items-center justify-center rounded-full"
            >
              <img
                src="/static/img/avatars/1.svg"
                class="max-w-full rounded-full object-cover shadow-sm dark:border-transparent"
                alt=""
              />
            </div>
            <div class="mt-3">
              <h6
                class="font-heading text-muted-800 text-sm font-medium dark:text-white"
              >
                {{user.first_name}} {{user.last_name}}
              </h6>
              <p class="text-muted-400 mb-4 font-sans text-xs">{{ user.email }}</p>
            </div>
          </div>
          <div class="px-6 py-1.5">
            <MenuItem as="div" v-slot="{ active }">
              <NuxtLink
                to="/account"
                class="!bg-transparrent  flex w-full items-center rounded-md p-2 text-sm transition-colors duration-300"
                @click.passive="close">
                  <h6 class="font-heading text-muted-800 text-xs leading-none dark:text-white flex gap-1 items-center">
                     <Icon name="icon-park-twotone:dashboard-one" class="text-muted-400 dark:text-muted-500 block h-4 w-4" />
                      My Dashboard
                  </h6>
              </NuxtLink>
              <NuxtLink
                to="/account/settings"
                class="!bg-transparrent  flex w-full items-center rounded-md p-2 text-sm transition-colors duration-300"
                @click.passive="close">
                  <h6 class="font-heading text-muted-800 text-xs leading-none dark:text-white flex gap-1 items-center">
                     <Icon name="material-symbols:settings-outline" class="text-muted-400 dark:text-muted-500 block h-4 w-4" />
                      Settings
                  </h6>
              </NuxtLink>
                            <NuxtLink
                to="/account/billing"
                class="!bg-transparrent  flex w-full items-center rounded-md p-2 text-sm transition-colors duration-300"
                @click.passive="close">
                  <h6 class="font-heading text-muted-800 text-xs leading-none dark:text-white flex gap-1 items-center">
                     <Icon name="ph:credit-card" class="text-muted-400 dark:text-muted-500 block h-4 w-4" />
                      Billing
                  </h6>
              </NuxtLink>
            </MenuItem>
              <NuxtLink
                to="/blog"
                class="!bg-transparrent  flex w-full items-center rounded-md p-2 text-sm transition-colors duration-300"
                @click.passive="close">
                  <h6 class="font-heading text-muted-800 text-xs leading-none dark:text-white flex gap-1 items-center">
                     <Icon name="ant-design:read-outlined" class="text-muted-400 dark:text-muted-500 block h-4 w-4" />
                      Blog
                  </h6>
              </NuxtLink>
              <NuxtLink
                target="_blank"
                to="/affiliate"
                class="!bg-transparrent  flex w-full items-center rounded-md p-2 text-sm transition-colors duration-300"
                @click.passive="close">
                  <h6 class="font-heading text-muted-800 text-xs leading-none dark:text-white flex gap-1 items-center">
                     <Icon name="fluent:megaphone-loud-28-regular" class="text-muted-400 dark:text-muted-500 block h-4 w-4" />
                      Affiliate
                  </h6>
              </NuxtLink>
              <NuxtLink
                to="/support"
                class="!bg-transparrent  flex w-full items-center rounded-md p-2 text-sm transition-colors duration-300"
                @click.passive="close">
                  <h6 class="font-heading text-muted-800 text-xs leading-none dark:text-white flex gap-1 items-center">
                     <Icon name="ri:customer-service-line" class="text-muted-400 dark:text-muted-500 block h-4 w-4" />
                      Support
                  </h6>
              </NuxtLink>
          </div>

          <div class="p-6">
            <BaseButton @click.passive="logOutUser" shape="curved" class="w-full">
              Logout
            </BaseButton>
          </div>
        </MenuItems>
      </Transition>
    </Menu>
  </div>
</template>
