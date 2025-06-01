<script setup lang="ts">
import { toTypedSchema } from "@vee-validate/zod";
import { DatePicker } from "v-calendar";
import { Field, useForm } from "vee-validate";
import { z } from "zod";

import "v-calendar/dist/style.css";
import "~/assets/css/vcalendar.css";
const Api = useApi();
definePageMeta({
  layout: "dashboard",
});

const VALIDATION_TEXT = {
  first_name: "First name cannot be empty",
  last_name: "Last name cannot be empty",
  email: "Email name cannot be empty",
  phone_number: "Phone Number name cannot be empty",
  address: "Address name cannot be empty",
  city: "City name cannot be empty",
  state: "State name cannot be empty",
  country: "Country name cannot be empty",
  zip_code: "Zip Code name cannot be empty",
};

// This is the Zod schema for the form input
// It's used to define the shape that the form data will have
const zodSchema = z.object({
  event: z.object({
    first_name: z.string().min(1, VALIDATION_TEXT.first_name),
    last_name: z.string().min(1, VALIDATION_TEXT.last_name),
    email: z.string().min(1, VALIDATION_TEXT.email),
    phone_number: z.string().min(1, VALIDATION_TEXT.phone_number),
    address: z.string().min(1, VALIDATION_TEXT.address),
    city: z.string().min(1, VALIDATION_TEXT.city),
    state: z.string().min(1, VALIDATION_TEXT.state),
    country: z.string().min(1, VALIDATION_TEXT.country),
    zip_code: z.string().min(1, VALIDATION_TEXT.zip_code),
  }),
});

// Zod has a great infer method that will
// infer the shape of the schema into a TypeScript type
type FormInput = z.infer<typeof zodSchema>;

const validationSchema = toTypedSchema(zodSchema);
const initialValues = computed<FormInput>(() => ({
  event: {
    first_name: "",
    last_name: "",
    email: "",
    phone_number: "",
    address: "",
    city: "",
    state: "",
    country: "",
    zip_code: "",
  },
}));

const {
  handleSubmit,
  isSubmitting,
  setFieldError,
  meta,
  values,
  errors,
  resetForm,
  setFieldValue,
  setErrors,
} = useForm({
  validationSchema,
  initialValues,
});

async function getProfile() {
  const res = await Api.get("/api/account/profile");
  setFieldValue("event", { ...values.event, ...res.data });
}
getProfile();

const success = ref(false);
const fieldsWithErrors = computed(() => Object.keys(errors.value).length);

// Ask the user for confirmation before leaving the page if the form has unsaved changes
onBeforeRouteLeave(() => {
  // if (meta.value.dirty) {
  //   return confirm('You have unsaved changes. Are you sure you want to leave?')
  // }
});

const toaster = useToaster();

// This is where you would send the form data to the server
const onSubmit = handleSubmit(
  async (values) => {
    success.value = false;

    // here you have access to the validated form values
    const res = await Api.post("/api/account/profile", values.event);
    setFieldValue("event", { ...values.event, ...res.data });

    toaster.clearAll();
    toaster.show({
      title: "Success",
      message: `Profile has been updated!`,
      color: "success",
      icon: "ph:check",
      closable: true,
    });

    document.documentElement.scrollTo({
      top: 0,
      behavior: "smooth",
    });

    success.value = true;
    setTimeout(() => {
      success.value = false;
    }, 3000);
  },
  (error) => {
    // this callback is optional and called only if the form has errors
    success.value = false;

    // here you have access to the error
    console.log("event-create-error", error);

    // you can use it to scroll to the first error
    document.documentElement.scrollTo({
      top: 0,
      behavior: "smooth",
    });
  }
);
</script>

<template>
  <form
    action=""
    method="POST"
    @submit.prevent="onSubmit"
    class="relative py-3 sm:mx-auto sm:max-w-xl"
  >
    <BaseCard shape="curved" class="relative px-4 py-10 sm:p-10 md:mx-0">
      <div class="mx-auto max-w-md">
        <div class="flex items-center gap-4">
          <div
            class="bg-primary-500/20 text-primary-500 flex h-14 w-14 shrink-0 items-center justify-center rounded-full font-sans text-2xl"
          >
            <Icon name="ph:calendar-blank-duotone" class="h-5 w-5" />
          </div>
          <div class="block text-xl font-semibold">
            <BaseHeading as="h3" size="lg" weight="medium">
              Update Profile
            </BaseHeading>
            <BaseText size="sm" class="text-muted-400"
              >Your General Profile</BaseText
            >
          </div>
        </div>
        <div class="divide-y divide-gray-200">
          <div class="grid grid-cols-12 gap-4 py-8">
            <div class="col-span-12">
              <div class="flex w-full flex-col gap-4 sm:flex-row">
                <div class="relative grow">
                  <Field
                    v-slot="{ field, errorMessage, handleChange, handleBlur }"
                    name="event.first_name"
                  >
                    <BaseInput
                      label="First Name"
                      shape="curved"
                      placeholder=""
                      :classes="{
                        input: '!h-11',
                        icon: '!h-11 !w-11',
                      }"
                      :model-value="field.value"
                      :error="errorMessage"
                      :disabled="isSubmitting"
                      type="text"
                      @update:model-value="handleChange"
                      @blur="handleBlur"
                    />
                  </Field>
                </div>
                <div class="relative grow">
                  <Field
                    v-slot="{ field, errorMessage, handleChange, handleBlur }"
                    name="event.last_name"
                  >
                    <BaseInput
                      label="Last Name"
                      shape="curved"
                      placeholder=""
                      :classes="{
                        input: '!h-11',
                        icon: '!h-11 !w-11',
                      }"
                      :model-value="field.value"
                      :error="errorMessage"
                      :disabled="isSubmitting"
                      type="text"
                      @update:model-value="handleChange"
                      @blur="handleBlur"
                    />
                  </Field>
                </div>
              </div>
            </div>
            <div class="col-span-12">
              <div class="flex w-full flex-col gap-4 sm:flex-row">
                <div class="relative grow">
                  <Field
                    v-slot="{ field, errorMessage, handleChange, handleBlur }"
                    name="event.email"
                  >
                    <BaseInput
                      label="Email"
                      shape="curved"
                      placeholder=""
                      :classes="{
                        input: '!h-11',
                        icon: '!h-11 !w-11',
                      }"
                      :model-value="field.value"
                      :error="errorMessage"
                      :disabled="isSubmitting"
                      type="text"
                      @update:model-value="handleChange"
                      @blur="handleBlur"
                    />
                  </Field>
                </div>
                <div class="relative grow">
                  <Field
                    v-slot="{ field, errorMessage, handleChange, handleBlur }"
                    name="event.phone_number"
                  >
                    <BaseInput
                      label="Phone"
                      shape="curved"
                      placeholder=""
                      :classes="{
                        input: '!h-11',
                        icon: '!h-11 !w-11',
                      }"
                      :model-value="field.value"
                      :error="errorMessage"
                      :disabled="isSubmitting"
                      type="text"
                      @update:model-value="handleChange"
                      @blur="handleBlur"
                    />
                  </Field>
                </div>
              </div>
            </div>
            <div class="col-span-12">
              <Field
                v-slot="{ field, errorMessage, handleChange, handleBlur }"
                name="event.address"
              >
                <BaseInput
                  label="Address"
                  shape="curved"
                  placeholder=""
                  :classes="{
                    input: '!h-11',
                    icon: '!h-11 !w-11',
                  }"
                  :model-value="field.value"
                  :error="errorMessage"
                  :disabled="isSubmitting"
                  type="text"
                  @update:model-value="handleChange"
                  @blur="handleBlur"
                />
              </Field>
            </div>
            <div class="col-span-12">
              <div class="flex w-full flex-col gap-4 sm:flex-row">
                <div class="relative grow">
                  <Field
                    v-slot="{ field, errorMessage, handleChange, handleBlur }"
                    name="event.city"
                  >
                    <BaseInput
                      label="City"
                      shape="curved"
                      placeholder=""
                      :classes="{
                        input: '!h-11',
                        icon: '!h-11 !w-11',
                      }"
                      :model-value="field.value"
                      :error="errorMessage"
                      :disabled="isSubmitting"
                      type="text"
                      @update:model-value="handleChange"
                      @blur="handleBlur"
                    />
                  </Field>
                </div>
                <div class="relative grow">
                  <Field
                    v-slot="{ field, errorMessage, handleChange, handleBlur }"
                    name="event.state"
                  >
                    <BaseInput
                      label="State"
                      shape="curved"
                      placeholder=""
                      :classes="{
                        input: '!h-11',
                        icon: '!h-11 !w-11',
                      }"
                      :model-value="field.value"
                      :error="errorMessage"
                      :disabled="isSubmitting"
                      type="text"
                      @update:model-value="handleChange"
                      @blur="handleBlur"
                    />
                  </Field>
                </div>
              </div>
            </div>
            <div class="col-span-12">
              <div class="flex w-full flex-col gap-4 sm:flex-row">
                <div class="relative grow">
                  <Field
                    v-slot="{ field, errorMessage, handleChange, handleBlur }"
                    name="event.country"
                  >
                    <BaseInput
                      label="Country"
                      shape="curved"
                      placeholder=""
                      :classes="{
                        input: '!h-11',
                        icon: '!h-11 !w-11',
                      }"
                      :model-value="field.value"
                      :error="errorMessage"
                      :disabled="isSubmitting"
                      type="text"
                      @update:model-value="handleChange"
                      @blur="handleBlur"
                    />
                  </Field>
                </div>
                <div class="relative grow">
                  <Field
                    v-slot="{ field, errorMessage, handleChange, handleBlur }"
                    name="event.zip_code"
                  >
                    <BaseInput
                      label="Zip Code"
                      shape="curved"
                      placeholder=""
                      :classes="{
                        input: '!h-11',
                        icon: '!h-11 !w-11',
                      }"
                      :model-value="field.value"
                      :error="errorMessage"
                      :disabled="isSubmitting"
                      type="text"
                      @update:model-value="handleChange"
                      @blur="handleBlur"
                    />
                  </Field>
                </div>
              </div>
            </div>
          </div>
          <div class="flex items-center gap-4 pt-4">
            <BaseButton shape="curved" class="!h-12 w-full opacity-0"
              >Cancel</BaseButton
            >
            <BaseButton
              type="submit"
              shape="curved"
              color="primary"
              class="!h-12 w-full"
              >Update Profile</BaseButton
            >
          </div>
        </div>
      </div>
    </BaseCard>
  </form>
</template>
