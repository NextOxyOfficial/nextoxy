<template>
  <div>
    <section class="bg-gray-2 pb-4">
      <BaseCard
        shape="rounded mt-1"
        class="py-3 px-4 mb-4 sm:flex sm:items-center sm:justify-between"
      >
        <h3 class="text-lg font-medium leading-6">Category</h3>
        <div class="mt-3 sm:mt-0 sm:ml-4">
          <BaseButton
            color="primary"
            @click="catAddForm = true"
            type="submit"
            class="inline-flex gap-2 justify-center rounded-md border border-transparent bg-gray-800 py-2 px-4 text-sm font-medium text-white -sm hover:bg-gray-900 focus:outline-none focus:ring-2 focus:ring-gray-900 focus:ring-offset-2"
          >
            + Add Category
          </BaseButton>
        </div>
      </BaseCard>
      <BaseCard
        shape="rounded"
        v-if="catAddForm"
        class="py-3 px-4 mb-4 sm:flex sm:items-center justify-start gap-2"
      >
        <span v-if="newSection.image" class="relative">
          <!-- <svg
            @click="newSection.image = ''"
            class="absolute -top-1 -left-1 text-rose-400 bg-rose-50 p-1 -lg hover:-xl cursor-pointer"
            xmlns="http://www.w3.org/2000/svg"
            width="22"
            height="22"
            viewBox="0 0 24 24"
          >
            <path
              fill="currentColor"
              d="m9.4 16.5l2.6-2.6l2.6 2.6l1.4-1.4l-2.6-2.6L16 9.9l-1.4-1.4l-2.6 2.6l-2.6-2.6L8 9.9l2.6 2.6L8 15.1ZM5 21V6H4V4h5V3h6v1h5v2h-1v15Zm2-2h10V6H7ZM7 6v13Z"
            />
          </svg> -->
          <UIcon
            @click="newSection.image = ''"
            name="i-heroicons:trash"
            class="absolute -top-1 -left-1 text-rose-400 bg-rose-50 p-1 -lg hover:-xl cursor-pointer"
          />

          <img
            :src="newSection.image"
            alt=""
            srcset=""
            class="w-12 h-12 object-cover rounded"
          />
        </span>
        <span v-else>
          <input
            type="file"
            class="hidden"
            id="fileUploader"
            @change="uploadSectionImage"
          />
          <label
            for="fileUploader"
            @click="uploader = true"
            class="w-12 h-10 -slate-400 text-slate-500 flex flex-col gap-1 justify-center items-center text-sm p-1 rounded cursor-pointer"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="20"
              height="20"
              class="text-slate-500"
              viewBox="0 0 48 48"
            >
              <g fill="none">
                <path
                  fill="#000"
                  d="M44 24C44 22.8954 43.1046 22 42 22C40.8954 22 40 22.8954 40 24H44ZM24 8C25.1046 8 26 7.10457 26 6C26 4.89543 25.1046 4 24 4V8ZM39 40H9V44H39V40ZM8 39V9H4V39H8ZM40 24V39H44V24H40ZM9 8H24V4H9V8ZM9 40C8.44772 40 8 39.5523 8 39H4C4 41.7614 6.23857 44 9 44V40ZM39 44C41.7614 44 44 41.7614 44 39H40C40 39.5523 39.5523 40 39 40V44ZM8 9C8 8.44772 8.44771 8 9 8V4C6.23858 4 4 6.23857 4 9H8Z"
                />
                <path
                  stroke="#000"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="4"
                  d="M6 35L16.6931 25.198C17.4389 24.5143 18.5779 24.4953 19.3461 25.1538L32 36"
                />
                <path
                  stroke="#000"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="4"
                  d="M28 31L32.7735 26.2265C33.4772 25.5228 34.5914 25.4436 35.3877 26.0408L42 31"
                />
                <path
                  stroke="#000"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="4"
                  d="M37 18L37 6"
                />
                <path
                  stroke="#000"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="4"
                  d="M32 11L37 6L42 11"
                />
              </g>
            </svg>
          </label>
        </span>
        <input
          v-model="newSection.name"
          type="text"
          class="block max-w-xs w-full -gray-300 rounded-md -sm py-2 px-3 focus:outline-none focus:ring-indigo-500 focus:-indigo-500 sm:text-sm border"
          placeholder="New Category"
        />

        <BaseButton
          color="primary"
          @click="addSection"
          type="submit"
          class="inline-flex gap-2 justify-center rounded-md border border-transparent bg-gray-800 py-2 px-4 text-sm font-medium text-white -sm hover:bg-gray-900 focus:outline-none focus:ring-2 focus:ring-gray-900 focus:ring-offset-2"
        >
          + Add
        </BaseButton>
        <button
          @click="catAddForm = false"
          type="button"
          class="inline-flex items-center rounded-md bg-slate-100 px-4 py-2 text-sm font-medium text-slate-700 hover:bg-slate-200 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2"
        >
          Cancel
        </button>
      </BaseCard>
      <p v-if="showError" class="text-red-500 mb-4">* Fill all the fields</p>
      <BaseCard shape="rounded" class="mx-auto">
        <div class="mx-auto w-full rounded-lg -stroke">
          <div class="max-w-full">
            <table class="w-full table-auto min-w-[700px]">
              <thead>
                <tr class="-b -stroke">
                  <th class="max-w-[200px] py-5 px-4">
                    <p class="text-left text-base font-medium">Category</p>
                  </th>
                  <th class="min-w-[90px] py-5 pl-4 pr-8">
                    <p class="text-left text-base font-medium">Sub Category</p>
                  </th>
                </tr>
              </thead>
              <tbody>
                <tr
                  class="-b -stroke align-middle"
                  v-for="section in categories"
                  :key="section.id"
                  style="vertical-align: middle"
                >
                  <td class="p-1 px-5 pr-3 w-[320px]">
                    <div class="flex items-center">
                      <div class="flex items-center gap-1 -l-2 px-4">
                        <img
                          v-if="section.image"
                          :src="Api.baseURL + section.image"
                          alt="product"
                          class="mr-4 h-[40px] w-[40px] rounded object-contain object-center"
                        />
                        <img
                          v-else
                          src="/static/frontend/images/blank-product.jpg"
                          alt="product"
                          class="mr-4 h-[40px] w-[40px] rounded object-contain object-center border"
                        />
                        <p class="text-sm text-body-color">
                          {{ section.name }}
                        </p>
                      </div>
                    </div>
                  </td>
                  <td
                    class="p-4 px-2 flex-1 flex gap-2 items-center h-full flex-wrap"
                  >
                    <div
                      class="flex h-full gap-1 items-center rounded p-2 px-2"
                      v-for="cat in section.category_set"
                      :key="cat.id"
                    >
                      <img
                        v-if="cat.image"
                        :src="Api.baseURL + cat.image"
                        alt="product"
                        class="rounded-full mr-4 h-[30px] w-[30px] object-contain object-center"
                      />
                      <img
                        v-else
                        src="/static/frontend/images/blank-product.jpg"
                        alt="product"
                        class="rounded-full mr-0 h-[30px] w-[30] object-contain object-center border"
                      />
                      <p class="text-sm text-body-color">{{ cat.name }}</p>
                    </div>
                    <div
                      v-if="section.category_set.length < 1"
                      class="rounded px-2 py-1 cursor-pointer text-xs text-indigo-800"
                      @click="updateSection(section)"
                    >
                      + Add Sub-Category
                    </div>
                  </td>
                  <td class="py-[18px] px-4 w-[50px]">
                    <div class="relative subaddplus flex gap-1.5">
                      <button
                        class="text-body-color cursor-pointer dark:bg-slate-800 p-1"
                        @click="updateSection(section)"
                      >
                        <svg
                          xmlns="http://www.w3.org/2000/svg"
                          width="16"
                          height="16"
                          viewBox="0 0 24 24"
                        >
                          <path
                            fill="currentColor"
                            d="m19.3 8.925l-4.25-4.2l1.4-1.4q.575-.575 1.413-.575q.837 0 1.412.575l1.4 1.4q.575.575.6 1.388q.025.812-.55 1.387ZM17.85 10.4L7.25 21H3v-4.25l10.6-10.6Z"
                          />
                        </svg>
                      </button>
                      <button
                        @click="deleteSection(update.id)"
                        class="mx-auto flex items-center rounded gap-2 text-rose-500 px-1 py-1 hover: hover:bg-transparent"
                        type="button"
                      >
                        <UIcon
                          name="i-heroicons-trash"
                          class="text-rose-400 p-1 -lg hover:-xl cursor-pointer"
                        />
                      </button>
                    </div>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </BaseCard>
    </section>
    <CommonOver :show="update != ''">
      <DialogPanel class="pointer-events-auto relative w-screen max-w-md">
        <div
          class="flex h-full flex-col text-muted-500 overflow-y-scroll-no custom-scroll bg-slate-50 dark:bg-slate-800 shadow-xl m-2 rounded-md"
          v-if="update"
        >
          <div class="p-2 pt-6 h-full rounded">
            <div
              class="px-2 flex-col md:flex-row flex items-center justify-between mb-6"
            >
              <h5 class="font-semibold leading-4">
                Customize Category: {{ update.name }}
              </h5>
              <TransitionChild
                as="template"
                enter="ease-in-out duration-500"
                enter-from="opacity-0"
                enter-to="opacity-100"
                leave="ease-in-out duration-500"
                leave-from="opacity-100"
                leave-to="opacity-0"
              >
                <div
                  class="absolute top-2 right-2 flex pt-4 pr-2 sm:-ml-10 sm:pr-4"
                >
                  <span
                    type="button"
                    class="rounded-md hover: cursor-pointer p-1 bg-slate-500/10"
                    @click="closeUpdate"
                  >
                    <span class="sr-only">Close panel</span>
                    <svg
                      xmlns="http://www.w3.org/2000/svg"
                      width="22"
                      height="22"
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
            </div>

            <div class="relative mt-8 flex-1">
              <!-- Your content -->
              <div
                class="py-3 px-4 mb-4 flex flex-wrap md:flex-nowrap sm:items-center justify-start gap-2 rounded-md bg-slate-400/10"
              >
                <div
                  class="flex flex-wrap sm:items-center justify-start gap-2 rounded min-w-[80px]"
                >
                  <span
                    v-if="update.newimage"
                    class="relative -l-2 px-4 text-rose-500"
                  >
                    <UIcon
                      @click="update.newimage = ''"
                      name="i-heroicons-trash"
                      class="absolute -top-1 left-3 text-rose-400 bg-red-500 p-1 z-[9999] text-lg cursor-pointer"
                    />
                    <img
                      :src="update.newimage"
                      alt=""
                      srcset=""
                      class="w-12 h-12 object-cover rounded"
                    />
                  </span>
                  <span
                    v-else-if="update.image"
                    class="relative -l-2 px-4 text-rose-500"
                  >
                    <UIcon
                      @click="update.newimage = ''"
                      name="i-heroicons-trash"
                      class="absolute -top-1 left-3 text-rose-400 bg-rose-50 p-1 z-[9999] text-lg cursor-pointer"
                    />
                    <img
                      :src="Api.baseURL + update.image"
                      alt=""
                      srcset=""
                      class="w-12 h-12 object-contain rounded-full"
                    />
                  </span>
                  <span v-else>
                    <input
                      type="file"
                      class="hidden border"
                      id="fileUploader"
                      @change="updateSectionImage"
                    />
                    <label
                      for="fileUploader"
                      @click="uploader = true"
                      class="w-12 h-12 flex flex-col gap-1 justify-center items-center text-sm p-1 rounded text-slate-400 cursor-pointer"
                    >
                      <svg
                        xmlns="http://www.w3.org/2000/svg"
                        width="32"
                        height="22"
                        viewBox="0 0 2048 2048"
                      >
                        <path
                          fill="currentColor"
                          d="M1408 576q0-26 19-45t45-19q26 0 45 19t19 45q0 26-19 45t-45 19q-26 0-45-19t-19-45zm640 960v128h-256v256h-128v-256h-256v-128h256v-256h128v256h256zM922 1216l358 357v91H0V256h1792v896h-128V384H128v421l192-191l512 512l256-256l448 447v91h-91l-357-358l-166 166zM320 794L128 987v549h933L320 794z"
                        />
                      </svg>
                    </label>
                  </span>
                </div>
                <input
                  v-model="update.name"
                  type="text"
                  class="block max-w-xs w-full -gray-300 rounded-md -sm py-2 px-3 focus:outline-none focus:ring-indigo-500 focus:-indigo-500 sm:text-sm border"
                  placeholder="Main Category"
                />
              </div>

              <div class="px-2">
                <h6 class="my-2 mt-6">Sub Categories</h6>
                <div class="flex gap-0 flex-wrap">
                  <div
                    v-for="cat in update.category_set"
                    :key="cat.id"
                    :class="{ hidden: cat.deleted }"
                    class="p-2 mb-4 flex-1 flex items-center sm:items-center justify-start gap-2"
                  >
                    <span v-if="cat.newimage" class="relative">
                      <svg
                        @click="cat.newimage = ''"
                        class="absolute -top-1 -left-1 text-rose-400 bg-rose-50 p-1 -lg hover:-xl cursor-pointer"
                        xmlns="http://www.w3.org/2000/svg"
                        width="22"
                        height="22"
                        viewBox="0 0 24 24"
                      >
                        <path
                          fill="currentColor"
                          d="m9.4 16.5l2.6-2.6l2.6 2.6l1.4-1.4l-2.6-2.6L16 9.9l-1.4-1.4l-2.6 2.6l-2.6-2.6L8 9.9l2.6 2.6L8 15.1ZM5 21V6H4V4h5V3h6v1h5v2h-1v15Zm2-2h10V6H7ZM7 6v13Z"
                        />
                      </svg>
                      <img
                        :src="cat.newimage"
                        alt=""
                        srcset=""
                        class="w-10 h-10 rounded-full object-cover"
                      />
                    </span>
                    <span v-else-if="cat.image" class="relative">
                      <svg
                        @click="cat.image = ''"
                        class="absolute -top-1 -left-1 text-rose-400 bg-rose-50 p-1 -lg hover:-xl cursor-pointer"
                        xmlns="http://www.w3.org/2000/svg"
                        width="22"
                        height="22"
                        viewBox="0 0 24 24"
                      >
                        <path
                          fill="currentColor"
                          d="m9.4 16.5l2.6-2.6l2.6 2.6l1.4-1.4l-2.6-2.6L16 9.9l-1.4-1.4l-2.6 2.6l-2.6-2.6L8 9.9l2.6 2.6L8 15.1ZM5 21V6H4V4h5V3h6v1h5v2h-1v15Zm2-2h10V6H7ZM7 6v13Z"
                        />
                      </svg>
                      <img
                        :src="Api.baseURL + cat.image"
                        alt=""
                        srcset=""
                        class="w-10 h-10 rounded-full object-cover"
                      />
                    </span>
                    <span v-else>
                      <input
                        type="file"
                        class="hidden"
                        id="fileUploader"
                        @change="updateCategoryImage(cat, $event)"
                      />
                      <label
                        for="fileUploader"
                        @click="uploader = true"
                        class="w-10 h-10 flex flex-col gap-1 justify-center items-center text-sm p-1 rounded-full text-slate-400 cursor-pointer"
                      >
                        <svg
                          xmlns="http://www.w3.org/2000/svg"
                          width="32"
                          height="22"
                          viewBox="0 0 2048 2048"
                        >
                          <path
                            fill="currentColor"
                            d="M1408 576q0-26 19-45t45-19q26 0 45 19t19 45q0 26-19 45t-45 19q-26 0-45-19t-19-45zm640 960v128h-256v256h-128v-256h-256v-128h256v-256h128v256h256zM922 1216l358 357v91H0V256h1792v896h-128V384H128v421l192-191l512 512l256-256l448 447v91h-91l-357-358l-166 166zM320 794L128 987v549h933L320 794z"
                          />
                        </svg>
                      </label>
                    </span>
                    <input
                      v-model="cat.name"
                      type="text"
                      class="block w-[140px] -gray-300 rounded-md py-1.5 px-3 focus:outline-none focus:ring-indigo-500 focus:-indigo-500 sm:text-sm"
                      placeholder="Category Name"
                    />

                    <UIcon
                      @click="deleteCat(cat)"
                      name="i-heroicons-trash"
                      class="p-0 cursor-pointer text-rose-600"
                    />
                  </div>
                </div>
                <div
                  class="py-3 px-1 mb-4 flex flex-wrap md:flex-nowrap items-center sm:items-center justify-start gap-2"
                >
                  <span v-if="newCategory.newimage" class="relative">
                    <svg
                      @click="newCategory.newimage = ''"
                      class="absolute -top-1 -left-1 text-rose-400 bg-rose-50 p-1 cursor-pointer"
                      xmlns="http://www.w3.org/2000/svg"
                      width="22"
                      height="22"
                      viewBox="0 0 24 24"
                    >
                      <path
                        fill="currentColor"
                        d="m9.4 16.5l2.6-2.6l2.6 2.6l1.4-1.4l-2.6-2.6L16 9.9l-1.4-1.4l-2.6 2.6l-2.6-2.6L8 9.9l2.6 2.6L8 15.1ZM5 21V6H4V4h5V3h6v1h5v2h-1v15Zm2-2h10V6H7ZM7 6v13Z"
                      />
                    </svg>
                    <img
                      :src="newCategory.newimage"
                      alt=""
                      srcset=""
                      class="w-12 h-12 object-cover rounded border"
                    />
                  </span>
                  <span v-else>
                    <input
                      type="file"
                      class="hidden"
                      id="fileUploader2"
                      @change="updateNewCatImage"
                    />
                    <label
                      for="fileUploader2"
                      @click="uploader = true"
                      class="w-10 h-10 -slate-400 text-slate-500 flex flex-col gap-1 justify-center items-center text-sm p-1 rounded cursor-pointer"
                    >
                      <svg
                        xmlns="http://www.w3.org/2000/svg"
                        width="20"
                        height="20"
                        class="text-slate-500"
                        viewBox="0 0 48 48"
                      >
                        <g fill="none">
                          <path
                            fill="#000"
                            d="M44 24C44 22.8954 43.1046 22 42 22C40.8954 22 40 22.8954 40 24H44ZM24 8C25.1046 8 26 7.10457 26 6C26 4.89543 25.1046 4 24 4V8ZM39 40H9V44H39V40ZM8 39V9H4V39H8ZM40 24V39H44V24H40ZM9 8H24V4H9V8ZM9 40C8.44772 40 8 39.5523 8 39H4C4 41.7614 6.23857 44 9 44V40ZM39 44C41.7614 44 44 41.7614 44 39H40C40 39.5523 39.5523 40 39 40V44ZM8 9C8 8.44772 8.44771 8 9 8V4C6.23858 4 4 6.23857 4 9H8Z"
                          />
                          <path
                            stroke="#000"
                            stroke-linecap="round"
                            stroke-linejoin="round"
                            stroke-width="4"
                            d="M6 35L16.6931 25.198C17.4389 24.5143 18.5779 24.4953 19.3461 25.1538L32 36"
                          />
                          <path
                            stroke="#000"
                            stroke-linecap="round"
                            stroke-linejoin="round"
                            stroke-width="4"
                            d="M28 31L32.7735 26.2265C33.4772 25.5228 34.5914 25.4436 35.3877 26.0408L42 31"
                          />
                          <path
                            stroke="#000"
                            stroke-linecap="round"
                            stroke-linejoin="round"
                            stroke-width="4"
                            d="M37 18L37 6"
                          />
                          <path
                            stroke="#000"
                            stroke-linecap="round"
                            stroke-linejoin="round"
                            stroke-width="4"
                            d="M32 11L37 6L42 11"
                          />
                        </g>
                      </svg>
                    </label>
                  </span>
                  <input
                    v-model="newCategory.name"
                    type="text"
                    class="block max-w-[180px] w-full border -gray-300 rounded-md -sm py-[9px] px-3 focus:outline-none focus:ring-indigo-500 focus:-indigo-500 sm:text-sm"
                    placeholder="New Sub-Category"
                  />

                  <BaseButton
                    color="primary"
                    @click="addCategory"
                    type="submit"
                    class="inline-flex gap-2 justify-center rounded-md border border-transparent bg-gray-800 py-2 px-4 text-sm font-medium text-white -sm hover:bg-gray-900 focus:outline-none focus:ring-2 focus:ring-gray-900 focus:ring-offset-2"
                  >
                    + Add
                  </BaseButton>
                </div>
                <div class="flex gap-1">
                  <BaseButton
                    :class="{ 'opacity-90': !unsaved }"
                    color="primary"
                    @click="saveSection"
                    type="submit"
                    class="inline-flex gap-2 justify-center rounded-md border border-transparent bg-gray-800 py-2 px-4 text-sm font-medium text-white -sm hover:bg-gray-900 focus:outline-none focus:ring-2 focus:ring-gray-900 focus:ring-offset-2 md:w-1/2"
                  >
                    <svg
                      xmlns="http://www.w3.org/2000/svg"
                      width="18"
                      height="18"
                      viewBox="0 0 24 24"
                    >
                      <path
                        fill="currentColor"
                        d="M14 12.8c-.5-.49-1.22-.8-2-.8a2.996 2.996 0 0 0-1 5.82a6.034 6.034 0 0 1 3-5.02M11.09 19H5V5h11.17L19 7.83v4.52c.75.26 1.42.65 2 1.19V7l-4-4H5a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h6.81c-.35-.61-.6-1.28-.72-2M6 10h9V6H6v4m9.75 11L13 18l1.16-1.16l1.59 1.59l3.59-3.59l1.16 1.41L15.75 21"
                      />
                    </svg>
                    Save Changes
                  </BaseButton>

                  <button
                    @click="update = ''"
                    class="bg-red-500 hover:bg-red-700 text-white font-bold py-1.5 px-4 rounded md:w-1/2"
                  >
                    Cancel
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </DialogPanel>
    </CommonOver>
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
const { $swal } = useNuxtApp();
const { notifs } = useAuth();
const Api = useApi();
const catAddForm = ref(false);
const showError = ref(false);
const newSection = ref({
  type: "section",
  name: "",
  image: "",
});
const uploadSectionImage = (e) => {
  const file = e.target.files[0];
  console.log("file", file);
  const reader = new FileReader();
  reader.readAsDataURL(file);
  reader.onload = () => {
    newSection.value.image = reader.result;
  };
};
const categories = ref([]);
const getCategories = () => {
  Api.get("/api/ecommerce/dash/categories").then((res) => {
    categories.value = res.data;
  });
};
getCategories();
const addSection = () => {
  if (newSection.value.name === "" || newSection.value.image === "") {
    showError.value = true;
    return;
  }
  showError.value = false;
  Api.post("/api/ecommerce/dash/categories", newSection.value).then((res) => {
    getCategories();
    catAddForm.value = false;
    newSection.value = {
      type: "section",
      name: "",
      image: "",
    };
    notifs.value.push({ type: "success", message: "New category added" });
  });
};
const update = ref("");
const unsaved = ref(false);
const newCategory = ref({
  type: "cat",
  name: "",
  newimage: "",
});
const closeUpdate = (section) => {
  if (unsaved.value) {
    $swal
      .fire({
        title: "Are you sure?",
        text: "You have unsaved changes, if you close this section, your changes will be lost.",
        icon: "warning",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        confirmButtonText: "Yes, close it!",
      })
      .then((result) => {
        if (result.isConfirmed) {
          update.value = "";
          unsaved.value = false;
        }
      });
  } else {
    update.value = "";
  }
};
const updateSection = (section) => {
  update.value = JSON.parse(JSON.stringify(section));
};
const updateSectionImage = (e) => {
  const file = e.target.files[0];
  console.log("file", file);
  const reader = new FileReader();
  reader.readAsDataURL(file);
  reader.onload = () => {
    update.value.newimage = reader.result;
  };
};
const updateCategoryImage = (cat, e) => {
  console.log("cat", cat);
  console.log("e", e);
  const file = e.target.files[0];
  const reader = new FileReader();
  reader.readAsDataURL(file);
  reader.onload = () => {
    cat.newimage = reader.result;
  };
};
const updateNewCatImage = (e) => {
  const file = e.target.files[0];
  const reader = new FileReader();
  reader.readAsDataURL(file);
  reader.onload = () => {
    newCategory.value.newimage = reader.result;
  };
};
const deleteCat = (cat) => {
  cat["deleted"] = true;
  notifs.value.push({ type: "success", message: "Sub category deleted" });
};
const addCategory = () => {
  if (!newCategory.value.name) {
    showError.value = true;
    return;
  }
  update.value.category_set.push(newCategory.value);
  newCategory.value = {
    type: "cat",
    name: "",
    newimage: "",
  };
  unsaved.value = true;
  notifs.value.push({ type: "success", message: "New sub category added" });
};
const saveSection = () => {
  Api.put("/api/ecommerce/dash/categories", update.value).then((res) => {
    getCategories();
    update.value = "";
    notifs.value.push({ type: "success", message: "Category updated" });
    unsaved.value = false;
  });
};
const deleteSection = (id) => {
  $swal
    .fire({
      title: "Are you sure?",
      text: "You won't be able to revert this!",
      icon: "warning",
      showCancelButton: true,
      confirmButtonColor: "#3085d6",
      cancelButtonColor: "#d33",
      confirmButtonText: "Yes, delete it!",
    })
    .then((result) => {
      if (result.isConfirmed) {
        Api.del("/api/ecommerce/dash/categories?id=" + id).then((res) => {
          getCategories();
          update.value = "";
          notifs.value.push({ type: "success", message: "Category deleted" });
        });
      }
    });
};
</script>

<style scoped></style>
