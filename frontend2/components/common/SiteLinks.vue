<script setup lang="ts">
import { Menu, MenuButton, MenuItem, MenuItems } from '@headlessui/vue'
const {shop}= useShop()
const Api = useApi()
const { currentName } = useSidebar()

</script>

<template>
  <div class="group inline-flex items-center justify-center text-right" v-if="currentName != 'Account' && shop">
    <Menu as="div" class="relative text-left" v-slot="{ close }">
      <MenuButton as="div" class="flex gap-2 whitespace-nowrap items-center">
        <button
          type="button"
          class="group-hover:ring-muted-200 dark:group-hover:ring-muted-700 dark:ring-offset-muted-900 inline-flex h-9 w-9 items-center justify-center rounded-full ring-1 ring-transparent transition-all duration-300 group-hover:ring-offset-4 md:hidden"
        >
          <span
            class="border-muted-200 dark:border-muted-700 dark:bg-muted-800 flex h-9 w-9 items-center justify-center rounded-full border bg-white"
          >
            <Icon name="mdi:web" class="text-muted-400 h-5 w-5" />
          </span>
        </button>
        <BaseButton size="sm" class="cursor-pointer opacity-[.8] hidden md:flex">
            <Icon name="mdi:web" class="text-muted-400 h-4 w-4" />
            <p>Site Links</p>
            <Icon name="ic:outline-arrow-drop-down" class="text-muted-400 h-5 w-5" />
        </BaseButton>
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
          class="divide-muted-100 border-muted-200 dark:divide-muted-700 dark:border-muted-700 dark:bg-muted-800 absolute start-[0] translate-x-[-30%] mt-2 w-72 origin-top-right divide-y rounded-md border bg-white shadow-lg focus:outline-none"
        >
          <div class="px-4 py-2">
            <div class="relative flex items-center justify-between">
              <h4
                class="font-heading text-muted-500 dark:text-muted-200 text-xs uppercase"
              >
                All Domains
              </h4>
            </div>
          </div>
          <div class="px-4 py-2" v-if="shop && shop.domains">
            <MenuItem as="div" class="hover:bg-slate-500/10 font-heading text-muted-500 dark:text-muted-200" v-for="domain in shop.domains">
                <template v-if="domain.subdomain">
                    <a :href="'http://'+domain.domain+'.localhost:8000'" target="_blank" rel="noopener noreferrer" class="flex gap-1 items-center my-1" v-if="Api.baseURL=='http://127.0.0.1:8000'">
                        <span>http://{{ domain.domain }}.localhost:8000</span>
                        <svg class="text-lime-900" xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24"><path fill="currentColor" d="M19 19H5V5h7V3H5a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14c1.1 0 2-.9 2-2v-7h-2v7zM14 3v2h3.59l-9.83 9.83l1.41 1.41L19 6.41V10h2V3h-7z"/></svg>
                    </a>
                    <a :href="'https://'+domain.domain+'.nextoxy.com'" target="_blank" rel="noopener noreferrer" class="flex gap-1 items-center my-1" v-else>
                        <span>https://{{ domain.domain }}.nextoxy.com</span>
                        <svg class="text-lime-900" xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24"><path fill="currentColor" d="M19 19H5V5h7V3H5a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14c1.1 0 2-.9 2-2v-7h-2v7zM14 3v2h3.59l-9.83 9.83l1.41 1.41L19 6.41V10h2V3h-7z"/></svg>
                    </a>
                </template>
                <template v-else>
                    <a :href="'https://'+domain.domain" target="_blank" rel="noopener noreferrer" class="flex gap-1 items-center my-1">
                        <span>https://{{ domain.domain }}</span>
                        <svg class="text-lime-900" xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24"><path fill="currentColor" d="M19 19H5V5h7V3H5a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14c1.1 0 2-.9 2-2v-7h-2v7zM14 3v2h3.59l-9.83 9.83l1.41 1.41L19 6.41V10h2V3h-7z"/></svg>
                    </a>
                </template>
            </MenuItem>
          </div>
        </MenuItems>
      </Transition>
    </Menu>
  </div>
</template>
