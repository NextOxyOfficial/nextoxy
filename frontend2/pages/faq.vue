<script setup lang="ts">
definePageMeta({
  title: 'The Nuxt & Tailwind CSS dashboard system',
  description:
    'Nuxt & Tailwind CSS dashboard system template that comes with 100+ prebuilt pages and 40+ custom UI components.',
  breadcrumb: {
    label: 'Tairo',
  },
  layout: 'landing',
})
const accordion = ref([
  {
    title: 'How do I get free .com domain?',
    content:
      'With our enterprise subscription, you will receive a complimentary .com domain at no additional cost.',
  },
  {
    title: 'Is registration free?',
    content:
      'Yes. Its absolutely free. Anyone can register anytime.',
  },
  {
    title: "How long my information will remain stored if I'm not willing to renew?",
    content:
      'In that case site will be live for 1 month and data will be stored for two months.',
  },
  {
    title: 'How many times will I able to change my themes?',
    content:
      "It's unlimited, if you have multiple themes subscription you can change over the theme one to another whenever you want.",
  },
  {
    title: 'Is it easy to build a website?',
    content:
      "It's very easy, Only takes a few minutes to setup your category and products. NextOxy has the guideline for registering, theme purchase, products upload, banners upload, payment methords etc. In addition the NextOxy 24/7 support team is ready to help at all round the clock.",
  },
  {
    title: 'Can I build a website without coding knowledge?',
    content:
      "Yes, you don't need any coding knowledge. NextOxy has it's own AI which can build front-end & back-end by it self for you.",
  },
  {
    title: 'Should I use a website builder or hire a developer?',
    content:
      'We have our own site editor features. Also you may hire an expert who can help you to complete your project simply.',
  },
  {
    title: 'Will I get SSL for free?',
    content:
      'Initially you will get a free SSL certificate. you may purchase premium for advance security encryption.',
  },
  {
    title: 'How many products can be uploaded?',
    content:
      "There has no limit of uploading products. So it's unlimited.",
  },
  {
    title: 'How my and clients data remain secured?',
    content:
      'For secure all data automatically encrypted to prevent data breaches.',
  },
  {
    title: 'Do you provide API for third party programs?',
    content:
      "NextOxy provides open source API's. So anyone can use this API's on third party programs.",
  },
  {
    title: 'Do you backup files and data?',
    content:
      "Yes, NextOxy securely stores all the data as long as they continue there subscription.",
  },
])
</script>

<template>
  <div>
    <section class="mx-auto w-full max-w-7xl px-4 pt-40">
        
        <div class="">

<!-- Page Title Area -->
<div class="relative z-1 text-center">
    <div class="sub-container px-4">
        <h1 class="font-black text-25px md:text-35px lg:text-[66px] text-black-color mb-8">Frequently Asked <span class="text-primary-color">Questions</span></h1>
        <p class="lg:text-[20px] text-17px lg:max-w-2xl lg:mx-auto leading-7 md:leading-8 text-optional-color">Find answers to common queries in our comprehensive Frequently Asked Questions section, designed to provide clarity and assistance on key topics and services.</p>
    </div>
    <div class="left-0 -bottom-90 absolute -z-1 hidden xl:inline"><img src="/static/frontend/images/home/shape/shape34.png" class="animate-custom-movebounce" alt="shape"></div>
    <div class="right-0 bottom-100 absolute -z-1 hidden xl:inline"><img src="/static/frontend/images/home/shape/shape35.png" class="animate-custom-movebounce" alt="shape"></div>
</div>

<!-- FAQ Area -->
<div class="py-18 bg-[#FBFBFB] bg-cover bg-no-repeat bg-center" style="background-image: url(/static/frontend/images/home/shape/bg6.jpg);">
    <section class="pb-10 pt-20 lg:pb-20 lg:pt-[120px]">
    <div class="container mx-auto">
        <div class="-mx-4 flex flex-wrap justify-center">
        <div class="w-full px-4 xl:w-10/12">
            <div class="md:max-w-3xl mx-auto">
                <BaseAccordion :items="accordion" action="plus" />
            </div>
        </div>
        </div>
    </div>
    </section>

</div>

</div>
    </section>
  </div>
</template>