// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  modules: [
    "nuxt-swiper",
    "@nuxt/ui",
    "@nuxtjs/tailwindcss",
    "@cssninja/nuxt-toaster",
    "@vueuse/nuxt",
  ],
  extends: ["@shuriken-ui/nuxt"],
  ssr: false,
  // app: {
  // 	buildAssetsDir: "/static/frontend",
  // },
  css: [
    "~/assets/css/colors.css",
    "@fontsource-variable/fira-code/index.css",
    "@fontsource-variable/inter/index.css",
    "@fontsource-variable/karla/index.css",
  ],
});
