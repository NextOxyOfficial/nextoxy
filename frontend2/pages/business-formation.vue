<template>
  <section class="p-2">
    <!-- ====== Hero Section Start -->
    <div class=" relative z-10 overflow-hidden pb-[110px] pt-[120px] md:pt-[150px] lg:pt-[180px]" >
      <div
        class="dark:slate-800/10 absolute left-0 top-0 z-[-1] h-full w-full rounded-br-[200px] bg-slate-500/10 lg:w-1/2"
      ></div>
      <div class="max-w-7xl mx-auto">
        <div class="-mx-4 flex flex-wrap items-center">
          <div class="w-full px-4 lg:w-5/12">
            <div class="hero-content">
              <span class="text-primary-500 mb-4 block text-lg font-medium">
                Globalize Your Business
              </span>
              <h1
                class="text-dark mb-4 text-4xl font-bold !leading-[1.208] dark:PayPal sm:text-[42px] lg:text-[40px] xl:text-5xl"
              >
                Accept International <br />
                Payments More Easily
              </h1>
              <p
                class="text-body-color dark:text-dark-6 mb-16 max-w-[440px] text-base"
              >
                Get USA/UK - International bank accounts, Stripe, PayPal, Wise and other payment solutions from anywhere in the world. 
              </p>
              <BaseButton to="/account/services/formation" color="primary" class="inline-flex gap-1 items-center justify-center">
                <span>Apply Now</span>
                <Icon name="material-symbols:line-end-arrow-outline-rounded" class="h-5 w-5" />
              </BaseButton>
            </div>
          </div>
          <div class="hidden px-4 lg:block lg:w-1/12"></div>
          <div class="w-full px-4 lg:w-6/12">
            <div class="mx-auto text-center">
              <div class="relative z-10 mt-16 inline-block lg:mt-0">
                <img
                  src="/static/frontend/banners/globe33.png"
                  alt="hero"
                  class="mx-auto max-w-full"
                />
                <div class="absolute -left-10 -top-10 z-[-1]">
                  <img
                    src="https://cdn.tailgrids.com/1.0/assets/images/hero/hero6-shape-1.svg"
                    alt="shape"
                  />
                </div>
                <div class="absolute -left-20 top-1/2 z-[-1]">
                  <svg
                    width="40"
                    height="38"
                    viewBox="0 0 40 38"
                    fill="none"
                    xmlns="http://www.w3.org/2000/svg"
                  >
                    <path
                      d="M4.03852 10.0507C2.56762 6.4938 5.49873 2.67846 9.31451 3.18306L32.4926 6.24813C36.3084 6.75273 38.147 11.1988 35.8021 14.2511L21.5587 32.7914C19.2138 35.8436 14.444 35.2129 12.9731 31.656L4.03852 10.0507Z"
                      stroke="#13C296"
                      stroke-width="6"
                    />
                  </svg>
                </div>
                <div class="absolute -right-16 bottom-10 z-[-1]">
                  <svg
                    width="53"
                    height="53"
                    viewBox="0 0 53 53"
                    fill="none"
                    xmlns="http://www.w3.org/2000/svg"
                  >
                    <path
                      d="M0.923995 43.5761C3.73599 46.3881 7.07432 48.6187 10.7484 50.1406C14.4224 51.6624 18.3603 52.4457 22.337 52.4457C26.3138 52.4457 30.2516 51.6624 33.9257 50.1406C37.5997 48.6187 40.9381 46.3881 43.7501 43.5761C46.5621 40.7641 48.7927 37.4258 50.3145 33.7517C51.8363 30.0777 52.6196 26.1399 52.6196 22.1631C52.6196 18.1863 51.8363 14.2485 50.3145 10.5744C48.7927 6.90038 46.5621 3.56205 43.7501 0.750054L35.1655 9.3346C36.8502 11.0193 38.1865 13.0192 39.0982 15.2204C40.01 17.4215 40.4792 19.7806 40.4792 22.1631C40.4792 24.5456 40.01 26.9047 39.0982 29.1058C38.1865 31.3069 36.8502 33.3069 35.1655 34.9916C33.4808 36.6762 31.4809 38.0126 29.2797 38.9243C27.0786 39.836 24.7195 40.3053 22.337 40.3053C19.9546 40.3053 17.5954 39.836 15.3943 38.9243C13.1932 38.0126 11.1932 36.6762 9.50854 34.9916L0.923995 43.5761Z"
                      fill="#F9BA45"
                    />
                  </svg>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- ====== Hero Section End -->
    <h1
        class=" text-center max-w-5xl mx-auto mt-12 mb-6 text-4xl font-bold capitalize !leading-[1.208] text-dark dark:PayPal sm:text-[42px] lg:text-[40px] xl:text-6xl"
        >
        <span>Register your business in USA/UK. Give your business an </span>
        <span class="pl-0.5 text-primary-500">international standard</span>
    </h1>
    <p class="mx-auto max-w-5xl text-center text-muted-500">
      Empower your international aspirations. Register your business and open bank accounts in the USA and UK from abroad, making global entrepreneurship accessible and efficient.
    </p>

    <section class="max-w-7xl mx-auto my-20 flex flex-wrap gap-10 justify-between p-2">
        <div class="flex-1 max-w-[800px]">
          <BaseCard shape="curved" class="relative border-2 p-8 opacity-100 mb-6 cursor-pointer hover:scale-105 hover:border-primary-500 flex gap-3 w-full" :class="{'scale-105 !border-primary-500': country == 'USA'}" @click="country = 'USA'">
            <Icon name="emojione:flag-for-united-states" class="h-12 w-12" />
            <div class="flex-1">
                <p class="text-xl">United States</p>
                <p class="text-muted-500">USA Business Formation</p>
            </div>
            <TairoCheckAnimated class="opacity-1 grayscale" :class="{'grayscale-0': country == 'USA'}" />
          </BaseCard>
          <BaseCard shape="curved" class="relative border-2 p-8 opacity-100 mb-6 cursor-pointer hover:scale-105 hover:border-primary-500 flex gap-3 w-full" :class="{'scale-105 !border-primary-500': country == 'UK'}" @click="country = 'UK'">
            <Icon name="emojione:flag-for-united-kingdom" class="h-12 w-12" />
            <div class="flex-1">
                <p class="text-xl">United Kingdom</p>
                <p class="text-muted-500">UK Business Formation</p>
            </div>
            <TairoCheckAnimated class="opacity-1 grayscale" :class="{'grayscale-0': country == 'UK'}" />
          </BaseCard>
          <p class="mx-auto max-w-5xl text-center text-muted-500 my-5">
            Business bank account openings are subject to partner approval. NextOxy bears no responsibility. We ensure accurate and timely document submission.
          </p>
          <div class="flex w-full justify-end items-center">
            <BaseButton to="/account/services/formation" color="primary" size="xl" class="inline-flex gap-1 items-center justify-center">
              <span>Apply Now</span>
              <Icon name="material-symbols:line-end-arrow-outline-rounded" class="h-5 w-5" />
            </BaseButton>
          </div>
        </div>
      <div class="max-w-[450px]">
        <BaseRadioHeadless name="radio_custom" value="business">
          <BaseCard shape="curved" class="!border-primary-500 relative border-2 p-8 opacity-100">
            <div class="flex flex-col text-center text-muted-500" v-if="country == 'USA'">
              <img
                src="/static/img/illustrations/onboarding/pricing-3.svg"
                alt="2 factor authentication with app"
                class="mx-auto mb-3 max-w-[160px]"
              />
              <BaseHeading size="md" weight="medium">USA Business Formation</BaseHeading>
              <BaseParagraph
                size="xs"
                lead="snug"
                class="text-muted-500 dark:text-muted-500 mb-3"
              >
                An all-in-one plan for your business, with everything you need.
                Perfect for growing at large scale.
              </BaseParagraph>
              <div class="my-1 text-left flex items-center gap-1">
                <Icon
                  name="ph:check-circle-duotone"
                  class="text-info-500 h-4 w-4 mt-[-2]"
                />
                <p>Employer ID Number (EIN)</p>
              </div>
              <div class="my-1 text-left flex items-center gap-1">
                <Icon
                  name="ph:check-circle-duotone"
                  class="text-info-500 h-4 w-4 mt-[-2]"
                />
                <p>Open USA Business Bank Accounts</p>
              </div>
              <div class="my-1 text-left flex items-center gap-1">
                <Icon
                  name="ph:check-circle-duotone"
                  class="text-info-500 h-4 w-4 mt-[-2]"
                />
                <p>Articles Of Incorporation Certificate</p>
              </div>
              <div class="my-1 text-left flex items-center gap-1">
                <Icon
                  name="ph:check-circle-duotone"
                  class="text-info-500 h-4 w-4 mt-[-2]"
                />
                <p>ByLaw Documents</p>
              </div>
              <div class="my-1 text-left flex items-center gap-1">
                <Icon
                  name="ph:check-circle-duotone"
                  class="text-info-500 h-4 w-4 mt-[-2]"
                />
                <p>Registered USA Address</p>
              </div>
              <div class="my-1 text-left flex items-center gap-1">
                <Icon
                  name="ph:check-circle-duotone"
                  class="text-info-500 h-4 w-4 mt-[-2]"
                />
                <p>Registered Filing Agent</p>
              </div>
              <div class="flex items-center justify-center gap-2 pt-4">
                <BaseText>
                  <span>$299</span>
                  <span class="text-muted-500 text-xs"> (One Time)</span>
                </BaseText>
              </div>
            </div>
            <div class="flex flex-col text-center text-muted-500" v-if="country == 'UK'">
              <img
                src="/static/img/illustrations/onboarding/pricing-3.svg"
                alt="2 factor authentication with app"
                class="mx-auto mb-3 max-w-[160px]"
              />
              <BaseHeading size="md" weight="medium">UK Business Formation</BaseHeading>
              <BaseParagraph
                size="xs"
                lead="snug"
                class="text-muted-500 dark:text-muted-500 mb-3"
              >
                An all-in-one plan for your business, with everything you need.
                Perfect for growing at large scale.
              </BaseParagraph>
              <div class="my-1 text-left flex items-center gap-1">
                <Icon
                  name="ph:check-circle-duotone"
                  class="text-info-500 h-4 w-4 mt-[-2]"
                />
                <p>Business Registration Certificate</p>
              </div>
              <div class="my-1 text-left flex items-center gap-1">
                <Icon
                  name="ph:check-circle-duotone"
                  class="text-info-500 h-4 w-4 mt-[-2]"
                />
                <p>Business Wise</p>
              </div>
              <div class="my-1 text-left flex items-center gap-1">
                <Icon
                  name="ph:check-circle-duotone"
                  class="text-info-500 h-4 w-4 mt-[-2]"
                />
                <p>Business PayPal</p>
              </div>
              <div class="my-1 text-left flex items-center gap-1">
                <Icon
                  name="ph:check-circle-duotone"
                  class="text-info-500 h-4 w-4 mt-[-2]"
                />
                <p>Bank Account By Wise</p>
              </div>
              <div class="my-1 text-left flex items-center gap-1">
                <Icon
                  name="ph:check-circle-duotone"
                  class="text-info-500 h-4 w-4 mt-[-2]"
                />
                <p>Registered Filing Agent</p>
              </div>
              <div class="my-1 text-left flex items-center gap-1">
                <Icon
                  name="ph:check-circle-duotone"
                  class="text-info-500 h-4 w-4 mt-[-2]"
                />
                <p>UK Registered Address</p>
              </div>
              <div class="flex items-center justify-center gap-2 pt-4">
                <BaseText>
                  <span>$149</span>
                  <span class="text-muted-500 text-xs"> (One Time)</span>
                </BaseText>
              </div>
            </div>
            <div class="child absolute end-2 top-3 opacity-1">
              <Icon
                name="ph:check-circle-duotone"
                class="text-primary-500 h-7 w-7"
              />
            </div>
          </BaseCard>
        </BaseRadioHeadless>
      </div>
    </section>
      <div class="max-w-7xl mx-auto">
        <div class="-mx-4 flex flex-wrap items-center">
          <div class="w-full px-4 lg:w-5/12">
            <div class="mb-14 lg:mb-0">
              <span class="mb-4 block text-base font-medium text-primary-500"> Global entrepreneurship made easy </span>
              <h1 class="mb-3 text-3xl font-bold !leading-[1.208] PayPal xl:text-4xl">eCommerce & dropshipping endpoints :)</h1>
              <p class="text-gray-3 mb-9 max-w-[460px] text-base font-medium  text-muted-500">Register your business and open bank accounts in the USA and UK from abroad, ensuring a smooth start to your international ventures.</p>
            </div>
          </div>
          <div class="w-full px-4 lg:w-7/12">
            <div class="mx-auto text-center">
              <img src="/static/frontend/images/formation-feature-3.png" alt="image" class="mx-auto max-w-[400px]" />
            </div>
          </div>
        </div>
      </div>
      <div class="flex justify-start md:justify-center items-center w-full p-2 pt-20 mt-8">
        <BaseButton to="/account/services/formation" color="primary" size="xl" class="inline-flex gap-1 items-center justify-center text-xl relative">
          <img src="/static/frontend/images/formation-text.svg" alt="image" class="max-w-[250px] absolute top-[-120%] right-[-70%] md:right-[-110%]" />
          <span>Get Started!</span>
        </BaseButton>
      </div>
  </section>
</template>

<script setup>
definePageMeta({
  title: "The Nuxt & Tailwind CSS dashboard system",
  description:
    "Nuxt & Tailwind CSS dashboard system template that comes with 100+ prebuilt pages and 40+ custom UI components.",
  breadcrumb: {
    label: "Tairo",
  },
  layout: "landing",
});

const country = ref('USA')

</script>

<style scoped></style>
