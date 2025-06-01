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
</script>

<template>
  <div class="dark:bg-muted-900">
    <LandingHero />
    <HomeServices />
    <LandingVideo />

    <LandingServices />
    <HomeMarqueeSlider />
    <HomeMarqueeSliderReverse />
    <LandingOverview />

    <LandingPlugins />
    <!-- <LandingDemos :limit="12" /> -->
    <!-- <LandingLayers /> -->
    <!-- <LandingLayouts /> -->

    <LandingFeatures />
    <LandingBenefits />
    <!-- <LandingCta /> -->
    <LandingContent />
  </div>
</template>
