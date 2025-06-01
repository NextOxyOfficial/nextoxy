<script setup lang="ts">
import { debounce } from "lodash";
definePageMeta({
  layout: "dashboard",
});
const preloader = useState("preloader");
const Api = useApi();
const { shop } = useShop();

const route = useRoute();
const router = useRouter();
const page = computed(() => parseInt((route.query.page as string) ?? "1"));

const filter = ref("");
const perPage = ref(10);

watch([filter, perPage], () => {
  router.push({
    query: {
      page: undefined,
    },
  });
});

const query = computed(() => {
  return {
    filter: filter.value,
    perPage: perPage.value,
    page: page.value,
  };
});
const products = ref("");

const getProducts = async () => {
  const response = await Api.get("/api/ecommerce/dash/products");
  products.value = response.data;
};
getProducts();
const delProduct = async (id) => {
  const response = await Api.get("/api/ecommerce/dash/products?del=" + id);
  products.value = response.data;
};
const loadMore = async (url) => {
  var url = url.split("/api/ecommerce/dash/products");
  url = url[url.length - 1];
  const response = await Api.get("/api/ecommerce/dash/products" + url);
  products.value.results = products.value.results.concat(response.data.results);
  products.value.next = response.data.next;
};
const search = ref("");
const searchProduct = async () => {
  const response = await Api.get(
    "/api/ecommerce/dash/products?search=" + search.value
  );
  products.value = response.data;
  filter.value = true;
};
const debouncedSearchProduct = debounce(searchProduct, 1000);
</script>

<template>
  <div>
    <TairoContentWrapper>
      <template #left>
        <span class="relative">
          <BaseInput
            v-model="search"
            icon="lucide:search"
            placeholder="Find products..."
            shape="full"
            :classes="{
              wrapper: 'w-full sm:w-auto',
            }"
            @keyup="debouncedSearchProduct"
          />
          <svg
            v-if="shop.local_active"
            class="absolute top-[50%] translate-y-[-50%] right-2 rounded"
            xmlns="http://www.w3.org/2000/svg"
            width="22"
            height="22"
            viewBox="0 0 24 24"
          >
            <path
              fill="none"
              stroke="currentColor"
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="1.5"
              d="M10 12V6h1m-1 6h1V6m-1 12v-3h1m0 0v3h-1M7 6v6m0 3v3m7-12v6m0 3v3m3-12v6m0 3v3M6 3H3v3m-1 6h20m-4-9h3v3M6 21H3v-3m15 3h3v-3"
            />
          </svg>
        </span>
      </template>
      <template #right>
        <nuxt-link to="/ecommerce/productadd/add">
          <BaseButtonAction
            color="success"
            class="px-4 py-4 h-[40px] whitespace-nowrap"
            muted
            >Add Product</BaseButtonAction
          >
        </nuxt-link>
        <!-- <BaseSelect
          v-model="perPage"
          label=""
          :classes="{
            wrapper: 'w-full sm:w-40',
          }"
        >
          <option :value="10">10 per page</option>
          <option :value="25">25 per page</option>
          <option :value="50">50 per page</option>
          <option :value="100">100 per page</option>
        </BaseSelect> -->
      </template>
      <BasePlaceload
        v-if="preloader"
        class="h-[50vh] w-full rounded opacity-35"
      />
      <div v-else>
        <div v-if="products && products.results.length === 0" class="mt-28">
          <BasePlaceholderPage
            title="Add your first product"
            subtitle="Start your eCommerce journey with NextOxy by adding your first product"
          >
            <template #image>
              <img
                class="block dark:hidden"
                src="/static/frontend/images/no-product.png"
                alt="Placeholder image"
              />
              <img
                class="hidden dark:block"
                src="/static/frontend/images/no-product.png"
                alt="Placeholder image"
              />
            </template>
          </BasePlaceholderPage>
        </div>
        <div v-else>
          <div class="w-full">
            <TairoTable shape="rounded">
              <template #header>
                <TairoTableHeading uppercase spaced>Product</TairoTableHeading>
                <TairoTableHeading uppercase spaced>Name</TairoTableHeading>
                <TairoTableHeading uppercase spaced>Sku</TairoTableHeading>
                <TairoTableHeading uppercase spaced>Price</TairoTableHeading>
                <TairoTableHeading uppercase spaced>Stock</TairoTableHeading>
                <TairoTableHeading uppercase spaced>Category</TairoTableHeading>
                <TairoTableHeading uppercase spaced>Action</TairoTableHeading>
              </template>

              <TairoTableRow v-for="item in products.results" :key="item.id">
                <TairoTableCell spaced>
                  <div class="flex items-center">
                    <img
                      v-if="item.productimage_set.length > 0"
                      :src="Api.baseURL + item.productimage_set[0].thumbnail"
                      alt="item.name"
                      class="max-w-[80px]"
                    />
                    <img
                      v-else
                      src="https://via.placeholder.com/200"
                      alt="No Image"
                      class="max-w-[80px]"
                    />
                  </div>
                </TairoTableCell>
                <TairoTableCell spaced>
                  <p
                    class="max-w-[420px] whitespace-pre-wrap text-base first-letter:uppercase"
                  >
                    <nuxt-link :to="'/ecommerce/productadd/' + item.id">{{
                      item.name
                    }}</nuxt-link>
                  </p>
                  <p class="text-xs mb-1">
                    ID: {{ item.id }}, Created On: {{ item.created_at }}
                  </p>
                  <p class="px-1 py-[1px] bg-slate-500/10 inline">
                    {{ item.highlight }}
                  </p>
                </TairoTableCell>
                <TairoTableCell light spaced>
                  <p v-if="item.sku">{{ item.sku }}</p>
                  <p v-else>N/A</p>
                </TairoTableCell>
                <TairoTableCell spaced>
                  <p class="">Buy {{ shop.currency }}{{ item.buy_price }}</p>
                  <p class="">Sale {{ shop.currency }}{{ item.sale_price }}</p>
                  <p class="">
                    Est. Profit {{ shop.currency
                    }}{{ item.buy_price - item.sale_price }}
                  </p>
                </TairoTableCell>
                <TairoTableCell light spaced>
                  {{ item.stock }}
                </TairoTableCell>
                <TairoTableCell light spaced>
                  <span
                    class="text-primary-500 text-sm font-medium mr-1 mb-1"
                    v-for="(cat, ind) in item.categories"
                    :key="ind"
                  >
                    {{ cat.name }}
                    <span v-if="item.categories.length - 1 != ind">,</span>
                  </span>
                </TairoTableCell>
                <TairoTableCell spaced class="">
                  <div class="flex gap-1 items-center justify-center">
                    <nuxt-link :to="'/ecommerce/productadd/' + item.id">
                      <BaseButton color="success" size="sm"
                        ><Icon name="ic:twotone-edit" class="h-4 w-4"
                      /></BaseButton>
                    </nuxt-link>
                    <nuxt-link
                      target="_blank"
                      class=""
                      v-if="shop.local_active"
                      :to="'/ecommerce/barcode/' + item.id"
                    >
                      <BaseButton color="success" flavor="pastel">
                        <Icon name="ion:ios-barcode-outline" class="h-4 w-4" />
                      </BaseButton>
                    </nuxt-link>
                    <button shape="rounded" @click="delProduct(item.id)">
                      <Icon
                        name="material-symbols-light:delete-outline-rounded"
                        class="h-6 w-6 text-rose-500"
                      />
                    </button>
                  </div>
                </TairoTableCell>
              </TairoTableRow>
            </TairoTable>
          </div>
          <div class="flex items-center justify-center my-2">
            <BaseButton
              shape="rounded"
              class="flex w-[200px] justify-center"
              @click="loadMore(products.next)"
              v-if="products && products.next"
            >
              Load More
            </BaseButton>
            <p v-else class="w-full text-muted-500 text-center text-xs">
              End of list.
            </p>
          </div>
        </div>
      </div>
    </TairoContentWrapper>
  </div>
</template>
