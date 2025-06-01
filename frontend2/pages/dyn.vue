<template>
  <section>
    <div v-for="(item, index) in list" :key="item.id" class="flex gap-3">
      <component v-bind:is="item.comp"></component>
      <button @click="deleteItem(index)">Delete</button>
    </div>
    <input type="text" v-model="cid">
    <button @click="addItem">Add Item</button>

    <dotlottie-player src="https://lottie.host/a9263a8a-6ef3-408c-a0d9-d423cb490328/KEjpEvXqsF.json" background="transparent" speed="1" style="width: 300px; height: 300px;" loop autoplay></dotlottie-player>
  </section>
</template>

<script setup>
definePageMeta({
    layout: 'blanksss'
})
useHead({
    script: [
        { src: 'https://unpkg.com/@dotlottie/player-component@latest/dist/dotlottie-player.mjs', body: true, defer: false },
    ]
})
const list = ref([
  {
    comp: shallowRef(resolveComponent('dyn/A1')),
    id: '1',
    active: false
  },
  {
    comp: shallowRef(resolveComponent('DynA2')),
    id: '2',
    active: true
  },
  {
    comp: shallowRef(resolveComponent('DynA3')),
    id: '3',
    active: false
  }
]);

const deleteItem = (index) => {
  list.value.splice(index, 1);
};
const cid = ref(1)
const addItem = async() => {
    const componentName = 'A'+cid.value;
    const dynamicComponent = import(`@/components/dyn/${componentName}.vue`);
    dynamicComponent.then((module) => {
      const c = shallowRef(module.default);
      const newItem = {
        comp: c,
        id: `${list.value.length + 1}`,
        active: false,
      };
      list.value.push(newItem);
    });
};
</script>

<style scoped>
</style>