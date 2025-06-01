<template>
  <section>
    <div class="px-2 lg:p-1 max-w-7xl my-4 mx-auto">
      <div class="pb-5 mb-4 sm:flex sm:items-center sm:justify-between">
        <CommonTitleIcon
          :filename="'seo-tag-min.png'"
          :title="'Keywords & Searches'"
        />
      </div>
      <BaseCard shape="rounded" class="box p-6 my-4">
        <p class="text-center text-xl font-semibold">Add SEO Tags & Keywords</p>
        <div
          class="search-area flex relative items-center max-w-md m-auto justify-center text-center my-4"
        >
          <input
            v-model="newTag"
            @keydown.enter="addNewTag"
            class="border border-slate-500/50 px-4 py-2 rounded-md w-full"
            type="text"
            placeholder="Search tags/keywords"
          />
          <button
            @click="addNewTag"
            class="absolute right-2 px-4 py-1 rounded-2xl"
          >
            + Add
          </button>
        </div>
        <BasePlaceload
          v-if="preloader"
          class="h-[20vh] w-full rounded opacity-35"
        />
        <div class="my-8" v-else>
          <h5 class="pb-2 text-sm font-medium">All Tags</h5>
          <div class="flex flex-wrap gap-2">
            <div
              class="flex relative tag-box"
              v-for="tag in tagList"
              :key="tag"
            >
              <div
                class="tag-action absolute bg-red-500 gap-2 px-1.5 z-10 -top-4 rounded hidden justify-center -right-4 py-1"
                @click="deleteTag(tag)"
              >
                <span>
                  <svg
                    class="h-3 w-3 cursor-pointer"
                    xmlns="http://www.w3.org/2000/svg"
                    width="20"
                    height="20"
                    viewBox="0 0 24 24"
                  >
                    <path
                      fill="#fff"
                      d="M19 6.41L17.59 5L12 10.59L6.41 5L5 6.41L10.59 12L5 17.59L6.41 19L12 13.41L17.59 19L19 17.59L13.41 12L19 6.41z"
                    />
                  </svg>
                </span>
              </div>
              <div
                class="icon bg-[#268cbf] flex items-center px-1.5 rounded-s-sm py-2"
              >
                <UIcon name="i-heroicons-tag-solid" class="text-white" />
              </div>
              <div
                class="relative w-max px-3 py-2 rounded-e-sm bg-[#39c] text-white text-xs flex items-center justify-center"
              >
                {{ tag.name }} ({{ tag.qty }})
              </div>
            </div>
          </div>
        </div>
      </BaseCard>
    </div>
  </section>
</template>

<script setup>
definePageMeta({
  layout: "dashboard",
});
const preloader = useState("preloader");
const Api = useApi();
const tagList = ref("");
async function getSearchTags() {
  const res = await Api.get("/api/ecommerce/dash/tags");
  tagList.value = res.data;
}
getSearchTags();
const newTag = ref("");
async function addNewTag(params) {
  if (newTag.value == "") return;
  const res = await Api.post("/api/ecommerce/dash/tags", {
    name: newTag.value,
  });
  getSearchTags();
  newTag.value = "";
}
async function deleteTag(tag) {
  const res = await Api.del("/api/ecommerce/dash/tags?id=" + tag.id);
  getSearchTags();
}
</script>

<style scoped>
.tag-box:hover .tag-action {
  display: flex;
}
</style>
