<template>
  <div v-if="shop">
    <div class="flex justify-between items-center">
      <CommonTitleIcon
        :filename="'add-product-min.png'"
        :title="'Add New Product'"
      />
      <div class="flex gap-1 justify-end whitespace-nowrap flex-wrap">
        <BaseButton
          color="primary"
          flavor="pastel"
          class="!rounded-xl"
          v-if="!newProduct.loading2"
          @click="saveDraftProduct"
          >Save as draft</BaseButton
        >
        <button v-else class="px-3 flex justify-center rounded-xl">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="22"
            height="22"
            viewBox="0 0 24 24"
          >
            <path
              fill="currentColor"
              d="M12,1A11,11,0,1,0,23,12,11,11,0,0,0,12,1Zm0,19a8,8,0,1,1,8-8A8,8,0,0,1,12,20Z"
              opacity=".25"
            />
            <path
              fill="currentColor"
              d="M10.14,1.16a11,11,0,0,0-9,8.92A1.59,1.59,0,0,0,2.46,12,1.52,1.52,0,0,0,4.11,10.7a8,8,0,0,1,6.66-6.61A1.42,1.42,0,0,0,12,2.69h0A1.57,1.57,0,0,0,10.14,1.16Z"
            >
              <animateTransform
                attributeName="transform"
                dur="0.75s"
                repeatCount="indefinite"
                type="rotate"
                values="0 12 12;360 12 12"
              />
            </path>
          </svg>
        </button>
        <BaseButton
          color="primary"
          v-if="!newProduct.loading1"
          @click="saveProduct"
          class="!rounded-xl"
          >Publish</BaseButton
        >
        <button v-else class="px-3 flex justify-center rounded-xl">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="22"
            height="22"
            viewBox="0 0 24 24"
          >
            <path
              fill="currentColor"
              d="M12,1A11,11,0,1,0,23,12,11,11,0,0,0,12,1Zm0,19a8,8,0,1,1,8-8A8,8,0,0,1,12,20Z"
              opacity=".25"
            />
            <path
              fill="currentColor"
              d="M10.14,1.16a11,11,0,0,0-9,8.92A1.59,1.59,0,0,0,2.46,12,1.52,1.52,0,0,0,4.11,10.7a8,8,0,0,1,6.66-6.61A1.42,1.42,0,0,0,12,2.69h0A1.57,1.57,0,0,0,10.14,1.16Z"
            >
              <animateTransform
                attributeName="transform"
                dur="0.75s"
                repeatCount="indefinite"
                type="rotate"
                values="0 12 12;360 12 12"
              />
            </path>
          </svg>
        </button>
      </div>
    </div>
    <div class="flex gap-1 justify-end mb-4" v-if="newProduct.error">
      <span class="text-red-500">{{ newProduct.error }}</span>
    </div>
    <BaseCard shape="rounded" class="mt-2 text-sm !border-none !bg-transparent">
      <div class="flex flex-col md:flex-row gap-4">
        <!-- Body Content -->
        <div class="bodyContent w-4/6">
          <div class="mb-8">
            <div class="importers cj flex gap-1">
              <EcommercePluginsCjimport
                @setCJData="setCJData"
                v-if="shop.cj_active"
              />
              <EcommercePluginsNdsimport
                @setCJData="setCJData"
                v-if="shop.nds_active"
              />
              <EcommercePluginsOxyManagerimport
                @setCJData="setCJData"
                v-if="shop.oxymanager_active"
              />
            </div>

            <div
              class="flex flex-col bg-gray-50/70 dark:bg-slate-700/90 p-4 rounded-xl mb-5"
            >
              <h4 class="text-xl">General Information</h4>
              <div class="">
                <label
                  for="title"
                  class="block text-sm font-medium text-gray-700 dark:text-gray-100 mt-4 mb-1"
                  >Product Name
                  <span class="text-rose-600/50 dark:text-rose-600/90 text-lg"
                    >*</span
                  >
                </label>
                <input
                  v-model="newProduct.name"
                  type="text"
                  name="title"
                  id="title"
                  :class="{
                    'border-rose-400': newProduct.error && !newProduct.name,
                  }"
                  class="bg-[#eeeeeed6] dark:bg-[#202a38] mt-1 block w-full rounded-xl py-3 px-4 focus:border-primary-500/50 focus:outline-none"
                  placeholder="Short T-shirt "
                />
              </div>
              <div
                class="flex flex-col editor rounded-sm overflow-hidden"
                :class="{ full: fullScreenEditor }"
              >
                <div
                  class="flex justify-between items-center py-2 px-2"
                  :class="{
                    'bg-rose-600': newProduct.error && !newProduct.description,
                  }"
                >
                  <label
                    class="block text-sm font-medium text-gray-700 dark:text-gray-100 mt-4 mb-1"
                    for="desclong"
                    >Product Description
                    <span class="text-rose-600/50 dark:text-rose-600/90 text-lg"
                      >*</span
                    >
                  </label>
                  <span
                    class="flex gap-2 cursor-pointer items-center"
                    @click="fullScreenEditor = !fullScreenEditor"
                    v-if="fullScreenEditor"
                  >
                    <svg
                      xmlns="http://www.w3.org/2000/svg"
                      width="20"
                      height="20"
                      viewBox="0 0 24 24"
                    >
                      <path
                        fill="currentColor"
                        d="M14 10V4h2v2.59l3.29-3.29l1.41 1.41L17.41 8H20v2zM4 10V8h2.59l-3.3-3.29l1.42-1.42L8 6.59V4h2v6zm16 4v2h-2.59l3.29 3.29l-1.41 1.41L16 17.41V20h-2v-6zm-10 0v6H8v-2.59l-3.29 3.3l-1.42-1.42L6.59 16H4v-2z"
                      />
                    </svg>
                    Exit Full Screen
                  </span>
                  <span
                    class="flex gap-2 cursor-pointer items-center"
                    @click="fullScreenEditor = !fullScreenEditor"
                    v-else
                  >
                    <svg
                      xmlns="http://www.w3.org/2000/svg"
                      width="20"
                      height="20"
                      viewBox="0 0 24 24"
                    >
                      <path
                        fill="currentColor"
                        d="M21 3v6h-2V6.41l-3.29 3.3l-1.42-1.42L17.59 5H15V3zM3 3v6h2V6.41l3.29 3.3l1.42-1.42L6.41 5H9V3zm18 18v-6h-2v2.59l-3.29-3.29l-1.41 1.41L17.59 19H15v2zM9 21v-2H6.41l3.29-3.29l-1.41-1.42L5 17.59V15H3v6z"
                      />
                    </svg>
                    Enter Full Screen
                  </span>
                </div>
                <div class="w-full">
                  <CommonTiptap
                    :content="newProduct.description"
                    @updateContent="
                      (newVal) => {
                        newProduct.description = newVal;
                      }
                    "
                  />
                </div>
                <!-- <textarea class="text-sm  rounded border border-gray-300/50 py-3 px-4 shadow-sm focus:border-gray-900 focus:outline-none focus:ring-gray-900" name="desclong" id="desclong" cols="30" rows="10"></textarea> -->
              </div>

              <div class="flex flex-col">
                <label
                  class="block text-sm font-medium text-gray-700 dark:text-gray-100 mt-4 mb-1"
                  for="descshort"
                  >Short Description (Meta)
                  <span class="text-rose-600/50 dark:text-rose-600/90 text-lg"
                    >*</span
                  >
                </label>
                <textarea
                  v-model="newProduct.short_description"
                  :class="{
                    'border-rose-400':
                      newProduct.error && !newProduct.short_description,
                  }"
                  class="bg-[#eeeeeed6] dark:bg-[#202a38] mt-1 block w-full rounded-xl py-3 px-4 focus:border-primary-500/50 focus:outline-none"
                  name="descshort"
                  id="descshort"
                  cols="30"
                  rows="5"
                ></textarea>
              </div>
            </div>
            <div
              class="flex flex-col bg-gray-50/70 dark:bg-slate-700/90 p-4 rounded-xl mb-5"
            >
              <h4 class="text-xl">Pricing and stock</h4>
              <div class="grid-cols-2 grid gap-2 w-full md:flex">
                <div class="flex flex-col w-full md:w-2/5">
                  <label
                    for="pricing"
                    class="block text-sm font-medium text-gray-700 dark:text-gray-100 mt-4 mb-1"
                    >Buying Price({{ shop.currency }})
                    <span class="text-rose-600/50 dark:text-rose-600/90 text-lg"
                      >*</span
                    >
                  </label>
                  <input
                    v-model="newProduct.buy_price"
                    type="number"
                    name="pricing"
                    id="pricing"
                    :class="{
                      'border-rose-400':
                        newProduct.error && !newProduct.buy_price,
                    }"
                    class="bg-[#eeeeeed6] dark:bg-[#202a38] mt-1 block w-full rounded-xl py-3 px-4 focus:border-primary-500/50 focus:outline-none"
                    :placeholder="shop.currency + '0.00'"
                  />
                </div>
                <div class="flex flex-col w-full md:w-2/5">
                  <label
                    for="compare-pricing"
                    class="block text-sm font-medium text-gray-700 dark:text-gray-100 mt-4 mb-1"
                    >Selling Price({{ shop.currency }})
                    <span class="text-rose-600/50 dark:text-rose-600/90 text-lg"
                      >*</span
                    >
                  </label>
                  <input
                    v-model="newProduct.sale_price"
                    type="number"
                    name="compare-pricing"
                    id="compare-pricing"
                    :class="{
                      'border-rose-400':
                        newProduct.error && !newProduct.sale_price,
                    }"
                    class="bg-[#eeeeeed6] dark:bg-[#202a38] mt-1 block w-full rounded-xl py-3 px-4 focus:border-primary-500/50 focus:outline-none"
                    :placeholder="shop.currency + '0.00'"
                  />
                </div>
                <div class="flex flex-col w-full md:w-2/5">
                  <label
                    for="compare-pricing"
                    class="block text-sm font-medium text-gray-700 dark:text-gray-100 mt-4 mb-1"
                    >Discount<span
                      class="text-rose-600/50 dark:text-rose-600/90 opacity-0 font-bold text-xl"
                      >*</span
                    >
                  </label>
                  <select
                    v-model="newProduct.discount_type"
                    name="shippingList"
                    id="shippingList"
                    class="cursor-pointer bg-[#eeeeeed6] dark:bg-[#202a38] mt-1 block w-full rounded-xl py-3 px-4 focus:border-primary-500/50 focus:outline-none"
                  >
                    <option value="no">No Discount</option>
                    <option value="flat">Flat Rate</option>
                    <option value="percentage">Percentage</option>
                  </select>
                </div>
                <div
                  class="flex flex-col w-full md:w-2/5"
                  v-if="newProduct.discount_type == 'percentage'"
                >
                  <label
                    for="discount"
                    class="block text-sm font-medium text-gray-700 dark:text-gray-100 mt-4 mb-1"
                    >Discount (%)
                    <span
                      class="opacity-0 text-rose-600/50 dark:text-rose-600/90 text-lg"
                      >*</span
                    ></label
                  >
                  <input
                    v-model="newProduct.discount_p"
                    type="number"
                    name="discount"
                    id="discount"
                    class="bg-[#eeeeeed6] dark:bg-[#202a38] mt-1 block w-full rounded-xl py-3 px-4 focus:border-primary-500/50 focus:outline-none"
                    placeholder="0"
                  />
                </div>
                <div
                  class="flex flex-col w-full md:w-2/5"
                  v-if="newProduct.discount_type == 'flat'"
                >
                  <label
                    for="discount"
                    class="block text-sm font-medium text-gray-700 dark:text-gray-100 mt-4 mb-1"
                    >Discount ({{ shop.currency }})
                    <span
                      class="opacity-0 text-rose-600/50 dark:text-rose-600/90 text-lg"
                      >*</span
                    ></label
                  >
                  <input
                    v-model="newProduct.discount_f"
                    type="number"
                    name="discount"
                    id="discount"
                    class="bg-[#eeeeeed6] dark:bg-[#202a38] mt-1 block w-full rounded-xl py-3 px-4 focus:border-primary-500/50 focus:outline-none"
                    placeholder="0"
                  />
                </div>
              </div>
              <p class="text-sm dark:text-gray-100 mt-4">
                Estimated Profit:
                <span class="text-green-600"
                  >{{ shop.currency }}{{ calculateProfit() }}</span
                >
              </p>
            </div>
          </div>

          <div
            class="flex flex-col bg-gray-50/70 dark:bg-slate-700/90 p-4 rounded-xl mb-5"
          >
            <div class="flex flex-wrap py-4 gap-2 items-center justify-between">
              <div class="flex py-0 gap-2 items-center">
                <input
                  v-model="newProduct.has_variants"
                  class="cursor-pointer"
                  type="checkbox"
                  id="has-variants"
                  name="has-variants"
                  value="has-variants"
                />
                <label
                  class="cursor-pointer text-base font-medium dark:text-gray-100"
                  for="has-variants"
                  >This product has variants
                </label>
              </div>
              <div
                class="flex py-2 gap-2 items-center dark:text-gray-100"
                :class="{ 'opacity-10': !newProduct.has_variants }"
              >
                <span class="flex gap-1 justify-center">
                  <input
                    v-model="newProduct.color_variant"
                    class="cursor-pointer"
                    type="checkbox"
                    id="color-variants"
                    name="has-variants"
                    value="has-variants"
                  />
                  <label
                    class="cursor-pointer text-base font-medium"
                    for="color-variants"
                    >Color</label
                  >
                </span>
                <span class="flex gap-1 justify-center">
                  <input
                    v-model="newProduct.size_variant"
                    class="cursor-pointer"
                    type="checkbox"
                    id="size-variants"
                    name="has-variants"
                    value="has-variants"
                  />
                  <label
                    class="cursor-pointer text-base font-medium"
                    for="size-variants"
                    >Size</label
                  >
                </span>
                <span class="flex gap-1 justify-center">
                  <input
                    v-model="newProduct.weight_variant"
                    class="cursor-pointer"
                    type="checkbox"
                    id="weight-variants"
                    name="has-variants"
                    value="has-variants"
                  />
                  <label
                    class="cursor-pointer text-base font-medium"
                    for="weight-variants"
                    >Weight</label
                  >
                </span>
                <span class="flex gap-1 justify-center">
                  <input
                    v-model="newProduct.model_variant"
                    class="cursor-pointer"
                    type="checkbox"
                    id="model-variants"
                    name="has-variants"
                    value="has-variants"
                  />
                  <label
                    class="cursor-pointer text-base font-medium"
                    for="model-variants"
                    >Model</label
                  >
                </span>
                <span class="flex gap-1 justify-center">
                  <input
                    v-model="newProduct.material_variant"
                    class="cursor-pointer"
                    type="checkbox"
                    id="material-variants"
                    name="has-variants"
                    value="has-variants"
                  />
                  <label
                    class="cursor-pointer text-base font-medium"
                    for="material-variants"
                    >Material</label
                  >
                </span>
              </div>
            </div>
            <table
              class="w-full table-auto text-sm"
              v-if="newProduct.has_variants"
            >
              <thead>
                <tr class="bg-primary-500 text-center">
                  <th
                    v-if="newProduct.color_variant"
                    class="w-1/6 border-l border-transparent p-1 font-semibold text-white uppercase"
                  >
                    color
                  </th>
                  <th
                    v-if="newProduct.size_variant"
                    class="w-1/6 p-1 font-semibold text-white uppercase"
                  >
                    size
                  </th>
                  <th
                    v-if="newProduct.weight_variant"
                    class="w-1/6 p-1 font-semibold text-white uppercase"
                  >
                    weight
                  </th>
                  <th
                    v-if="newProduct.model_variant"
                    class="w-1/6 p-1 font-semibold text-white uppercase"
                  >
                    model
                  </th>
                  <th
                    v-if="newProduct.material_variant"
                    class="w-1/6 p-1 font-semibold text-white uppercase"
                  >
                    material
                  </th>
                  <th class="w-1/6 p-1 font-semibold text-white uppercase">
                    stock
                  </th>
                  <th class="w-1/6 p-1 font-semibold text-white uppercase">
                    buy
                  </th>
                  <th class="w-1/6 p-1 font-semibold text-white uppercase">
                    sale
                  </th>
                  <th class="w-1/6 p-1 font-semibold text-white uppercase">
                    action
                  </th>
                </tr>
              </thead>
              <tbody>
                <template v-for="variant in newProduct.productvariant_set">
                  <tr class="stripe" v-if="!variant.deleted">
                    <td
                      v-if="newProduct.color_variant"
                      class="text-dark p-1 text-center"
                    >
                      <div
                        class="flex w-full justify-center items-center gap-2"
                      >
                        <div
                          class="h-4 w-5 shadow"
                          :style="'background:' + variant.color"
                        ></div>
                        <span>{{ variant.color }}</span>
                      </div>
                    </td>
                    <td
                      v-if="newProduct.size_variant"
                      class="text-dark p-1 text-center"
                    >
                      {{ variant.size }}
                    </td>
                    <td
                      v-if="newProduct.weight_variant"
                      class="text-dark p-1 text-center"
                    >
                      {{ variant.weight }}
                    </td>
                    <td
                      v-if="newProduct.model_variant"
                      class="text-dark p-1 text-center"
                    >
                      {{ variant.model }}
                    </td>
                    <td
                      v-if="newProduct.material_variant"
                      class="text-dark p-1 text-center"
                    >
                      {{ variant.material }}
                    </td>
                    <td class="text-dark p-1 text-center">
                      {{ variant.stock }}
                    </td>
                    <td class="text-dark p-1 text-center">
                      {{ variant.buy_price }}
                    </td>
                    <td class="text-dark p-1 text-center">
                      {{ variant.sale_price }}
                    </td>
                    <td class="text-dark p-1 text-center">
                      <svg
                        @click="
                          newVariation = JSON.parse(JSON.stringify(variant))
                        "
                        :class="{
                          'bg-indigo-400': newVariation.id == variant.id,
                        }"
                        class="p-1 bg-slate-50/10 inline-block mx-auto border cursor-pointer hover:shadow-lg"
                        xmlns="http://www.w3.org/2000/svg"
                        width="28"
                        height="28"
                        viewBox="0 0 24 24"
                      >
                        <path
                          fill="currentColor"
                          d="M5 19h1.4l8.625-8.625l-1.4-1.4L5 17.6V19ZM19.3 8.925l-4.25-4.2l1.4-1.4q.575-.575 1.413-.575t1.412.575l1.4 1.4q.575.575.6 1.388t-.55 1.387L19.3 8.925ZM4 21q-.425 0-.713-.288T3 20v-2.825q0-.2.075-.388t.225-.337l10.3-10.3l4.25 4.25l-10.3 10.3q-.15.15-.337.225T6.825 21H4ZM14.325 9.675l-.7-.7l1.4 1.4l-.7-.7Z"
                        />
                      </svg>
                      <svg
                        @click="deleteVariant(variant)"
                        class="p-1 bg-slate-50/10 inline-block mx-auto border cursor-pointer hover:shadow-lg"
                        xmlns="http://www.w3.org/2000/svg"
                        width="28"
                        height="28"
                        viewBox="0 0 24 24"
                      >
                        <path
                          fill="currentColor"
                          d="M6 19c0 1.1.9 2 2 2h8c1.1 0 2-.9 2-2V7H6v12zM8 9h8v10H8V9zm7.5-5l-1-1h-5l-1 1H5v2h14V4h-3.5z"
                        />
                      </svg>
                    </td>
                  </tr>
                </template>
                <tr class="stripe form">
                  <td
                    v-if="newProduct.color_variant"
                    class="text-dark p-1 text-center relative"
                  >
                    <input
                      type="text"
                      class="w-full"
                      placeholder="Code/Name"
                      @keyup="
                        newVariation.color = nameToHex(newVariation.color)
                      "
                      v-model="newVariation.color"
                    />
                    <input
                      type="color"
                      class="color-picker absolute right-0"
                      v-model="newVariation.color"
                    />
                  </td>
                  <td
                    v-if="newProduct.size_variant"
                    class="text-dark p-1 text-center"
                  >
                    <input
                      type="text"
                      class="w-full"
                      placeholder="Size"
                      v-model="newVariation.size"
                    />
                  </td>
                  <td
                    v-if="newProduct.weight_variant"
                    class="text-dark p-1 text-center"
                  >
                    <input
                      type="text"
                      class="w-full"
                      placeholder="Weight"
                      v-model="newVariation.weight"
                    />
                  </td>
                  <td
                    v-if="newProduct.model_variant"
                    class="text-dark p-1 text-center"
                  >
                    <input
                      type="text"
                      class="w-full"
                      placeholder="Model"
                      v-model="newVariation.model"
                    />
                  </td>
                  <td
                    v-if="newProduct.material_variant"
                    class="text-dark p-1 text-center"
                  >
                    <input
                      type="text"
                      class="w-full"
                      placeholder="Material"
                      v-model="newVariation.material"
                    />
                  </td>
                  <td class="text-dark p-1 text-center">
                    <input
                      type="number"
                      class="w-full"
                      placeholder="Stock"
                      v-model="newVariation.stock"
                    />
                  </td>
                  <td class="text-dark p-1 text-center">
                    <input
                      type="number"
                      class="w-full"
                      placeholder="Buy price"
                      v-model="newVariation.buy_price"
                    />
                  </td>
                  <td class="text-dark p-1 text-center">
                    <input
                      type="number"
                      class="w-full"
                      placeholder="Sale price"
                      v-model="newVariation.sale_price"
                    />
                  </td>
                  <td class="text-dark p-1 text-center">
                    <svg
                      @click="saveVariant"
                      class="p-1 bg-slate-50/10 inline-block mx-auto border cursor-pointer hover:shadow-lg"
                      xmlns="http://www.w3.org/2000/svg"
                      width="28"
                      height="28"
                      viewBox="0 0 24 24"
                    >
                      <path
                        fill="currentColor"
                        d="M9 16.17L4.83 12l-1.42 1.41L9 19L21 7l-1.41-1.41L9 16.17z"
                      />
                    </svg>
                    <svg
                      @click="cancelVariantSave"
                      class="p-1 bg-slate-50/10 inline-block mx-auto border cursor-pointer hover:shadow-lg"
                      xmlns="http://www.w3.org/2000/svg"
                      width="28"
                      height="28"
                      viewBox="0 0 24 24"
                    >
                      <path
                        fill="currentColor"
                        d="M19 6.41L17.59 5L12 10.59L6.41 5L5 6.41L10.59 12L5 17.59L6.41 19L12 13.41L17.59 19L19 17.59L13.41 12L19 6.41Z"
                      />
                    </svg>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>

          <div class="rounded">
            <div
              class="flex flex-col bg-gray-50/70 dark:bg-slate-700/90 p-4 rounded-xl mb-5"
            >
              <h4 class="text-xl">Other Details</h4>
              <div class="grid grid-cols-2 gap-2 w-full md:flex">
                <div class="flex flex-col w-full my-2 md:w-2/5">
                  <label
                    for="stock"
                    class="block text-sm font-medium text-gray-700 dark:text-gray-100 mt-4 mb-1"
                    >Stock
                    <span class="text-rose-600/50 dark:text-rose-600/90 text-lg"
                      >*</span
                    >
                  </label>
                  <input
                    v-model="newProduct.stock"
                    type="number"
                    name="stock"
                    id="stock"
                    :class="{
                      'border-rose-400': newProduct.error && !newProduct.stock,
                    }"
                    class="bg-[#eeeeeed6] dark:bg-[#202a38] mt-1 block w-full rounded-xl py-3 px-4 focus:border-primary-500/50 focus:outline-none"
                    placeholder="Stock"
                  />
                </div>
                <div class="flex flex-col w-full my-2 md:w-2/5">
                  <label
                    for="sku"
                    class="block text-sm font-medium text-gray-700 dark:text-gray-100 mt-4 mb-1"
                    >SKU
                    <span class="text-rose-600/50 dark:text-rose-600/90 text-lg"
                      >*</span
                    >
                  </label>
                  <input
                    v-model="newProduct.sku"
                    type="text"
                    name="sku"
                    id="sku"
                    :class="{
                      'border-rose-400': newProduct.error && !newProduct.sku,
                    }"
                    class="bg-[#eeeeeed6] dark:bg-[#202a38] mt-1 block w-full rounded-xl py-3 px-4 focus:border-primary-500/50 focus:outline-none"
                    placeholder="Sku"
                  />
                </div>
                <div class="flex flex-col w-full my-2 md:w-2/5">
                  <label
                    for="material"
                    class="block text-sm font-medium text-gray-700 dark:text-gray-100 mt-4 mb-1"
                    >Material
                    <span
                      class="opacity-0 text-rose-600/50 dark:text-rose-600/90 text-lg"
                      >*</span
                    ></label
                  >
                  <input
                    v-model="newProduct.material"
                    type="text"
                    name="material"
                    id="material"
                    class="bg-[#eeeeeed6] dark:bg-[#202a38] mt-1 block w-full rounded-xl py-3 px-4 focus:border-primary-500/50 focus:outline-none"
                    placeholder="Material"
                  />
                </div>
              </div>
              <div class="flex gap-2 w-full">
                <div class="flex flex-col w-full md:w-2/4">
                  <label
                    for="model"
                    class="block text-sm font-medium text-gray-700 dark:text-gray-100 mt-4 mb-1"
                    >Model</label
                  >
                  <input
                    v-model="newProduct.model"
                    type="text"
                    name="model"
                    id="model"
                    class="bg-[#eeeeeed6] dark:bg-[#202a38] mt-1 block w-full rounded-xl py-3 px-4 focus:border-primary-500/50 focus:outline-none"
                    placeholder="Model"
                  />
                </div>
                <div class="flex flex-col w-full md:w-2/4">
                  <label
                    for="brand"
                    class="block text-sm font-medium text-gray-700 dark:text-gray-100 mt-4 mb-1"
                    >Brand</label
                  >
                  <input
                    type="text"
                    name="brand"
                    id="brand"
                    class="bg-[#eeeeeed6] dark:bg-[#202a38] mt-1 block w-full rounded-xl py-3 px-4 focus:border-primary-500/50 focus:outline-none"
                    placeholder="Brand"
                  />
                </div>
              </div>
              <div class="flex gap-2 w-full">
                <div class="flex flex-col w-full md:w-2/4">
                  <label
                    for="product_weight"
                    class="block text-sm font-medium text-gray-700 dark:text-gray-100 mt-4 mb-1"
                    >Product Weight</label
                  >
                  <input
                    v-model="newProduct.productWeight"
                    type="text"
                    name="product_weight"
                    id="product_weight"
                    class="bg-[#eeeeeed6] dark:bg-[#202a38] mt-1 block w-full rounded-xl py-3 px-4 focus:border-primary-500/50 focus:outline-none"
                    placeholder="Weight"
                  />
                </div>
                <div class="flex flex-col w-full md:w-2/4">
                  <label
                    for="packing_weight"
                    class="block text-sm font-medium text-gray-700 dark:text-gray-100 mt-4 mb-1"
                    >Packaging Weight</label
                  >
                  <input
                    v-model="newProduct.packingWeight"
                    type="text"
                    name="packing_weight"
                    id="packing_weight"
                    class="bg-[#eeeeeed6] dark:bg-[#202a38] mt-1 block w-full rounded-xl py-3 px-4 focus:border-primary-500/50 focus:outline-none"
                    placeholder="Packaging Weight"
                  />
                </div>
              </div>
            </div>
          </div>
          <!-- variation  -->
        </div>

        <!-- Side Filter -->
        <div class="sideFilter w-full md:w-2/6 rounded h-max mb-8">
          <div>
            <div
              class="space-y-8"
              :class="{
                'text-rose-400':
                  newProduct.error && newProduct.categories.length == 0,
              }"
            >
              <div
                class="flex flex-col bg-gray-50/70 dark:bg-slate-700/90 p-4 rounded-xl mb-5"
              >
                <div class="flex flex-col">
                  <label
                    class="block text-sm font-medium text-gray-700 dark:text-gray-100 mt-4 mb-1"
                  >
                    Upload Images
                  </label>
                  <div class="flex justify-center flex-wrap gap-1 rounded mt-1">
                    <div
                      class="p-0 bg-[#eeeeeed6] rounded-lg max-h-[300px] object-contain"
                      v-if="
                        newProduct.productimage_set &&
                        newProduct.productimage_set[0]
                      "
                    >
                      <img
                        class="w-full h-full object-contain rounded"
                        :src="
                          Api.baseURL + newProduct.productimage_set[0].image
                        "
                        alt=""
                        srcset=""
                      />
                    </div>
                    <div
                      class="p-0 bg-[#eeeeeed6] rounded-lg max-h-[300px] object-contain"
                      v-else-if="
                        newProduct.newImages && newProduct.newImages[0]
                      "
                    >
                      <img
                        class="w-full h-full object-contain rounded"
                        :src="Api.baseURL + newProduct.newImages[0].file"
                        alt=""
                        srcset=""
                      />
                    </div>

                    <TransitionGroup
                      name="list"
                      tag="ul"
                      class="flex flex-wrap gap-1 items-center w-full my-1 rounded-lg"
                    >
                      <li
                        class="relative w-20 h-20 rounded"
                        v-for="img in newProduct.newImages"
                        :key="img.id"
                      >
                        <span
                          class="absolute rounded top-1 left-1 text-rose-500 bg-rose-50 h-5 w-5 flex items-center justify-center shadow-lg hover:shadow-xl cursor-pointer"
                        >
                          <UIcon
                            @click="removeNewImg(img)"
                            name="i-heroicons-x-mark"
                          />
                        </span>
                        <span
                          @click="makePrimaryImg(img)"
                          class="pr-btn absolute text-sm left-[50%] whitespace-nowrap translate-x-[-50%] bottom-1 shadow-lg z-10 cursor-pointer px-2 my-1 bg-slate-700 text-slate-50 rounded hidden"
                          >Make Primary</span
                        >
                        <img
                          class="w-full h-full object-cover rounded"
                          :src="Api.baseURL + img.file"
                          alt=""
                          srcset=""
                        />
                      </li>
                      <template v-if="newProduct.productimage_set">
                        <template v-for="img in newProduct.productimage_set">
                          <li
                            class="relative w-20 h-20 border rounded"
                            v-if="!img.deleted"
                          >
                            <span
                              class="absolute rounded top-1 left-1 text-rose-500 bg-rose-50 h-5 w-5 flex items-center justify-center shadow-lg hover:shadow-xl cursor-pointer"
                            >
                              <UIcon
                                @click="removeProductImg(img)"
                                name="i-heroicons-x-mark"
                              />
                            </span>
                            <span
                              @click="makePrimaryProductImg(img)"
                              class="pr-btn absolute text-sm left-[50%] whitespace-nowrap translate-x-[-50%] bottom-1 shadow-lg z-10 cursor-pointer px-2 my-1 bg-slate-700 text-slate-50 rounded hidden"
                              >Make Primary</span
                            >
                            <img
                              class="w-full h-full object-cover rounded"
                              :src="Api.baseURL + img.image"
                              alt=""
                              srcset=""
                            />
                          </li>
                        </template>
                      </template>
                      <template v-if="newProduct.newUrlImages">
                        <li
                          class="relative w-24 h-24 rounded"
                          v-for="img in newProduct.newUrlImages"
                          :key="img"
                        >
                          <span
                            class="absolute rounded top-1 left-1 text-rose-500 bg-rose-50 h-5 w-5 flex items-center justify-center shadow-lg hover:shadow-xl cursor-pointer"
                          >
                            <UIcon
                              @click="removeNewUrlImg(img)"
                              name="i-heroicons-x-mark"
                            />
                          </span>
                          <span
                            @click="makePrimaryImgUrl(img)"
                            class="pr-btn absolute text-sm left-[50%] whitespace-nowrap translate-x-[-50%] bottom-1 shadow-lg z-10 cursor-pointer px-2 my-1 bg-slate-700 text-slate-50 rounded hidden"
                            >Make Primary</span
                          >
                          <img
                            class="w-full h-full object-cover"
                            :src="img"
                            alt=""
                            srcset=""
                          />
                        </li>
                      </template>
                      <div
                        @click="uploader = true"
                        key="8678562"
                        class="w-20 h-20 bg-[#eeeeee] border flex flex-col gap-1 justify-center items-center border-dashed text-sm p-3 rounded text-slate-400 cursor-pointer shadow hover:shadow-lg"
                      >
                        <UIcon
                          @click="removeNewUrlImg(img)"
                          name="i-heroicons-photo"
                          class="h-12 w-12"
                        />
                      </div>
                    </TransitionGroup>
                  </div>
                </div>
                <label
                  class="block text-sm font-medium text-gray-700 dark:text-gray-100 mt-4 mb-1"
                >
                  Product Video
                </label>
                <video
                  class="w-full my-2 rounded-lg"
                  controls
                  :src="newProduct.newVideo"
                  v-if="newProduct.newVideo"
                ></video>
                <video
                  class="w-full my-2 rounded-lg"
                  controls
                  v-if="newProduct.video"
                  :src="Api.baseURL + newProduct.video"
                ></video>
                <input
                  @change="videoAdded"
                  type="file"
                  name="video"
                  id="video"
                  accept="video/mp4,video/x-m4v,video/*"
                  class="border-rose-400 bg-[#eeeeeed6] dark:bg-[#202a38] mt-1 block w-full rounded-xl py-3 px-4 focus:border-primary-500/50 focus:outline-none"
                  placeholder="Video Url"
                />
                <p>{{ newProduct.newVideoError }}</p>
              </div>
              <div
                class="flex flex-col bg-gray-50/70 dark:bg-slate-700/90 p-4 rounded-xl mb-5"
              >
                <div>
                  <h5
                    class="block text-sm font-medium text-gray-700 dark:text-gray-100 mt-4 mb-1"
                  >
                    Categories
                    <span class="text-rose-600/50 dark:text-rose-600/90 text-lg"
                      >*</span
                    >
                  </h5>
                  <div class="my-2">
                    <input
                      v-model="categoryFilterQuery"
                      class="bg-[#eeeeeed6] dark:bg-[#202a38] mt-1 block w-full rounded-xl py-3 px-4 focus:border-primary-500/50 focus:outline-none"
                      type="search"
                      placeholder="Search here"
                    />
                  </div>
                  <section class="max-h-[300px] overflow-y-scroll">
                    <div
                      class="mb-0 px-2 py-1 dark:text-gray-100"
                      v-for="section in sectionAndCategories"
                      :key="section.id"
                    >
                      <a
                        @click="section.hidden = !section.hidden"
                        class="text-sm cursor-pointer flex justify-between gap-1 items-center bg-slate-400/10 p-1 rounded-t-md"
                      >
                        {{ section.name }}
                        <svg
                          class="h-6 transition-all"
                          :class="{ 'rotate-180': section.hidden }"
                          xmlns="http://www.w3.org/2000/svg"
                          width="32"
                          height="32"
                          viewBox="0 0 24 24"
                        >
                          <path fill="currentColor" d="m12 15l-5-5h10Z" />
                        </svg>
                      </a>
                      <div
                        class="grid grid-cols-1 gap-1 w-full"
                        v-if="!section.hidden"
                      >
                        <div
                          class="flex items-center gap-1 ml-5"
                          :class="{ hidden: categoryFilter(category.name) }"
                          v-for="category in section.category_set"
                          :key="category.id"
                        >
                          <input
                            v-model="newProduct.categories"
                            class="cursor-pointer mr-2"
                            type="checkbox"
                            :id="'cat' + category.id"
                            name="sub-cat"
                            :value="category.id"
                          />
                          <label
                            class="text-sm cursor-pointer flex-1"
                            :for="'cat' + category.id"
                            >{{ category.name }}</label
                          ><br />
                        </div>
                      </div>
                    </div>
                  </section>
                </div>
              </div>
              <div
                class="flex flex-col bg-gray-50/70 dark:bg-slate-700/90 p-4 rounded-xl mb-5"
              >
                <div>
                  <div class="">
                    <label
                      class="block text-sm font-medium text-gray-700 dark:text-gray-100 mt-4 mb-1"
                    >
                      Product Highlight
                    </label>
                    <select
                      v-model="newProduct.highlight"
                      :class="{
                        'border-rose-400 text-rose-400':
                          newProduct.error && !newProduct.origin,
                      }"
                      class="cursor-pointer bg-[#eeeeeed6] dark:bg-[#202a38] mt-1 block w-full rounded-xl py-3 px-4 focus:border-primary-500/50 focus:outline-none"
                      name=""
                      id=""
                    >
                      <option
                        :value="item"
                        v-for="item in highlights"
                        :key="item.id"
                      >
                        {{ item }}
                      </option>
                    </select>
                  </div>
                  <div class="">
                    <label
                      class="block text-sm font-medium text-gray-700 dark:text-gray-100 mt-4 mb-1"
                    >
                      Product Origin Country
                    </label>
                    <select
                      v-model="newProduct.origin"
                      :class="{
                        'border-rose-400 text-rose-400':
                          newProduct.error && !newProduct.origin,
                      }"
                      class="cursor-pointer bg-[#eeeeeed6] dark:bg-[#202a38] mt-1 block w-full rounded-xl py-3 px-4 focus:border-primary-500/50 focus:outline-none"
                      name=""
                      id=""
                    >
                      <option value="">Select country</option>
                      <option
                        :value="con.code2"
                        v-for="con in countries"
                        :key="con.id"
                      >
                        {{ con.name }}
                      </option>
                    </select>
                  </div>
                  <div class="">
                    <h5
                      class="block text-sm font-medium text-gray-700 dark:text-gray-100 mt-4 mb-1"
                    >
                      Product Brand
                    </h5>
                    <select
                      v-model="newProduct.brandname"
                      class="cursor-pointer bg-[#eeeeeed6] dark:bg-[#202a38] mt-1 block w-full rounded-xl py-3 px-4 focus:border-primary-500/50 focus:outline-none"
                      name=""
                      id=""
                      placeholder="Select Brand"
                    >
                      <option value="" disabled>Select Brand</option>
                      <option
                        :value="brand.id"
                        v-for="brand in brands"
                        :key="brand.id"
                      >
                        {{ brand.name }}
                      </option>
                      <option disabled class="p-1" v-if="brands.length == 0">
                        No brand found
                      </option>
                    </select>
                  </div>
                  <div class="">
                    <h5
                      class="block text-sm font-medium text-gray-700 dark:text-gray-100 mt-4 mb-1"
                    >
                      Shipping Profile
                      <span
                        class="text-rose-600/50 dark:text-rose-600/90 text-lg"
                        >*</span
                      >
                    </h5>
                    <select
                      v-model="newProduct.shipping"
                      name="shippingList"
                      id="shippingList"
                      :class="{
                        'border-rose-400 text-rose-400':
                          newProduct.error && !newProduct.shipping,
                      }"
                      class="cursor-pointer bg-[#eeeeeed6] dark:bg-[#202a38] mt-1 block w-full rounded-xl py-3 px-4 focus:border-primary-500/50 focus:outline-none"
                    >
                      <option value="" disabled>Select Shipping Profile</option>
                      <option
                        v-for="shipping in shippings"
                        :key="shipping.id"
                        :value="shipping.id"
                      >
                        {{ shipping.name }}
                      </option>
                      <option disabled class="p-1" v-if="shippings.length == 0">
                        No Profile found
                      </option>
                    </select>
                  </div>
                  <div class="">
                    <h5
                      class="block text-sm font-medium text-gray-700 dark:text-gray-100 mt-4 mb-1"
                    >
                      Search Tags
                    </h5>
                    <div class="flex gap-1 flex-wrap pb-[2px]">
                      <template v-for="tag in newProduct.tags">
                        <div
                          class="flex relative tag-box"
                          v-if="!tag.deleted && tag.name"
                          :key="tag"
                        >
                          <div
                            class="tag-action absolute bg-red-500 gap-2 px-1.5 z-10 -top-4 rounded hidden justify-center -right-4 py-1"
                            @click="removeSearchTag(tag)"
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
                            <UIcon
                              name="i-heroicons-tag-solid"
                              class="text-white"
                            />
                          </div>
                          <div
                            class="relative w-max px-3 py-2 rounded-e-sm bg-[#39c] text-white text-xs flex items-center justify-center"
                          >
                            {{ tag.name }}
                          </div>
                        </div>
                      </template>
                    </div>
                    <div
                      :class="{
                        'text-rose-400':
                          newProduct.error && newProduct.tags.length == 0,
                      }"
                      class="mb-2 relative"
                    >
                      <input
                        v-model="newSearchTag"
                        @keyup="debouncedSearchTag()"
                        class="bg-[#eeeeeed6] dark:bg-[#202a38] mt-1 block w-full rounded-xl py-3 px-4 focus:border-primary-500/50 focus:outline-none"
                        type="search"
                        placeholder="Search tag"
                      />
                      <div
                        class="absolute left-0 top-[45px] shadow-xl border p-3 z-[999]"
                        v-if="tagSuggestions && tagSuggestions"
                      >
                        <div
                          v-if="tagSuggestions.length == 0"
                          class="text-sm text-gray-400"
                        >
                          No tag found
                        </div>
                        <button
                          v-for="tag in tagSuggestions"
                          :key="tag.name"
                          @click="addSearchTag(tag)"
                          class="w-full text-slate-900 mb-1 py-1 px-2 bg-gray-50 border p-1 hover:bg-gray-100"
                        >
                          {{ tag.name }} ({{ tag.qty }})
                        </button>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <div class="p-4 pb-3 my-2" v-if="shop.local_active">
              <h5
                class="block text-sm font-medium text-gray-700 dark:text-gray-100 mt-4 mb-1"
              >
                Local Storage
                <span
                  class="text-rose-600/50 dark:text-rose-600/90 text-lg"
                ></span>
              </h5>
              <div
                class="flex items-center gap-1 w-full my-2"
                v-if="shop.warehouse"
              >
                <label
                  for="packing_weight"
                  class="w-[80px] block text-sm font-medium text-gray-700 dark:text-gray-100 mt-4 mb-1"
                  >Warehouse</label
                >
                <input
                  v-model="newProduct.warehouse"
                  type="text"
                  name="packing_weight"
                  id="packing_weight"
                  class="flex-1 w-full mt-1 block rounded border border-gray-300/50 py-3 px-4 shadow-sm focus:border-gray-900 focus:outline-none focus:ring-gray-900 sm:text-sm"
                  placeholder="N/A"
                />
              </div>
              <div class="flex items-center gap-1 w-full my-2" v-if="shop.room">
                <label
                  for="packing_weight2"
                  class="w-[80px] block text-sm font-medium text-gray-700 dark:text-gray-100 mt-4 mb-1"
                  >Room</label
                >
                <input
                  v-model="newProduct.room"
                  type="text"
                  name="packing_weight2"
                  id="packing_weight2"
                  class="flex-1 w-full mt-1 block rounded border border-gray-300/50 py-3 px-4 shadow-sm focus:border-gray-900 focus:outline-none focus:ring-gray-900 sm:text-sm"
                  placeholder="N/A"
                />
              </div>
              <div class="flex items-center gap-1 w-full my-2" v-if="shop.sec">
                <label
                  for="packing_weight3"
                  class="w-[80px] block text-sm font-medium text-gray-700 dark:text-gray-100 mt-4 mb-1"
                  >Section</label
                >
                <input
                  v-model="newProduct.section"
                  type="text"
                  name="packing_weight3"
                  id="packing_weight3"
                  class="flex-1 w-full mt-1 block rounded border border-gray-300/50 py-3 px-4 shadow-sm focus:border-gray-900 focus:outline-none focus:ring-gray-900 sm:text-sm"
                  placeholder="N/A"
                />
              </div>
              <div
                class="flex items-center gap-1 w-full my-2"
                v-if="shop.shelf"
              >
                <label
                  for="packing_weight4"
                  class="w-[80px] block text-sm font-medium text-gray-700 dark:text-gray-100 mt-4 mb-1"
                  >Shelf</label
                >
                <input
                  v-model="newProduct.shelf"
                  type="text"
                  name="packing_weight4"
                  id="packing_weight4"
                  class="flex-1 w-full mt-1 block rounded border border-gray-300/50 py-3 px-4 shadow-sm focus:border-gray-900 focus:outline-none focus:ring-gray-900 sm:text-sm"
                  placeholder="N/A"
                />
              </div>
              <div class="flex items-center gap-1 w-full my-2" v-if="shop.rack">
                <label
                  for="packing_weight5"
                  class="w-[80px] block text-sm font-medium text-gray-700 dark:text-gray-100 mt-4 mb-1"
                  >Rack</label
                >
                <input
                  v-model="newProduct.rack"
                  type="text"
                  name="packing_weight5"
                  id="packing_weight5"
                  class="flex-1 w-full mt-1 block rounded border border-gray-300/50 py-3 px-4 shadow-sm focus:border-gray-900 focus:outline-none focus:ring-gray-900 sm:text-sm"
                  placeholder="N/A"
                />
              </div>
              <div
                class="flex items-center gap-1 w-full my-2"
                v-if="shop.drawer"
              >
                <label
                  for="packing_weight6"
                  class="w-[80px] block text-sm font-medium text-gray-700 dark:text-gray-100 mt-4 mb-1"
                  >Drawer</label
                >
                <input
                  v-model="newProduct.drawer"
                  type="text"
                  name="packing_weight6"
                  id="packing_weight6"
                  class="flex-1 bg-[#eeeeeed6] dark:bg-[#202a38] mt-1 block w-full rounded-xl py-3 px-4 focus:border-primary-500/50 focus:outline-none"
                  placeholder="N/A"
                />
              </div>
              <div class="flex items-center gap-1 w-full my-2" v-if="shop.file">
                <label
                  for="packing_weight7"
                  class="w-[80px] block text-sm font-medium text-gray-700 dark:text-gray-100 mt-4 mb-1"
                  >File</label
                >
                <input
                  v-model="newProduct.file"
                  type="text"
                  name="packing_weight7"
                  id="packing_weight7"
                  class="flex-1 w-full mt-1 block rounded border border-gray-300/50 py-3 px-4 shadow-sm focus:border-gray-900 focus:outline-none focus:ring-gray-900 sm:text-sm"
                  placeholder="N/A"
                />
              </div>
            </div>
          </div>
        </div>
      </div>
    </BaseCard>
    <CommonOver :show="uploader">
      <DialogPanel
        class="pointer-events-auto relative w-screen max-w-2xl bg-white dark:bg-slate-800"
      >
        <TransitionChild
          as="template"
          enter="ease-in-out duration-500"
          enter-from="opacity-0"
          enter-to="opacity-100"
          leave="ease-in-out duration-500"
          leave-from="opacity-100"
          leave-to="opacity-0"
        >
          <div class="absolute top-0 -left-2 flex pt-4 pr-2 sm:-ml-10 sm:pr-4">
            <span
              type="button"
              class="rounded-full text-slate-600 shadow-xl hover:text-slate-500 cursor-pointer p-1 bg-white dark:bg-slate-800"
              @click="uploader = false"
            >
              <span class="sr-only">Close panel</span>
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="32"
                height="32"
                viewBox="0 0 24 24"
              >
                <path
                  fill="currentColor"
                  d="M20 6.91L17.09 4L12 9.09L6.91 4L4 6.91L9.09 12L4 17.09L6.91 20L12 14.91L17.09 20L20 17.09L14.91 12L20 6.91Z"
                />
              </svg>
            </span>
          </div>
        </TransitionChild>
        <div class="flex h-full flex-col overflow-y-scroll py-6 shadow-xl">
          <div class="p-4">
            <input
              type="file"
              class="hidden"
              id="fileUploader"
              @change="uploadFiles"
              multiple
            />
            <label
              for="fileUploader"
              class="cursor-pointer my-4 text-indigo-400 font-bold"
            >
              <div
                class="flex gap-2 items-center justify-center shadow-lg p-2 bg-indigo-50 max-w-md mx-auto"
              >
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  width="22"
                  height="22"
                  viewBox="0 0 2048 2048"
                >
                  <path
                    fill="currentColor"
                    d="M1408 576q0-26 19-45t45-19q26 0 45 19t19 45q0 26-19 45t-45 19q-26 0-45-19t-19-45zm640 960v128h-256v256h-128v-256h-256v-128h256v-256h128v256h256zM922 1216l358 357v91H0V256h1792v896h-128V384H128v421l192-191l512 512l256-256l448 447v91h-91l-357-358l-166 166zM320 794L128 987v549h933L320 794z"
                  />
                </svg>
                <span class="text-sm">Upload From Device</span>
              </div>
            </label>
          </div>
          <div class="p-4 border-t">
            <DialogTitle class="text-base font-semibold leading-6 mb-6 py-1"
              >Your Media Library</DialogTitle
            >
            <div
              class="flex flex-wrap gap-1"
              v-if="mediaFiles && mediaFiles.results.length > 0"
            >
              <span
                @click="addNewImage(file)"
                v-for="file in mediaFiles.results"
                :key="file"
                class="relative"
              >
                <span
                  class="absolute z-10 left-1 top-1 text-black dark:text-white shadow-lg rounded bg-white dark:bg-black p-1 transition-all"
                >
                  <svg
                    v-if="IfInNewImage(file)"
                    xmlns="http://www.w3.org/2000/svg"
                    width="22"
                    height="22"
                    viewBox="0 0 24 24"
                  >
                    <path
                      fill="currentColor"
                      d="m6.7 18l-5.65-5.65l1.425-1.4l4.25 4.25l1.4 1.4Zm5.65 0L6.7 12.35l1.4-1.425l4.25 4.25l9.2-9.2l1.4 1.425Zm0-5.65l-1.425-1.4L15.875 6L17.3 7.4Z"
                    />
                  </svg>
                </span>
                <img
                  class="w-44 h-36 rounded object-cover shadow hover:shadow-lg cursor-pointer"
                  :src="Api.baseURL + file.file"
                  alt=""
                  srcset=""
                />
              </span>
            </div>
            <div
              v-else
              class="flex-1 max-w-md mx-auto h-36 border flex flex-col gap-1 justify-center items-center border-dashed text-sm p-3 rounded text-slate-400"
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="52"
                height="52"
                viewBox="0 0 24 24"
              >
                <g fill="none" stroke="currentColor" stroke-width="1.5">
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    d="M8.992 14h3m3 0h-3m0 0v-3m0 3v3"
                  />
                  <path
                    d="M3.04 4.294a.496.496 0 0 1 .191-.479C3.927 3.32 6.314 2 12 2s8.073 1.32 8.769 1.815a.496.496 0 0 1 .192.479l-1.7 12.744a4 4 0 0 1-1.98 2.944l-.32.183a10 10 0 0 1-9.922 0l-.32-.183a4 4 0 0 1-1.98-2.944l-1.7-12.744Z"
                  />
                  <path d="M3 5c2.571 2.667 15.429 2.667 18 0" />
                </g>
              </svg>
              <p class="text-sm text-gray-500">No Media Found</p>
            </div>
          </div>
          <div class="relative mt-6 flex-1 px-4 sm:px-6">
            <!-- Your content -->
          </div>
        </div>
      </DialogPanel>
    </CommonOver>
    <div class="dummy-color opacity-0">..</div>
    <!-- <EcommerceSetup :state="true" /> -->
  </div>
</template>

<script setup>
import {
  Dialog,
  DialogPanel,
  DialogTitle,
  TransitionChild,
  TransitionRoot,
} from "@headlessui/vue";
import { debounce } from "lodash";
const Api = useApi();
const router = useRoute();
const { notifs } = useAuth();
const { shop } = useShop();
const fullScreenEditor = ref(false);
definePageMeta({
  layout: "dashboard",
});

function nameToHex(colorName) {
  colorName = colorName.toLowerCase();
  if (colorName.includes("#")) {
    return colorName;
  }
  const dummy = document.querySelector(".dummy-color");
  dummy.style.color = colorName;
  const rgbColor = window.getComputedStyle(dummy).color;
  const rgbValues = rgbColor.substring(4, rgbColor.length - 1);
  const rgbArray = rgbValues.split(",").map(Number);
  const hexColor =
    "#" +
    rgbArray
      .map((value) => {
        const hexValue = value.toString(16).padStart(2, "0");
        return hexValue;
      })
      .join("");
  if (hexColor == "#475569") {
    return colorName;
  }
  return hexColor;
}

onMounted(() => {
  getMediaFiles();
});

const newProduct = ref({
  name: "",
  buy_price: "",
  sale_price: "",
  sku: "",
  short_description: "",
  description: "",
  highlight: "new",
  material: "",
  origin: "",
  model: "",
  brandname: "",
  productWeight: "",
  packingWeight: "",
  shipping: "",
  categories: [],
  productvariant_set: [],
  has_variants: true,
  color_variant: true,
  size_variant: true,
  weight_variant: false,
  model_variant: false,
  material_variant: false,
  tags: [],
  newImages: [],
  draft: false,
  discount_type: "no",
  discount_f: "",
  discount_p: "",
  error: "",
  loading1: false,
  loading2: false,
  cj_pid: "",
  oxymanager_id: "",
  warehouse: "",
  room: "",
  section: "",
  shelf: "",
  rack: "",
  drawer: "",
  file: "",
  video: null,
  newVideo: false,
  newVideoError: "",
});

const highlights = ref([
  "none",
  "new",
  "hot",
  "sale",
  "offer",
  "featured",
  "discount",
  "old",
  "promo",
  "flash",
]);

if (router.params.id != "add") {
  getProduct(router.params.id);
}

function calculateProfit() {
  var profit = "0.00";
  if (newProduct.value.buy_price && newProduct.value.sale_price) {
    profit = (newProduct.value.sale_price - newProduct.value.buy_price).toFixed(
      2
    );
  }
  return profit;
}

async function getProduct(id) {
  var res = await Api.get("/api/ecommerce/dash/products?detail=" + id);
  console.log(res);
  if (res.data) {
    console.log(res.data);
    newProduct.value = res.data;
    // var tags = JSON.parse(JSON.stringify( newProduct.value.tags))
    // newProduct.value.tags = []
    // for (let i = 0; i < tags.length; i++) {
    //     const element = tags[i];
    //     newProduct.value.tags.push(element.name)
    // }
    var categories = JSON.parse(JSON.stringify(newProduct.value.categories));
    newProduct.value.categories = [];
    for (let i = 0; i < categories.length; i++) {
      const element = categories[i];
      newProduct.value.categories.push(element.id);
    }
    if (newProduct.value.brand) {
      newProduct.value.brandname = newProduct.value.brand.id;
    }
    if (newProduct.value.shipping) {
      newProduct.value.shipping = newProduct.value.shipping.id;
    } else {
      newProduct.value.shipping = "";
    }
    newProduct.value.draft = false;
    newProduct.value.loading1 = false;
    newProduct.value.loading2 = false;
    newProduct.value.newImages = [];
    if (!newProduct.value.buy_price) {
      newProduct.value.buy_price = "0.00";
    }
  }
}

async function videoAdded(e) {
  newProduct.value.newVideoError = "";
  console.log(e.target.files[0]);
  var file = e.target.files[0];
  if (file.size > 10000000) {
    newProduct.value.newVideoError = "Video size must be less than 10MB";
    return;
  }
  var reader = new FileReader();
  reader.onload = function (e) {
    newProduct.value.video = e.target.result;
    newProduct.value.newVideo = true;
  };
  reader.readAsDataURL(file);
}
async function addNewImage(img) {
  var exist = newProduct.value.newImages.find((i) => i.id == img.id);
  if (exist) {
    removeNewImg(img);
    return;
  }
  newProduct.value.newImages.push(img);
}
function IfInNewImage(img) {
  var exist = newProduct.value.newImages.find((i) => i.id == img.id);
  if (exist) return true;
  return false;
}
async function removeNewImg(img) {
  newProduct.value.newImages = newProduct.value.newImages.filter(
    (i) => i.id != img.id
  );
}
async function removeProductImg(img) {
  img.deleted = true;
}
async function removeNewUrlImg(img) {
  newProduct.value.newUrlImages = newProduct.value.newUrlImages.filter(
    (i) => i != img
  );
}
async function saveProduct() {
  newProduct.value.error = "";
  newProduct.value.draft = false;
  if (!newProduct.value.error && newProduct.value.name == "") {
    newProduct.value.error = "Please enter product name";
  }
  if (!newProduct.value.error && newProduct.value.buy_price == "") {
    newProduct.value.error = "Please enter product buy price";
  }
  if (!newProduct.value.error && newProduct.value.sale_price == "") {
    newProduct.value.error = "Please enter product sale price";
  }
  if (!newProduct.value.error && newProduct.value.short_description == "") {
    newProduct.value.error = "Please enter product short description";
  }
  if (!newProduct.value.error && newProduct.value.description == "") {
    newProduct.value.error = "Please enter product description";
  }
  if (!newProduct.value.error && newProduct.value.categories.length == 0) {
    newProduct.value.error = "Please enter product categories";
  }
  if (!newProduct.value.error && newProduct.value.shipping == "") {
    newProduct.value.error = "Please enter product shipping profile";
  }
  if (!newProduct.value.discount_f) {
    newProduct.value.discount_f = 0;
  }
  if (!newProduct.value.discount_p) {
    newProduct.value.discount_p = 0;
  }
  if (newProduct.value.error) {
    notifs.value.push({
      type: "error",
      title: "",
      message: newProduct.value.error,
    });
    return;
  }
  console.log(newProduct.value);
  console.log(newProduct.value.description);
  newProduct.value.loading1 = true;
  var res = await Api.post("/api/ecommerce/dash/products", newProduct.value);
  console.log(res);
  notifs.value.push({
    type: "success",
    title: "Product added",
    message: "The product has been added successfully",
  });
  navigateTo("/ecommerce/products");
}

async function saveDraftProduct() {
  newProduct.value.draft = true;
  newProduct.value.loading2 = true;
  console.log(newProduct.value.buy_price);
  var res = await Api.post("/api/ecommerce/dash/products", newProduct.value);
  console.log(res);
  notifs.value.push({
    type: "success",
    title: "Product added",
    message: "The product has been added successfully",
  });
  navigateTo("/ecommerce/products");
}

// uploader
const uploader = ref(false);
const mediaFiles = ref([]);
const getMediaFiles = async () => {
  const res = await Api.get("/api/ecommerce/dash/mediafiles");
  mediaFiles.value = res.data;
};
const uploadFiles = async (e) => {
  const files = e.target.files;
  const formData = [];
  const promises = Array.from(files).map((file) => {
    return new Promise((resolve, reject) => {
      const reader = new FileReader();

      reader.readAsDataURL(file);
      reader.onload = () => {
        formData.push(reader.result);
        resolve();
      };
      reader.onerror = reject;
    });
  });

  await Promise.all(promises);
  const res = await Api.post("/api/ecommerce/dash/mediafiles", formData);
  console.log(res);
  if (res.data) {
    newProduct.value.newImages.push(...res.data);
  }
  getMediaFiles();
};
const makePrimaryImg = async (img) => {
  console.log(img);
  newProduct.value.newImages = newProduct.value.newImages.filter(
    (i) => i.id != img.id
  );
  newProduct.value.newImages.unshift(img);
};
const makePrimaryImgUrl = async (img) => {
  console.log(img);
  newProduct.value.newUrlImages = newProduct.value.newUrlImages.filter(
    (i) => i != img
  );
  newProduct.value.newUrlImages.unshift(img);
};

const countries = ref([]);
const getCountry = async () => {
  const res = await Api.get("/api/utils/countries/");
  countries.value = res.data;
};
getCountry();

const sectionAndCategories = ref([]);
const getSectionAndCategories = async () => {
  const res = await Api.get("/api/ecommerce/dash/categories");
  sectionAndCategories.value = res.data;
};
getSectionAndCategories();
const categoryFilterQuery = ref("");
function categoryFilter(name) {
  if (!categoryFilterQuery.value) return false;
  return !name.toLowerCase().includes(categoryFilterQuery.value.toLowerCase());
}

const brands = ref([]);
const getBrands = async () => {
  const res = await Api.get("/api/ecommerce/dash/brands");
  brands.value = res.data;
};
getBrands();

const newSearchTag = ref("");
const tagSuggestions = ref("");
const debouncedSearchTag = debounce(findSearchTag, 500);
async function findSearchTag() {
  if (!newSearchTag.value) return;
  const res = await Api.get(
    "/api/ecommerce/dash/tags?search=" + newSearchTag.value
  );
  tagSuggestions.value = res.data;
}
const addSearchTag = (tag) => {
  newProduct.value.tags.push(tag);
  newSearchTag.value = "";
  tagSuggestions.value = "";
};
const removeSearchTag = (tag) => {
  if (!tag.id) {
    newProduct.value.tags = newProduct.value.tags.filter((t) => t != tag);
  } else {
    tag.deleted = true;
  }
};

const shippings = ref([]);
const getShippings = async () => {
  const res = await Api.get("/api/ecommerce/dash/shipping");
  shippings.value = res.data;
};
getShippings();

// product variation management
const newVariation = ref({
  buy_price: "",
  sale_price: "",
  stock: "",
  color: "",
  hex: "",
  size: "",
  weight: "",
  model: "",
  material: "",
});
function saveVariant() {
  if (newVariation.value.id) {
    newProduct.value.productvariant_set =
      newProduct.value.productvariant_set.map((v) => {
        if (v.id == newVariation.value.id) {
          return newVariation.value;
        }
        return v;
      });
    notifs.value.push({
      type: "success",
      title: "Variant updated",
      message: "The variant has been updated successfully",
    });
    cancelVariantSave();
    return;
  }
  newVariation.value.id =
    Math.random().toString(36).substring(2, 15) +
    Math.random().toString(36).substring(2, 15);
  newVariation.value.new = true;
  newProduct.value.productvariant_set.push(newVariation.value);
  notifs.value.push({
    type: "success",
    title: "Variant added",
    message: "The variant has been added successfully",
  });
  cancelVariantSave();
}
function cancelVariantSave() {
  newVariation.value = {
    buy_price: "",
    sale_price: "",
    stock: "",
    color: "",
    size: "",
    weight: "",
    model: "",
    material: "",
  };
}

function deleteVariant(variant) {
  console.log(variant.id);
  if (variant.new) {
    newProduct.value.productvariant_set =
      newProduct.value.productvariant_set.filter((v) => v.id != variant.id);
    return;
  } else {
    variant.deleted = true;
  }
  notifs.value.push({
    type: "success",
    title: "Variant deleted",
    message: "The variant has been deleted successfully",
  });
}

// CJ
function setCJData(data) {
  newProduct.value = data;
}
</script>

<style>
.tag-box:hover .tag-action {
  display: flex;
}

.tox-notifications-container {
  opacity: 0;
  display: none;
}
.color-picker {
  padding: 0 !important;
  width: 30px;
  width: 30px;
  cursor: pointer;
}
.editor {
  border-radius: 5px;
  overflow: hidden;
}
.editor.full {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100vh;
  z-index: 10;
  display: flex;
  flex-direction: column;
  background-color: aliceblue;
  margin: 0px;
  padding: 0px;
  border-radius: 0px;
}
.tox-tinymce {
  border-radius: 0px !important;
  border: none !important;
}
.editor.full .tox-tinymce {
  flex: 1;
}
</style>

<style scoped>
tr.stripe > * {
  min-width: 100px;
}
tr.stripe > *:nth-child(odd) {
  background-color: #f3f6ff;
}
tr.form > * {
  padding: 1px;
  background-color: rgb(233, 233, 233) !important;
}
.dark tr.stripe > *:nth-child(odd) {
  background-color: #202a38;
}
.dark tr.form > * {
  padding: 1px;
  background-color: #202a38 !important;
}
tr.stripe.form input {
  outline: none;
  border: 1px solid #cbcaca3d;
  background: #cbcaca3d;
  padding: 3px 8px;
}
.sideFilter.active {
  display: flex;
  width: 100%;
  position: absolute;
  justify-content: flex-end;
  right: 0;
}
@media (max-width: 768px) {
  .bodyContent {
    width: 100%;
  }
  .filter-btn {
    display: block;
  }
}
.product-photo .pr-btn {
  display: none;
}
.product-photo:hover .pr-btn {
  display: block;
}
.parent {
  display: grid;
  grid-template-columns: repeat(1, 1fr);
  grid-template-rows: repeat(1, 1fr);
  grid-column-gap: 10px;
  grid-row-gap: 10px;
  margin: auto;
  position: relative;
}
.parent li {
  height: 135px;
  width: 155px;
}
.parent li img {
  width: 100% !important;
  height: 100% !important;
  object-fit: contain !important;
  border: 1px solid rgba(128, 128, 128, 0.308);
  border-radius: 4px;
}
.parent li:nth-child(1) {
  grid-area: 1 / 1 / 3 / 3;
  height: 280px;
  width: 320px;
  border: none !important;
  box-shadow: none !important;
}
.parent li:nth-child(2) {
  grid-area: 1 / 3 / 2 / 4;
}
.parent li:nth-child(3) {
  grid-area: 2 / 3 / 3 / 4;
}
.parent li:nth-child(4) {
  grid-area: 1 / 4 / 2 / 5;
}
.parent li:nth-child(5) {
  grid-area: 2 / 4 / 3 / 5;
}
.parent li:nth-child(6) {
  grid-area: 1 / 5 / 2 / 6;
}
.parent li:nth-child(7) {
  grid-area: 2 / 5 / 3 / 6;
}
.parent li:nth-child(8) {
  grid-area: 3 / 1 / 4 / 2;
}
.parent li:nth-child(9) {
  grid-area: 3 / 2 / 4 / 3;
}
.parent li:nth-child(10) {
  grid-area: 3 / 3 / 4 / 4;
}
.parent li:nth-child(11) {
  grid-area: 3 / 4 / 4 / 5;
}
.parent li:nth-child(12) {
  grid-area: 3 / 5 / 4 / 6;
}
.parent li:nth-child(13) {
  grid-area: 4 / 1 / 5 / 2;
}
.parent li:nth-child(14) {
  grid-area: 4 / 2 / 5 / 3;
}
.parent li:nth-child(15) {
  grid-area: 4 / 3 / 5 / 4;
}
.parent li:nth-child(16) {
  grid-area: 4 / 4 / 5 / 5;
}
.parent li:nth-child(17) {
  grid-area: 4 / 5 / 5 / 6;
}
.parent li:nth-child(18) {
  grid-area: 5 / 1 / 6 / 2;
}
.parent li:nth-child(19) {
  grid-area: 5 / 2 / 6 / 3;
}
.parent li:nth-child(20) {
  grid-area: 5 / 3 / 6 / 4;
}
.parent li:nth-child(21) {
  grid-area: 5 / 4 / 6 / 5;
}
.parent li:nth-child(22) {
  grid-area: 5 / 5 / 6 / 6;
}
.parent li:nth-child(23) {
  grid-area: 6 / 1 / 7 / 2;
}
.parent li:nth-child(24) {
  grid-area: 6 / 2 / 7 / 3;
}
.parent li:nth-child(25) {
  grid-area: 6 / 3 / 7 / 4;
}
.parent li:nth-child(26) {
  grid-area: 6 / 4 / 7 / 5;
}
.parent li:nth-child(27) {
  grid-area: 6 / 5 / 7 / 6;
}

.list-move, /* apply transition to moving elements */
    .list-enter-active,
    .list-leave-active {
  transition: all 0.5s ease;
}

.list-enter-from,
.list-leave-to {
  opacity: 0;
  transform: translateX(30px);
}

/* ensure leaving items are taken out of layout flow so that moving
       animations can be calculated correctly. */
.list-leave-active {
  position: absolute;
}
</style>
