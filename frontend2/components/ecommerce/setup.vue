<template>
    <section v-if="steps && percentage && percentage != '100'">
        <!-- Modal component -->
        <TairoModal :open="isModalXlOpen" size="xl" @close="isModalXlOpen = false">
            <template #header>
            <!-- Header -->
            <div class="flex w-full items-center justify-between p-4 md:p-6">
                <h3 class="font-heading text-muted-900 text-lg font-medium leading-6 dark:text-white">Set Up Your Shop - {{percentage}} % Complete</h3>

                <BaseButtonClose @click="isModalXlOpen = false" />
            </div>
            <div class="px-3">
                <BaseProgress title="sm progress bar" size="sm" :value="percentage" color="primary" />
            </div>
            </template>
            <!-- Body -->
            <div class="overflow-y-scroll max-h-[70vh]">
                <div class="mx-auto w-full max-w-4xl p-8">
                <div v-if="steps && steps.length === 0"></div>
                <div v-else class="">
                    <div
                    v-for="item in steps"
                    :key="item.id"
                    class="relative flex items-center gap-4 after:absolute after:start-[8px] after:top-3 after:h-full after:w-px [&:not(:first-child)]:pt-3"
                    >
                    <div
                        class="dark:bg-muted-800 relative z-10 h-4 w-4 shrink-0 rounded-full bg-white"
                    >
                        <div class="rounded-full border-2 border-rose-500 w-6 h-6" v-if="item.status != 'complete'"> </div>
                        <TairoCheckAnimated v-else class="w-6 h-6" />
                    </div>

                    <BaseCard class="p-4">
                        <div class="flex w-full items-center gap-4">
                        <div>
                            <BaseText size="sm" lead="tight">
    
                            <span class="text-muted-500 dark:text-muted-400"
                                >{{ item.name }}&nbsp;</span
                            >
                            <NuxtLink
                                :to="item.href"
                                class="text-primary-500 underline-offset-4 hover:underline cursor-pointer"
                                >GO</NuxtLink
                            >
                            </BaseText>
                            <BaseText size="xs" class="text-muted-400">
                              <span>{{ item.description }}</span>
                            </BaseText>
                        </div>
                        <div class="ms-auto hidden items-center gap-3 sm:flex">
                            <BaseAvatar
                            v-for="user in item.people"
                            :key="user.name"
                            :src="user.src"
                            size="xxs"
                            />
                        </div>
                        </div>
                    </BaseCard>
                    </div>
                </div>
                </div>
            </div>

            <template #footer>
            <!-- Footer -->
            <div class="p-4 md:p-6">
                <div class="flex gap-x-2">
                <BaseButton @click="isModalXlOpen = false">Ok</BaseButton>
                </div>
            </div>
            </template>
        </TairoModal>



    </section>
    
</template>

<script setup lang="ts">
const Api = useApi()
const isModalXlOpen = ref(false)
const steps = ref([])
const percentage = ref(0)
async function getSteps(){
  const {data} = await Api.get('/api/ecommerce/dash/steps')
  steps.value = data.data
  percentage.value = data.percentage
}
getSteps()

const props = defineProps({
  state: {
    type: Boolean,
  }
})
if(props.state){
    setTimeout(() => {
        isModalXlOpen.value = true
    }, 2000);
}

</script>