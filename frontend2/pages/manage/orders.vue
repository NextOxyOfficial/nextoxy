<template>
    <div class="w-full overflow-x-scroll max-w-full">
        <div class="w-full min-w-[1170px]">
            <!--- more free and premium Tailwind CSS components at https://tailwinduikit.com/ --->
            <div class="bg-slate-50 px-3 py-3">
                <div class="flex items-center justify-between">
                    <p
                        class="focus:outline-none text-base sm:text-lg md:text-xl lg:text-2xl font-bold leading-normal text-gray-800">
                        Custom Orders</p>
                    <div
                        class="py-3 px-4 flex items-center text-sm font-medium leading-none text-gray-600 bg-gray-200 hover:bg-gray-300 cursor-pointer rounded">
                        <p>Sort By:</p>
                        <select aria-label="select" class="focus:text-indigo-600 focus:outline-none bg-transparent ml-1">
                            <option class="text-sm text-indigo-800">Latest</option>
                            <option class="text-sm text-indigo-800">Oldest</option>
                            <option class="text-sm text-indigo-800">Latest</option>
                        </select>
                    </div>
                </div>
            </div>
            <div class="bg-white py-4 md:py-7">
                <div class="sm:flex items-center justify-between border-b border-gray-200">
                    
                    <ul class="flex flex-wrap text-sm font-medium text-center text-gray-500">
                        <li class="mr-2">
                            <a href="#" aria-current="page" class="inline-block p-4 text-blue-600 bg-gray-100 rounded-t-lg active">All Posts</a>
                        </li>
                        <li class="mr-2">
                            <a href="#" class="inline-block p-4 rounded-t-lg hover:text-gray-600 hover:bg-gray-50 dark:hover:bg-gray-800 dark:hover:text-gray-300">Featured</a>
                        </li>
                        <li class="mr-2">
                            <a href="#" class="inline-block p-4 rounded-t-lg hover:text-gray-600 hover:bg-gray-50 dark:hover:bg-gray-800 dark:hover:text-gray-300">Top picks</a>
                        </li>
                        <li class="mr-2">
                            <a href="#" class="inline-block p-4 rounded-t-lg hover:text-gray-600 hover:bg-gray-50 dark:hover:bg-gray-800 dark:hover:text-gray-300">Best Reads</a>
                        </li>
                    </ul>

                    <nuxt-link to="/manage/no-blog-add/new" 
                        class="focus:ring-2 focus:ring-offset-2 focus:ring-indigo-600 mt-4 sm:mt-0 inline-flex items-start justify-start px-6 py-3 bg-indigo-700 hover:bg-indigo-600 focus:outline-none rounded">
                        <p class="text-sm font-medium leading-none text-white">Add Post</p>
                    </nuxt-link>
                </div>
                <div class="mt-1 overflow-x-auto">
                    <table class="w-full whitespace-nowrap">
                        <tbody v-if="orders && orders.results">
                            <template v-for="order in orders.results">
                                <tr tabindex="0" class="focus:outline-none h-14 border border-gray-100 rounded">
                                    <td>
                                        <div class="ml-5">
                                                <p>{{ order.id }}</p>
                                                <p class="mt-3 text-xs">{{ order.type }}</p>
                                        </div>
                                    </td>
                                    <td class="pl-24">
                                        <div class=" items-center">
                                            <p class="text-sm leading-none text-gray-600 ml-2 mb-1">{{ order.created_at }}</p>
                                            <p class="text-sm leading-none text-gray-600 ml-2">{{ order.f_name }} {{ order.l_name }}</p>
                                        </div>
                                    </td>
                                    <td class="text-sm">
                                            <p class="mb-2 font-medium leading-none text-gray-700 mr-2">{{ order.email }}</p>
                                            <p class="text-xs font-medium leading-none text-gray-700 mr-2">{{ order.phone }}</p>
                                    </td>
                                    <td class="pl-5">
                                        <div class="flex items-center">
                                            <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" viewBox="0 0 24 24"><path fill="currentColor" d="M5 22q-.825 0-1.413-.588T3 20V6q0-.825.588-1.413T5 4h1V2h2v2h8V2h2v2h1q.825 0 1.413.588T21 6v14q0 .825-.588 1.413T19 22H5Zm0-2h14V10H5v10ZM5 8h14V6H5v2Zm0 0V6v2Zm7 6q-.425 0-.713-.288T11 13q0-.425.288-.713T12 12q.425 0 .713.288T13 13q0 .425-.288.713T12 14Zm-4 0q-.425 0-.713-.288T7 13q0-.425.288-.713T8 12q.425 0 .713.288T9 13q0 .425-.288.713T8 14Zm8 0q-.425 0-.713-.288T15 13q0-.425.288-.713T16 12q.425 0 .713.288T17 13q0 .425-.288.713T16 14Zm-4 4q-.425 0-.713-.288T11 17q0-.425.288-.713T12 16q.425 0 .713.288T13 17q0 .425-.288.713T12 18Zm-4 0q-.425 0-.713-.288T7 17q0-.425.288-.713T8 16q.425 0 .713.288T9 17q0 .425-.288.713T8 18Zm8 0q-.425 0-.713-.288T15 17q0-.425.288-.713T16 16q.425 0 .713.288T17 17q0 .425-.288.713T16 18Z"/></svg>
                                            <p class="text-sm leading-none text-gray-600 ml-2">{{ order.created_at }}</p>
                                        </div>
                                    </td>
                                    <td class="pl-5">
                                        <div class="flex items-center">
                                            <img :src="Api.baseURL + order.image" alt="" class="max-h-12" srcset="">
                                        </div>
                                    </td>
                                    <td class="pl-5 flex gap-1 items-center justify-end">
                                        <nuxt-link :to="'/manage/no-blog-add/'+order.id"
                                            class="py-3 px-3 text-sm focus:outline-none leading-none text-red-700 bg-red-100 rounded">Edit</nuxt-link>
                                        <a :href="'/home/blog/'+order.id" target="_blank"
                                            class="focus:ring-2 focus:ring-offset-2 focus:ring-red-300 text-sm leading-none text-gray-600 py-3 px-5 bg-gray-100 rounded hover:bg-gray-200 focus:outline-none">View</a>
                                    </td>
                                </tr>
                                <tr class="h-1"></tr>
                            </template>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
    definePageMeta({
        layout: 'manage'
    })
    const Api = useApi()

    getBlog()
    const orders = ref('')
    async function getBlog(){
        const {data} = await Api.get('/api/office/home/custom-order')
        orders.value = data
        console.log(orders.value);
    }
</script>

<style scoped>.checkbox:checked+.check-icon {
    display: flex;
}</style>