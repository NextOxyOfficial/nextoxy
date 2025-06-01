<script setup lang="ts">
import { useSidebar } from "../composables/sidebar";

const props = withDefaults(
  defineProps<{
    subsidebar?: boolean;
    expanded?: boolean;
  }>(),
  {
    subsidebar: true,
    expanded: false,
  }
);

const { isOpen, current, sidebars } = useSidebar();

const startSidebars = computed(
  () =>
    sidebars.value?.filter(
      (sidebar) => !sidebar.position || sidebar.position === "start"
    )
);
const endSidebars = computed(
  () => sidebars.value?.filter((sidebar) => sidebar.position === "end")
);

const subsidebarEnabled = computed(() => {
  return Boolean(
    props.subsidebar !== false && current.value?.subsidebar?.component
  );
});

const topBarRef = ref(null);
const topPosition = ref("103px");

const handleScroll = () => {
  if (window.scrollY > 38) {
    topPosition.value = "64px";
  } else {
    topPosition.value = "103px";
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
  <div
    class="pointer-events-none fixed start-0 z-[60] flex h-full xl:z-10 transition-all"
    ref="topBarRef"
    :style="{ top: topPosition }"
  >
    <!-- Icon sidebar -->
    <div
      class="border-muted-200 dark:border-muted-700 dark:bg-muted-800 pointer-events-auto relative z-20 flex h-full w-[80px] flex-col border-r transition-all duration-300 bg-slate-50/90"
      :class="
        isOpen
          ? ''
          : '-translate-x-full rtl:translate-x-full xl:translate-x-0 rtl:xl:-translate-x-0'
      "
    >
      <slot></slot>

      <!-- Top Menu -->
      <div>
        <slot name="top"></slot>

        <TairoSidebarNavigationItem
          v-for="item in startSidebars"
          :key="item.title"
          :sidebar="item"
        />
      </div>
      <!-- Bottom Menu -->
      <div class="mt-auto">
        <TairoSidebarNavigationItem
          v-for="item in endSidebars"
          :key="item.title"
          :sidebar="item"
        />

        <slot name="end"></slot>
      </div>
    </div>

    <!-- Menu panel -->
    <div
      v-if="subsidebarEnabled"
      class="border-muted-200 dark:border-muted-700 dark:bg-muted-800 pointer-events-auto relative z-10 h-full w-[240px] border-r transition-all duration-300 bg-slate-50/90"
      :class="
        isOpen
          ? ''
          : 'rtl:translate-x-[calc(100%_+_80px)] translate-x-[calc(-100%_-_80px)]'
      "
    >
      <slot name="subnav" v-if="isOpen && current">
        <KeepAlive>
          <component
            :is="resolveComponentOrNative(current.subsidebar?.component)"
            :key="current?.subsidebar?.component"
            v-if="current?.subsidebar?.component"
          ></component>
        </KeepAlive>
      </slot>
    </div>
  </div>
</template>
