<script setup>
definePageMeta({
  title: "The Nuxt & Tailwind CSS dashboard system",
  description:
    "Nuxt & Tailwind CSS dashboard system template that comes with 100+ prebuilt pages and 40+ custom UI components.",
  breadcrumb: {
    label: "Tairo",
  },
  layout: "landing",
});

const Api = useApi();
const contact = ref({
  name: "",
  email: "",
  website: "",
  phone: "",
  message: "",
  success: false,
  error: false,
  serverError: false,
});
const accordion = ref([
  {
    title: "How do I get free .com domain?",
    content:
      "With our enterprise subscription, you will receive a complimentary .com domain at no additional cost.",
  },
  {
    title: "Is registration free?",
    content: "Yes. Its absolutely free. Anyone can register anytime.",
  },
  {
    title:
      "How long my information will remain stored if I'm not willing to renew?",
    content:
      "In that case site will be live for 1 month and data will be stored for two months.",
  },
  {
    title: "How many times will I able to change my themes?",
    content:
      "It's unlimited, if you have multiple themes subscription you can change over the theme one to another whenever you want.",
  },
  {
    title: "Is it easy to build a website?",
    content:
      "It's very easy, Only takes a few minutes to setup your category and products. NextOxy has the guideline for registering, theme purchase, products upload, banners upload, payment methords etc. In addition the NextOxy 24/7 support team is ready to help at all round the clock.",
  },
  {
    title: "Can I build a website without coding knowledge?",
    content:
      "Yes, you don't need any coding knowledge. NextOxy has it's own AI which can build front-end & back-end by it self for you.",
  },
  {
    title: "Should I use a website builder or hire a developer?",
    content:
      "We have our own site editor features. Also you may hire an expert who can help you to complete your project simply.",
  },
  {
    title: "Will I get SSL for free?",
    content:
      "Initially you will get a free SSL certificate. you may purchase premium for advance security encryption.",
  },
  {
    title: "How many products can be uploaded?",
    content: "There has no limit of uploading products. So it's unlimited.",
  },
  {
    title: "How my and clients data remain secured?",
    content:
      "For secure all data automatically encrypted to prevent data breaches.",
  },
  {
    title: "Do you provide API for third party programs?",
    content:
      "NextOxy provides open source API's. So anyone can use this API's on third party programs.",
  },
  {
    title: "Do you backup files and data?",
    content:
      "Yes, NextOxy securely stores all the data as long as they continue there subscription.",
  },
]);

const submitContact = async () => {
  // Reset previous success and error states
  contact.value.success = false;
  contact.value.error = "";

  // Validate form fields
  if (
    !contact.value.name ||
    !contact.value.email ||
    !contact.value.website ||
    !contact.value.phone ||
    !contact.value.message
  ) {
    contact.value.error = true;
    return;
  }

  try {
    const { data } = await Api.post("/api/office/home/contact", contact.value);
    if (data) {
      contact.value = {
        name: "",
        email: "",
        website: "",
        phone: "",
        message: "",
        success: true,
        error: false,
        serverError: false,
      };
    }
  } catch (error) {
    contact.value.serverError = true;
  }
};

const departments = [
  {
    id: 1,
    image: "/static/frontend/images/department1.png",
    title: "Customer Support",
    email: "support@nextoxy.com",
    icon: "i-ic:round-support-agent",
  },
  {
    id: 2,
    image: "/static/frontend/images/department2.png",
    title: "Finance Department",
    email: "finance@nextoxy.com",
    icon: "i-solar:wallet-money-linear",
  },
  {
    id: 3,
    image: "/static/frontend/images/department3.png",
    title: "HR Department",
    email: "hr@nextoxy.com",
    icon: "i-ph:circles-three-duotone",
  },
];
const departments2 = [
  {
    id: 4,
    image: "/static/frontend/images/department3.png",
    title: "Tech & Development",
    email: "dev@nextoxy.com",
    icon: "i-noto-v1:man-technologist-light-skin-tone",
  },
  {
    id: 5,
    image: "/static/frontend/images/department3.png",
    title: "Business Promotion",
    email: "promotion@nextoxy.com",
    icon: "i-hugeicons:promotion",
  },
  {
    id: 6,
    image: "/static/frontend/images/department3.png",
    title: "Partnership",
    email: "partnership@nextoxy.com",
    icon: "i-heroicons:user-group-solid",
  },
  {
    id: 7,
    image: "/static/frontend/images/department3.png",
    title: "CEO",
    email: "ceo@nextoxy.com",
    icon: "i-material-symbols:person-apron-rounded",
  },
];
</script>

<template>
  <div>
    <section class="mx-auto w-full max-w-7xl px-4 pt-32">
      <div>
        <!-- Page Title Area -->
        <div class="relative z-10 text-center py-10">
          <div class="sub-container px-4">
            <h1
              class="font-black text-[28px] md:text-35px lg:text-[66px] text-black-color mb-8"
            >
              <span class="text-primary-color">Help Center</span>
            </h1>
            <p
              class="lg:text-[20px] md:text-15px text-13px lg:max-w-2xl lg:mx-auto leading-7 md:leading-8 text-optional-color"
            >
              Get in touch with us today to see how NextOxy can transform your
              digital presence.
            </p>
          </div>
        </div>
        <div
          class="grid grid-cols-1 md:grid-cols-[294px_294px_294px] justify-center mb-10 gap-6 relative z-10"
        >
          <UCard
            v-for="(department, index) in departments"
            :key="index"
            class="text-center py-10 bg-blue-50/80"
          >
            <!-- <img :src="department.image" :alt="department.title" /> -->
            <UIcon :name="department.icon" dynamic class="text-5xl mb-2" />
            <p class="text-lg font-semibold mt-2 capitalize">
              {{ department.title }}
            </p>
            <a
              :href="'mailto:' + department.email"
              class="text-base text-blue-500 block my-2"
              >{{ department.email }}</a
            >
            <p class="text-sm">
              Mon - Fri 9AM - 6PM <br />
              GMT+6
            </p>
          </UCard>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-4 gap-6 relative z-10">
          <UCard
            v-for="(department, index) in departments2"
            :key="index"
            class="text-center py-10 bg-blue-50/80"
          >
            <!-- <img :src="department.image" :alt="department.title" /> -->
            <UIcon :name="department.icon" dynamic class="text-5xl mb-2" />
            <p class="text-lg font-semibold mt-2 capitalize">
              {{ department.title }}
            </p>
            <a
              :href="'mailto:' + department.email"
              class="text-base text-blue-500 block my-2"
              >{{ department.email }}</a
            >
            <p class="text-sm">
              Mon - Fri 9AM - 6PM <br />
              GMT+6
            </p>
          </UCard>
        </div>
        <!-- End Page Title Area -->

        <!-- Contact Area -->
        <div
          class="pb-16 md:pb-28 pt-20 -mt-10 bg-[#d7d7d7ba] max-w-4xl mx-auto px-2 md:px-10"
        >
          <div class="sub-container px-4">
            <div
              class="grid gap-10 grid-cols-1 sm:grid-cols-1 md:grid-cols-1 lg:grid-cols-1 xl:grid-cols-1"
            >
              <div class="xl:pr-15 wow fadeInLeft mx-auto">
                <h1
                  class="font-bold text-lg md:text-2xl lg:text-4xl lg:leading-tight text-black-color mb-6 text-center"
                >
                  Send Us Message At Anytime From Anywhere
                </h1>
                <div>
                  <div
                    class="grid gap-3 grid-cols-1 sm:grid-cols-2 md:grid-cols-2 lg:grid-cols-2 xl:grid-cols-2"
                  >
                    <input
                      v-model="contact.name"
                      type="text"
                      placeholder="Your Name"
                      class="block w-full border border-[#c5c5c5] bg-white py-2 px-2.5 text-black-color placeholder:text-optional-color outline-0 placeholder:ease-in placeholder:duration-300 focus:placeholder:text-transparent text-13px md:text-15px lg:text-base rounded-lg"
                    />
                    <input
                      v-model="contact.email"
                      type="email"
                      placeholder="Your Email"
                      class="block w-full border border-[#c5c5c5] bg-white py-2 px-2.5 text-black-color placeholder:text-optional-color outline-0 placeholder:ease-in placeholder:duration-300 focus:placeholder:text-transparent text-13px md:text-15px lg:text-base rounded-lg"
                    />
                    <input
                      v-model="contact.website"
                      type="text"
                      placeholder="Store Username"
                      class="block w-full border border-[#c5c5c5] bg-white py-2 px-2.5 text-black-color placeholder:text-optional-color outline-0 placeholder:ease-in placeholder:duration-300 focus:placeholder:text-transparent text-13px md:text-15px lg:text-base rounded-lg"
                    />
                    <input
                      v-model="contact.phone"
                      type="text"
                      placeholder="Phone No"
                      class="block w-full border border-[#c5c5c5] bg-white py-2 px-2.5 text-black-color placeholder:text-optional-color outline-0 placeholder:ease-in placeholder:duration-300 focus:placeholder:text-transparent text-13px md:text-15px lg:text-base rounded-lg"
                    />
                  </div>
                  <textarea
                    v-model="contact.message"
                    cols="30"
                    rows="5"
                    class="mt-3 block w-full border border-[#c5c5c5] bg-white py-2 px-2.5 text-black-color p-6 placeholder:text-optional-color outline-0 placeholder:ease-in placeholder:duration-300 focus:placeholder:text-transparent text-13px md:text-15px lg:text-base rounded-lg"
                    placeholder="Your message here..."
                  ></textarea>

                  <!-- <BaseButton
                    @click="submitContact"
                    color="primary"
                    shape="curved"
                    type="submit"
                    class="mt-8 flex items-center"
                  >
                    <span>Send Message</span>
                    <Icon name="lucide:arrow-right" class="me-1 h-4 w-4" />
                  </BaseButton> -->
                  <PublicButton
                    :handleEvent="submitContact"
                    class="mt-8"
                    firstColor="bg-[#022b46]"
                    secondColor=""
                    label="Send Message"
                  />

                  <!-- <button @click="submitContact" type="submit" class="inline-block font-normal text-16px lg:text-[18px] mt-8 rounded text-white px-10 py-4 bg-gradient-color shadow-custom-box-shadow hover:shadow-primary-btn ease-in duration-300">Send Message</button> -->

                  <p
                    v-if="contact.success"
                    class="text-green-500 text-14px mt-4"
                  >
                    Thank you for your message. It has been sent.
                  </p>
                  <p
                    v-if="contact.serverError"
                    class="text-red-500 text-14px mt-4"
                  >
                    Sorry, your message was not sent. Please try again.
                  </p>
                  <p v-if="contact.error" class="text-red-500 text-14px mt-4">
                    Please fill the form. And try again.
                  </p>
                </div>
              </div>
              <!-- <div class="xl:pl-15 wow fadeInRight">
                <iframe
                  src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3621.7164621717156!2d89.1511258!3d23.8963632!2m3!1f0!2f17.5!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x39fe97e296028421%3A0x7866959ca1bed744!2sNextOxy%20-%20Cloud%20Business%20Solutions!5e0!3m2!1sen!2sbd!4v1651866186495!5m2!1sen!2sbd"
                  loading="lazy"
                  class="w-full h-[450px] lg:h-full rounded-sm lg:rounded-lg"
                ></iframe>
              </div> -->
            </div>
          </div>
        </div>
      </div>
    </section>
    <section class="mx-auto w-full max-w-7xl px-4 pt-20 md:pt-40">
      <div class="">
        <!-- Page Title Area -->
        <div class="relative z-1 text-center">
          <div class="sub-container px-4">
            <h1
              class="font-black text-25px md:text-35px lg:text-[66px] text-black-color mb-8"
            >
              Frequently Asked <span class="text-primary-color">Questions</span>
            </h1>
            <p
              class="lg:text-[20px] text-17px lg:max-w-2xl lg:mx-auto leading-7 md:leading-8 text-optional-color"
            >
              Find answers to common queries in our comprehensive Frequently
              Asked Questions section, designed to provide clarity and
              assistance on key topics and services.
            </p>
          </div>
        </div>

        <!-- FAQ Area -->
        <div class="py-18 bg-cover bg-no-repeat bg-center">
          <section class="pb-10 pt-20 lg:pb-20 lg:pt-[120px]">
            <div class="container mx-auto">
              <div class="-mx-4 flex flex-wrap justify-center">
                <div class="w-full px-4 xl:w-10/12">
                  <div class="md:max-w-3xl mx-auto">
                    <BaseAccordion :items="accordion" action="plus" />
                  </div>
                </div>
              </div>
            </div>
          </section>
        </div>
      </div>
    </section>
  </div>
</template>
