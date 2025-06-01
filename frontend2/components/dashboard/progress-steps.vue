<template>
  <div>
    <div class="flex py-3 px-2 justify-between items-center">
      <p>Basic</p>
      <ULink
        to="/ecommerce/subscription"
        active-class="text-primary"
        inactive-class="text-gray-500 dark:text-gray-400"
        ><UButton size="sm" color="primary" variant="solid" label="Upgrade"
      /></ULink>
    </div>
    <UDivider label="" />
    <div class="px-2 py-3">
      <p v-if="completed.length === steps?.data?.length">WOW! Awesome Shop</p>
      <NuxtLink
        v-else
        to="/ecommerce"
        class="flex justify-between items-center"
      >
        <p>Your store setup progress!</p>
        <UIcon
          class="text-sm"
          name="i-material-symbols:arrow-forward-ios-rounded"
          dynamic
        />
      </NuxtLink>
      <UProgress :value="(100 / 6) * completed.length" class="my-1" />
      <small>{{ completed.length }}/{{ steps?.data?.length }} Completed</small>
    </div>
    <UDivider label="" />
  </div>
</template>

<script setup>
const Api = useApi();

const steps = ref([]);
const completed = ref(0);
async function getSteps() {
  var res = await Api.get("/api/ecommerce/dash/steps");
  steps.value = res.data;
  console.log(steps.value, 333);
  completed.value = steps.value?.data?.filter(
    (item) => item.status === "complete"
  );
}

getSteps();
</script>

<style scoped></style>
