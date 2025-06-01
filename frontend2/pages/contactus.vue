<template>
  <div>
    <section class="mx-auto w-full max-w-7xl px-4 pt-32">
      <div>
        <!-- Page Title Area -->
        <div class="relative z-1 text-center py-10">
          <div class="sub-container px-4">
            <h1
              class="font-black text-[28px] md:text-35px lg:text-[66px] text-black-color mb-8"
            >
              <span class="text-primary-color">Contact Us</span>
            </h1>
            <p
              class="lg:text-[20px] md:text-15px text-13px lg:max-w-2xl lg:mx-auto leading-7 md:leading-8 text-optional-color"
            >
              Get in touch with us today to see how NextOxy can transform your
              digital presence.
            </p>
          </div>
        </div>
        <!-- End Page Title Area -->

        <!-- Contact Area -->
        <div class="py-28">
          <div class="sub-container px-4">
            <div
              class="grid gap-10 grid-cols-1 sm:grid-cols-1 md:grid-cols-1 lg:grid-cols-2 xl:grid-cols-2"
            >
              <div class="xl:pr-15 wow fadeInLeft">
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
                      class="block w-full border py-2 px-2.5 text-black-color placeholder:text-optional-color outline-0 placeholder:ease-in placeholder:duration-300 focus:placeholder:text-transparent text-13px md:text-15px lg:text-base rounded-lg"
                    />
                    <input
                      v-model="contact.email"
                      type="email"
                      placeholder="Your Email"
                      class="block w-full border py-2 px-2.5 text-black-color placeholder:text-optional-color outline-0 placeholder:ease-in placeholder:duration-300 focus:placeholder:text-transparent text-13px md:text-15px lg:text-base rounded-lg"
                    />
                    <input
                      v-model="contact.website"
                      type="text"
                      placeholder="Website"
                      class="block w-full border py-2 px-2.5 text-black-color placeholder:text-optional-color outline-0 placeholder:ease-in placeholder:duration-300 focus:placeholder:text-transparent text-13px md:text-15px lg:text-base rounded-lg"
                    />
                    <input
                      v-model="contact.phone"
                      type="text"
                      placeholder="Phone No"
                      class="block w-full border py-2 px-2.5 text-black-color placeholder:text-optional-color outline-0 placeholder:ease-in placeholder:duration-300 focus:placeholder:text-transparent text-13px md:text-15px lg:text-base rounded-lg"
                    />
                  </div>
                  <textarea
                    v-model="contact.message"
                    cols="30"
                    rows="5"
                    class="mt-3 block w-full border py-2 px-2.5 text-black-color p-6 placeholder:text-optional-color outline-0 placeholder:ease-in placeholder:duration-300 focus:placeholder:text-transparent text-13px md:text-15px lg:text-base rounded-lg"
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
                    class="mt-8"
                    @click="submitContact"
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
              <div class="xl:pl-15 wow fadeInRight">
                <iframe
                  src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3621.7164621717156!2d89.1511258!3d23.8963632!2m3!1f0!2f17.5!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x39fe97e296028421%3A0x7866959ca1bed744!2sNextOxy%20-%20Cloud%20Business%20Solutions!5e0!3m2!1sen!2sbd!4v1651866186495!5m2!1sen!2sbd"
                  loading="lazy"
                  class="w-full h-[450px] lg:h-full rounded-sm lg:rounded-lg"
                ></iframe>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>
<script setup>
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

definePageMeta({
  title: "The Nuxt & Tailwind CSS dashboard system",
  description:
    "Nuxt & Tailwind CSS dashboard system template that comes with 100+ prebuilt pages and 40+ custom UI components.",
  breadcrumb: {
    label: "Tairo",
  },
  layout: "landing",
});

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
</script>
