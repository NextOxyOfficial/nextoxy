<template>
  <div
    class="ltablet:gap-y-0 relative z-30 mt-32 grid grid-cols-12 gap-y-8 overflow-hidden sm:w-full sm:gap-x-16 lg:gap-y-0"
  >
    <div class="col-span-12">
      <div class="mx-auto flex flex-col lg:flex-row h-full w-full justify-center gap-9 items-center">
        <div class="text-left flex-1">
          <BaseText
            class="text-primary-500 mb-2 text-[0.65rem] uppercase tracking-wider"
            >Nuxt Ready</BaseText
          >
          <BaseHeading
            as="h2"
            size="4xl"
            weight="light"
            lead="tight"
            class="text-muted-800 mb-4 max-w-xl dark:text-white"
          >
            Manage Everything in One Workspace
          </BaseHeading>
          <BaseParagraph
            size="lg"
            class="text-muted-500 dark:text-muted-100 ptablet:max-w-lg ptablet:mx-auto mb-4 max-w-2xl"
          >
            NextOxy's all-in-one workspace allows you to effortlessly manage every aspect of your ecommerce and dropshipping business from a single platform.
          </BaseParagraph>
          <div class="card-list mt-6 grid grid-cols-2 md:grid-cols-3 w-full gap-4 max-w-[700px]" >
            <BaseCard shape="rounded" class="flex flex-col items-center text-center px-1 py-2 max-w-[220px]">
              <div class="nui-mask nui-mask-hexed relative mb-2 flex h-20 w-20 shrink-0 items-center justify-center" >
                <div
                  class="motion-safe:animate-spin-slow from-success-100 to-success-500 dark:from-success-800 absolute inset-0 flex h-full w-full items-center justify-center bg-gradient-to-tr blur-sm transition-all duration-200"
                ></div>
                <div
                  class="nui-mask nui-mask-hexed dark:bg-muted-800 flex h-[76px] w-[76px] items-center justify-center bg-white"
                >
                  <!-- <Icon
                    name="simple-icons:nuxtdotjs"

                    class="text-success-500 relative -top-0.5 h-7 w-7"
                  /> -->
                  <img src="/static/img/services/ecommerce.png" alt="">
                </div>
              </div>
              <BaseText size="md" class="text-muted-500 dark:text-muted-300"
                >eCommerce</BaseText
              >
            </BaseCard>
            <BaseCard shape="rounded" class="flex flex-col items-center text-center px-1 py-2 max-w-[220px]">
              <div
                class="nui-mask nui-mask-hexed relative mb-2 flex h-20 w-20 shrink-0 items-center justify-center"
              >
                <div
                  class="motion-safe:animate-spin-slow from-success-100 to-success-500 dark:from-success-800 absolute inset-0 flex h-full w-full items-center justify-center bg-gradient-to-tr blur-sm transition-all duration-200"
                ></div>
                <div
                  class="nui-mask nui-mask-hexed dark:bg-muted-800 flex h-[76px] w-[76px] items-center justify-center bg-white"
                >
                  <!-- <Icon
                    name="simple-icons:nuxtdotjs"

                    class="text-success-500 relative -top-0.5 h-7 w-7"
                  /> -->
                  <img src="/static/img/services/dropshipping.png" alt="">

                </div>
              </div>
              <BaseText size="md" class="text-muted-500 dark:text-muted-300"
                >Dropshipping</BaseText
              >
            </BaseCard>
            <BaseCard shape="rounded" class="flex flex-col items-center text-center px-1 py-2 max-w-[220px]">
              <div
                class="nui-mask nui-mask-hexed relative mb-2 flex h-20 w-20 shrink-0 items-center justify-center"
              >
                <div
                  class="motion-safe:animate-spin-slow [animation-delay: 0.3s] absolute inset-0 flex h-full w-full items-center justify-center bg-gradient-to-tr from-sky-100 to-sky-500 blur-sm transition-all duration-200 dark:from-sky-800"
                ></div>
                <div
                  class="nui-mask nui-mask-hexed dark:bg-muted-800 flex h-[76px] w-[76px] items-center justify-center bg-white"
                >
                  <!-- <Icon
                    name="simple-icons:tailwindcss"
                    class="h-8 w-8 text-sky-500"
                  /> -->
                  <img src="/static/img/services/digital-marketing.png" alt="">
                </div>
              </div>
              <BaseText size="md" class="text-muted-500 dark:text-muted-300"
                >Facebook Boosting</BaseText
              >
            </BaseCard>
            <BaseCard shape="rounded" class="flex flex-col items-center text-center px-1 py-2 max-w-[220px]">
              <div
                class="nui-mask nui-mask-hexed relative mb-2 flex h-20 w-20 shrink-0 items-center justify-center"
              >
                <div
                  class="motion-safe:animate-spin-slow [animation-delay: 0.6s] absolute inset-0 flex h-full w-full items-center justify-center bg-gradient-to-tr from-indigo-100 to-indigo-500 blur-sm transition-all duration-200 dark:from-indigo-800"
                ></div>
                <div
                  class="nui-mask nui-mask-hexed dark:bg-muted-800 flex h-[76px] w-[76px] items-center justify-center bg-white"
                >
                  <!-- <Icon
                    name="nonicons:typescript-16"
                    class="h-6 w-6 text-indigo-500"
                  /> -->
                  <img src="/static/img/services/seo.png" alt="">
                </div>
              </div>
              <BaseText size="md" class="text-muted-500 dark:text-muted-300"
                >Seo</BaseText
              >
            </BaseCard>
            <BaseCard shape="rounded" class="flex flex-col items-center text-center px-1 py-2 max-w-[220px]">
              <div
                class="nui-mask nui-mask-hexed relative mb-2 flex h-20 w-20 shrink-0 items-center justify-center"
              >
                <div
                  class="motion-safe:animate-spin-slow [animation-delay: 0.6s] absolute inset-0 flex h-full w-full items-center justify-center bg-gradient-to-tr from-indigo-100 to-indigo-500 blur-sm transition-all duration-200 dark:from-indigo-800"
                ></div>
                <div
                  class="nui-mask nui-mask-hexed dark:bg-muted-800 flex h-[76px] w-[76px] items-center justify-center bg-white"
                >
                  <!-- <Icon
                    name="nonicons:typescript-16"
                    class="h-6 w-6 text-indigo-500"
                  /> -->
                  <img src="/static/img/services/graphics-design.png" alt="">
                </div>
              </div>
              <BaseText size="md" class="text-muted-500 dark:text-muted-300"
                >Graphics Design</BaseText
              >
            </BaseCard>
            <BaseCard shape="rounded" class="flex flex-col items-center text-center px-1 py-2 max-w-[220px]">
              <div
                class="nui-mask nui-mask-hexed relative mb-2 flex h-20 w-20 shrink-0 items-center justify-center"
              >
                <div
                  class="motion-safe:animate-spin-slow [animation-delay: 0.6s] absolute inset-0 flex h-full w-full items-center justify-center bg-gradient-to-tr from-indigo-100 to-indigo-500 blur-sm transition-all duration-200 dark:from-indigo-800"
                ></div>
                <div
                  class="nui-mask nui-mask-hexed dark:bg-muted-800 flex h-[76px] w-[76px] items-center justify-center bg-white"
                >
                  <!-- <Icon
                    name="nonicons:typescript-16"
                    class="h-6 w-6 text-indigo-500"
                  /> -->
                  <img src="/static/img/services/graphics-design.png" alt="">
                </div>
              </div>
              <BaseText size="md" class="text-muted-500 dark:text-muted-300"
                >Business Formation</BaseText
              >
            </BaseCard>
          </div>
        </div>
        <img src="/static/frontend/banners/globe33.png" class="object-contain" alt="" srcset="">
      </div>
    </div>
  </div>
</template>
