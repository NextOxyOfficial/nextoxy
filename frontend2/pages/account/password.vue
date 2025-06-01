<script setup lang="ts">
import Slider from '@vueform/slider'
import '~/assets/css/slider.css'

definePageMeta({
    layout: 'dashboard',
})

const toaster = useToaster()

const showPasswordField = ref(false)
const passwordScore = ref(0)

const old_password = ref('')
const password = ref('')
const password_confirm = ref('')



function checkStrength() {
  if (!password.value) return (passwordScore.value = 0)
  passwordScore.value = 1
}
function changePassword() {
  console.log(123);
  if(!password.value || !password_confirm.value || !old_password.value){
    toaster.show({
      title: 'All Fields Are Required.',
      message: 'Your Password Has Not Changed',
      color: 'danger',
      icon: 'material-symbols:cancel-rounded',
      closable: true,
    })
    return
  }
  if(password.value != password_confirm.value){
    toaster.show({
      title: 'New Password Does Not Match.',
      message: 'Your Password Has Not Changed',
      color: 'danger',
      icon: 'material-symbols:cancel-rounded',
      closable: true,
    })
    return
  }
  const data = {}
  Api.post('/api/account/password/',data).then(res => {
      toaster.show({
        title: 'Shop Deletion Successful.',
        message: 'Your Shop Has Been Deleted Successfully',
        color: 'success',
        icon: 'lucide:check',
        closable: true,
      })
  })
}

</script>

<template>
  <div class="relative py-3 sm:mx-auto sm:max-w-xl">
    <BaseCard shape="curved" class="relative px-4 py-10 sm:p-10 md:mx-0">
      <div class="mx-auto max-w-md">
        <div class="flex items-center gap-4">
          <div
            class="bg-primary-500/20 text-primary-500 flex h-14 w-14 shrink-0 items-center justify-center rounded-full font-sans text-2xl"
          >
            <Icon name="ph:lock-duotone" class="h-5 w-5" />
          </div>
          <div class="text-muted-700 block text-xl font-semibold">
            <BaseHeading
              as="h3"
              size="lg"
              weight="medium"
              class="text-muted-800 dark:text-muted-100"
            >
              New Password
            </BaseHeading>
            <BaseText size="sm" class="text-muted-400"
              >Change Your password.</BaseText
            >
          </div>
        </div>
        <div class="divide-muted-200 dark:divide-muted-700 divide-y">
          <div class="text-muted-800 mx-auto w-full pt-5">
            <div class="relative mb-2">
              <label
                class="text-muted-500 dark:text-muted-400 mb-2 block text-xs font-semibold"
                >Old password</label
              >
              <BaseInput
                v-model="old_password"
                :type="showPasswordField ? 'password' : 'text'"
                shape="curved"
                placeholder="Password"
                @input="checkStrength()"
              >
                <template #action>
                  <button
                    class="leading-0 text-muted-400 peer-focus-within:text-primary-500 absolute right-0 top-0 flex h-10 w-10 items-center justify-center text-center text-xl"
                    @click.prevent="showPasswordField = !showPasswordField"
                  >
                    <div
                      class="relative flex h-full w-full items-center justify-center"
                      :data-nui-tooltip="`${
                        showPasswordField ? 'Show' : 'Hide'
                      } password`"
                    >
                      <Icon
                        :name="
                          showPasswordField
                            ? 'mdi:eye-outline'
                            : 'mdi:eye-off-outline'
                        "
                        class="h-5 w-5"
                      />
                    </div>
                  </button>
                </template>
              </BaseInput>
            </div>
            <hr class="border-muted-200 dark:border-muted-700 my-5 h-px border bg-transparent"/>
            <div class="relative mb-2">
              <label
                class="text-muted-500 dark:text-muted-400 mb-2 block text-xs font-semibold"
                >New password</label
              >
              <BaseInput
                v-model="password"
                :type="showPasswordField ? 'password' : 'text'"
                shape="curved"
                placeholder="Password"
                @input="checkStrength()"
              >
                <template #action>
                  <button
                    class="leading-0 text-muted-400 peer-focus-within:text-primary-500 absolute right-0 top-0 flex h-10 w-10 items-center justify-center text-center text-xl"
                    @click.prevent="showPasswordField = !showPasswordField"
                  >
                    <div
                      class="relative flex h-full w-full items-center justify-center"
                      :data-nui-tooltip="`${
                        showPasswordField ? 'Show' : 'Hide'
                      } password`"
                    >
                      <Icon
                        :name="
                          showPasswordField
                            ? 'mdi:eye-outline'
                            : 'mdi:eye-off-outline'
                        "
                        class="h-5 w-5"
                      />
                    </div>
                  </button>
                </template>
              </BaseInput>
            </div>
            <TairoPasswordStrength :value="password" />
            <div class="relative my-2">
              <label
                class="text-muted-500 dark:text-muted-400 mb-2 block text-xs font-semibold"
                >Confirm New password</label
              >
              <BaseInput
                v-model="password_confirm"
                :type="showPasswordField ? 'password' : 'text'"
                shape="curved"
                placeholder="Password"
                @input="checkStrength()"
              >
                <template #action>
                  <button
                    class="leading-0 text-muted-400 peer-focus-within:text-primary-500 absolute right-0 top-0 flex h-10 w-10 items-center justify-center text-center text-xl"
                    @click.prevent="showPasswordField = !showPasswordField"
                  >
                    <div
                      class="relative flex h-full w-full items-center justify-center"
                      :data-nui-tooltip="`${
                        showPasswordField ? 'Show' : 'Hide'
                      } password`"
                    >
                      <Icon
                        :name="
                          showPasswordField
                            ? 'mdi:eye-outline'
                            : 'mdi:eye-off-outline'
                        "
                        class="h-5 w-5"
                      />
                    </div>
                  </button>
                </template>
              </BaseInput>
            </div>
            <div
              class="mt-6 flex flex-col gap-2 sm:flex-row"
            >
              <BaseButton
                color="primary"
                shape="curved"
                class="!h-12 w-full"
                @click="changePassword()"
              >
                <Icon name="ph:arrows-clockwise" class="h-5 w-5" />
                <span>Change Password</span>
              </BaseButton>
            </div>
          </div>
        </div>
      </div>
    </BaseCard>
  </div>
</template>
