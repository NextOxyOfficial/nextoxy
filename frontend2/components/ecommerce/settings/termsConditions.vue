<template>
  <div class="rounded my-5">
    <h6 class="my-4">Terms & Conditions</h6>
    <CommonTiptap
      :content="content.content"
      @updateContent="
        (newVal) => {
          content.content = newVal;
        }
      "
    />
    <BaseButton
      color="primary"
      @click="saveContent"
      type="submit"
      class="inline-flex gap-2 my-4 justify-center rounded-md border border-transparent bg-gray-800 py-2 px-4 text-sm font-medium text-white -sm hover:bg-gray-900 focus:outline-none focus:ring-2 focus:ring-gray-900 focus:ring-offset-2"
    >
      Save Changes
    </BaseButton>
  </div>
</template>

<script setup>
import Editor from "@tinymce/tinymce-vue";
const { notifs } = useAuth();
const Api = useApi();
const content = ref("uu");
async function getContent() {
  const response = await Api.get("/api/ecommerce/dash/pages?name=terms");
  console.log(response);
  content.value = response.data;
}
getContent();

async function saveContent() {
  const response = await Api.put("/api/ecommerce/dash/pages", content.value);
  console.log(response);
  notifs.value.push({
    type: "success",
    message: "Terms and conditions updated successfully",
  });
}
</script>

<style>
.tox-tinymce {
  height: 70vh !important;
  border-radius: 2px !important;
  border: 1px solid #e4e4e4 !important;
  box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1) !important;
  cursor: pointer;
}
</style>
