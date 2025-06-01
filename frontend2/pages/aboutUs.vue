<script setup>
import { debounce } from "lodash";
definePageMeta({
  title: "The Nuxt & Tailwind CSS dashboard system",
  description:
    "Nuxt & Tailwind CSS dashboard system template that comes with 100+ prebuilt pages and 40+ custom UI components.",
  breadcrumb: {
    label: "Tairo",
  },
  layout: "landing",
});
const Api = useApi();

const posts = ref("");
const filter = ref("");
async function getPosts() {
  var url = "/api/account/blog/?type=blog";
  if (filter.value) {
    url += `&search=${encodeURIComponent(filter.value)}`;
  }
  const res = await Api.get(url);
  console.log(res);
  posts.value = res.data;
}
getPosts();
const debouncedGetPosts = debounce(getPosts, 1000);
const loadMore = async (url) => {
  url = url.split("/api/");
  url = "/api/" + url[1];
  const res = await Api.get(url);
  posts.value.results = [...posts.value.results, ...res.data.results];
  posts.value.next = res.data.next;
};

const blogs = [
  {
    title: "Introduction to JavaScript",
    description:
      "A beginner's guide to programming with JavaScript, covering basic syntax, variables, and control structures.",
    to: "https://example.com/intro-to-javascript",
  },
  {
    title: "Mastering CSS",
    description:
      "An advanced course on CSS, teaching techniques for creating responsive and visually appealing web designs.",
    to: "https://example.com/mastering-css",
  },
  {
    title: "Data Analysis with Python",
    description:
      "Learn how to use Python for data analysis, including libraries such as pandas, NumPy, and Matplotlib.",
    to: "https://example.com/data-analysis-python",
  },
  {
    title: "Understanding Machine Learning",
    description:
      "An overview of machine learning concepts, algorithms, and applications, designed for both beginners and experienced developers.",
    to: "https://example.com/understanding-ml",
  },
  {
    title: "Web Development with React",
    description:
      "A comprehensive guide to building dynamic web applications using the React library, covering components, state management, and hooks.",
    to: "https://example.com/web-dev-react",
  },
];
</script>

<template>
  <div class="pt-32 pb-20">
    <UContainer>
      <h1 class="text-3xl font-semibold text-center mb-5">About Us</h1>
      <div>
        <img
          src="/static/frontend/images/about-us.png"
          class="rounded-md w-full max-h-[400px]"
          alt="about-image"
        />
      </div>
      <hr class="mb-2 mt-8" />
      <div class="grid grid-cols-1 sm:grid-cols-3 lg:grid-cols-4 gap-6 mt-10">
        <UCard
          class="text-center overflow-hidden bg-[#f1f1f1]"
          v-for="(blog, index) in posts.results"
          :key="index"
          :ui="{
            header: {
              padding: 'px-0 py-0 sm:px-0',
            },
            body: {
              padding: 'px-0 py-0 sm:px-0 sm:p-0',
            },
          }"
        >
          <template #header>
            <div class="px-0">
              <img
                class="w-full h-40 bg-cover"
                :src="Api.baseURL + blog.image"
                :alt="blog.title"
              />
            </div>
          </template>
          <div class="p-6 h-full">
            <h2
              class="text-base font-semibold uppercase text-[#022b46] dark:text-slate-400 h-12"
            >
              {{ blog.title.slice(0, 40) }}
            </h2>
            <p class="text-sm mb-5 text-[#022b46] dark:text-slate-400 h-10">
              {{ blog.meta.slice(0, 60) }}
            </p>
            <ULink
              :to="'/blog/' + blog.id"
              active-class="text-primary"
              inactive-class="text-gray-500 dark:text-gray-400"
            >
              <PublicButton
                label="Read More"
                firstColor="bg-[#022b46]"
                secondColor="uppercase"
              />
            </ULink>
          </div>
        </UCard>
      </div>
    </UContainer>
  </div>
</template>

<style>
.abc:hover {
  background-image: linear-gradient(91.43deg, #4a00e0 1.22%, #8e2de2 98.84%);
}
.asd:hover {
  background-image: linear-gradient(90deg, #ff0080 67.19%, #ff8c00 100%);
}
.asf:hover {
  background-image: linear-gradient(91.43deg, #11998e 1.22%, #38ef7d 98.84%);
}
</style>
