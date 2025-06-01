<script setup lang="ts">
import { useSidebar } from "../composables/sidebar";

const props = withDefaults(
  defineProps<{
    sidebar?: boolean;
    horizontalScroll?: boolean;
  }>(),
  {
    sidebar: true,
  }
);

const app = useAppConfig();
const { hasSubsidebar, currentName } = useSidebar();

const route = useRoute();

const showNavBurger = computed(() => {
  return (
    props.sidebar &&
    app.tairo.sidebar?.toolbar?.showNavBurger &&
    hasSubsidebar.value
  );
});
</script>

<template>
  <div
    class="relative z-50 flex h-16 items-center gap-2 p-1"
    :class="props.horizontalScroll && 'pe-4 xl:pe-10'"
  >
    <TairoSidebarBurger v-if="showNavBurger" class="" />
    <BaseButton
      color="success"
      size="sm"
      to="/account/ecommerce"
      flavor="pastel"
      class="!bg-transparent ml-3 md:ml-24"
      v-if="currentName == 'eCommerce'"
    >
      <Icon name="ph:arrow-fat-lines-left-thin" class="h-4 w-4" />
      <span class="hidden md:block">All Shops</span>
    </BaseButton>
    <CommonSiteLinks />

    <BaseHeading
      v-if="app.tairo.sidebar?.toolbar?.showTitle"
      as="h1"
      size="2xl"
      weight="light"
      class="text-muted-800 hidden dark:text-white md:block"
    >
      <slot name="title">{{ route.meta.title }}</slot>
    </BaseHeading>

    <div class="ms-auto"></div>
    <TairoSidebarTools class="h-16" />
  </div>
</template>
