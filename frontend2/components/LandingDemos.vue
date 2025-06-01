<script setup lang="ts">
import type { RouteRecordRaw } from 'vue-router'

const props = withDefaults(
  defineProps<{
    limit?: number
    cta?: boolean
  }>(),
  {
    limit: undefined,
    cta: true,
  },
)

const selectedCategory = ref('')

const router = useRouter()

const demoPages = computed(() => {
  const match: RouteRecordRaw[] = []

  function traverseRoutes(routes: Readonly<RouteRecordRaw[]>) {
    for (const route of routes) {
      if (route.children) {
        // recurse
        traverseRoutes(route.children)
      } else if (
        route.path.includes(':') &&
        Array.isArray(route.meta?.preview)
      ) {
        match.push(route)
      } else if (!route.path.includes(':') && route.meta?.preview) {
        // has preview data
        match.push(route)
      }
    }
  }

  // start on top route
  traverseRoutes(router.options.routes)

  return match.sort((a, b) => {
    if (a.meta?.preview?.order === undefined) return 0
    if (b.meta?.preview?.order === undefined) return 0
    if (a.meta.preview?.order < b.meta.preview?.order) return -1
    if (a.meta.preview?.order > b.meta.preview?.order) return 1
    return 0
  })
})

const categories = computed(() => {
  const categories = new Set<string>()

  function extractPreview(preview: any) {
    if (!preview) {
      return
    }
    if (Array.isArray(preview)) {
      for (const item of preview) {
        extractPreview(item)
      }
      return
    }
    if (!preview.categories) {
      return
    }
    if (!Array.isArray(preview.categories)) {
      return
    }
    for (const category of preview.categories) {
      categories.add(category)
    }
  }

  for (const route of demoPages.value) {
    extractPreview(route.meta?.preview)
  }
  return Array.from(categories).sort((a, b) => {
    return a.localeCompare(b)
  })
})

const filteredDemos = computed(() => {
  if (selectedCategory.value.length === 0) {
    return demoPages.value
  }

  function filterPreview(preview: any) {
    if (!preview) {
      return false
    }
    if (Array.isArray(preview)) {
      for (const item of preview) {
        if (filterPreview(item)) {
          return true
        }
      }
      return false
    }
    if (!preview.categories) {
      return false
    }
    if (!Array.isArray(preview.categories)) {
      return false
    }
    return preview.categories.some((category: string) =>
      selectedCategory.value.includes(category),
    )
  }

  return demoPages.value.filter((page) => {
    return filterPreview(page.meta?.preview)
  })
})


const layouts = [
      {
        name: 'sidebar',
        title: 'Student/Educational',
        description: 'Free Forever',
        text: 'Unlock the door to endless knowledge with our Student/Educational plan, absolutely free forever! This plan empowers students and educators alike, providing access to a wealth of resources without any cost. Enjoy the freedom to explore, learn, and grow without limitations.',
        img: '/static/frontend/packages/pro_light-min.png',
        imgDark: '/static/frontend/packages/pro_dark-min.png',
        icon: 'game-icons:rank-1',
      },
      {
        name: 'collapse',
        title: 'Basic',
        description: 'Basic Startup Package',
        text: "Introducing the Basic Startup Package, designed for budding entrepreneurs. For just $2.99 per month, kickstart your venture with essential tools and insights. Unleash your potential with curated articles, captivating titles, and impactful taglines. ",
        img: '/static/frontend/packages/basic_light-min.png',
        imgDark: '/static/frontend/packages/basic_dark-min.png',
        icon: 'game-icons:rank-2',
      },
      {
        name: 'topnav',
        title: 'Pro',
        description: 'Professional Premium Package',
        text: 'Elevate your career with exclusive access to premium articles, compelling titles, and standout taglines. Unleash a world of opportunities with our advanced features and resources tailored for professionals.',
        img: '/static/frontend/packages/pro_light-min.png',
        imgDark: '/static/frontend/packages/pro_dark-min.png',
        icon: 'game-icons:rank-3',
      },
      {
        name: 'topnav2',
        title: 'EnterPrize',
        description: 'Grow Big',
        text: 'Our EnterPrize plan is your key to unlocking unparalleled insights and strategies. Stay at the forefront of innovation and lead your industry with the Revelatory Enterprise Package.',
        img: '/static/frontend/packages/enterprize_light-min.png',
        imgDark: '/static/frontend/packages/enterprize_dark-min.png',
        icon: 'solar:ranking-bold-duotone',
      },
    ]

    const activeLayout = ref('sidebar')
    const list = ['sidebar', 'collapse', 'topnav', 'topnav2']
    let currentIndex = 0;

    const changeStyle = () => {
      activeLayout.value = list[currentIndex];
      currentIndex = (currentIndex + 1) % list.length;
    }

    const interval = setInterval(changeStyle, 2000);

    // Clear the interval when the component is unmounted to avoid memory leaks
    onUnmounted(() => {
      clearInterval(interval);
    });
</script>


<template>
  <div class="dark:bg-muted-900 bg-white py-24">
    <div class="mx-auto w-full max-w-7xl px-4">
      <div class="mb-16 max-w-2xl">
        <BaseText
          class="text-primary-500 mb-2 text-[0.65rem] uppercase tracking-wider"
          >Prebuilt Themes</BaseText
        >
        <BaseHeading
          as="h2"
          size="4xl"
          weight="light"
          lead="tight"
          class="text-muted-800 mx-auto mb-4 dark:text-white"
        >
          <!-- {{ demoPages.length }}+  -->
          Amazing Unlimited Themes Access Under One Subscription :)
        </BaseHeading>
        <BaseParagraph
          size="lg"
          class="text-muted-500 dark:text-muted-100 mx-auto mb-4"
        >
          Simplify your eCommerce workflow website & Start selling in less than 5 minutes with NextOxy's easy and ready-to-use ecommerce and dropshipping solutions
        </BaseParagraph>
      </div>
      <!-- <div class="md:flex items-center justify-around space-y-10 md:space-y-0">
        <img src="../public/img/theme-pic.png" alt="">
        <img src="../public/img/theme-pic-2.png" alt="">
      </div> -->
      <!-- <div v-if="props.cta" class="mt-24 flex items-center justify-center">
        <BaseButton
          shape="curved"
          color="primary"
          flavor="outline"
          to="/themes"
          >View All Demos</BaseButton
        >
      </div> -->

      <!-- <div class="grid grid-cols-12 gap-6">
        
        <div
          class="ltablet:col-span-2 ltablet:block relative col-span-12 hidden lg:col-span-2 lg:block"
        >
          <ul class="space-y-3 lg:sticky lg:top-28">
            <li class="capitalize">
              <BaseRadio
                v-model="selectedCategory"
                value=""
                color="primary"
                label="All"
              />
            </li>
            <li
              v-for="category in categories"
              :key="category"
              class="capitalize"
            >
              <BaseRadio
                v-model="selectedCategory"
                :value="category"
                color="primary"
                :label="category"
              />
            </li>
          </ul>
        </div>
        
        <div class="ltablet:col-span-10 col-span-12 lg:col-span-10">
          <div class="grid gap-8 sm:grid-cols-2">
            <template
              v-for="page in filteredDemos.slice(0, props.limit)"
              :key="page.name"
            >
              <LandingDemoLink
                v-if="!Array.isArray(page.meta?.preview)"
                :name="page.name"
                :preview="page.meta?.preview"
              />
              <template v-else>
                <LandingDemoLink
                  v-for="preview in page.meta?.preview"
                  :key="preview.title"
                  :name="page.name"
                  :preview="preview"
                />
              </template>
            </template>
          </div>

          <div v-if="props.cta" class="mt-24 flex items-center justify-center">
            <BaseButton
              shape="curved"
              color="primary"
              flavor="outline"
              to="/themes"
              >View All Themes</BaseButton
            >
          </div>
        </div>
      </div> -->
      <div class="grid grid-cols-12 gap-6">
            <div class="col-span-12 flex h-full md:col-span-5">
              <div class="w-full space-y-2 sm:max-w-xs">
                <button
                  v-for="(layout, index) in layouts"
                  :key="index"
                  type="button"
                  class="flex w-full items-center gap-3 rounded-xl p-4 text-start"
                  :class="
                    activeLayout === layout.name
                      ? 'bg-muted-50 dark:bg-muted-950/50'
                      : ''
                  "
                  @click="activeLayout = layout.name"
                >
                  <Icon
                    :name="layout.icon"
                    class="h-6 w-6"
                    :class="
                      activeLayout === layout.name
                        ? 'text-primary-500'
                        : 'text-muted-400'
                    "
                  />
                  <span class="block">
                    <BaseText size="md" lead="tight">{{ layout.title }}</BaseText>
                    <BaseText
                      size="xs"
                      class="text-muted-500 dark:text-muted-400"
                      >{{ layout.description }}</BaseText
                    >
                  </span>
                </button>
              </div>
            </div>
            <div class="col-span-12 md:col-span-7">
              <BaseCard
                v-for="(layout, index) in layouts"
                :key="index"
                color="white-contrast"
                shape="curved"
                class="relative flex flex-col overflow-hidden rounded-xl text-start"
                v-show="activeLayout === layout.name"
              >
                <div class="bg-muted-100 dark:bg-muted-900/40 relative">
                  <img
                    :src="layout.img"
                    class="block w-full dark:hidden"
                    :alt="layout.title"
                    width="717"
                    height="384"
                    loading="lazy"
                    decoding="async"
                  />
                  <img
                    :src="layout.imgDark"
                    class="hidden w-full dark:block"
                    :alt="layout.title"
                    width="717"
                    height="384"
                    loading="lazy"
                    decoding="async"
                  />
                  <NuxtLink
                    to="/themes"
                    class="border-muted-200 text-muted-600 dark:text-muted-400 hover:text-primary-500 dark:hover:text-primary-500 hover:border-primary-500 dark:bg-muted-950 dark:border-muted-800 dark:hover:border-primary-500 absolute start-6 top-6 inline-flex items-center gap-1 rounded-full border bg-white px-5 py-2 transition-colors duration-300"
                  >
                    <span class="font-sans text-sm">Browse Themes</span>
                    <Icon name="lucide:arrow-right" class="h-3 w-3" />
                  </NuxtLink>
                </div>
                <div class="relative flex grow flex-col px-8 pb-8 pt-4">
                  <div
                    class="absolute -top-8 start-0 z-10 h-6 w-full bg-white blur-md dark:hidden"
                  ></div>
                  <div class="mt-auto space-y-2">
                    <BaseHeading weight="light">{{ layout.title }}</BaseHeading>
                    <BaseParagraph
                      size="sm"
                      class="text-muted-500 dark:text-muted-400"
                    >
                      {{ layout.text }}
                    </BaseParagraph>
                  </div>
                </div>
              </BaseCard>
            </div>
            
          </div>
          <div v-if="props.cta" class="mt-24 flex items-center justify-center">
            <BaseButton
              shape="curved"
              color="primary"
              flavor="outline"
              to="/themes"
              >View All Demos</BaseButton
            >
          </div>
    </div>
  </div>
</template>
