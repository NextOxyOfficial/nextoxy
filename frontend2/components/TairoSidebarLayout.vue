<script setup lang="ts">
import { useSidebar } from "../composables/sidebar";
const { setup, currentName, isOpen, toggle } = useSidebar();
const props = withDefaults(
  defineProps<{
    sidebar?: boolean;
    subsidebar?: boolean;
    toolbar?: boolean;
    circularMenu?: boolean;
    condensed?: boolean;
    horizontalScroll?: boolean;
  }>(),
  {
    sidebar: true,
    subsidebar: true,
    toolbar: true,
    circularMenu: true,
  }
);

const app = useAppConfig();
setup();

onUnmounted(() => {
  currentName.value = "";
  isOpen.value = undefined;
});

const sidebarEnabled = computed(() => {
  return (
    app.tairo.sidebar?.navigation?.enabled !== false && props.sidebar !== false
  );
});
const toolbarEnabled = computed(() => {
  return (
    app.tairo.sidebar?.toolbar?.enabled !== false && props.toolbar !== false
  );
});
const circularMenuEnabled = computed(() => {
  return (
    app.tairo.sidebar?.circularMenu?.enabled !== false &&
    props.circularMenu !== false
  );
});

const wrapperClass = computed(() => {
  if (props.condensed) {
    return "bg-muted-100 dark:bg-muted-900 relative min-h-screen w-full overflow-x-hidden";
  }

  if (!sidebarEnabled.value) {
    return "bg-white dark:bg-muted-900 relative min-h-screen w-full overflow-x-hidden px-2 md:px-4 transition-all duration-300 xl:px-10";
  }

  const list = [
    "bg-white dark:bg-muted-900 relative min-h-screen w-full overflow-x-hidden px-2 md:px-4 transition-all duration-300 xl:px-10",
  ];

  if (isOpen.value) {
    list.push("xl:max-w-[calc(100%_-_300px)] xl:ms-[300px]");
  } else {
    list.push("xl:max-w-[calc(100%_-_80px)] xl:ms-[80px]");
  }

  if (props.horizontalScroll) {
    list.push("!pe-0 xl:!pe-0");
  }

  return list;
});

const topBarRef = ref(null);
const topPosition = ref("38px");

const handleScroll = () => {
  if (window.scrollY > 38) {
    topPosition.value = "0";
  } else {
    topPosition.value = "38px";
  }
};

onMounted(() => {
  window.addEventListener("scroll", handleScroll);
});

onUnmounted(() => {
  window.removeEventListener("scroll", handleScroll);
});
</script>

<template>
  <div class="bg-slate-100 dark:bg-muted-900 pb-20">
    <CommonTopbar />
    <div
      ref="topBarRef"
      :style="{ top: topPosition }"
      class="flex w-full items-center gap-3 md:gap-4 fixed z-[70] bg-slate-50 dark:bg-slate-900 border-b dark:border-slate-600 transition-all"
    >
      <div
        class="transition-all"
        :class="isOpen ? 'xl:w-[320px]' : 'xl:w-[88px]'"
      >
        <div class="flex items-center px-2 md:px-6 gap-6">
          <slot name="logo">
            <NuxtLink to="/" class="flex items-center justify-center">
              <component
                :is="
                  resolveComponentOrNative(
                    app.tairo.sidebar?.navigation.logo.component
                  )
                "
                v-bind="app.tairo.sidebar?.navigation.logo.props"
              ></component>
            </NuxtLink>
          </slot>

          <p
            v-if="isOpen"
            class="text-lg hidden md:block truncate font-semibold"
          >
            {{ currentName }}
            <!-- My Store -->
          </p>
        </div>
      </div>
      <div class="flex-1">
        <div class="max-w-7xl w-full px-2 md:px-4 lg:px-10 mx-auto">
          <slot name="toolbar">
            <TairoSidebarToolbar
              v-if="toolbarEnabled"
              :sidebar="props.sidebar"
              :horizontal-scroll="props.horizontalScroll"
            >
              <template #title><slot name="toolbar-title"></slot></template>
            </TairoSidebarToolbar>
          </slot>
        </div>
      </div>
    </div>
    <slot name="sidebar">
      <TairoSidebarNavigation
        v-if="sidebarEnabled"
        :subsidebar="props.subsidebar"
      >
        <!-- <div
          v-if="app.tairo.sidebar?.navigation?.logo?.component"
          class="flex h-16 w-full items-center justify-center"
        ></div> -->
      </TairoSidebarNavigation>
      <div
        role="button"
        class="bg-muted-800 dark:bg-muted-900 fixed start-0 top-0 z-[59] block h-full w-full transition-opacity duration-300 lg:hidden"
        :class="
          isOpen
            ? 'opacity-50 dark:opacity-75'
            : 'opacity-0 pointer-events-none'
        "
        @click="toggle"
      ></div>
    </slot>

    <div :class="wrapperClass">
      <div
        :class="[
          props.condensed && !props.horizontalScroll && 'w-full',
          !props.condensed && props.horizontalScroll && 'mx-auto w-full',
          !props.condensed &&
            !props.horizontalScroll &&
            'mx-auto w-full max-w-7xl',
        ]"
      >
        <main class="pt-28">
          <slot />
        </main>
      </div>
    </div>

    <TairoPanels />
    <TairoSidebarCircularMenu v-if="circularMenuEnabled" />
  </div>
</template>
