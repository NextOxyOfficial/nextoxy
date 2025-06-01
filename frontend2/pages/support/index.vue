<template>
  <div>
    <h1 class="mb-3 text-2xl font-semibold">Support tickets</h1>
    <BaseCard
      class="flex flex-col md:flex-row gap-4 md:p-6 !border-none"
      v-if="all_tickets?.length > 0"
    >
      <div
        class="w-full md:w-[384px] bg-slate-50/90 dark:bg-slate-900 max-w-sm border rounded-md p-3"
      >
        <div
          class="bg-slate-200 dark:bg-slate-700 py-2.5 md:py-4 rounded-ss-lg rounded-se-lg"
        >
          <h2 class="font-semibold text-lg md:text-2xl text-center">
            My Tickets
          </h2>
        </div>
        <div
          class="border-l dark:border-none pl-2 h-[160px] md:h-auto overflow-y-scroll md:overflow-auto py-2"
        >
          <div
            class="p-2.5 border-b last-of-type:border-0 mb-2 cursor-pointer hover:bg-slate-300/10 text-sm"
            :class="{
              'bg-blue-100 rounded-md shadow-lg':
                selectedTicket && selectedTicket.id == t.id,
            }"
            v-for="t in all_tickets"
            :key="t"
            @click="selectTicket(t)"
          >
            <div class="block gap-1">
              <div class="flex gap-1">
                <p>
                  <strong class="flex">ID#</strong>
                </p>
                <p>
                  <strong class="text-[#58608a]">NXOA09{{ t.id }}</strong>
                </p>
              </div>
              <p class="sentence-case my-1 flex gap-1">
                <span class="font-semibold">Subject: </span>
                <span
                  v-if="t.subject.length > 35"
                  class="first-letter:uppercase inline-block"
                  >{{ t.subject.slice(0, 35) }} ...
                </span>
                <span v-else class="first-letter:uppercase inline-block"
                  >{{ t.subject }}
                </span>
              </p>
            </div>
            <em class="text-xs">Created at: {{ t.created_at }}</em>
          </div>
        </div>
      </div>
      <div class="flex-1 border p-3 rounded-md">
        <h2 class="my-2 text-lg font-semibold md:hidden">Chat</h2>
        <div class="flex flex-col" v-if="selectedTicketMessages">
          <section
            class="flex-1 overflow-y-scroll min-h-[50vh] max-h-[80vh] pb-4"
          >
            <div
              class="border p-2.5 mb-2.5 last-of-type:mb-0 w-3/5 rounded-xl pl-6 shadow"
              :class="
                m.by_admin
                  ? 'ml-auto  rounded-se-none mr-2 bg-green-100'
                  : 'rounded-es-none'
              "
              v-for="m in selectedTicketMessages"
              :key="m"
            >
              <p class="first-letter:uppercase">{{ m.content }}</p>
              <small class="italic">{{ m.created_at }}</small>
              <a
                v-if="m.image"
                :href="Api.baseURL + m.image"
                target="_blank"
                class="group relative w-full h-full max-w-[200px] max-h-[200px] block"
              >
                <span
                  class="absolute z-20 left-[50%] top-[50%] translate-x-[-50%] translate-y-[-50%] hidden group-hover:inline-flex px-4 py-1 justify-center items-center text-white bg-slate-800/70 rounded"
                >
                  <UIcon name="i-heroicons-eye-solid" />
                </span>
                <img
                  :src="Api.baseURL + m.image"
                  alt=""
                  srcset=""
                  class="w-full h-full object-contain rounded"
                />
              </a>
            </div>
          </section>
          <section class="p-3 mt-4">
            <BaseCard shape="rounded" class="p-2.5">
              <BaseTextarea
                v-model="replyMessage"
                rows="2"
                class="mb-3 !text-gray-700 dark:!text-slate-100"
                label="Message"
                shape="rounded"
                placeholder="Write a message..."
                color-focus
              />
              <BaseInputFile
                v-model="second"
                @click="imageUploaded"
                shape="rounded"
                label="Attachment"
                class="text-gray-700 dark:text-slate-100"
              />
              <p class="text-sm">
                <span class="text-red-500">*</span> Max file size allowed is 5MB
                and supported file png, jpg, pdf, mp4
              </p>
              <BaseButtonAction
                @click="replyTicket"
                class="mt-4"
                shape="rounded"
                color="primary"
                >Reply</BaseButtonAction
              >
            </BaseCard>
          </section>
        </div>
        <p v-else>Select a message</p>
      </div>
    </BaseCard>
    <BasePlaceholderPage
      v-else
      title="No tickets available"
      subtitle="Please create a ticket to start the conversion"
    >
      <template #image>
        <UIcon
          name="i-heroicons-chat-bubble-oval-left-ellipsis"
          class="text-8xl"
        />
      </template>
    </BasePlaceholderPage>
  </div>
</template>

<script setup>
definePageMeta({
  layout: "dashboard",
});
const Api = useApi();
const all_tickets = ref();
getTickets();
async function getTickets() {
  const { data } = await Api.get("/api/auth/tickets/");
  all_tickets.value = data;
}
const selectedTicket = ref();
const selectedTicketMessages = ref();
async function selectTicket(t) {
  selectedTicket.value = t;
  const { data } = await Api.get("/api/auth/tickets/?tid=" + t.id);
  selectedTicketMessages.value = data;
}
const replyMessage = ref();
const attachment = ref();
async function replyTicket() {
  const { data } = await Api.post(
    "/api/auth/tickets/?tid=" + selectedTicket.value.id,
    {
      message: replyMessage.value,
      tid: selectedTicket.value.id,
      image: attachment.value,
    }
  );
  selectedTicketMessages.value = data;
  replyMessage.value = null;
  replyAttachment.value = null;
}
function imageUploaded(e) {
  let reader = new FileReader();
  reader.onload = function () {
    attachment.value = reader.result;
  };
  reader.readAsDataURL(e.target.files[0]);
}
</script>

<style scoped></style>
