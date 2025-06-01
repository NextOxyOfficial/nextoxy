<template>
    <div aria-live="assertive" class="z-[999] pointer-events-none fixed inset-0 flex flex-col justify-end items-start p-6 bottom-0 sm:items-start sm:p-4" v-if="notifs">
      <div class="flex w-full flex-col items-center space-y-4 sm:items-start">
        <TransitionGroup enter-active-class="transform ease-out duration-900 transition" enter-from-class="translate-y-2 opacity-0 sm:translate-y-0 sm:translate-x-2" enter-to-class="translate-y-0 opacity-100 sm:translate-x-0" leave-active-class="transition ease-in duration-100" leave-from-class="opacity-100" leave-to-class="opacity-0">
          <div v-for="notif in notifs" :key="notif" class="pointer-events-auto w-full max-w-sm overflow-hidden rounded-lg bg-gradient-to-r from-slate-50 via-slate-200/70 to-slate-200/50 shadow-lg ring-1 ring-black ring-opacity-5">
            <div class="p-4">
              <div class="flex items-start">
                <div class="flex-shrink-0">
                  <CheckCircleIcon class="h-6 w-6 text-green-400" aria-hidden="true" v-if="notif.type=='success'" />
                  <ExclamationTriangleIcon class="h-6 w-6 text-rose-400" aria-hidden="true" v-if="notif.type=='error'" />
                  <ExclamationTriangleIcon class="h-6 w-6 text-yellow-400" aria-hidden="true" v-if="notif.type=='warning'" />
                  <ChatBubbleLeftIcon class="h-6 w-6 text-indigo-400" aria-hidden="true" v-if="notif.type=='info'" />
                </div>
                <div class="ml-3 w-0 flex-1 pt-0.5">
                  <p class="text-sm font-medium text-gray-900">{{ notif.title }}</p>
                  <p class="mt-1 text-sm text-gray-500">{{ notif.message }}</p>
                </div>
                <div class="ml-4 flex flex-shrink-0">
                  <button @click="dismiss(notif)" type="button" class="inline-flex rounded-md bg-indigo-800 opacity-70 text-gray-400 hover:text-gray-500 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2">
                    <span class="sr-only">Close</span>
                    <XMarkIcon class="h-5 w-5" aria-hidden="true" />
                  </button>
                </div>
              </div>
            </div>
          </div>
        </TransitionGroup>
      </div>
    </div>
  </template>
  
  <script setup>
    import { CheckCircleIcon, ExclamationTriangleIcon, ChatBubbleLeftIcon } from '@heroicons/vue/24/outline'
    import { XMarkIcon } from '@heroicons/vue/20/solid'
    const {notifs} = useAuth()
    function dismiss(notif){
        notifs.value = notifs.value.filter(n => n != notif)
    }

    function autoDismiss(notif){
        setTimeout(() => {
            dismiss(notif)
        }, 3000);
    }
    setInterval(()=>{
        if(notifs.value.length > 0){
          autoDismiss(notifs.value[0])
        }
    }, 2500)
  </script>