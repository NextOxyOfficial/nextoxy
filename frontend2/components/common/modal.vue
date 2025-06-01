<template>
  <TransitionRoot as="template" :show="open">
    <Dialog as="div" class="relative z-[10000000000]" @close="open = false">
      <TransitionChild
        as="template"
        enter="ease-out duration-300"
        enter-from="opacity-0"
        enter-to="opacity-100"
        leave="ease-in duration-200"
        leave-from="opacity-100"
        leave-to="opacity-0"
      >
        <div
          class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity"
        />
      </TransitionChild>

      <div class="fixed inset-0 z-10 overflow-y-auto">
        <div
          class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0"
        >
          <TransitionChild
            as="template"
            enter="ease-out duration-300"
            enter-from="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95"
            enter-to="opacity-100 translate-y-0 sm:scale-100"
            leave="ease-in duration-200"
            leave-from="opacity-100 translate-y-0 sm:scale-100"
            leave-to="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95"
          >
            <DialogPanel
              class="relative transform text-left shadow transition-all sm:my-8 w-full sm:max-w-xl"
            >
              <div class="bg-white relative rounded overflow-hidden w-full">
                <slot>
                  <div class="absolute right-[10px] top-[12px]">
                    <div
                      @click="open = false"
                      class="mx-auto cursor-pointer flex h-10 w-10 p-2 flex-shrink-0 items-center justify-center rounded-full bg-white border text-rose-800 hover:shadow-lg"
                    >
                      <svg
                        xmlns="http://www.w3.org/2000/svg"
                        width="32"
                        height="32"
                        viewBox="0 0 24 24"
                      >
                        <path
                          fill="currentColor"
                          d="M18.3 5.71a.996.996 0 0 0-1.41 0L12 10.59L7.11 5.7A.996.996 0 1 0 5.7 7.11L10.59 12L5.7 16.89a.996.996 0 1 0 1.41 1.41L12 13.41l4.89 4.89a.996.996 0 1 0 1.41-1.41L13.41 12l4.89-4.89c.38-.38.38-1.02 0-1.4z"
                        />
                      </svg>
                    </div>
                  </div>
                  <div class="mt-3 text-center sm:mt-0 sm:text-left w-full">
                    <h3 class="text-slate-100 p-4 bg-purple-600">
                      Please Provide Billing Information
                    </h3>
                    <div class="flex flex-1 flex-col justify-center p-5 w-full">
                      <div class="md:col-span-2 md:mt-0">
                        <p>
                          Lorem ipsum dolor sit amet consectetur adipisicing
                          elit. Aliquid labore itaque, ratione corrupti
                          assumenda error atque architecto porro et dolor nulla
                          eius laboriosam doloribus dolores ullam sed soluta
                          enim tempore.
                        </p>
                      </div>
                      <div class="flex justify-end my-4 gap-1">
                        <button class="btn px-3 py-2">Save Changes</button>
                      </div>
                    </div>
                  </div>
                </slot>
              </div>
            </DialogPanel>
          </TransitionChild>
        </div>
      </div>
    </Dialog>
  </TransitionRoot>
</template>

<script setup>
import {
  Dialog,
  DialogPanel,
  DialogTitle,
  TransitionChild,
  TransitionRoot,
} from "@headlessui/vue";
const open = ref(true);
</script>
