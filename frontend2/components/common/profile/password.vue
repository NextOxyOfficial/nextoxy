<template>
    <div>
        <section class="bg-[#F4F7FF] py-4">
          <div class="container mx-auto">
            <div class="-mx-4 flex flex-wrap">
              <div class="w-full px-4">
                <div class="relative mx-auto max-w-[525px] overflow-hidden rounded-lg bg-white py-16 px-10 text-center sm:px-12 md:px-[60px]">
                  <section>
                    <div class="mb-6 text-left  text-body-color text-slate-500 focus:border-primary w-full rounded-md bg-[#FCFDFE] py-1 text-base outline-none focus-visible:shadow-none ">
                        Change Password
                    </div>
                    <div class="mb-6">
                      <input v-model="password.old" type="password" placeholder="Old Password" class="bordder-[#E9EDF4] text-body-color focus:border-primary w-full rounded-md border bg-[#FCFDFE] py-3 px-5 text-base placeholder-[#ACB6BE] outline-none focus-visible:shadow-none" />
                    </div>
                    <div class="mb-6">
                      <input v-model="password.new" type="password" placeholder="New Password" class="bordder-[#E9EDF4] text-body-color focus:border-primary w-full rounded-md border bg-[#FCFDFE] py-3 px-5 text-base placeholder-[#ACB6BE] outline-none focus-visible:shadow-none" />
                    </div>
                    <div class="mb-6">
                      <input v-model="password.confirm" type="password" placeholder="Confirm New Password" class="bordder-[#E9EDF4] text-body-color focus:border-primary w-full rounded-md border bg-[#FCFDFE] py-3 px-5 text-base placeholder-[#ACB6BE] outline-none focus-visible:shadow-none" />
                    </div>
                    <p class="my-2 text-rose-500" v-if="password.error">{{ password.error }}</p>
                    <p class="my-2 text-lime-500" v-if="password.success">{{ password.success }}</p>
                    <div class="mb-10">
                      <input @click="change" type="submit" value="Submit" class="border-primary bg-black w-full cursor-pointer rounded-md border py-3 px-5 text-base text-white transition hover:bg-opacity-90" />
                    </div>
                  </section>
                  <p class="text-base text-primary">
                      Are you having any trouble? <nuxt-link to="/home/contact">
                      Contact Support
                    </nuxt-link> 
                  </p>
                  <div>
                    <span class="absolute top-1 right-1">
                      <svg width="40" height="40" viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <circle cx="1.39737" cy="38.6026" r="1.39737" transform="rotate(-90 1.39737 38.6026)" fill="#3056D3" />
                        <circle cx="1.39737" cy="1.99122" r="1.39737" transform="rotate(-90 1.39737 1.99122)" fill="#3056D3" />
                        <circle cx="13.6943" cy="38.6026" r="1.39737" transform="rotate(-90 13.6943 38.6026)" fill="#3056D3" />
                        <circle cx="13.6943" cy="1.99122" r="1.39737" transform="rotate(-90 13.6943 1.99122)" fill="#3056D3" />
                        <circle cx="25.9911" cy="38.6026" r="1.39737" transform="rotate(-90 25.9911 38.6026)" fill="#3056D3" />
                        <circle cx="25.9911" cy="1.99122" r="1.39737" transform="rotate(-90 25.9911 1.99122)" fill="#3056D3" />
                        <circle cx="38.288" cy="38.6026" r="1.39737" transform="rotate(-90 38.288 38.6026)" fill="#3056D3" />
                        <circle cx="38.288" cy="1.99122" r="1.39737" transform="rotate(-90 38.288 1.99122)" fill="#3056D3" />
                        <circle cx="1.39737" cy="26.3057" r="1.39737" transform="rotate(-90 1.39737 26.3057)" fill="#3056D3" />
                        <circle cx="13.6943" cy="26.3057" r="1.39737" transform="rotate(-90 13.6943 26.3057)" fill="#3056D3" />
                        <circle cx="25.9911" cy="26.3057" r="1.39737" transform="rotate(-90 25.9911 26.3057)" fill="#3056D3" />
                        <circle cx="38.288" cy="26.3057" r="1.39737" transform="rotate(-90 38.288 26.3057)" fill="#3056D3" />
                        <circle cx="1.39737" cy="14.0086" r="1.39737" transform="rotate(-90 1.39737 14.0086)" fill="#3056D3" />
                        <circle cx="13.6943" cy="14.0086" r="1.39737" transform="rotate(-90 13.6943 14.0086)" fill="#3056D3" />
                        <circle cx="25.9911" cy="14.0086" r="1.39737" transform="rotate(-90 25.9911 14.0086)" fill="#3056D3" />
                        <circle cx="38.288" cy="14.0086" r="1.39737" transform="rotate(-90 38.288 14.0086)" fill="#3056D3" />
                      </svg>
                    </span>
                    <span class="absolute left-1 bottom-1">
                      <svg width="29" height="40" viewBox="0 0 29 40" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <circle cx="2.288" cy="25.9912" r="1.39737" transform="rotate(-90 2.288 25.9912)" fill="#3056D3" />
                        <circle cx="14.5849" cy="25.9911" r="1.39737" transform="rotate(-90 14.5849 25.9911)" fill="#3056D3" />
                        <circle cx="26.7216" cy="25.9911" r="1.39737" transform="rotate(-90 26.7216 25.9911)" fill="#3056D3" />
                        <circle cx="2.288" cy="13.6944" r="1.39737" transform="rotate(-90 2.288 13.6944)" fill="#3056D3" />
                        <circle cx="14.5849" cy="13.6943" r="1.39737" transform="rotate(-90 14.5849 13.6943)" fill="#3056D3" />
                        <circle cx="26.7216" cy="13.6943" r="1.39737" transform="rotate(-90 26.7216 13.6943)" fill="#3056D3" />
                        <circle cx="2.288" cy="38.0087" r="1.39737" transform="rotate(-90 2.288 38.0087)" fill="#3056D3" />
                        <circle cx="2.288" cy="1.39739" r="1.39737" transform="rotate(-90 2.288 1.39739)" fill="#3056D3" />
                        <circle cx="14.5849" cy="38.0089" r="1.39737" transform="rotate(-90 14.5849 38.0089)" fill="#3056D3" />
                        <circle cx="26.7216" cy="38.0089" r="1.39737" transform="rotate(-90 26.7216 38.0089)" fill="#3056D3" />
                        <circle cx="14.5849" cy="1.39761" r="1.39737" transform="rotate(-90 14.5849 1.39761)" fill="#3056D3" />
                        <circle cx="26.7216" cy="1.39761" r="1.39737" transform="rotate(-90 26.7216 1.39761)" fill="#3056D3" />
                      </svg>
                    </span>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>
        <!-- Billing history -->
        <section aria-labelledby="billing-history-heading">
        <div class="bg-white pt-6 shadow sm:overflow-hidden sm:rounded-md">
            <div class="px-4 sm:px-6">
            <h2 id="billing-history-heading" class="text-lg font-medium leading-6 text-gray-900">Last Logins</h2>
            </div>
            <div class="mt-6 flex flex-col">
            <div class="-my-2 overflow-x-auto sm:-mx-6 lg:-mx-8">
                <div class="inline-block min-w-full py-2 align-middle sm:px-6 lg:px-8">
                <div class="overflow-hidden border-t border-gray-200">
                    <table class="min-w-full divide-y divide-gray-200">
                    <thead class="bg-gray-50">
                        <tr>
                        <th scope="col" class="px-6 py-3 text-left text-sm font-semibold text-gray-900">Date</th>
                        <th scope="col" class="px-6 py-3 text-left text-sm font-semibold text-gray-900">Description</th>
                        <th scope="col" class="px-6 py-3 text-left text-sm font-semibold text-gray-900">Amount</th>
                        <!--
                            `relative` is added here due to a weird bug in Safari that causes `sr-only` headings to introduce overflow on the body on mobile.
                        -->
                        <th scope="col" class="relative px-6 py-3 text-left text-sm font-medium text-gray-500">
                            <span class="sr-only">View receipt</span>
                        </th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-gray-200 bg-white">
                        <tr v-for="payment in payments" :key="payment.id">
                        <td class="whitespace-nowrap px-6 py-4 text-sm font-medium text-gray-900">
                            <time :datetime="payment.datetime">{{ payment.date }}</time>
                        </td>
                        <td class="whitespace-nowrap px-6 py-4 text-sm text-gray-500">{{ payment.description }}</td>
                        <td class="whitespace-nowrap px-6 py-4 text-sm text-gray-500">{{ payment.amount }}</td>
                        <td class="whitespace-nowrap px-6 py-4 text-right text-sm font-medium">
                            <a :href="payment.href" class="text-orange-600 hover:text-orange-900">View receipt</a>
                        </td>
                        </tr>
                    </tbody>
                    </table>
                </div>
                </div>
            </div>
            </div>
        </div>
        </section>
    </div>
</template>

<script setup>
    const Api = useApi()
    const password = ref({
      new: '',
      old: '',
      confirm: '',
      error: "",
      success: '',
    })

    function change(){
      password.value.error = ''
      if(!password.value.new || !password.value.old){
        password.value.error = "Please fill all fields"
        return
      }
      if( password.value.new != password.value.confirm ){
        password.value.error = "New passwords doesn't match"
        return
      }
      Api.post('/api/account/password', password.value)
      .then( res => {
        console.log(res)
        if(res.data){
          password.value.success = "Password changed successfully"
          password.value.new = ''
          password.value.old = ''
          password.value.confirm = ''
        }else{
          password.value.error = "Please check your old password."
        }
      })
    }

</script>

<style scoped>

</style>