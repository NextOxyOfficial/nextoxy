<template>
  <span class="flex justify-center items-center gap-4">
    <!-- <img :src="'/static/frontend/images/ecommerce/title-icons/'+filename" alt="" :class="classes" srcset=""> -->
    <BaseHeading
      as="h2"
      size="2xl"
      :weight="weight"
      lead="tight"
      class="text-muted-800 dark:text-white"
    >
      <span>{{ title }}</span>
    </BaseHeading>
  </span>
</template>

<script setup>
defineProps({
  filename: {
    type: String,
    required: true,
  },
  classes: {
    type: String,
    default: "h-12 w-12",
  },
  title: {
    type: String,
    default: "",
  },
  weight: {
    type: String,
    default: "light",
  },
});
</script>

<style scoped></style>
