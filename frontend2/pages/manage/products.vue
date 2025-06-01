<template>
    <div class="w-full overflow-x-scroll max-w-full">
      <div class="w-full min-w-[1170px]">
        <div class="bg-slate-50 px-3 py-3">
          <div class="flex items-center justify-between">
            <p class="focus:outline-none text-base sm:text-lg md:text-xl lg:text-2xl font-bold leading-normal text-gray-800">
              Products
            </p>
            <div class="py-3 px-4 flex items-center text-sm font-medium leading-none text-gray-600 bg-gray-200 hover:bg-gray-300 cursor-pointer rounded">
              <p>Sort By:</p>
              <select aria-label="select" class="focus:text-indigo-600 focus:outline-none bg-transparent ml-1">
                <option class="text-sm text-indigo-800">Latest</option>
                <option class="text-sm text-indigo-800">Oldest</option>
                <option class="text-sm text-indigo-800">Price: Low to High</option>
                <option class="text-sm text-indigo-800">Price: High to Low</option>
              </select>
            </div>
          </div>
        </div>
        <div class="bg-white py-4 md:py-7">
          <div class="sm:flex items-center justify-between border-b border-gray-200">
            <ul class="flex flex-wrap text-sm font-medium text-center text-gray-500">
              <li class="mr-2">
                <a href="#" aria-current="page" class="inline-block p-4 text-blue-600 bg-gray-100 rounded-t-lg active">Products</a>
              </li>
              <li class="mr-2">
                <a href="#" class="inline-block p-4 rounded-t-lg hover:text-gray-600 hover:bg-gray-50 dark:hover:bg-gray-800 dark:hover:text-gray-300">Categories</a>
              </li>
            </ul>
            <button @click="modalOpen = true" class="focus:ring-2 focus:ring-offset-2 focus:ring-indigo-600 mt-4 sm:mt-0 inline-flex items-start justify-start px-6 py-3 bg-indigo-700 hover:bg-indigo-600 focus:outline-none rounded">
              <p class="text-sm font-medium leading-none text-white">New Product</p>
            </button>
          </div>
          <div class="mt-1 overflow-x-auto">
            <table class="w-full whitespace-nowrap">
              <tbody v-if="products && products.results">
                <template v-for="product in products.results">
                  <tr tabindex="0" class="focus:outline-none h-14 border border-gray-100 rounded">
                    <td class="">
                      <div class="flex items-center pl-5">
                        <p class="text-base font-medium leading-none text-gray-700 mr-2">{{ product.name }}</p>
                      </div>
                    </td>
                    <td class="pl-5">
                      <p class="text-sm leading-none text-gray-600 ml-2">{{ product.description }}</p>
                    </td>
                    <td class="pl-5">
                      <p class="text-sm leading-none text-gray-600 ml-2">{{ product.category }}</p>
                    </td>
                    <td class="pl-5">
                      <p class="text-sm leading-none text-gray-600 ml-2">$ {{ product.price }}</p>
                    </td>
                    <td class="pl-5">
                      <p class="text-sm leading-none text-gray-600 ml-2">{{ product.quantity_in_stock }}</p>
                    </td>
                    <td class="pl-4 flex justify-end">
                      <button @click="viewProduct(product)" class="focus:ring-2 focus:ring-offset-2 focus:ring-blue-300 text-sm leading-none text-gray-600 py-3 px-5 bg-gray-100 rounded hover:bg-gray-200 focus:outline-none">View</button>
                    </td>
                  </tr>
                  <tr class="h-1"></tr>
                </template>
              </tbody>
            </table>
          </div>
        </div>
      </div>
      <!-- Modal Section Start -->
      <section>
        <div v-if="modalOpen" class="fixed top-0 left-0 h-screen w-full overflow-y-scroll py-10 bg-slate-800/10">
          <div class="mx-auto max-w-[465px] rounded-[10px] bg-white max-w-[500px] p-8 shadow-two">
            <div class="text-center">
              <div class="mt-4">
                <div class="grid grid-cols-2 gap-4">
                  <div>
                    <label for="name" class="block font-medium mb-1 text-left">Product Name</label>
                    <input v-model="productForm.name" type="text" id="name" required class="w-full border rounded-md px-3 py-2 border-gray-300 focus:ring-blue-500 focus:border-blue-500" />
                  </div>
                  <div>
                    <label for="category" class="block font-medium mb-1 text-left">Category</label>
                    <input v-model="productForm.category" type="text" id="category" required class="w-full rounded-md px-3 py-2 border border-gray-300 focus:ring-blue-500 focus:border-blue-500" />
                  </div>
                  <div>
                    <label for="price" class="block font-medium mb-1 text-left">Price ($)</label>
                    <input v-model="productForm.price" type="number" id="price" required step="0.01" class="w-full rounded-md px-3 py-2 border border-gray-300 focus:ring-blue-500 focus:border-blue-500" />
                  </div>
                  <div>
                    <label for="quantity_in_stock" class="block font-medium mb-1 text-left">Quantity in Stock</label>
                    <input v-model="productForm.quantity_in_stock" type="number" id="quantity_in_stock" required class="w-full rounded-md px-3 py-2 border border-gray-300 focus:ring-blue-500 focus:border-blue-500" />
                  </div>
                  <div class="col-span-2">
                    <label for="description" class="block font-medium mb-1 text-left">Description</label>
                    <textarea v-model="productForm.description" id="description" rows="3" required class="w-full rounded-md px-3 py-2 border border-gray-300 focus:ring-blue-500 focus:border-blue-500"></textarea>
                  </div>
                </div>
              </div>
            </div>
            <div class="flex justify-center mt-8">
              <button @click="addNewProduct" class="inline-flex justify-center px-4 py-2 text-sm font-medium text-white bg-blue-600 border border-transparent rounded-md hover:bg-blue-700 focus:outline-none focus-visible:ring-2 focus-visible:ring-offset-2 focus-visible:ring-blue-500">
                Save Product
              </button>
              <button @click="modalOpen = false" class="inline-flex justify-center ml-4 px-4 py-2 text-sm font-medium text-white bg-red-600 border border-transparent rounded-md hover:bg-red-700 focus:outline-none focus-visible:ring-2 focus-visible:ring-offset-2 focus-visible:ring-red-500">
                Cancel
              </button>
            </div>
          </div>
        </div>
      </section>
      <!-- Modal Section End -->
    </div>
  </template>
  
  <script setup>
  
  const products = ref(null);
  const modalOpen = ref(false);
  const productForm = ref({
    name: '',
    description: '',
    price: 0,
    quantity_in_stock: 0,
    category: '',
  });
  definePageMeta({
      layout: 'manage'
  })
  const Api = useApi()
  
  onMounted(async () => {
    // Fetch products from the backend API
    getProducts()
  });
  async function getProducts(){
    const {data} = await Api.get('/api/office/manage/products/')
    products.value = data
    console.log(data);
 }
  
  const viewProduct = (product) => {
    // Implement the logic to view a single product
    // For example, you can show a modal with the product details
    console.log('View product:', product);
  };
  
  const addNewProduct = async () => {
    Api.post('/api/office/manage/products/', productForm.value)
        .then(res => {
            console.log(res);
            modalOpen.value = false;
            getProducts()
        })

    
  };
  </script>
  
  <style>
  /* Custom styles can be added here */
  </style>