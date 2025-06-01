<template>
  <div class="bg-muted-100 dark:bg-slate-700 py-8">
    <div class="container px-4 mx-auto">
      <div class="flex w-full flex-col">
        <div class="mx-auto w-full max-w-md text-center mb-6">
          <BaseHeading
            tag="h2"
            size="2xl"
            weight="bold"
            class="mt-4 md:!text-5xl"
          >
            Our Services
          </BaseHeading>
          <BaseParagraph size="sm" class="mb-3 mt-1">
            Please Read Our Terms & Conditions Before Availing Our Services.
          </BaseParagraph>
          <div
            class="divide-muted-200 dark:divide-muted-800 flex items-center justify-center divide-x"
          ></div>
        </div>
      </div>
      <div class="flex flex-wrap gap-x-1.5 gap-y-3 justify-center">
        <BaseCard
          v-for="(service, index) in services"
          :key="index"
          shape="curved"
          elevated-hover
          class="hover:!border-primary-500 group border-2 w-[calc(50%-6px)] md:w-[245px]"
        >
          <a
            v-if="service.newTab"
            :href="service.to"
            target="_blank"
            class="block p-6"
          >
            <div class="text-center">
              <Icon
                v-if="service.icon"
                :name="service.icon"
                class="group-hover:text-primary-500 text-success-400 h-10 w-10 transition-all duration-300 group-hover:rotate-6"
              />
              <img
                v-else
                class="h-10 transition-all duration-300 group-hover:rotate-2 mx-auto"
                :src="service.image"
                alt=""
                srcset=""
              />
              <BaseHeading
                tag="h3"
                size="sm"
                weight="semibold"
                class="mt-2 uppercase"
              >
                {{ service.title }}
              </BaseHeading>
              <BaseText size="sm" class="min-h-[36px]">
                {{ service.description }}
              </BaseText>
            </div>
          </a>
          <NuxtLink v-else :to="service.to" class="block p-6">
            <div class="text-center">
              <Icon
                v-if="service.icon"
                :name="service.icon"
                class="group-hover:text-primary-500 text-success-400 h-10 w-10 transition-all duration-300 group-hover:rotate-6"
              />
              <img
                v-else
                class="h-10 transition-all duration-300 group-hover:rotate-2 mx-auto"
                :src="service.image"
                alt=""
                srcset=""
              />
              <BaseHeading
                tag="h3"
                size="sm"
                weight="semibold"
                class="mt-2 uppercase"
              >
                {{ service.title }}
              </BaseHeading>
              <BaseText size="sm" class="min-h-[36px]">
                {{ service.description }}
              </BaseText>
            </div>
          </NuxtLink>
        </BaseCard>
      </div>
    </div>
  </div>
</template>

<script setup>
const services = [
  {
    title: "eCommerce Dropshipping",
    description: "eCommerce",
    icon: "material-symbols:shopping-bag-outline-sharp",
    to: "/account/ecommerce",
  },
  {
    title: "Blog",
    description: "Coming Soon",
    icon: "solar:ruler-cross-pen-bold-duotone",
    to: "/account/services/blog",
  },
  // {
  //   title: "Domain",
  //   description: "Purchase And Manage Domains",
  //   icon: "ph:users-four-duotone",
  //   to: "/account/services/domains",
  // },
  {
    title: "SEO Marketing",
    description: "Order SEO Marketing Services",
    icon: "ph:lock-open-duotone",
    to: "/account/services/seo",
  },
  {
    title: "Facebook Boosting",
    description: "Boost Your Facebook Page",
    icon: "ph:note-duotone",
    to: "/account/services/boosting",
  },
  {
    title: "Graphic Design",
    description: "Order Graphic Design Services",
    icon: "ph:upload-duotone",
    to: "/account/services/graphic",
  },
  {
    title: " UK & USA Business Formation ",
    description: " UK & USA Business Registration Service",
    icon: "fluent:building-bank-28-regular",
    to: "/business-formation",
  },
  {
    title: "OxyManager",
    description: "POS & SMS Marketing",
    image:
      "https://nextdropshipping.com/media/site_logo/imgs/nextdroplogo_2_FgAINnU.png",
    to: "https://oxymanager.com/",
    newTab: true,
  },
  {
    title: "Next Dropshipping",
    description: "Wholesale Marketplace",
    image:
      "https://nextdropshipping.com/media/site_logo/imgs/nextdroplogo_2_FgAINnU.png",
    to: "https://nextdropshipping.com/",
    newTab: true,
  },
  {
    title: "NDS Academy",
    description: "Invest With NDS",
    image:
      "https://nextdropshipping.com/media/site_logo/imgs/nextdroplogo_2_FgAINnU.png",
    to: "https://academy.nextdropshipping.com/",
    newTab: true,
  },
];
</script>

<style scoped></style>
