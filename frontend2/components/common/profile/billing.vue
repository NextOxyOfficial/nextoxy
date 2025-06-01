<template>
    <div>
        <section class="bg-white ">
          <div class="pb-1">
            <p class="pb-1 font-semibold text-lg">Pending</p>
            <div class="flex flex-wrap justify-center">
              <div class="w-full ">
                <div class="rounded-10 shadow-card bg-white ">
                  <div class="max-w-full overflow-x-auto" v-if="unpaid.results && paid.results">
                    <p class="my-4" v-if="unpaid.results.length==0">No Pending Invoice, You're so good!</p>
                    <table class="w-full table-auto" v-if="unpaid.results.length > 0">
                      <thead>
                        <tr class="rounded bg-[#F3F6FF] text-left">
                          <th class="min-w-[220px] py-4 pr-4 pl-9 text-base font-medium uppercase text-black xl:pl-11">Invoice ID</th>
                          <th class="min-w-[150px] py-4 px-4 text-base font-medium uppercase text-black">Invoice date</th>
                          <th class="text-body-color min-w-[120px] py-4 px-4 text-base font-medium uppercase">Status</th>
                          <th class="text-body-color py-4 px-4 text-base font-medium uppercase">Actions</th>
                        </tr>
                      </thead>
                      <tbody v-if="unpaid.results">
                        <tr v-for="inv in unpaid.results">
                          <td class="flex gap-6 border-b border-[#eee] py-5 px-4 ">
                            <input type="checkbox" name="billcheck" id="billcheck" class="w-4" >
                            <div>
                                <h5 class="text-base font-medium text-black capitalize">{{ inv.note }}</h5>
                                <p class="text-body-color text-sm font-medium">${{ inv.amount }}</p>
                            </div>
                          </td>
                          <td class="border-b border-[#eee] py-5 px-4">
                            <p class="text-base text-black">{{ inv.created_at }}</p>
                          </td>
                          <td class="border-b border-[#eee] py-5 px-4">
                            <p class="text-success bg-success inline-flex rounded-full bg-opacity-10 py-1 px-3 text-sm font-medium">Unpaid</p>
                          </td>
                          <td class="border-b border-[#eee] py-5 px-4">
                            <div class="flex items-center space-x-4">
                              <button class="text-slate-800 bg-white">
                                <svg width="23" height="14" viewBox="0 0 23 14" class="fill-current">
                                  <path d="M11.4865 4.39979C10.0715 4.39979 8.94686 5.59701 8.94686 7.01871C8.94686 8.44041 10.1078 9.63763 11.4865 9.63763C12.8651 9.63763 14.0261 8.44041 14.0261 7.01871C14.0261 5.59701 12.9014 4.39979 11.4865 4.39979ZM11.4865 8.32817C10.7972 8.32817 10.2167 7.72956 10.2167 7.01871C10.2167 6.30786 10.7972 5.70925 11.4865 5.70925C12.1758 5.70925 12.7563 6.30786 12.7563 7.01871C12.7563 7.72956 12.1758 8.32817 11.4865 8.32817Z" />
                                  <path fill-rule="evenodd" clip-rule="evenodd" d="M8.59857 7.01871C8.59857 5.40199 9.87597 4.04062 11.4865 4.04062C13.097 4.04062 14.3744 5.40199 14.3744 7.01871C14.3744 8.63877 13.0575 9.99679 11.4865 9.99679C9.91547 9.99679 8.59857 8.63877 8.59857 7.01871ZM10.565 7.01871C10.565 7.5312 10.9895 7.969 11.4865 7.969C11.9834 7.969 12.408 7.5312 12.408 7.01871C12.408 6.50622 11.9834 6.06841 11.4865 6.06841C10.9895 6.06841 10.565 6.50622 10.565 7.01871ZM8.94686 7.01871C8.94686 5.59701 10.0715 4.39979 11.4865 4.39979C12.9014 4.39979 14.0261 5.59701 14.0261 7.01871C14.0261 8.44041 12.8651 9.63763 11.4865 9.63763C10.1078 9.63763 8.94686 8.44041 8.94686 7.01871ZM10.2167 7.01871C10.2167 7.72956 10.7972 8.32817 11.4865 8.32817C12.1758 8.32817 12.7563 7.72956 12.7563 7.01871C12.7563 6.30786 12.1758 5.70925 11.4865 5.70925C10.7972 5.70925 10.2167 6.30786 10.2167 7.01871Z" />
                                  <path d="M22.5157 6.56975C20.1212 2.67878 15.9852 0.359167 11.4865 0.359167C6.98773 0.359167 2.85179 2.67878 0.457293 6.56975C0.312172 6.83164 0.312172 7.16836 0.457293 7.43025C2.85179 11.3212 6.98773 13.6408 11.4865 13.6408C15.9852 13.6408 20.1212 11.3212 22.5157 7.43025C22.6971 7.16836 22.6971 6.83164 22.5157 6.56975ZM11.4865 12.3314C7.53193 12.3314 3.86763 10.3485 1.69082 6.98129C3.86763 3.65152 7.53193 1.66863 11.4865 1.66863C15.441 1.66863 19.1053 3.65152 21.2821 6.98129C19.1053 10.3485 15.441 12.3314 11.4865 12.3314Z" />
                                  <path fill-rule="evenodd" clip-rule="evenodd" d="M0.457293 7.43025C0.312172 7.16836 0.312172 6.83164 0.457293 6.56975C2.85179 2.67878 6.98773 0.359167 11.4865 0.359167C15.9852 0.359167 20.1212 2.67878 22.5157 6.56975C22.6971 6.83164 22.6971 7.16836 22.5157 7.43025C20.1212 11.3212 15.9852 13.6408 11.4865 13.6408C6.98773 13.6408 2.85179 11.3212 0.457293 7.43025ZM22.805 7.6303C20.345 11.622 16.0998 14 11.4865 14C6.87025 14 2.62254 11.619 0.163222 7.6227L0.154568 7.60864C-0.0517391 7.23633 -0.0514142 6.76386 0.154893 6.39155L0.162906 6.37709C2.62222 2.38078 6.87025 0 11.4865 0C16.0998 0 20.345 2.37797 22.805 6.3697C23.065 6.7524 23.065 7.2476 22.805 7.6303ZM2.11309 6.98243C4.23806 10.1255 7.72479 11.9722 11.4865 11.9722C15.2482 11.9722 18.7349 10.1255 20.8599 6.98243C18.7348 3.87429 15.2479 2.02779 11.4865 2.02779C7.72501 2.02779 4.23816 3.87429 2.11309 6.98243ZM1.69082 6.98129C3.86763 3.65152 7.53193 1.66863 11.4865 1.66863C15.441 1.66863 19.1053 3.65152 21.2821 6.98129C19.1053 10.3485 15.441 12.3314 11.4865 12.3314C7.53193 12.3314 3.86763 10.3485 1.69082 6.98129Z" />
                                </svg>
                              </button>
                              <button class="text-slate-800 bg-white">
                                <svg width="14" height="14" viewBox="0 0 14 14" class="fill-current">
                                  <path d="M13.2998 10.0463C13.0836 10.0463 12.9106 10.2191 12.9106 10.4352V12.8981H1.12454V10.4136C1.12454 10.1975 0.951533 10.0247 0.735276 10.0247C0.519018 10.0247 0.346013 10.1975 0.346013 10.4136V13.0926C0.346013 13.3951 0.648773 13.6543 1.01641 13.6543H12.9754C13.3431 13.6543 13.6458 13.4167 13.6458 13.0926V10.4136C13.6891 10.2191 13.5161 10.0463 13.2998 10.0463Z" />
                                  <path fill-rule="evenodd" clip-rule="evenodd" d="M12.5645 10.4352C12.5645 10.0282 12.8925 9.70062 13.2998 9.70062C13.6582 9.70062 14.0627 9.99745 13.9918 10.4453V13.0926C13.9918 13.6678 13.4677 14 12.9754 14H1.01641C0.514814 14 0 13.6384 0 13.0926V10.4136C0 10.0066 0.327921 9.67901 0.735274 9.67901C1.14263 9.67901 1.47055 10.0066 1.47055 10.4136V12.5525H12.5645V10.4352ZM13.6458 10.4136C13.6891 10.2191 13.5161 10.0463 13.2998 10.0463C13.0836 10.0463 12.9106 10.2191 12.9106 10.4352V12.8981H1.12454V10.4136C1.12454 10.1975 0.951533 10.0247 0.735276 10.0247C0.519018 10.0247 0.346013 10.1975 0.346013 10.4136V13.0926C0.346013 13.3951 0.648773 13.6543 1.01641 13.6543H12.9754C13.3431 13.6543 13.6458 13.4167 13.6458 13.0926V10.4136Z" />
                                  <path d="M6.35796 9.41975C6.55259 9.59259 6.79048 9.70062 7.02836 9.70062C7.26624 9.70062 7.50413 9.6142 7.67713 9.44136L9.34231 7.84259C9.49369 7.69136 9.49369 7.4537 9.34231 7.30247C9.19093 7.15124 8.95305 7.15124 8.80167 7.30247L7.396 8.66358V0.734568C7.396 0.518519 7.22299 0.345679 7.00673 0.345679C6.79048 0.345679 6.61747 0.518519 6.61747 0.734568V8.64198L5.2118 7.25926C5.06042 7.10803 4.82254 7.10803 4.67116 7.25926C4.51978 7.41049 4.51978 7.64815 4.67116 7.79938L6.35796 9.41975Z" />
                                  <path fill-rule="evenodd" clip-rule="evenodd" d="M6.12302 9.67362L4.42644 8.04386C4.13994 7.75763 4.13998 7.30106 4.42649 7.01483C4.71264 6.72896 5.16881 6.7286 5.45539 7.01375C5.45575 7.01411 5.45611 7.01447 5.45647 7.01483L6.27146 7.8165V0.734568C6.27146 0.327605 6.59938 0 7.00673 0C7.41409 0 7.74201 0.327605 7.74201 0.734568V7.84714L8.5592 7.05585C8.84584 6.77181 9.3012 6.77254 9.58698 7.05804C9.87348 7.34427 9.87348 7.80079 9.58698 8.08702L9.58212 8.09188L7.91915 9.68842C7.67443 9.93138 7.34631 10.0463 7.02836 10.0463C6.68634 10.0463 6.36988 9.89284 6.12808 9.67812L6.12302 9.67362ZM7.67713 9.44136L9.34231 7.84259C9.49369 7.69136 9.49369 7.4537 9.34231 7.30247C9.19093 7.15124 8.95305 7.15124 8.80167 7.30247L7.396 8.66358V0.734568C7.396 0.518519 7.22299 0.345679 7.00673 0.345679C6.79048 0.345679 6.61747 0.518519 6.61747 0.734568V8.64198L5.2118 7.25926C5.06042 7.10803 4.82254 7.10803 4.67116 7.25926C4.51978 7.41049 4.51978 7.64815 4.67116 7.79938L6.35796 9.41975C6.55259 9.59259 6.79048 9.70062 7.02836 9.70062C7.26624 9.70062 7.50413 9.6142 7.67713 9.44136Z" />
                                </svg>
                              </button>
                                <nuxt-link :to="'/account/stripe/' + inv.id" class="inline-flex items-center justify-center rounded-full bg-black py-2 px-3 text-center text-xs font-medium text-white hover:bg-opacity-90">
                                    <span class="mr-[4px]">
                                      <svg width="16" height="16" viewBox="0 0 20 20" class="fill-current">
                                        <g clip-path="url(#clip0_3182_775)">
                                          <path d="M18.875 11.4375C18.3125 10.8438 17.5625 10.5312 16.75 10.5312C16.125 10.5312 15.5625 10.7188 15.0625 11.0938C15 11.125 14.9688 11.1562 14.9062 11.2188C14.8438 11.1875 14.8125 11.125 14.75 11.0938C14.25 10.7188 13.6875 10.5312 13.0625 10.5312C12.9062 10.5312 12.7812 10.5312 12.6562 10.5625C11.7188 9.5 10.5625 8.75 9.3125 8.40625C10.625 7.75 11.5312 6.40625 11.5312 4.875C11.5312 2.6875 9.75 0.9375 7.59375 0.9375C5.40625 0.9375 3.65625 2.71875 3.65625 4.875C3.65625 6.4375 4.5625 7.78125 5.875 8.40625C4.5625 8.78125 3.40625 9.53125 2.4375 10.6562C1.125 12.2188 0.375 14.4062 0.3125 16.7812C0.3125 17.0312 0.4375 17.25 0.65625 17.3438C1.5 17.75 4.4375 19.0938 7.59375 19.0938C9.28125 19.0938 10.8438 18.8125 10.9062 18.8125C11.25 18.75 11.4688 18.4375 11.4062 18.0938C11.3438 17.75 11.0312 17.5312 10.6875 17.5938C10.6875 17.5938 9.15625 17.875 7.59375 17.875C5.0625 17.8438 2.65625 16.875 1.5625 16.375C1.65625 14.4375 2.3125 12.7187 3.375 11.4375C4.46875 10.125 5.96875 9.40625 7.59375 9.40625C9.03125 9.40625 10.375 10 11.4375 11.0312C11.2812 11.1562 11.125 11.2812 11 11.4062C10.4688 11.9688 10.1875 12.75 10.1875 13.5938C10.1875 14.4375 10.5 15.2188 11.1562 16C11.6875 16.6562 12.4375 17.2812 13.2812 18L13.3125 18.0312C13.5937 18.25 13.9062 18.5312 14.2188 18.8125C14.4062 19 14.6875 19.0938 14.9375 19.0938C15.1875 19.0938 15.4687 19 15.6562 18.8125C16 18.5312 16.3125 18.25 16.5938 18C17.4375 17.2812 18.1875 16.6562 18.7188 16C19.375 15.2188 19.6875 14.4375 19.6875 13.5938C19.6875 12.7812 19.4062 12.0312 18.875 11.4375ZM4.875 4.875C4.875 3.375 6.09375 2.1875 7.5625 2.1875C9.0625 2.1875 10.25 3.40625 10.25 4.875C10.25 6.375 9.03125 7.5625 7.5625 7.5625C6.09375 7.5625 4.875 6.34375 4.875 4.875ZM17.75 15.2188C17.2812 15.7812 16.5938 16.375 15.7812 17.0625C15.5312 17.2812 15.2188 17.5312 14.9062 17.7812C14.625 17.5312 14.3438 17.2812 14.0938 17.0938L14.0625 17.0625C13.25 16.375 12.5625 15.7812 12.0938 15.2188C11.625 14.6562 11.4062 14.1562 11.4062 13.625C11.4062 13.0937 11.5938 12.625 11.9062 12.2812C12.2188 11.9375 12.6563 11.75 13.0938 11.75C13.4375 11.75 13.75 11.8438 14 12.0625C14.125 12.1562 14.2188 12.25 14.3125 12.375C14.5938 12.7188 15.1875 12.7188 15.5 12.375C15.5938 12.25 15.7187 12.1562 15.8125 12.0625C16.0937 11.8438 16.4062 11.75 16.7188 11.75C17.1875 11.75 17.5938 11.9375 17.9062 12.2812C18.2188 12.625 18.4062 13.0937 18.4062 13.625C18.4375 14.1875 18.2188 14.6562 17.75 15.2188Z"></path>
                                        </g>
                                        <defs>
                                          <clipPath id="clip0_3182_775">
                                            <rect width="20" height="20"></rect>
                                          </clipPath>
                                        </defs>
                                      </svg>
                                    </span>
                                    Pay
                                </nuxt-link>
                            </div>
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
        <!-- ====== Checkout Section Start -->
        <div class="my-10 overflow-hidden rounded-lg border border-[#e7e7e7] bg-[#f4f7ff] py-10 px-6 sm:px-10 hidden">
            
            <h4 class="mb-6 text-lg font-semibold text-black">Your Saved Cards</h4>
            <div class="mx-1 flex flex-wrap">
              <div class="w-1/3 px-3">
                <div class="cursor-pointer hover:shadow-xl rounded-xl">
                  <img src="https://cdn.tailgrids.com/1.0/assets/images/ecommerce/checkout/checkout-04/card-01.svg" alt="card" class="w-full" />
                </div>
              </div>
              <div class="w-1/3 px-3">
                <div class="cursor-pointer hover:shadow-xl rounded-xl">
                  <img src="https://cdn.tailgrids.com/1.0/assets/images/ecommerce/checkout/checkout-04/card-02.svg" alt="card" class="w-full" />
                </div>
              </div>
              <div class="w-1/3 px-3">
                <div class="cursor-pointer hover:shadow-xl rounded-xl">
                    <img src="https://cdn.tailgrids.com/1.0/assets/images/ecommerce/checkout/checkout-04/card-02.svg" alt="card" class="w-full" />
                </div>
              </div>
            </div>
            <h4 class="my-8 text-lg font-semibold text-black sm:text-2xl lg:text-xl xl:text-2xl">Personal Details</h4>
            <form class="mb-10 border-b border-[#e7e7e7] pb-5">
              <div class=" flex flex-wrap">
                <div class="w-full px-3 md:w-1/2">
                  <div class="mb-5">
                    <label for="" class="text-body-color mb-[10px] block text-base font-medium"> Full Name </label>
                    <input type="text" placeholder="Mark Litho" class="mt-1 block w-full rounded-md border border-gray-300 py-2 px-3 shadow-sm focus:border-gray-900 focus:outline-none focus:ring-gray-900 sm:text-SM" />
                  </div>
                </div>
                <div class="w-full px-3 md:w-1/2">
                  <div class="mb-5">
                    <label for="" class="text-body-color mb-[10px] block text-base font-medium"> Phone Number </label>
                    <input type="text" placeholder="883-992-145" class="mt-1 block w-full rounded-md border border-gray-300 py-2 px-3 shadow-sm focus:border-gray-900 focus:outline-none focus:ring-gray-900 sm:text-SM" />
                  </div>
                </div>
                <div class="w-full px-3 md:w-1/2">
                  <div class="mb-5">
                    <label for="" class="text-body-color mb-[10px] block text-base font-medium"> Email </label>
                    <input type="email" placeholder="yourmail@gmail.com" class="mt-1 block w-full rounded-md border border-gray-300 py-2 px-3 shadow-sm focus:border-gray-900 focus:outline-none focus:ring-gray-900 sm:text-SM" />
                  </div>
                </div>
                <div class="w-full px-3 md:w-1/2">
                  <div class="mb-5">
                    <label for="" class="text-body-color mb-[10px] block text-base font-medium"> Address </label>
                    <input type="text" placeholder="2707 Davis Anenue" class="mt-1 block w-full rounded-md border border-gray-300 py-2 px-3 shadow-sm focus:border-gray-900 focus:outline-none focus:ring-gray-900 sm:text-SM" />
                  </div>
                </div>
                <div class="w-full px-3 md:w-1/3">
                  <div class="mb-5">
                    <label for="" class="text-body-color mb-[10px] block text-base font-medium"> Country </label>
                    <input type="text" placeholder="2707 Davis Anenue" class="mt-1 block w-full rounded-md border border-gray-300 py-2 px-3 shadow-sm focus:border-gray-900 focus:outline-none focus:ring-gray-900 sm:text-SM" />
                  </div>
                </div>
                <div class="w-full px-3 md:w-1/3">
                  <div class="mb-5">
                    <label for="" class="text-body-color mb-[10px] block text-base font-medium"> City </label>
                    <input type="text" placeholder="New York" class="mt-1 block w-full rounded-md border border-gray-300 py-2 px-3 shadow-sm focus:border-gray-900 focus:outline-none focus:ring-gray-900 sm:text-SM" />
                  </div>
                </div>
                <div class="w-full px-3 md:w-1/3">
                  <div class="mb-5">
                    <label for="" class="text-body-color mb-[10px] block text-base font-medium"> Post Code </label>
                    <input type="text" placeholder="94612" class="mt-1 block w-full rounded-md border border-gray-300 py-2 px-3 shadow-sm focus:border-gray-900 focus:outline-none focus:ring-gray-900 sm:text-SM" />
                  </div>
                </div>
              </div>
            </form>
            <h4 class="my-8 text-lg font-semibold text-black sm:text-2xl lg:text-xl xl:text-2xl">Payment Details</h4>
            <div class="mx-1 mb-9 flex">
              <div class="px-3">
                <input type="radio" name="paymentDetails" id="paymentDetails1" class="payment sr-only" />
                <label for="paymentDetails1" class="shadow-input flex h-11 cursor-pointer items-center overflow-hidden rounded-md border border-transparent bg-white py-3 px-6 text-base font-semibold text-black"> Card </label>
              </div>
              <div class="px-3">
                <input type="radio" name="paymentDetails" id="paymentDetails2" class="payment sr-only" />
                <label for="paymentDetails2" class="shadow-input flex h-11 cursor-pointer items-center overflow-hidden rounded-md border border-transparent bg-white py-3 px-6 text-base font-semibold text-black">
                  <svg width="67" height="16" viewBox="0 0 67 16" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <g clip-path="url(#clip0_1759_423)">
                      <path fill-rule="evenodd" clip-rule="evenodd" d="M5.76278 3.76562H10.2756C12.6986 3.76562 13.6108 4.99227 13.4698 6.79438C13.2368 9.76956 11.4382 11.4156 9.05248 11.4156H7.84797C7.52063 11.4156 7.30046 11.6322 7.21193 12.2194L6.70054 15.6325C6.66675 15.8539 6.55026 15.982 6.37553 15.9995H3.54014C3.27338 15.9995 3.17902 15.7956 3.24891 15.3541L4.97764 4.41215C5.0452 3.97415 5.28517 3.76562 5.76278 3.76562Z" fill="#009EE3" />
                      <path fill-rule="evenodd" clip-rule="evenodd" d="M25.3554 3.5625C26.8779 3.5625 28.2828 4.38842 28.0906 6.44681C27.8576 8.89312 26.5471 10.2467 24.4794 10.2526H22.6726C22.4128 10.2526 22.287 10.4646 22.2195 10.8991L21.87 13.1206C21.8176 13.4561 21.6452 13.6215 21.3912 13.6215H19.7103C19.4423 13.6215 19.3491 13.4502 19.4085 13.067L20.796 4.16359C20.8647 3.72559 21.0289 3.5625 21.3283 3.5625H25.3519H25.3554ZM22.6179 8.3293H23.9866C24.8428 8.29668 25.4113 7.70374 25.4684 6.63436C25.5033 5.97386 25.0572 5.5009 24.3478 5.5044L23.0594 5.51023L22.6179 8.3293ZM32.6605 12.94C32.8143 12.8002 32.9704 12.728 32.9483 12.9004L32.8935 13.3128C32.8656 13.5283 32.9506 13.6424 33.151 13.6424H34.6444C34.896 13.6424 35.0183 13.5411 35.0801 13.152L36.0003 7.37641C36.0469 7.08634 35.9759 6.94423 35.7557 6.94423H34.1132C33.9652 6.94423 33.893 7.02693 33.8546 7.25293L33.794 7.60822C33.7625 7.79344 33.6775 7.82606 33.5983 7.63968C33.3199 6.98034 32.6093 6.68445 31.6179 6.70775C29.3149 6.75551 27.7621 8.50404 27.5955 10.7453C27.4674 12.4787 28.7092 13.8405 30.347 13.8405C31.5352 13.8405 32.0664 13.491 32.6652 12.9435L32.6605 12.94ZM31.4094 12.0512C30.4181 12.0512 29.7273 11.2602 29.8706 10.291C30.0139 9.3218 30.9411 8.53083 31.9325 8.53083C32.9238 8.53083 33.6146 9.3218 33.4713 10.291C33.328 11.2602 32.4019 12.0512 31.4094 12.0512ZM38.9231 6.92559H37.4087C37.0965 6.92559 36.9695 7.15857 37.0686 7.44513L38.9487 12.9505L37.1047 15.5704C36.9497 15.7894 37.0697 15.9886 37.2876 15.9886H38.9895C39.0887 16 39.1891 15.9827 39.2787 15.9387C39.3683 15.8948 39.4434 15.8259 39.4951 15.7404L45.2777 7.4463C45.4559 7.19119 45.372 6.92326 45.0796 6.92326H43.4686C43.1925 6.92326 43.0818 7.03276 42.9234 7.26225L40.512 10.757L39.4345 7.25409C39.3716 7.04208 39.2143 6.92559 38.9243 6.92559H38.9231Z" fill="#113984" />
                      <path fill-rule="evenodd" clip-rule="evenodd" d="M51.2932 3.56288C52.8157 3.56288 54.2206 4.3888 54.0284 6.44719C53.7954 8.8935 52.4849 10.2471 50.4172 10.2529H48.6116C48.3518 10.2529 48.226 10.465 48.1584 10.8995L47.809 13.1209C47.7565 13.4564 47.5841 13.6219 47.3302 13.6219H45.6492C45.3813 13.6219 45.2881 13.4506 45.3475 13.0674L46.7372 4.16164C46.806 3.72363 46.9702 3.56055 47.2696 3.56055H51.2932V3.56288ZM48.5557 8.32968H49.9244C50.7806 8.29706 51.3491 7.70412 51.4062 6.63474C51.4411 5.97424 50.995 5.50128 50.2856 5.50478L48.9972 5.5106L48.5557 8.32968ZM58.5983 12.9404C58.7521 12.8006 58.9082 12.7284 58.8861 12.9008L58.8313 13.3131C58.8034 13.5287 58.8884 13.6428 59.0888 13.6428H60.5822C60.8338 13.6428 60.9561 13.5415 61.0179 13.1524L61.9381 7.37678C61.9847 7.08672 61.9137 6.9446 61.6935 6.9446H60.0533C59.9054 6.9446 59.8332 7.02731 59.7947 7.2533L59.7341 7.6086C59.7027 7.79382 59.6176 7.82644 59.5384 7.64005C59.26 6.98072 58.5494 6.68483 57.5581 6.70813C55.2551 6.75589 53.7022 8.50442 53.5357 10.7457C53.4075 12.4791 54.6493 13.8409 56.2872 13.8409C57.4754 13.8409 58.0066 13.4914 58.6053 12.9439L58.5983 12.9404ZM57.3484 12.0516C56.3571 12.0516 55.6663 11.2606 55.8096 10.2914C55.9528 9.32218 56.8801 8.53121 57.8714 8.53121C58.8628 8.53121 59.5536 9.32218 59.4103 10.2914C59.267 11.2606 58.3397 12.0516 57.3484 12.0516ZM64.2365 13.6521H62.5124C62.4825 13.6535 62.4525 13.6482 62.4248 13.6366C62.3971 13.6251 62.3723 13.6075 62.3522 13.5853C62.332 13.563 62.3171 13.5366 62.3083 13.5079C62.2996 13.4792 62.2973 13.4489 62.3016 13.4192L63.816 3.82498C63.8304 3.7595 63.8666 3.70085 63.9186 3.65854C63.9707 3.61624 64.0355 3.59279 64.1025 3.592H65.8266C65.8566 3.59066 65.8865 3.59596 65.9142 3.60752C65.9419 3.61907 65.9667 3.63661 65.9869 3.65886C66.007 3.68112 66.022 3.70755 66.0307 3.73627C66.0395 3.76498 66.0418 3.79528 66.0375 3.82498L64.5231 13.4192C64.5091 13.4851 64.4731 13.5443 64.421 13.587C64.3689 13.6298 64.3039 13.6536 64.2365 13.6545V13.6521Z" fill="#009EE3" />
                      <path fill-rule="evenodd" clip-rule="evenodd" d="M2.94052 0H7.45802C8.7301 0 10.2398 0.0407717 11.2486 0.931926C11.9231 1.52719 12.2772 2.47426 12.1957 3.49472C11.9184 6.94401 9.8554 8.87659 7.08758 8.87659H4.86028C4.48052 8.87659 4.23007 9.12821 4.12289 9.80851L3.50083 13.7692C3.46006 14.0255 3.3494 14.1769 3.15136 14.1956H0.363743C0.0550431 14.1956 -0.0544591 13.9626 0.0259194 13.4477L2.02956 0.752529C2.10994 0.2423 2.39068 0 2.94052 0Z" fill="#113984" />
                      <path fill-rule="evenodd" clip-rule="evenodd" d="M4.18787 9.40727L4.97651 4.41332C5.04524 3.97531 5.28521 3.76562 5.76282 3.76562H10.2757C11.0224 3.76562 11.627 3.88212 12.0999 4.09762C11.6468 7.16832 9.6606 8.87374 7.06053 8.87374H4.83672C4.5385 8.87491 4.3195 9.02402 4.18787 9.40727Z" fill="#172C70" />
                    </g>
                    <defs>
                      <clipPath id="clip0_1759_423">
                        <rect width="66.0421" height="16" fill="white" />
                      </clipPath>
                    </defs>
                  </svg>
                </label>
              </div>
            </div>
            <div class="mx-1 flex flex-wrap">
                <div class="flex w-full">
                    <div class="flex-1 px-3">
                      <div class="mb-6">
                        <label for="" class="text-body-color mb-[10px] block text-base font-medium"> Cardholder Name </label>
                        <input type="text" placeholder="Cardholder Name" class="mt-1 block w-full rounded-md border border-gray-300 py-2 px-3 shadow-sm focus:border-gray-900 focus:outline-none focus:ring-gray-900 sm:text-SM" />
                      </div>
                    </div>
                    <div class="flex-1 px-3">
                      <div class="mb-6">
                        <label for="" class="text-body-color mb-[10px] block text-base font-medium"> Card Number </label>
                        <div class="relative">
                          <input type="text" placeholder="0000 0000 0000 0000" class="mt-1 block w-full rounded-md border border-gray-300 py-2 px-3 shadow-sm focus:border-gray-900 focus:outline-none focus:ring-gray-900 sm:text-SM" />
                          <span class="absolute right-5 top-1/2 -translate-y-1/2">
                            <svg width="60" height="10" viewBox="0 0 60 10" fill="none" xmlns="http://www.w3.org/2000/svg">
                              <path d="M53.617 1.03516H49.1125V8.96614H53.617V1.03516Z" fill="#F26122" />
                              <path d="M49.6008 4.99991C49.5922 3.4701 50.3068 2.02137 51.5378 1.06982C49.4309 -0.542193 46.4047 -0.308103 44.5861 1.60748C42.7675 3.52315 42.7675 6.47691 44.5861 8.39258C46.4047 10.308 49.4309 10.5423 51.5378 8.93006C50.3068 7.97869 49.5922 6.52997 49.6008 4.99991Z" fill="#EA1D25" />
                              <path d="M59.8542 4.99987C59.8524 6.91413 58.7293 8.65997 56.9598 9.49664C55.1909 10.3333 53.0859 10.1145 51.5378 8.93291C53.7674 7.22479 54.1531 4.08261 52.4008 1.91136C52.1493 1.5969 51.8598 1.31348 51.5378 1.06725C53.0859 -0.114461 55.1909 -0.333395 56.9598 0.503353C58.7293 1.34011 59.8524 3.08592 59.8542 4.99987Z" fill="#F69E1E" />
                              <path fill-rule="evenodd" clip-rule="evenodd" d="M22.3133 6.76452C22.3197 5.16311 20.9958 4.4717 19.968 3.93446C19.3175 3.59473 18.7857 3.31687 18.7857 2.90986C18.7857 2.56295 19.1224 2.19564 19.839 2.1008C20.6909 2.01676 21.5504 2.1656 22.3235 2.53176L22.7663 0.430964C22.0122 0.14886 21.2131 0.00300476 20.4076 0C17.9224 0 16.1952 1.3235 16.1952 3.21421C16.1952 4.61152 17.4485 5.38882 18.3963 5.85096C19.3441 6.31317 19.7126 6.63849 19.7018 7.05865C19.7018 7.70991 18.923 8.00397 18.1962 8.01477C17.2999 8.0262 16.4156 7.80952 15.6266 7.38453L15.1737 9.48532C16.0662 9.83287 17.0172 10.0076 17.9752 9.99975C20.6178 9.99975 22.3559 8.69722 22.3661 6.68048L22.3133 6.76452ZM15.4793 0.168667L13.3734 9.88451H10.8463L12.9522 0.168667H15.4793ZM26.0728 6.4704L27.3992 2.82588L28.1685 6.4704H26.0728ZM31.2221 9.91628H28.8844L28.5788 8.46675H25.4096L24.8931 9.91628H22.2396L26.02 0.914144C26.1941 0.485583 26.6089 0.204076 27.0733 0.199877H29.1792L31.2221 9.91628ZM7.84476 9.85269L11.9307 0.136853H9.19278L6.57107 6.7435L5.51783 1.12422C5.42444 0.552805 4.92895 0.134452 4.34896 0.136853H0.0635294L0 0.420157C0.8595 0.58822 1.69485 0.863127 2.48511 1.23946C2.82179 1.39732 3.04985 1.72085 3.08543 2.09057L5.09666 9.85269H7.84476Z" fill="#212B36" />
                            </svg>
                          </span>
                        </div>
                      </div>
                    </div>
                </div>
              <div class="w-full px-3 md:w-1/3">
                <div class="mb-6">
                  <label for="" class="text-body-color mb-[10px] block text-base font-medium"> Expiration </label>
                  <input type="text" placeholder="MM" class="mt-1 block w-full rounded-md border border-gray-300 py-2 px-3 shadow-sm focus:border-gray-900 focus:outline-none focus:ring-gray-900 sm:text-SM" />
                </div>
              </div>
              <div class="w-full self-end px-3 md:w-1/3">
                <div class="mb-6">
                  <input type="text" placeholder="YYYY" class="mt-1 block w-full rounded-md border border-gray-300 py-2 px-3 shadow-sm focus:border-gray-900 focus:outline-none focus:ring-gray-900 sm:text-SM" />
                </div>
              </div>
              <div class="w-full px-3 md:w-1/3">
                <div class="mb-6">
                  <label for="" class="text-body-color mb-[10px] block text-base font-medium"> CVC/CVV </label>
                  <input type="text" placeholder="CVC/CVV" class="mt-1 block w-full rounded-md border border-gray-300 py-2 px-3 shadow-sm focus:border-gray-900 focus:outline-none focus:ring-gray-900 sm:text-SM" />
                </div>
              </div>
              
              <div class="w-full px-3">
                <div class="flex items-center gap-2 my-3">
                    <input type="checkbox" class="form-checkbox h-4 w-4 text-primary border-form-stroke rounded focus:border-primary focus:ring-0" />
                    <label for="" class="text-body-color text-base font-medium">Save & link this card for automatic future payments</label>
                </div>
                <div class="mb-8">
                  <p class="text-body-color text-base font-medium">By clicking “Confirm Payment” I agree to the company's Terms of Service</p>
                </div>
                <div class="mb-8">
                  <p class="text-body-color text-base font-medium">Total: $12.99</p>
                </div>
              </div>
              <div class="w-full px-3">
                <div>
                  <button class="bg-primary inline-flex items-center justify-center rounded-md py-3 px-6 text-center text-sm font-semibold text-white hover:bg-opacity-90">Confirm Payment</button>
                </div>
              </div>
            </div>
          </div>
        <!-- ====== Checkout Section End -->
        <section class="bg-white ">
          <div class="mt-5">
            <p class="pb-1 font-semibold text-lg border-b mb-2">Settled</p>

            <div class="flex flex-wrap justify-center">
              <div class="w-full ">
                <div class="rounded-10 shadow-card bg-white ">
                  <div class="max-w-full overflow-x-auto">
                    <table class="w-full table-auto">
                      <thead>
                        <tr class="rounded bg-[#F3F6FF] text-left">
                          <th class="min-w-[220px] py-4 pr-4 pl-9 text-base font-medium uppercase text-black xl:pl-11">Invoice ID</th>
                          <th class="min-w-[150px] py-4 px-4 text-base font-medium uppercase text-black">Invoice date</th>
                          <th class="text-body-color min-w-[120px] py-4 px-4 text-base font-medium uppercase">Status</th>
                          <th class="text-body-color py-4 px-4 text-base font-medium uppercase">Actions</th>
                        </tr>
                      </thead>
                      <tbody v-if="paid.results">
                        <tr v-for="inv in paid.results">
                          <td class="flex gap-6 border-b border-[#eee] py-5 px-4 ">
                            <input type="checkbox" name="billcheck" id="billcheck">
                            <div>
                                <h5 class="text-base font-medium text-black capitalize">{{ inv.note }}</h5>
                                <p class="text-body-color text-sm font-medium">${{ inv.amount }}</p>
                            </div>
                          </td>
                          <td class="border-b border-[#eee] py-5 px-4">
                            <p class="text-base text-black">{{ inv.created_at }}</p>
                          </td>
                          <td class="border-b border-[#eee] py-5 px-4">
                            <p class="text-success bg-success inline-flex rounded-full bg-opacity-10 py-1 px-3 text-sm font-medium">Paid</p>
                          </td>
                          <td class="border-b border-[#eee] py-5 px-4">
                            <div class="flex items-center space-x-4">
                              <a class="text-slate-800 bg-white">
                                <svg width="23" height="14" viewBox="0 0 23 14" class="fill-current">
                                  <path d="M11.4865 4.39979C10.0715 4.39979 8.94686 5.59701 8.94686 7.01871C8.94686 8.44041 10.1078 9.63763 11.4865 9.63763C12.8651 9.63763 14.0261 8.44041 14.0261 7.01871C14.0261 5.59701 12.9014 4.39979 11.4865 4.39979ZM11.4865 8.32817C10.7972 8.32817 10.2167 7.72956 10.2167 7.01871C10.2167 6.30786 10.7972 5.70925 11.4865 5.70925C12.1758 5.70925 12.7563 6.30786 12.7563 7.01871C12.7563 7.72956 12.1758 8.32817 11.4865 8.32817Z" />
                                  <path fill-rule="evenodd" clip-rule="evenodd" d="M8.59857 7.01871C8.59857 5.40199 9.87597 4.04062 11.4865 4.04062C13.097 4.04062 14.3744 5.40199 14.3744 7.01871C14.3744 8.63877 13.0575 9.99679 11.4865 9.99679C9.91547 9.99679 8.59857 8.63877 8.59857 7.01871ZM10.565 7.01871C10.565 7.5312 10.9895 7.969 11.4865 7.969C11.9834 7.969 12.408 7.5312 12.408 7.01871C12.408 6.50622 11.9834 6.06841 11.4865 6.06841C10.9895 6.06841 10.565 6.50622 10.565 7.01871ZM8.94686 7.01871C8.94686 5.59701 10.0715 4.39979 11.4865 4.39979C12.9014 4.39979 14.0261 5.59701 14.0261 7.01871C14.0261 8.44041 12.8651 9.63763 11.4865 9.63763C10.1078 9.63763 8.94686 8.44041 8.94686 7.01871ZM10.2167 7.01871C10.2167 7.72956 10.7972 8.32817 11.4865 8.32817C12.1758 8.32817 12.7563 7.72956 12.7563 7.01871C12.7563 6.30786 12.1758 5.70925 11.4865 5.70925C10.7972 5.70925 10.2167 6.30786 10.2167 7.01871Z" />
                                  <path d="M22.5157 6.56975C20.1212 2.67878 15.9852 0.359167 11.4865 0.359167C6.98773 0.359167 2.85179 2.67878 0.457293 6.56975C0.312172 6.83164 0.312172 7.16836 0.457293 7.43025C2.85179 11.3212 6.98773 13.6408 11.4865 13.6408C15.9852 13.6408 20.1212 11.3212 22.5157 7.43025C22.6971 7.16836 22.6971 6.83164 22.5157 6.56975ZM11.4865 12.3314C7.53193 12.3314 3.86763 10.3485 1.69082 6.98129C3.86763 3.65152 7.53193 1.66863 11.4865 1.66863C15.441 1.66863 19.1053 3.65152 21.2821 6.98129C19.1053 10.3485 15.441 12.3314 11.4865 12.3314Z" />
                                  <path fill-rule="evenodd" clip-rule="evenodd" d="M0.457293 7.43025C0.312172 7.16836 0.312172 6.83164 0.457293 6.56975C2.85179 2.67878 6.98773 0.359167 11.4865 0.359167C15.9852 0.359167 20.1212 2.67878 22.5157 6.56975C22.6971 6.83164 22.6971 7.16836 22.5157 7.43025C20.1212 11.3212 15.9852 13.6408 11.4865 13.6408C6.98773 13.6408 2.85179 11.3212 0.457293 7.43025ZM22.805 7.6303C20.345 11.622 16.0998 14 11.4865 14C6.87025 14 2.62254 11.619 0.163222 7.6227L0.154568 7.60864C-0.0517391 7.23633 -0.0514142 6.76386 0.154893 6.39155L0.162906 6.37709C2.62222 2.38078 6.87025 0 11.4865 0C16.0998 0 20.345 2.37797 22.805 6.3697C23.065 6.7524 23.065 7.2476 22.805 7.6303ZM2.11309 6.98243C4.23806 10.1255 7.72479 11.9722 11.4865 11.9722C15.2482 11.9722 18.7349 10.1255 20.8599 6.98243C18.7348 3.87429 15.2479 2.02779 11.4865 2.02779C7.72501 2.02779 4.23816 3.87429 2.11309 6.98243ZM1.69082 6.98129C3.86763 3.65152 7.53193 1.66863 11.4865 1.66863C15.441 1.66863 19.1053 3.65152 21.2821 6.98129C19.1053 10.3485 15.441 12.3314 11.4865 12.3314C7.53193 12.3314 3.86763 10.3485 1.69082 6.98129Z" />
                                </svg>
                              </a>
                              <a class="text-slate-800 bg-white">
                                <svg width="14" height="14" viewBox="0 0 14 14" class="fill-current">
                                  <path d="M13.2998 10.0463C13.0836 10.0463 12.9106 10.2191 12.9106 10.4352V12.8981H1.12454V10.4136C1.12454 10.1975 0.951533 10.0247 0.735276 10.0247C0.519018 10.0247 0.346013 10.1975 0.346013 10.4136V13.0926C0.346013 13.3951 0.648773 13.6543 1.01641 13.6543H12.9754C13.3431 13.6543 13.6458 13.4167 13.6458 13.0926V10.4136C13.6891 10.2191 13.5161 10.0463 13.2998 10.0463Z" />
                                  <path fill-rule="evenodd" clip-rule="evenodd" d="M12.5645 10.4352C12.5645 10.0282 12.8925 9.70062 13.2998 9.70062C13.6582 9.70062 14.0627 9.99745 13.9918 10.4453V13.0926C13.9918 13.6678 13.4677 14 12.9754 14H1.01641C0.514814 14 0 13.6384 0 13.0926V10.4136C0 10.0066 0.327921 9.67901 0.735274 9.67901C1.14263 9.67901 1.47055 10.0066 1.47055 10.4136V12.5525H12.5645V10.4352ZM13.6458 10.4136C13.6891 10.2191 13.5161 10.0463 13.2998 10.0463C13.0836 10.0463 12.9106 10.2191 12.9106 10.4352V12.8981H1.12454V10.4136C1.12454 10.1975 0.951533 10.0247 0.735276 10.0247C0.519018 10.0247 0.346013 10.1975 0.346013 10.4136V13.0926C0.346013 13.3951 0.648773 13.6543 1.01641 13.6543H12.9754C13.3431 13.6543 13.6458 13.4167 13.6458 13.0926V10.4136Z" />
                                  <path d="M6.35796 9.41975C6.55259 9.59259 6.79048 9.70062 7.02836 9.70062C7.26624 9.70062 7.50413 9.6142 7.67713 9.44136L9.34231 7.84259C9.49369 7.69136 9.49369 7.4537 9.34231 7.30247C9.19093 7.15124 8.95305 7.15124 8.80167 7.30247L7.396 8.66358V0.734568C7.396 0.518519 7.22299 0.345679 7.00673 0.345679C6.79048 0.345679 6.61747 0.518519 6.61747 0.734568V8.64198L5.2118 7.25926C5.06042 7.10803 4.82254 7.10803 4.67116 7.25926C4.51978 7.41049 4.51978 7.64815 4.67116 7.79938L6.35796 9.41975Z" />
                                  <path fill-rule="evenodd" clip-rule="evenodd" d="M6.12302 9.67362L4.42644 8.04386C4.13994 7.75763 4.13998 7.30106 4.42649 7.01483C4.71264 6.72896 5.16881 6.7286 5.45539 7.01375C5.45575 7.01411 5.45611 7.01447 5.45647 7.01483L6.27146 7.8165V0.734568C6.27146 0.327605 6.59938 0 7.00673 0C7.41409 0 7.74201 0.327605 7.74201 0.734568V7.84714L8.5592 7.05585C8.84584 6.77181 9.3012 6.77254 9.58698 7.05804C9.87348 7.34427 9.87348 7.80079 9.58698 8.08702L9.58212 8.09188L7.91915 9.68842C7.67443 9.93138 7.34631 10.0463 7.02836 10.0463C6.68634 10.0463 6.36988 9.89284 6.12808 9.67812L6.12302 9.67362ZM7.67713 9.44136L9.34231 7.84259C9.49369 7.69136 9.49369 7.4537 9.34231 7.30247C9.19093 7.15124 8.95305 7.15124 8.80167 7.30247L7.396 8.66358V0.734568C7.396 0.518519 7.22299 0.345679 7.00673 0.345679C6.79048 0.345679 6.61747 0.518519 6.61747 0.734568V8.64198L5.2118 7.25926C5.06042 7.10803 4.82254 7.10803 4.67116 7.25926C4.51978 7.41049 4.51978 7.64815 4.67116 7.79938L6.35796 9.41975C6.55259 9.59259 6.79048 9.70062 7.02836 9.70062C7.26624 9.70062 7.50413 9.6142 7.67713 9.44136Z" />
                                </svg>
                              </a>
                                <span v-if="inv.paid" class="inline-flex items-center justify-center rounded-full bg-lime-300 py-2 px-3 text-center text-xs font-medium text-slate-800 hover:bg-opacity-90">
                                    <span class="mr-[4px]">
                                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24"><path fill="currentColor" d="m10.6 16.2l7.05-7.05l-1.4-1.4l-5.65 5.65l-2.85-2.85l-1.4 1.4ZM5 21q-.825 0-1.413-.587Q3 19.825 3 19V5q0-.825.587-1.413Q4.175 3 5 3h14q.825 0 1.413.587Q21 4.175 21 5v14q0 .825-.587 1.413Q19.825 21 19 21Zm0-2h14V5H5v14ZM5 5v14V5Z"/></svg>
                                    </span>
                                    <span>Completed</span>
                                </span>
                              <span v-else class="inline-flex items-center justify-center rounded-full bg-rose-300 py-2 px-3 text-center text-xs font-medium text-slate-800 hover:bg-opacity-90">
                                  <span class="mr-[4px]">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24"><path fill="currentColor" d="m8.4 17l3.6-3.6l3.6 3.6l1.4-1.4l-3.6-3.6L17 8.4L15.6 7L12 10.6L8.4 7L7 8.4l3.6 3.6L7 15.6L8.4 17Zm3.6 5q-2.075 0-3.9-.788t-3.175-2.137q-1.35-1.35-2.137-3.175T2 12q0-2.075.788-3.9t2.137-3.175q1.35-1.35 3.175-2.137T12 2q2.075 0 3.9.788t3.175 2.137q1.35 1.35 2.138 3.175T22 12q0 2.075-.788 3.9t-2.137 3.175q-1.35 1.35-3.175 2.138T12 22Zm0-2q3.35 0 5.675-2.325T20 12q0-3.35-2.325-5.675T12 4Q8.65 4 6.325 6.325T4 12q0 3.35 2.325 5.675T12 20Zm0-8Z"/></svg>
                                  </span>
                                  <span>Failed</span>
                              </span>
                            </div>
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
    const paid = ref('')
    function getPaid() {
      Api.get('/api/account/invoices?filter=settled')
        .then((response) => {
          paid.value = response.data
        })
    }
    const unpaid = ref('')
    function getUnpaid() {
      Api.get('/api/account/invoices?filter=due')
        .then((response) => {
          unpaid.value = response.data
        })
    }
    onMounted(() => {
      getPaid()
      getUnpaid()
    })

</script>

<style scoped>

</style>