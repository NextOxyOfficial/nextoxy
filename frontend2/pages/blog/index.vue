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
</script>

<template>
  <div class="mx-auto w-full max-w-7xl px-4 pt-36 pb-20">
    <div class="mb-3">
      <TairoContentWrapper>
        <h1 class="text-3xl font-semibold text-center mb-5">Blog</h1>
        <template #left>
          <div class="flex gap-[2px] items-center">
            <BaseInput
              v-model="filter"
              icon="lucide:search"
              shape="rounded"
              type="search"
              placeholder="Find theme..."
              :classes="{
                wrapper: 'w-full sm:w-auto',
              }"
              @keypress.enter="getPosts"
            />
            <BaseButton @click="getPosts" color="primary">Search</BaseButton>
          </div>
        </template>
        <template #right> </template>
        <div class="my-8">
          <img
            src="/static/frontend/images/blog.png"
            class="rounded-md w-full max-h-[400px]"
            alt="about-image"
          />
        </div>
        <div>
          <div v-if="posts && posts?.results.length === 0">
            <BasePlaceholderPage
              title="No matching results"
              subtitle="Looks like we couldn't find any matching results for your search terms. Try other search terms."
            >
              <template #image>
                <img
                  class="block dark:hidden"
                  src="/img/illustrations/placeholders/flat/placeholder-search-6.svg"
                  alt="Placeholder image"
                />
                <img
                  class="hidden dark:block"
                  src="/img/illustrations/placeholders/flat/placeholder-search-6-dark.svg"
                  alt="Placeholder image"
                />
              </template>
            </BasePlaceholderPage>
          </div>

          <div v-else>
            <h1 class="text-3xl font-semibold text-center mb-5">
              Read More Related Topics
            </h1>
            <hr class="mb-2 mt-8" />
            <div
              class="grid grid-cols-1 sm:grid-cols-3 lg:grid-cols-4 gap-6 mt-10"
            >
              <TransitionGroup
                enter-active-class="transform-gpu"
                enter-from-class="opacity-0 -translate-x-full"
                enter-to-class="opacity-100 translate-x-0"
                leave-active-class="absolute transform-gpu"
                leave-from-class="opacity-100 translate-x-0"
                leave-to-class="opacity-0 -translate-x-full"
              >
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
                    <p
                      class="text-sm mb-5 text-[#022b46] dark:text-slate-400 h-10"
                    >
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
              </TransitionGroup>
            </div>
            <div class="flex w-full justify-center">
              <BaseButton
                color="primary"
                @click="loadMore(posts.next)"
                v-if="posts && posts.next"
                >Load More</BaseButton
              >
            </div>
          </div>
        </div>
      </TairoContentWrapper>
    </div>
  </div>
</template>
