<script setup lang="ts">
definePageMeta({
  title: 'The Nuxt & Tailwind CSS dashboard system',
  description:
    'Nuxt & Tailwind CSS dashboard system template that comes with 100+ prebuilt pages and 40+ custom UI components.',
  breadcrumb: {
    label: 'Tairo',
  },
  layout: 'landing',
})
</script>

<template>
  <div>
    <section class="mx-auto w-full max-w-7xl px-4 pt-32">
        <div>
            <!-- Page Title Area -->
            <!-- <div class="relative z-1 text-center py-28">
                <div class="container">
                    <h1 class="font-black text-[28px] lg:text-[66px] text-black-color">The <span class="text-primary-color">Services</span> We Provide</h1>
                    <p class="mt-[25px] text-[20px] lg:max-w-2xl mx-auto leading-8 text-optional-color">NextOxy offers a comprehensive range of services including ecommerce, web development, software development, graphics design, and digital marketing solutions.</p>
                </div>
                <div class="left-0 -bottom-90 absolute -z-1 hidden xl:inline"><img src="/static/frontend/images/home/shape/shape34.png" class="animate-custom-movebounce" alt="shape"></div>
                <div class="right-0 bottom-100 absolute -z-1 hidden xl:inline"><img src="/static/frontend/images/home/shape/shape35.png" class="animate-custom-movebounce" alt="shape"></div>
            </div> -->

            <!-- service grid new -->
            <div class="container px-4 mb-40 mt-34 text-black mt-[90px]">
                <div class="title-container flex justify-between items-center gap-4">
                    <div class="">
                        <p class="mb-4 text-[18px] text-black italic">service <span class="sertext">it solutions</span>
                        <svg class="sertext" width="123" height="8" viewBox="0 0 123 8" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M0.384401 7.82144C0.645399 4.52972 8.83029 8.38041 10.8974 7.67652C12.4321 7.1486 11.6386 7.03474 12.9749 6.19628C14.0816 4.61253 15.7519 3.89829 17.9756 4.06391C18.6125 4.48831 19.2284 4.93342 19.8444 5.38888C21.1076 6.09277 22.1621 6.51717 23.6028 6.13417C24.8973 5.79258 25.5237 4.79885 26.6095 4.18812C30.8481 1.80732 31.3701 2.90456 34.5855 4.58147C36.0993 5.36817 37.634 6.48612 39.461 6.08242C40.1604 5.92715 40.2127 5.67871 40.672 5.54415C42.1023 4.10531 43.9606 3.52564 46.2469 3.80512C47.0612 4.28129 47.8651 4.75745 48.669 5.25431C50.9866 6.22733 54.5049 6.23769 54.6615 3.08053C54.3065 3.22545 53.962 3.37037 53.6175 3.51529C55.622 5.75117 58.6078 6.59998 61.5205 5.5752C64.8091 4.41585 63.8277 3.02877 67.1685 4.35374C68.6614 4.94377 70.2587 5.14045 71.856 4.96447C73.6412 4.7678 75.1028 3.27721 76.6271 3.07018C79.0491 2.73894 81.3354 4.89201 84.2482 4.15707C85.3235 3.88793 86.9417 2.27313 87.7978 2.21102C88.6329 2.14891 89.9484 3.68091 90.8358 4.14672C93.3936 5.51309 96.5882 5.75117 99.3234 4.7471C101.902 3.80512 100.858 3.60845 103.124 4.30199C104.366 4.67464 105.253 5.34747 106.652 5.45099C109.628 5.65801 112.175 4.26058 113.678 1.77626C113.25 1.77626 112.822 1.77626 112.384 1.77626C114.722 5.49239 119.587 6.10312 122.771 3.05983C123.471 2.39734 122.406 1.34151 121.707 2.00399C119.316 4.29164 115.516 3.95004 113.678 1.03097C113.386 0.554807 112.687 0.544455 112.384 1.03097C110.223 4.62288 105.159 4.84026 102.549 1.7038C102.278 1.38291 101.777 1.46572 101.495 1.7038C97.6113 4.99553 91.8171 4.46761 88.6747 0.368483C88.4242 0.0372403 87.85 -0.190489 87.5159 0.223564C84.9685 3.37037 80.7717 3.86723 77.6606 1.10343C77.3787 0.854995 76.9507 0.823941 76.6584 1.10343C73.422 4.26058 68.6823 4.52972 65.1432 1.63134C64.83 1.37256 64.3706 1.38291 64.1409 1.75556C61.9799 5.40958 57.2297 5.74082 54.4631 2.65613C54.0873 2.24207 53.44 2.59402 53.4191 3.09088C53.2103 7.04509 45.6727 1.72451 43.8979 1.92118C40.4841 2.30418 40.2127 5.74082 35.7026 3.82583C33.4894 2.88386 31.8085 0.989563 29.1777 1.39326C26.9226 1.74521 25.9622 3.86723 23.9682 4.63323C20.4603 5.9789 19.2702 2.13856 16.2531 2.33524C11.2941 2.66648 14.1442 7.41774 6.43955 5.75117C4.22629 5.27501 -0.221114 3.93969 0.00856432 7.82144C0.0190042 8.05952 0.363521 8.05952 0.384401 7.82144Z" fill="currentColor"></path></svg>
                        </p>

                        <h2 class="font-semibold">Best Digital <span class="sertext">Technology</span><br> Agency For People</h2>
                    </div>
                    <div class="max-w-[480px] w-full">
                        As the complexity of buildings to increase, the field of architecture became multi-disciplinary with technological expertise.
                    </div>
                </div>

                <div class="service_grid grid justify-center lg:grid-cols-3 md:grid-cols-2 sm:grid-cols-2 items-end gap-6 my-6">
                    <div class="service_box relative border py-4 px-8 max-w-[480px] w-full overflow-hidden h-[480px]">
                        <div class="angel absolute w-[50px] rotate-[45deg] h-[50px] right-[-45px] top-[-48px] "></div>
                        <div class="ser_icon relative my-4 sm:mt-12 mt-5">
                            <img src="/static/frontend/images/icons/ser10.png" alt="">
                            <div class="serround mt-4 w-[46px] h-[46px] rounded-full absolute -z-10 top-[-15px] left-[25px]"></div>
                        </div>
                        <h3 class="text-[25px] mb-6 leading-[30px] font-bold h-[60px] overflow-hidden">Software Development</h3>
                        <p class="my-2 leading-[25px] text-gray-800/80 text-[17px]">Creating powerful tech solutions that change industries.</p>
                        <div class="flex sm:flex-row flex-col sm:gap-4 gap-1 items-center justify-center mt-8">
                            <nuxt-link to="/home/service_forms/software_development" class="flex items-center "><p class="text-lg sertext font-bold">Chat with us</p><svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 16 16"><path fill="none" stroke="#6c53ff" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M5.25 4.25h6.5v6.5m-7.5 1l7.5-7.5"/></svg></nuxt-link>
                            <button class="btn-primary px-4 py-1.5 rounded">Order Now</button>
                        </div>
                    </div>
                    <div class="service_box relative border py-4 px-8 max-w-[480px] w-full overflow-hidden h-[480px]">
                        <div class="angel absolute w-[50px] rotate-[45deg] h-[50px] right-[-45px] top-[-48px] "></div>
                        <div class="ser_icon relative my-4 sm:mt-12 mt-5">
                            <img src="/static/frontend/images/icons/ser6.png" alt="">
                            <div class="serround w-[46px] h-[46px] rounded-full absolute -z-10 top-[-15px] left-[25px]"></div>
                        </div>
                        <h3 class="text-[25px] mb-6 leading-[30px] font-bold h-[60px] overflow-hidden">Web Development</h3>
                        <p class="my-2 leading-[25px] text-gray-800/80 text-[17px]">Unlocking digital potential through dynamic websites.</p>
                        <div class="flex sm:flex-row flex-col sm:gap-4 gap-1 items-center justify-center mt-8">
                            <nuxt-link to="/home/service_forms/web_development" class="flex items-center  "><p class="text-lg sertext font-bold">Chat with us</p><svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 16 16"><path fill="none" stroke="#6c53ff" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M5.25 4.25h6.5v6.5m-7.5 1l7.5-7.5"/></svg></nuxt-link>
                            <button class="btn-primary px-4 py-1.5 rounded">Order Now</button>
                        </div>
                    </div>
                    <div class="service_box relative border py-4 px-8 max-w-[480px] w-full overflow-hidden h-[480px]">
                        <div class="angel absolute w-[50px] rotate-[45deg] h-[50px] right-[-45px] top-[-48px] "></div>
                        <div class="ser_icon relative my-4 sm:mt-12 mt-5">
                            <img src="/static/frontend/images/icons/ser2.png" alt="">
                            <div class="serround w-[46px] h-[46px] rounded-full absolute -z-10 top-[-15px] left-[25px]"></div>
                        </div>
                        <h3 class="text-[25px] mb-6 leading-[30px] font-bold h-[60px] overflow-hidden">International payment gateway solution</h3>
                        <p class="my-2 leading-[25px] text-gray-800/80 text-[17px]">Effortless global transactions made simple and secure.</p>
                        <div class="flex sm:flex-row flex-col sm:gap-4 gap-1 items-center justify-center mt-8">
                            <nuxt-link to="/home/service_forms/web_development" class="flex items-center  "><p class="text-lg sertext font-bold">Chat with us</p><svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 16 16"><path fill="none" stroke="#6c53ff" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M5.25 4.25h6.5v6.5m-7.5 1l7.5-7.5"/></svg></nuxt-link>
                            <button class="btn-primary px-4 py-1.5 rounded">Order Now</button>
                        </div>
                    </div>

                    <div class="service_box relative border py-4 px-8 max-w-[480px] w-full overflow-hidden h-[480px]">
                        <div class="angel absolute w-[50px] rotate-[45deg] h-[50px] right-[-45px] top-[-48px] "></div>
                        <div class="ser_icon relative my-4 sm:mt-12 mt-5">
                            <img src="/static/frontend/images/icons/ser3.png" alt="">
                            <div class="serround w-[46px] h-[46px] rounded-full absolute -z-10 top-[-15px] left-[25px]"></div>
                        </div>
                        <h3 class="text-[25px] mb-6 leading-[30px] font-bold h-[60px] overflow-hidden">Facebook Bossting</h3>
                        <p class="my-2 leading-[25px] text-gray-800/80 text-[17px]">Elevate engagement, charm, and influence naturally.</p>
                        <div class="flex sm:flex-row flex-col sm:gap-4 gap-1 items-center justify-center mt-8">
                            <nuxt-link to="/home/service_forms/facebook_boost" class="flex items-center  "><p class="text-lg sertext font-bold">Chat with us</p><svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 16 16"><path fill="none" stroke="#6c53ff" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M5.25 4.25h6.5v6.5m-7.5 1l7.5-7.5"/></svg></nuxt-link>
                            <button class="btn-primary px-4 py-1.5 rounded">Order Now</button>
                        </div>
                    </div>
                    <div class="service_box relative border py-4 px-8 max-w-[480px] w-full overflow-hidden h-[480px]">
                        <div class="angel absolute w-[50px] rotate-[45deg] h-[50px] right-[-45px] top-[-48px] "></div>
                        <div class="ser_icon relative my-4 sm:mt-12 mt-5">
                            <img src="/static/frontend/images/icons/ser1.png" alt="">
                            <div class="serround w-[46px] h-[46px] rounded-full absolute -z-10 top-[-15px] left-[25px]"></div>
                        </div>
                        <h3 class="text-[25px] mb-6 leading-[30px] font-bold h-[60px] overflow-hidden">Dropshipping</h3>
                        <p class="my-2 leading-[25px] text-gray-800/80 text-[17px]">Effortless online retail: Source, ship, profit. Flourish.</p>
                        <div class="flex sm:flex-row flex-col sm:gap-4 gap-1 items-center justify-center mt-8">
                            <a href="https://nextdropshipping.com/" target="_blank" class="flex items-center  "><p class="text-lg sertext font-bold">Chat with us</p><svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 16 16"><path fill="none" stroke="#6c53ff" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M5.25 4.25h6.5v6.5m-7.5 1l7.5-7.5"/></svg></a>
                            <button class="btn-primary px-4 py-1.5 rounded">Order Now</button>
                        </div>
                    </div>
                    <div class="service_box relative border py-4 px-8 max-w-[480px] w-full overflow-hidden h-[480px]">
                        <div class="angel absolute w-[50px] rotate-[45deg] h-[50px] right-[-45px] top-[-48px] "></div>
                        <div class="ser_icon relative my-4 sm:mt-12 mt-5">
                            <img src="/static/frontend/images/icons/ser8.png" alt="">
                            <div class="serround w-[46px] h-[46px] rounded-full absolute -z-10 top-[-15px] left-[25px]"></div>
                        </div>
                        <h3 class="text-[25px] mb-6 leading-[30px] font-bold h-[60px] overflow-hidden">SEO Marketing</h3>
                        <p class="my-2 leading-[25px] text-gray-800/80 text-[17px]">Boost online presence, dominate search rankings, attract customers.</p>
                        <div class="flex sm:flex-row flex-col sm:gap-4 gap-1 items-center justify-center mt-8">
                            <nuxt-link to="/home/service_forms/seo" class="flex items-center  "><p class="text-lg sertext font-bold">Chat with us</p><svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 16 16"><path fill="none" stroke="#6c53ff" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M5.25 4.25h6.5v6.5m-7.5 1l7.5-7.5"/></svg></nuxt-link>
                            <button class="btn-primary px-4 py-1.5 rounded">Order Now</button>
                        </div>
                    </div>

                    <div class="service_box relative border py-4 px-8 max-w-[480px] w-full overflow-hidden h-[480px]">
                        <div class="angel absolute w-[50px] rotate-[45deg] h-[50px] right-[-45px] top-[-48px] "></div>
                        <div class="ser_icon relative my-4 sm:mt-12 mt-5">
                            <img src="/static/frontend/images/icons/ser9.png" alt="">
                            <div class="serround w-[46px] h-[46px] rounded-full absolute -z-10 top-[-15px] left-[25px]"></div>
                        </div>
                        <h3 class="text-[25px] mb-6 leading-[30px] font-bold h-[60px] overflow-hidden">Import Consulting Service</h3>
                        <p class="my-2 leading-[25px] text-gray-800/80 text-[17px]">Expert guidance for seamless international business growth.</p>
                        <div class="flex sm:flex-row flex-col sm:gap-4 gap-1 items-center justify-center mt-8">
                            <nuxt-link to="/home/service_forms/import" class="flex items-center  "><p class="text-lg sertext font-bold">Chat with us</p><svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 16 16"><path fill="none" stroke="#6c53ff" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M5.25 4.25h6.5v6.5m-7.5 1l7.5-7.5"/></svg></nuxt-link>
                            <button class="btn-primary px-4 py-1.5 rounded">Order Now</button>
                        </div>
                    </div>
                    <div class="service_box relative border py-4 px-8 max-w-[480px] w-full overflow-hidden h-[480px]">
                        <div class="angel absolute w-[50px] rotate-[45deg] h-[50px] right-[-45px] top-[-48px] "></div>
                        <div class="ser_icon relative my-4 sm:mt-12 mt-5">
                            <img src="/static/frontend/images/icons/ser11.png" alt="">
                            <div class="serround w-[46px] h-[46px] rounded-full absolute -z-10 top-[-15px] left-[25px]"></div>
                        </div>
                        <h3 class="text-[25px] mb-6 leading-[30px] font-bold h-[60px] overflow-hidden">Packaging Materials Solutions</h3>
                        <p class="my-2 leading-[25px] text-gray-800/80 text-[17px]">Innovative, Eco-friendly, Effective: Unleash Your Brand's Potential.</p>
                        <div class="flex sm:flex-row flex-col sm:gap-4 gap-1 items-center justify-center mt-8">
                            <nuxt-link to="/home/service_forms/packaging" class="flex items-center  "><p class="text-lg sertext font-bold">Chat with us</p><svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 16 16"><path fill="none" stroke="#6c53ff" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M5.25 4.25h6.5v6.5m-7.5 1l7.5-7.5"/></svg></nuxt-link>
                            <button class="btn-primary px-4 py-1.5 rounded">Order Now</button>
                        </div>
                    </div>
                    <div class="service_box relative border py-4 px-8 max-w-[480px] w-full overflow-hidden h-[480px]">
                        <div class="angel absolute w-[50px] rotate-[45deg] h-[50px] right-[-45px] top-[-48px] "></div>
                        <div class="ser_icon relative my-4 sm:mt-12 mt-5">
                            <img src="/static/frontend/images/icons/ser5.png" alt="">
                            <div class="serround w-[46px] h-[46px] rounded-full absolute -z-10 top-[-15px] left-[25px]"></div>
                        </div>
                        <h3 class="text-[25px] mb-6 leading-[30px] font-bold h-[60px] overflow-hidden">Account, Business, Office Management Software (OxyManager)</h3>
                        <p class="my-2 leading-[25px] text-gray-800/80 text-[17px]">Streamline operations with influential office management software.</p>
                        <div class="flex sm:flex-row flex-col sm:gap-4 gap-1 items-center justify-center mt-8">
                            <a href="https://www.oxymanager.com" target="_blank" class="flex items-center  "><p class="text-lg sertext font-bold">Chat with us</p><svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 16 16"><path fill="none" stroke="#6c53ff" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M5.25 4.25h6.5v6.5m-7.5 1l7.5-7.5"/></svg></a>
                            <button class="btn-primary px-4 py-1.5 rounded">Order Now</button>
                        </div>
                    </div>

                </div>
                <div class="flex sm:flex-row flex-col items-center justify-center gap-6">
                    <div class="service_box relative border py-4 px-8 max-w-[480px] w-full overflow-hidden h-[480px]">
                        <div class="angel absolute w-[50px] rotate-[45deg] h-[50px] right-[-45px] top-[-48px] "></div>
                        <div class="ser_icon relative my-4 sm:mt-12 mt-5">
                            <img src="/static/frontend/images/icons/ser4.png" alt="">
                            <div class="serround w-[46px] h-[46px] rounded-full absolute -z-10 top-[-15px] left-[25px]"></div>
                        </div>
                        <h3 class="text-[25px] mb-6 leading-[30px] font-bold h-[60px] overflow-hidden">Graphic Design</h3>
                        <p class="my-2 leading-[25px] text-gray-800/80 text-[17px]">Creative visuals speak persuasively to audiences.</p>
                        <div class="flex sm:flex-row flex-col sm:gap-4 gap-1 items-center justify-center mt-8">
                            <nuxt-link to="/home/service_forms/graphic_desgin" class="flex items-center  "><p class="text-lg sertext font-bold">Chat with us</p><svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 16 16"><path fill="none" stroke="#6c53ff" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M5.25 4.25h6.5v6.5m-7.5 1l7.5-7.5"/></svg></nuxt-link>
                            <button class="btn-primary px-4 py-1.5 rounded">Order Now</button>
                        </div>
                    </div>
                    <div class="service_box relative border py-4 px-8 max-w-[480px] w-full overflow-hidden h-[480px]">
                        <div class="angel absolute w-[50px] rotate-[45deg] h-[50px] right-[-45px] top-[-48px] "></div>
                        <div class="ser_icon relative my-4 sm:mt-12 mt-5">
                            <img src="/static/frontend/images/icons/ser7.png" alt="">
                            <div class="serround w-[46px] h-[46px] rounded-full absolute -z-10 top-[-15px] left-[25px]"></div>
                        </div>
                        <h3 class="text-[25px] mb-6 leading-[30px] font-bold h-[60px] overflow-hidden">SMS Marketing</h3>
                        <p class="my-2 leading-[25px] text-gray-800/80 text-[17px]">Engaging, Authentic, Persuasive, Human, Non-technical, Impactful, Convincing.</p>
                        <div class="flex sm:flex-row flex-col sm:gap-4 gap-1 items-center justify-center mt-8">
                            <nuxt-link to="/home/service_forms/sms" class="flex items-center  "><p class="text-lg sertext font-bold">Chat with us</p><svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 16 16"><path fill="none" stroke="#6c53ff" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M5.25 4.25h6.5v6.5m-7.5 1l7.5-7.5"/></svg></nuxt-link>
                            <button class="btn-primary px-4 py-1.5 rounded">Order Now</button>
                        </div>
                    </div>
                </div>
            </div>

            <!-- service grid old -->
            <!-- <div class=" relative z-1 pb-28">
                <div class="container">
                    <div class="grid gap-4 md:gap-8 grid-cols-1 sm:grid-cols-2 md:grid-cols-2 lg:grid-cols-3">
                        <nuxt-link to="/home/service_forms/facebook_boost">
                            <div class="bg-white shadow-custom-box-shadow3 rounded-sm md:rounded-lg wow animate__animated animate__fadeInUp" data-wow-delay=".1s">
                                <img src="/static/frontend/images/home/services/ecommerce.gif" class="rounded-t-sm md:rounded-t-lg" alt="support">
                                <div class="p-8">
                                    <h3 class="font-bold text-black text-[18px] md:text-[30px] lg:text-[30px]">
                                        Facebook Boosting
                                    </h3>
                                    <p class="py-4 leading-7 md:leading-8 text-optional-color text-13px text-[20px]">Create stunning eCommerce themes instantly with NextOxy's powerful AI technology. Boost your online presence and sales today!</p>
                                    <p class="link-btn flex items-center gap-2 relative font-medium text-[20px] text-secondary-color ease-in duration-100 hover:text-secondary-color hover:tracking-wide">
                                        Order Now <img src="/static/frontend/images/home/icon/secondary-arrow-right.svg" alt="arrow-right">
                                    </p>
                                </div>
                            </div>                    
                        </nuxt-link>
                        <nuxt-link to="/home/themes">
                            <div class="bg-white shadow-custom-box-shadow3 rounded-sm md:rounded-lg wow animate__animated animate__fadeInUp" data-wow-delay=".1s">
                                <img src="/static/frontend/images/home/services/ecommerce.gif" class="rounded-t-sm md:rounded-t-lg" alt="support">
                                <div class="p-8">
                                    <h3 class="font-bold text-black text-[18px] md:text-[30px] lg:text-[30px]">
                                            e-Commerce
                                    </h3>
                                    <p class="py-4 leading-7 md:leading-8 text-optional-color text-13px text-[20px]">Create stunning eCommerce themes instantly with NextOxy's powerful AI technology. Boost your online presence and sales today!</p>
                                    <p class="link-btn flex items-center gap-2 relative font-medium text-[20px] text-secondary-color ease-in duration-100 hover:text-secondary-color hover:tracking-wide">
                                        Demo Themes <img src="/static/frontend/images/home/icon/secondary-arrow-right.svg" alt="arrow-right">
                                    </p>
                                </div>
                            </div>                    
                        </nuxt-link>
                        <div>
                            <a target="_blank" href="https://nextdropshipping.com/register/">
                                <div class="bg-white shadow-custom-box-shadow3 rounded-sm md:rounded-lg wow animate__animated animate__fadeInUp" data-wow-delay=".1s">
                                    <img src="/static/frontend/images/home/services/dropshipping.gif" class="rounded-t-sm md:rounded-t-lg" alt="support">
                                    <div class="p-8">
                                        <h3 class="font-bold text-black text-[18px] md:text-[30px] lg:text-[30px]">
                                                Dropshipping
                                        </h3>
                                        <p class="py-4 leading-7 md:leading-8 text-optional-color text-13px text-[20px]">Get your eCommerce store up and running quickly with NextOxy's ready-to-use templates. Start dropshipping instantly and increase your sales!</p>
                                        <p href="#" class="link-btn flex items-center gap-2 relative font-medium text-[20px] text-secondary-color ease-in duration-100 hover:text-secondary-color hover:tracking-wide">
                                            Visit Now <img src="/static/frontend/images/home/icon/secondary-arrow-right.svg" alt="arrow-right">
                                        </p>
                                    </div>
                                </div>                    
                            </a>
                        </div>
                        <nuxt-link to="/home/service_forms/digital_marketing">
                            <div class="bg-white shadow-custom-box-shadow3 rounded-sm md:rounded-lg wow animate__animated animate__fadeInUp" data-wow-delay=".1s">
                                <img src="/static/frontend/images/home/services/digital-marketing.gif" class="rounded-t-sm md:rounded-t-lg" alt="support">
                                <div class="p-8">
                                    <h3 class="font-bold text-black text-[18px] md:text-[30px] lg:text-[30px]">
                                            Digital Marketing
                                    </h3>
                                    <p class="py-4 leading-7 md:leading-8 text-optional-color text-13px text-[20px]">Transform your online presence with NextOxy's expert digital marketing team. Drive growth and engagement!</p>
                                    <p class="link-btn flex items-center gap-2 relative font-medium text-[20px] text-secondary-color ease-in duration-100 hover:text-secondary-color hover:tracking-wide">
                                        Order Now! <img src="/static/frontend/images/home/icon/secondary-arrow-right.svg" alt="arrow-right">
                                    </p>
                                </div>
                            </div>                    
                        </nuxt-link>
                        <nuxt-link to="/home/service_forms/web_development">
                            <div class="bg-white shadow-custom-box-shadow3 rounded-sm md:rounded-lg wow animate__animated animate__fadeInUp" data-wow-delay=".1s">
                                <img src="/static/frontend/images/home/services/webdevelopment.gif" class="rounded-t-sm md:rounded-t-lg" alt="support">
                                <div class="p-8">
                                    <h3 class="font-bold text-black text-[18px] md:text-[30px] lg:text-[30px]">
                                            Web Development
                                    </h3>
                                    <p class="py-4 leading-7 md:leading-8 text-optional-color text-13px text-[20px]">NextOxy's experienced web development team provides customized solutions for any industry, delivering high-quality websites that drive business growth</p>
                                    <p class="link-btn flex items-center gap-2 relative font-medium text-[20px] text-secondary-color ease-in duration-100 hover:text-secondary-color hover:tracking-wide">
                                        Order Now! <img src="/static/frontend/images/home/icon/secondary-arrow-right.svg" alt="arrow-right">
                                    </p>
                                </div>
                            </div>                    
                        </nuxt-link>
                        <nuxt-link to="/home/service_forms/software_development">
                            <div class="bg-white shadow-custom-box-shadow3 rounded-sm md:rounded-lg wow animate__animated animate__fadeInUp" data-wow-delay=".1s">
                                <img src="/static/frontend/images/home/services/software-development.gif" class="rounded-t-sm md:rounded-t-lg" alt="support">
                                <div class="p-8">
                                    <h3 class="font-bold text-black text-[18px] md:text-[30px] lg:text-[30px]">
                                            Software Development
                                    </h3>
                                    <p class="py-4 leading-7 md:leading-8 text-optional-color text-13px text-[20px]">NextOxy's software development team delivers cutting-edge mobile and desktop app solutions tailored to your unique business needs and goals</p>
                                    <p class="link-btn flex items-center gap-2 relative font-medium text-[20px] text-secondary-color ease-in duration-100 hover:text-secondary-color hover:tracking-wide">
                                        Order Now! <img src="/static/frontend/images/home/icon/secondary-arrow-right.svg" alt="arrow-right">
                                    </p>
                                </div>
                            </div>                    
                        </nuxt-link>
                        <nuxt-link to="/home/service_forms/graphic_desgin">
                            <div class="bg-white shadow-custom-box-shadow3 rounded-sm md:rounded-lg wow animate__animated animate__fadeInUp" data-wow-delay=".1s">
                                <img src="/static/frontend/images/home/services/graphics-design.gif" class="rounded-t-sm md:rounded-t-lg" alt="support">
                                <div class="p-8">
                                    <h3 class="font-bold text-black text-[18px] md:text-[30px] lg:text-[30px]">
                                            Graphic Design
                                    </h3>
                                    <p class="py-4 leading-7 md:leading-8 text-optional-color text-13px text-[20px]">NextOxy's expert graphic designers provide customized solutions that elevate your brand with stunning designs and creative visuals that stand out.</p>
                                    <p class="link-btn flex items-center gap-2 relative font-medium text-[20px] text-secondary-color ease-in duration-100 hover:text-secondary-color hover:tracking-wide">
                                        Order Now! <img src="/static/frontend/images/home/icon/secondary-arrow-right.svg" alt="arrow-right">
                                    </p>
                                </div>
                            </div>                    
                        </nuxt-link>
                    
                    </div>
                </div>
                <div class="top-[29%] left-[5%] absolute -z-1 hidden lg:inline"><img src="/static/frontend/images/home//shape/shape27.svg" class="animate-custom-rotateme" alt="shape"></div>
                <div class="bottom-[22%] right-[4%] absolute -z-1 hidden lg:inline"><img src="/static/frontend/images/home//shape/shape28.svg" class="animate-custom-rotateme" alt="shape"></div>
            </div> -->


            <!-- Features Area -->
            <div class="features-area bg-[#fbfbfb]">
                <div class="container pb-28">
                    <div class="section-title mb-6 md:mb-40 lg:mb-[50px] text-center">
                        <h2 class="font-black text-[28px] lg:text-[50px] text-black-color">What We Do Specially</h2>
                        <p class="text-[20px] mt-[25px] lg:max-w-2xl lg:mx-auto leading-7 md:leading-8 text-optional-color">NextOxy is your one-stop solution for all your digital needs, providing high-quality services including ecommerce, web development, software development, graphics design, and more</p>
                    </div>
                    <div class="grid gap-[25px] grid-cols-1 sm:grid-cols-2 md:grid-cols-2 lg:grid-cols-2 xl:grid-cols-4">
                        <div class="single-features-box border p-[20px] sm:border-0 sm:p-0 text-center sm:text-left wow animate__animated animate__fadeInUp" data-wow-delay=".1s">
                            <div class="icon w-[90px] h-[90px] rounded-full bg-secondary-gradient-color text-center relative mb-[25px] ml-auto mr-auto sm:ml-0 sm:mr-0">
                                <img src="/static/frontend/images/home/icon/shield-tick.svg" class="absolute left-0 right-0 top-1/2 m-auto -translate-y-2/4" alt="shield-tick">
                            </div>
                            <h3 class="font-bold text-[18px] md:text-[30px] lg:text-24px mb-[25px]">
                                <a href="services-details.html" class="inline-block text-black-color hover:text-primary-color ease-in duration-300">
                                    Top Flexibility
                                </a>
                            </h3>
                            <p class="leading-7 md:leading-8 text-optional-color mb-[25px] text-[20px]">Experience the power of flexibility with NextOxy's customizable services.</p>
                            <a href="services-details.html" class="link-btn flex items-center gap-2 relative pr-20 font-medium text-13px md:text-14px lg:text-15px text-secondary-color ease-in duration-100 hover:text-secondary-color hover:tracking-wide">
                            </a>
                        </div>
                        <div class="single-features-box border p-[20px] sm:border-0 sm:p-0 text-center sm:text-left wow animate__animated animate__fadeInUp" data-wow-delay=".1s">
                            <div class="icon w-[90px] h-[90px] rounded-full bg-primary-gradient-color text-center relative mb-[25px] ml-auto mr-auto sm:ml-0 sm:mr-0">
                                <img src="/static/frontend/images/home//icon/shield-tick.svg" class="absolute left-0 right-0 top-1/2 m-auto -translate-y-2/4" alt="shield-tick">
                            </div>
                            <h3 class="font-bold text-[18px] md:text-[30px] lg:text-24px mb-[25px]">
                                <a href="services-details.html" class="inline-block text-black-color hover:text-primary-color ease-in duration-300">
                                    Time Savings
                                </a>
                            </h3>
                            <p class="leading-7 md:leading-8 text-optional-color mb-[25px] text-[20px]">Unlock the power of time savings with NextOxy's efficient and streamlined digital solutions.</p>
                            <a href="services-details.html" class="link-btn flex items-center gap-2 relative pr-20 font-medium text-13px md:text-14px lg:text-15px text-secondary-color ease-in duration-100 hover:text-secondary-color hover:tracking-wide">
                            </a>
                        </div>
                        <div class="single-features-box border p-[20px] sm:border-0 sm:p-0 text-center sm:text-left wow animate__animated animate__fadeInUp" data-wow-delay=".1s">
                            <div class="icon w-[90px] h-[90px] rounded-full bg-green-gradient-color text-center relative mb-[25px] ml-auto mr-auto sm:ml-0 sm:mr-0">
                                <img src="/static/frontend/images/home//icon/shield-tick.svg" class="absolute left-0 right-0 top-1/2 m-auto -translate-y-2/4" alt="shield-tick">
                            </div>
                            <h3 class="font-bold text-[18px] md:text-[30px] lg:text-24px mb-[25px]">
                                <a href="services-details.html" class="inline-block text-black-color hover:text-primary-color ease-in duration-300">
                                    Best Management
                                </a>
                            </h3>
                            <p class="leading-7 md:leading-8 text-optional-color mb-[25px] text-[20px]">Experience the best in business management with NextOxy's comprehensive suite of tools and services</p>
                            <a href="services-details.html" class="link-btn flex items-center gap-2 relative pr-20 font-medium text-13px md:text-14px lg:text-15px text-secondary-color ease-in duration-100 hover:text-secondary-color hover:tracking-wide">
                            </a>
                        </div>
                        <div class="single-features-box border p-[20px] sm:border-0 sm:p-0 text-center sm:text-left wow animate__animated animate__fadeInUp" data-wow-delay=".1s">
                            <div class="icon w-[90px] h-[90px] rounded-full bg-yello-gradient-color text-center relative mb-[25px] ml-auto mr-auto sm:ml-0 sm:mr-0">
                                <img src="/static/frontend/images/home/icon/shield-tick.svg" class="absolute left-0 right-0 top-1/2 m-auto -translate-y-2/4" alt="shield-tick">
                            </div>
                            <h3 class="font-bold text-[18px] md:text-[30px] lg:text-24px mb-[25px]">
                                <a href="services-details.html" class="inline-block text-black-color hover:text-primary-color ease-in duration-300">
                                    Collaborative
                                </a>
                            </h3>
                            <p class="leading-7 md:leading-8 text-optional-color mb-[25px] text-[20px]">Collaborate with ease and efficiency using NextOxy's advanced project management and communication tools</p>
                            <a href="services-details.html" class="link-btn flex items-center gap-2 relative pr-20 font-medium text-13px md:text-14px lg:text-15px text-secondary-color ease-in duration-100 hover:text-secondary-color hover:tracking-wide">
                            </a>
                        </div>
                    
                    </div>
                </div>
            </div>
        </div>
    </section>
  </div>
</template>
<style scoped>
    .shadow-custom-box-shadow3 {
  --tw-shadow: 0px 2px 15px rgba(58, 58, 58, 0.1);
  --tw-shadow-colored: 0px 2px 15px var(--tw-shadow-color);
  box-shadow: var(--tw-ring-offset-shadow, 0 0 #0000), var(--tw-ring-shadow, 0 0 #0000), var(--tw-shadow);
}
.service_box:hover{
    background-color: #020626e7;
}
.service_box{
    transition: .1s ease;
    
}
.service_box:hover .angel{
    transition: .1s ease ;
    top: -28px;
    background-color: #6c53ff;
    right: -25px;
}
.service_box:hover h3{
    color: #6c53ff;
}
.service_box:hover p{
    color: #c9c8c8b2;
}
.service_box:hover a p{
    color: #6c53ff !important;
}
.sertext{
    color: #6c53ff;
}
.serround{
    background: rgba(6,218,195,.1);
}
@media(max-width: 768px){
    .title-container{
        flex-direction: column;

    }
}
</style>