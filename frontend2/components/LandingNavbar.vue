<script setup lang="ts">
const { x, y } = useWindowScroll();
const isSearchOpen = useState("search-open", () => false);
const isMobileOpen = ref(false);

const metaKey = useMetaKey();
const { open } = usePanels();
const { logout, user, isAuthenticated } = useAuth();
function logoutUser() {
  logout();
  isMobileOpen.value = false;
}
const services = [
  {
    title: "eCommerce Dropshipping",
    description: "eCommerce",
    icon: "material-symbols:shopping-bag-outline-sharp",
    to: "/account/ecommerce",
  },
  {
    title: "Blog",
    description: "Coming Soon",
    icon: "solar:ruler-cross-pen-bold-duotone",
    to: "/account/services/blog",
  },
  // {
  //   title: "Domain",
  //   description: "Purchase And Manage Domains",
  //   icon: "ph:users-four-duotone",
  //   to: "/account/services/domains",
  // },
  {
    title: "SEO Marketing",
    description: "Order SEO Marketing Services",
    icon: "ph:lock-open-duotone",
    to: "/account/services/seo",
  },
  {
    title: "Facebook Boosting",
    description: "Boost Your Facebook Page",
    icon: "ph:note-duotone",
    to: "/account/services/boosting",
  },
  {
    title: "Graphic Design",
    description: "Order Graphic Design Services",
    icon: "ph:upload-duotone",
    to: "/account/services/graphic",
  },
  {
    title: " UK & USA Business Formation ",
    description: " UK & USA Business Registration Service",
    icon: "fluent:building-bank-28-regular",
    to: "/business-formation",
  },
  {
    title: "OxyManager",
    description: "POS & SMS Marketing",
    image:
      "https://nextdropshipping.com/media/site_logo/imgs/nextdroplogo_2_FgAINnU.png",
    to: "https://oxymanager.com/",
    newTab: true,
  },
  {
    title: "Next Dropshipping",
    description: "Wholesale Marketplace",
    image:
      "https://nextdropshipping.com/media/site_logo/imgs/nextdroplogo_2_FgAINnU.png",
    to: "https://nextdropshipping.com/",
    newTab: true,
  },
  {
    title: "NDS Academy",
    description: "Invest With NDS",
    image:
      "https://nextdropshipping.com/media/site_logo/imgs/nextdroplogo_2_FgAINnU.png",
    to: "https://academy.nextdropshipping.com/",
    newTab: true,
  },
];
</script>

<template>
  <div
    class="group/nav ltablet:max-w-[1000px] ptablet:max-w-[47rem] fixed inset-x-0 top-0 z-50 mx-auto max-w-[350px] group-[&.scrolled]/landing:mt-4 group-[&:not(.scrolled)]/landing:mt-12 motion-safe:transition-all motion-safe:duration-200 lg:max-w-7xl"
  >
    <div
      class="group-[&.scrolled]/landing:dark:bg-muted-950/95 group-[&.scrolled]/landing:border-muted-200 group-[&.scrolled]/landing:dark:border-muted-700 group-[&.scrolled]/landing:motion-safe:shadow-muted-300/30 group-[&.scrolled]/landing:motion-safe:dark:shadow-muted-800/20 flex items-center justify-between rounded-2xl border p-2 md:p-4 group-[&:not(.scrolled)]/landing:border-transparent group-[&.scrolled]/landing:bg-white/95 motion-safe:transition-all motion-safe:duration-200 group-[&.scrolled]/landing:motion-safe:shadow-xl"
    >
      <div class="flex w-1/2 items-center gap-2 md:w-1/5">
        <NuxtLink
          to="/"
          class="md:!ms-2 inline-flex"
          aria-label="Go to Tairo homepage"
        >
          <img
            class="h-10 md:h-12 object-contain dark:hidden"
            src="/static/frontend/images/home/logo.png"
            alt=""
            srcset=""
          />
          <img
            class="h-10 md:h-12 object-contain hidden dark:block"
            src="/static/frontend/images/home/logo-white.png"
            alt=""
            srcset=""
          />
        </NuxtLink>
      </div>
      <div
        class="nav-links ltablet:static ltablet:w-auto ltablet:flex ltablet:flex-row dark:bg-muted-950 ltablet:!bg-transparent ltablet:mx-0 fixed inset-x-0 top-20 mx-auto w-[calc(100%_-_2rem)] items-center justify-center bg-white lg:static lg:mx-0 lg:flex lg:w-auto lg:flex-row lg:!bg-transparent uppercase"
        :class="[
          isMobileOpen
            ? 'shadow-muted-300/30 dark:shadow-muted-900/20 group-[&.scrolled]/landing:ltablet:mt-0 group-[&:not(.scrolled)]/landing:ltablet:mt-0 flex flex-col space-y-4 rounded-xl p-6 shadow-xl group-[&.scrolled]/landing:mt-2 group-[&:not(.scrolled)]/landing:mt-4 motion-safe:transition-all motion-safe:duration-200 group-[&.scrolled]/landing:lg:mt-0 group-[&:not(.scrolled)]/landing:lg:mt-0'
            : 'hidden',
        ]"
      >
        <NuxtLink
          to="/"
          class="inline-flex items-center justify-center px-2 lg:!px-6 font-bold"
          @click="isMobileOpen = false"
        >
          Home
        </NuxtLink>
        <!-- <NuxtLink
          to="/services"
          class="inline-flex items-center justify-center px-2 lg:!px-6 font-bold"
          @click="isMobileOpen = false"
        >
          Services
        </NuxtLink> -->
        <!-- <div
          class="items-center justify-center px-2 lg:!px-6 font-bold relative group hover:cursor-pointer hover:text-gray-400"
        >
          Services

          <Icon name="ic:baseline-keyboard-arrow-down" class="size-6" />

          <ul
            class="absolute left-0 hidden group-hover:block py-5 min-w-96 bg-white"
          >
            <li
              class="text-black hover:text-gray-400 py-3"
              v-for="(service, index) in services"
              :key="index"
            >
              <a
                v-if="service.newTab"
                target="_blank"
                :href="service.to"
                class="inline-flex items-center justify-center px-2 lg:!px-6 font-bold"
                @click="isMobileOpen = false"
              >
                {{ service.title }}
              </a>
              <NuxtLink
                v-else
                :to="service.to"
                class="inline-flex items-center justify-center px-2 lg:!px-6 font-bold"
                @click="isMobileOpen = false"
              >
                {{ service.title }}
              </NuxtLink>
            </li>
          </ul>
        </div> -->
        <NuxtLink
          to="/themes"
          class="inline-flex items-center justify-center px-2 lg:!px-6 font-bold"
          @click="isMobileOpen = false"
        >
          Themes
        </NuxtLink>

        <NuxtLink
          to="/plugins"
          class="inline-flex items-center justify-center px-2 lg:!px-6 font-bold"
          @click="isMobileOpen = false"
        >
          Plugins
        </NuxtLink>
        <NuxtLink
          to="/blog"
          class="inline-flex items-center justify-center px-2 lg:!px-6 font-bold"
          @click="isMobileOpen = false"
        >
          Blog
        </NuxtLink>
        <NuxtLink
          to="/help-center"
          class="inline-flex items-center justify-center px-2 lg:!px-6 font-bold"
          @click="isMobileOpen = false"
        >
          Help Center
        </NuxtLink>
        <template v-if="!user">
          <BaseButton
            color="default"
            to="/auth/login/"
            @click="isMobileOpen = false"
            shape="curved"
            class="ltablet:!hidden !flex lg:!hidden min-w-[110px] w-32"
          >
            <Icon
              name="material-symbols:storefront-outline"
              class="-ms-1 h-4 w-4"
            />

            <span>Login</span>
          </BaseButton>
          <BaseButton
            shape="curved"
            color="primary"
            to="/auth/signup/"
            @click="isMobileOpen = false"
            class="ltablet:!hidden !flex lg:!hidden text-2xl w-32"
          >
            Start Free
          </BaseButton>
        </template>
        <template v-else>
          <BaseButton
            shape="curved"
            color="primary"
            to="/account"
            @click="isMobileOpen = false"
            class="ltablet:!hidden !flex lg:!hidden text-xl whitespace-nowrap w-32"
          >
            My Dashboard
          </BaseButton>
          <BaseButton
            @click="logoutUser"
            color="default"
            shape="curved"
            class="ltablet:!hidden !flex lg:!hidden w-32"
          >
            <Icon
              name="material-symbols:storefront-outline"
              class="-ms-1 h-4 w-4"
            />
            <span>Logout</span>
          </BaseButton>
        </template>
      </div>
      <div
        class="flex w-1/2 items-center justify-end gap-2 md:gap-3 lg:gap-4 md:max-w-[40%] lg:max-w-[301px]"
      >
        <BaseThemeToggle aria-label="Toggle darkmode" />
        <template v-if="!user">
          <BaseButton
            color="default"
            to="/auth/login/"
            shape="curved"
            class="ltablet:!flex !hidden lg:!flex w-32"
          >
            <Icon
              name="material-symbols:storefront-outline"
              class="-ms-1 h-4 w-4"
            />

            <span>Login</span>
          </BaseButton>
          <BaseButton
            shape="curved"
            color="primary"
            to="/auth/signup/"
            class="ltablet:!flex !hidden lg:!flex text-2xl w-32"
          >
            Start Free
          </BaseButton>
        </template>
        <template v-else>
          <BaseButton
            shape="curved"
            color="primary"
            to="/account"
            class="w-full ltablet:!flex !hidden lg:!flex text-xl whitespace-nowrap"
          >
            My Dashboard
          </BaseButton>
          <BaseButton
            @click="logoutUser"
            color="default"
            shape="curved"
            class="ltablet:!flex !hidden lg:!flex w-32"
          >
            <Icon
              name="material-symbols:storefront-outline"
              class="-ms-1 h-4 w-4"
            />
            <span>Logout</span>
          </BaseButton>
        </template>
        <button
          type="button"
          class="ltablet:hidden flex items-center justify-center lg:hidden"
          @click="isMobileOpen = !isMobileOpen"
          :aria-label="isMobileOpen ? 'Close menu' : 'Open menu'"
        >
          <div class="space-y-1.5">
            <span
              class="bg-primary-600 block h-0.5 motion-safe:transition-all motion-safe:duration-300"
              :class="isMobileOpen ? 'w-2' : 'w-6'"
            ></span>
            <span
              class="bg-primary-600 block h-0.5 motion-safe:transition-all motion-safe:duration-300"
              :class="isMobileOpen ? 'w-6' : 'w-6'"
            ></span>
            <span
              class="bg-primary-600 block h-0.5 motion-safe:transition-all motion-safe:duration-300"
              :class="isMobileOpen ? 'w-4' : 'w-6'"
            ></span>
          </div>
        </button>
      </div>
    </div>
  </div>
</template>

<style scoped>
.nav-links > a {
  padding: 5px;
}
.nav-links .router-link-active {
  border-bottom: 2px solid #ffc107;
}
</style>
