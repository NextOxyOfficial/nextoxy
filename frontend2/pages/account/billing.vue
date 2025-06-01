<template>
  <section class="relative z-10 overflow-hidden py-8">
    <div class="container mx-auto">
      <div
        class="border-b border-gray-200/10 pb-5 sm:flex sm:items-center sm:justify-between"
      >
        <CommonTitleIcon
          :filename="'pages-min.png'"
          :title="'Billing History'"
        />
      </div>
      <TairoFlexTable
        v-if="invoices && invoices.results"
        class="stripe billing"
      >
        <template #header>
          <TairoFlexTableHeading class="max-w-[250px]" type="grow"
            >Date</TairoFlexTableHeading
          >
          <TairoFlexTableHeading type="grow">Invoice ID</TairoFlexTableHeading>
          <TairoFlexTableHeading type="stable">Product</TairoFlexTableHeading>
          <TairoFlexTableHeading type="stable">Type</TairoFlexTableHeading>
          <TairoFlexTableHeading type="stable">Status</TairoFlexTableHeading>
          <TairoFlexTableHeading type="stable">Action</TairoFlexTableHeading>
        </template>

        <TairoFlexTableRow
          v-for="invoice in invoices.results"
          :key="invoice.id"
          shape="straight"
        >
          <TairoFlexTableCell
            type="grow"
            data-content="Member"
            class="max-w-[250px]"
          >
            <div class="flex items-center">
              <div class="ms-3 leading-none">
                {{ invoice.created_at }}
              </div>
            </div>
          </TairoFlexTableCell>

          <TairoFlexTableCell
            class="whitespace-nowrap"
            type="grow"
            data-content="Expertise"
            light
          >
            {{ invoice.order_id }}
          </TairoFlexTableCell>
          <TairoFlexTableCell
            class="whitespace-nowrap"
            type="stable"
            data-content="Expertise"
            light
          >
            {{ invoice.action }}
          </TairoFlexTableCell>

          <TairoFlexTableCell type="stable" data-content="Actions">
            {{ invoice.type }}
          </TairoFlexTableCell>
          <TairoFlexTableCell type="stable" data-content="Actions">
            <h4 class="font-sans text-sm font-medium whitespace-nowrap">
              USD ${{ invoice.amount }}
            </h4>
          </TairoFlexTableCell>
          <TairoFlexTableCell type="stable" data-content="Actions">
            <nuxt-link
              :to="'/account/checkout/' + invoice.id"
              v-if="!invoice.paid && !invoice.cancelled"
            >
              <BaseButton
                @click="payNow(order)"
                class="border border-success-400 border-dashed !font-xs"
                size="sm"
                color="success"
                flavor="pastel"
              >
                <span class="text-xs">Pay Now</span>
              </BaseButton>
            </nuxt-link>
            <BaseTag
              color="info"
              shape="full"
              flavor="pastel"
              size="sm"
              class="capitalize text-center"
              v-else-if="invoice.paid"
            >
              Paid
            </BaseTag>
            <BaseTag
              color="warning"
              shape="full"
              flavor="pastel"
              size="sm"
              class="capitalize text-center"
              v-else-if="invoice.cancelled"
            >
              Cancelled
            </BaseTag>
          </TairoFlexTableCell>
          <TairoFlexTableCell type="stable" data-content="Actions">
            <span v-if="!invoice.paid && !invoice.cancelled">
              <BaseButton
                @click="cancelNow(invoice.id)"
                class="w-full border-rose-400 border-dashed !font-xs"
                size="sm"
                color="danger"
                flavor="pastel"
              >
                <span class="text-xs">Cancel</span>
              </BaseButton>
            </span>
            <BaseTag
              color="success"
              shape="full"
              flavor="pastel"
              size="sm"
              class="capitalize w-full text-center opacity-5"
              v-else
            >
              ---
            </BaseTag>
          </TairoFlexTableCell>
        </TairoFlexTableRow>
      </TairoFlexTable>
    </div>
    <div class="flex items-center justify-center my-2">
      <BaseButton
        shape="rounded"
        class="flex w-[200px] justify-center"
        @click="loadMore(invoices.next)"
        v-if="invoices && invoices.next"
      >
        Load More
      </BaseButton>
      <p v-else class="w-full text-muted-500 text-center text-xs">
        End of list.
      </p>
    </div>
  </section>
</template>

<script setup>
import {
  Dialog,
  DialogPanel,
  DialogTitle,
  TransitionChild,
  TransitionRoot,
} from "@headlessui/vue";
import Editor from "@tinymce/tinymce-vue";
definePageMeta({
  layout: "dashboard",
});
const { notifs } = useAuth();
const { $swal } = useNuxtApp();
const Api = useApi();
const { shop } = useShop();
const invoices = ref("");
async function getInvoices() {
  const response = await Api.get("/api/account/invoices");
  invoices.value = response.data;
}
getInvoices();
async function cancelNow(id) {
  const response = await Api.get("/api/account/invoices?cancel=" + id);
  invoices.value = response.data;
}
const loadMore = async (url) => {
  var url = url.split("/api/account/invoices");
  url = url[url.length - 1];
  const response = await Api.get("/api/account/invoices" + url);
  invoices.value.results = invoices.value.results.concat(response.data.results);
  invoices.value.next = response.data.next;
};
</script>

<style>
.stripe.billing .gap-y-4 {
  gap: 1px !important;
}
.stripe.billing .gap-y-4 > div:nth-child(odd) {
  background: rgba(214, 214, 214, 0.068);
}
</style>
