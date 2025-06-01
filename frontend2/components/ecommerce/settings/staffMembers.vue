<template>
    <div>
        <div class="space-y-6  lg:col-span-9">
            <div class="border-b bg-slate-50 border-gray-200 py-3 px-5  sm:flex sm:items-center sm:justify-between">
                <h3 class="text-lg font-medium leading-6">Staff Members</h3>
                <div class="mt-3 sm:mt-0 sm:ml-4">
                    <button @click="form=true" type="button" class="inline-flex items-center rounded-md border border-transparent bg-indigo-600 px-4 py-2 text-sm font-medium text-white shadow-sm hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2">+ Add</button>
                </div>
            </div>
            <div v-if="form" class="border-b bg-slate-50 border-gray-200 py-6 px-4 mb-4 max-w-xl mx-auto shadow">
              <div class="flex flex-wrap gap-1 mb-4 w-full">
                <div class="max-w-[250px] w-full my-2">
                  <label for="">Name</label>
                  <input v-model="newStaff.name" type="text" class="w-full block border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm" placeholder="Staff Name" />
                </div>
                <div class="max-w-[250px] w-full my-2">
                  <label for="">Email</label>
                  <input v-model="newStaff.email" type="email" class="w-full block border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm" placeholder="Email" />
                </div>
                <div class="max-w-[250px] w-full my-2">
                  <label for="">Phone</label>
                  <input v-model="newStaff.phone" type="text" class="w-full block border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm" placeholder="Phone" />
                </div>
                <div class="max-w-[250px] w-full my-2">
                  <label for="">Password</label>
                  <input v-model="newStaff.password" type="password" class="w-full block border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm" placeholder="Password" />
                </div>
                <div class="max-w-[250px] w-full my-2">
                  <label for="">Confirm Password</label>
                  <input v-model="newStaff.password_confirmation" type="password" class="block max-w-xs w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm" placeholder="Confirm Password" />
                </div>
              </div>
                <p class="my-4 text-rose-500" v-if="newStaff.error">{{ newStaff.error }}</p>
                <button @click="addStaff" type="button" class="mr-2 inline-flex items-center rounded-md border border-transparent bg-indigo-600 px-4 py-2 text-sm font-medium text-white shadow-sm hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2">+ Add New Staff</button>
                <button @click="form = false" type="button" class="inline-flex items-center rounded-md border shadow bg-slate-100 px-4 py-2 text-sm font-medium text-slate-700 hover:bg-slate-200 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2">Cancel</button>
            </div>
            <div class="members grid grid-cols-3 gap-2">
                <section class="bg-gray-2" v-for="staff in staffs" :key="staff.id">
                  <div class="mx-auto px-4 md:container">
                    <div class="border-stroke shadow-card mx-auto w-full max-w-[370px] overflow-hidden rounded-lg border bg-white">
                      <div class="px-3 pt-10 pb-8">
                        <div class="text-center">
                          <h5 class="font-semibold text-black">{{staff.name}}</h5>
                          <p class="text-body-color mb-1 text-sm">Staff</p>
                          <p class="text-body-color mb-1 text-sm">{{staff.email}}</p>
                          <p class="text-body-color mb-1 text-sm">{{staff.phone}}</p>
                          <div class="flex items-center justify-center space-x-[10px]">
                            <button class="bg-primary h-[34px] rounded-full border border-transparent px-5 text-sm font-medium text-white hover:bg-opacity-90">MODIFY</button>
                            <button class="hover:borderprimary border-stroke hover:border-primary hover:bg-primary flex h-[34px] w-[34px] items-center justify-center rounded-full border bg-white text-[#98A6AD] hover:text-white">
                              <svg width="16" height="16" viewBox="0 0 16 16" class="fill-current">
                                <path fill-rule="evenodd" clip-rule="evenodd" d="M2.66667 7.33398C3.03486 7.33398 3.33333 7.63246 3.33333 8.00065V13.334C3.33333 13.5108 3.40357 13.6804 3.5286 13.8054C3.65362 13.9304 3.82319 14.0007 4 14.0007H12C12.1768 14.0007 12.3464 13.9304 12.4714 13.8054C12.5964 13.6804 12.6667 13.5108 12.6667 13.334V8.00065C12.6667 7.63246 12.9651 7.33398 13.3333 7.33398C13.7015 7.33398 14 7.63246 14 8.00065V13.334C14 13.8644 13.7893 14.3731 13.4142 14.7482C13.0391 15.1233 12.5304 15.334 12 15.334H4C3.46957 15.334 2.96086 15.1233 2.58579 14.7482C2.21071 14.3731 2 13.8644 2 13.334V8.00065C2 7.63246 2.29848 7.33398 2.66667 7.33398Z" />
                                <path fill-rule="evenodd" clip-rule="evenodd" d="M7.52843 0.861278C7.78878 0.600928 8.21089 0.600928 8.47124 0.861278L11.1379 3.52794C11.3983 3.78829 11.3983 4.2104 11.1379 4.47075C10.8776 4.7311 10.4554 4.7311 10.1951 4.47075L7.99984 2.27549L5.80458 4.47075C5.54423 4.7311 5.12212 4.7311 4.86177 4.47075C4.60142 4.2104 4.60142 3.78829 4.86177 3.52794L7.52843 0.861278Z" />
                                <path fill-rule="evenodd" clip-rule="evenodd" d="M8.00016 0.666016C8.36835 0.666016 8.66683 0.964492 8.66683 1.33268V9.99935C8.66683 10.3675 8.36835 10.666 8.00016 10.666C7.63197 10.666 7.3335 10.3675 7.3335 9.99935V1.33268C7.3335 0.964492 7.63197 0.666016 8.00016 0.666016Z" />
                              </svg>
                            </button>
                            <button class="hover:borderprimary border-stroke hover:border-primary hover:bg-primary flex h-[34px] w-[34px] items-center justify-center rounded-full border bg-white text-[#98A6AD] hover:text-white">
                              <svg width="14" height="14" viewBox="0 0 14 14" class="fill-current">
                                <g clip-path="url(#clip0_3019_3044)">
                                  <path d="M12.25 5.25C11.2835 5.25 10.5 6.0335 10.5 7C10.5 7.9665 11.2835 8.75 12.25 8.75C13.2165 8.75 14 7.9665 14 7C14 6.0335 13.2165 5.25 12.25 5.25Z" />
                                  <path d="M7 5.25C6.0335 5.25 5.25 6.0335 5.25 7C5.25 7.9665 6.0335 8.75 7 8.75C7.9665 8.75 8.75 7.9665 8.75 7C8.75 6.0335 7.9665 5.25 7 5.25Z" />
                                  <path d="M1.75 5.25C0.783502 5.25 2.37484e-07 6.0335 1.5299e-07 7C6.84959e-08 7.9665 0.783502 8.75 1.75 8.75C2.7165 8.75 3.5 7.9665 3.5 7C3.5 6.0335 2.7165 5.25 1.75 5.25Z" />
                                </g>
                                <defs>
                                  <clipPath id="clip0_3019_3044">
                                    <rect width="14" height="14" fill="white" transform="translate(14 14) rotate(-180)" />
                                  </clipPath>
                                </defs>
                              </svg>
                            </button>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </section>


            </div>

        </div>
    </div>
</template>

<script setup>
  const Api = useApi();
  const staffs = ref('')
  async function getStaff(){
    const res = await Api.get('/api/ecommerce/dash/staffs');
    staffs.value = res.data;
  }
  getStaff()
  const form = ref(false)
  const newStaff = ref({
    name: '',
    email: '',
    phone: '',
    password: '',
    password_confirmation: '',
    error: '',
  })

  async function addStaff(){
    newStaff.value.error = '';
    if ( !newStaff.value.name || !newStaff.value.email || !newStaff.value.phone || !newStaff.value.password || !newStaff.value.password_confirmation ) {
      newStaff.value.error = 'All fields are required';
      return;
    }
    if ( newStaff.value.password !== newStaff.value.password_confirmation ) {
      newStaff.value.error = 'Passwords do not match';
      return;
    }
    const res = await Api.post('/api/ecommerce/dash/staffs', newStaff.value);
    form.value = false;
    newStaff.value = {
      name: '',
      email: '',
      phone: '',
      password: '',
      password_confirmation: '',
      error: '',
    }
    getStaff()
  }

</script>

<style scoped>

</style>