<script setup lang="ts">
import { toTypedSchema } from "@vee-validate/zod";
import { Field, useForm } from "vee-validate";
import { z } from "zod";
const { login, jwtLogin, logout, user, isAuthenticated } = useAuth();
const Api = useApi();

definePageMeta({
  title: "Signup",
  preview: {
    title: "Signup 2",
    description: "For authentication and sign up",
    categories: ["layouts", "authentication"],
    src: "/img/screens/auth-signup-2.png",
    srcDark: "/img/screens/auth-signup-2-dark.png",
    order: 101,
  },
  layout: "landing",
});

const VALIDATION_TEXT = {
  EMAIL_REQUIRED: "A valid email is required",
  PASSWORD_LENGTH: "Password must be at least 8 characters",
  PASSWORD_CONTAINS_EMAIL: "Password cannot contain your email",
  PASSWORD_MATCH: "Passwords do not match",
  TERMS_REQUIRED: "You must agree to the terms and conditions",
};

// This is the Zod schema for the form input
// It's used to define the shape that the form data will have
const zodSchema = z
  .object({
    email: z.string().email(VALIDATION_TEXT.EMAIL_REQUIRED),
    password: z.string().min(8, VALIDATION_TEXT.PASSWORD_LENGTH),
    confirmPassword: z.string(),
    terms: z.boolean(),
  })
  .superRefine((data, ctx) => {
    // This is a custom validation function that will be called
    // before the form is submitted
    if (data.password.includes(data.email)) {
      ctx.addIssue({
        code: z.ZodIssueCode.custom,
        message: VALIDATION_TEXT.PASSWORD_CONTAINS_EMAIL,
        path: ["password"],
      });
    }
    if (data.password !== data.confirmPassword) {
      ctx.addIssue({
        code: z.ZodIssueCode.custom,
        message: VALIDATION_TEXT.PASSWORD_MATCH,
        path: ["confirmPassword"],
      });
    }
    if (!data.terms) {
      ctx.addIssue({
        code: z.ZodIssueCode.custom,
        message: VALIDATION_TEXT.TERMS_REQUIRED,
        path: ["terms"],
      });
    }
  });

// Zod has a great infer method that will
// infer the shape of the schema into a TypeScript type
type FormInput = z.infer<typeof zodSchema>;

const validationSchema = toTypedSchema(zodSchema);
const initialValues = computed<FormInput>(() => ({
  email: "",
  password: "",
  confirmPassword: "",
  terms: false,
}));

function getCookie(name) {
  var nameEQ = name + "=";
  var ca = document.cookie.split(";");
  for (var i = 0; i < ca.length; i++) {
    var c = ca[i];
    while (c.charAt(0) == " ") c = c.substring(1, c.length);
    if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length, c.length);
  }
  return null;
}

const { handleSubmit, isSubmitting, setErrors } = useForm({
  validationSchema,
  initialValues,
});

const router = useRouter();
const toaster = useToaster();

// This is where you would send the form data to the server
const onSubmit = handleSubmit(async (values) => {
  // here you have access to the validated form values
  console.log("auth-success", values);

  const res = await Api.post("/api/auth/register/", {
    email: values.email,
    password: values.password,
    confirm_password: values.confirmPassword,
    refer: getCookie("refer"),
    error: "",
  });
  console.log(res);
  if (res.data == 200) {
    console.log("success");
    loginUser(values);
  } else {
    setErrors({ email: res.data });
  }
});
async function loginUser(values) {
  const res = await login(values.email, values.password);
  if (res) {
    console.log("login success");
    navigateTo("/account");
  }
}
</script>

<template>
  <div
    class="bg-muted-100 dark:bg-muted-900 relative w-full overflow-hidden mt-28"
  >
    <div class="flex w-full items-center justify-center">
      <div class="relative mx-auto w-full max-w-lg">
        <!--Form-->
        <BaseCard
          shape="curved"
          elevated
          class="py-6 px-2 me-auto ms-auto my-14 w-full"
        >
          <form
            method="POST"
            action=""
            @submit.prevent="onSubmit"
            class="me-auto ms-auto my-4 w-full max-w-md"
            novalidate
          >
            <div class="text-center">
              <BaseHeading as="h2" size="3xl" weight="medium">
                Welcome to NextOxy
              </BaseHeading>
              <BaseParagraph size="sm" class="text-muted-400 mb-6">
                Let's start by creating you account
              </BaseParagraph>
            </div>
            <div class="px-8 py-4">
              <div class="mb-4 space-y-4">
                <Field
                  v-slot="{ field, errorMessage, handleChange, handleBlur }"
                  name="email"
                >
                  <BaseInput
                    :model-value="field.value"
                    :error="errorMessage"
                    :disabled="isSubmitting"
                    type="email"
                    label="Email address"
                    placeholder="example@example.com"
                    autocomplete="email"
                    :classes="{
                      input: 'h-12',
                    }"
                    @update:model-value="handleChange"
                    @blur="handleBlur"
                  />
                </Field>

                <Field
                  v-slot="{ field, errorMessage, handleChange, handleBlur }"
                  name="password"
                >
                  <BaseInput
                    :model-value="field.value"
                    :error="errorMessage"
                    :disabled="isSubmitting"
                    type="password"
                    label="Password"
                    placeholder="••••••••••"
                    autocomplete="new-password"
                    :classes="{
                      input: 'h-12',
                    }"
                    @update:model-value="handleChange"
                    @blur="handleBlur"
                  />
                </Field>

                <Field
                  v-slot="{ field, errorMessage, handleChange, handleBlur }"
                  name="confirmPassword"
                >
                  <BaseInput
                    :model-value="field.value"
                    :error="errorMessage"
                    :disabled="isSubmitting"
                    type="password"
                    label="Confirm Password"
                    placeholder="••••••••••"
                    :classes="{
                      input: 'h-12',
                    }"
                    @update:model-value="handleChange"
                    @blur="handleBlur"
                  />
                </Field>
              </div>
              <div class="mb-6">
                <div class="mt-6 flex items-center justify-between">
                  <Field
                    v-slot="{ field, errorMessage, handleChange, handleBlur }"
                    name="terms"
                  >
                    <BaseCheckbox
                      :model-value="field.value"
                      :disabled="isSubmitting"
                      :error="errorMessage"
                      shape="rounded"
                      color="primary"
                      @update:model-value="handleChange"
                      @blur="handleBlur"
                    >
                      <span>
                        <span>I accept the</span>
                        <NuxtLink
                          to="/terms-of-service"
                          class="text-primary-500 hover:underline focus:underline"
                        >
                          Terms of Service
                        </NuxtLink>
                      </span>
                    </BaseCheckbox>
                  </Field>
                </div>
              </div>
              <div class="mb-6">
                <BaseButton
                  :disabled="isSubmitting"
                  :loading="isSubmitting"
                  type="submit"
                  color="primary"
                  class="!h-12 w-full"
                >
                  Sign Up
                </BaseButton>
              </div>
              <div class="mb-6 grid gap-0 sm:grid-cols-3 hidden">
                <hr
                  class="border-muted-200 dark:border-muted-700 mt-3 hidden border-t sm:block"
                />
                <span
                  class="bg-muted-100 dark:bg-muted-900 text-muted-400 relative top-0.5 text-center font-sans text-sm"
                >
                  Or continue with
                </span>
                <hr
                  class="border-muted-200 dark:border-muted-700 mt-3 hidden border-t sm:block"
                />
              </div>
              <!--Social signup-->
              <div class="grid grid-cols-3 gap-2 hidden">
                <button
                  type="button"
                  class="bg-muted-200 dark:bg-muted-700 dark:hover:bg-muted-600 text-muted-600 dark:text-muted-400 nui-focus relative inline-flex w-full items-center justify-center rounded px-0 py-3 text-center text-sm font-semibold shadow-sm transition-all duration-300 hover:bg-white"
                >
                  <Icon name="fa6-brands:google" class="h-5 w-5" />
                </button>
                <button
                  type="button"
                  class="bg-muted-200 dark:bg-muted-700 dark:hover:bg-muted-600 text-muted-600 dark:text-muted-400 nui-focus relative inline-flex w-full items-center justify-center rounded px-0 py-3 text-center text-sm font-semibold shadow-sm transition-all duration-300 hover:bg-white"
                >
                  <Icon name="fa6-brands:twitter" class="h-5 w-5" />
                </button>
                <button
                  type="button"
                  class="bg-muted-200 dark:bg-muted-700 dark:hover:bg-muted-600 text-muted-600 dark:text-muted-400 nui-focus relative inline-flex w-full items-center justify-center rounded px-0 py-3 text-center text-sm font-semibold shadow-sm transition-all duration-300 hover:bg-white"
                >
                  <Icon name="fa6-brands:linkedin-in" class="h-5 w-5" />
                </button>
              </div>

              <!--No account link-->
              <p
                class="text-muted-400 mt-4 flex justify-between font-sans text-sm leading-5"
              >
                <span>Already have an account?</span>
                <NuxtLink
                  to="/auth/login"
                  class="text-primary-600 hover:text-primary-500 font-medium underline-offset-4 transition duration-150 ease-in-out hover:underline"
                >
                  Sign in
                </NuxtLink>
              </p>
            </div>
          </form>
        </BaseCard>
      </div>
    </div>
  </div>
</template>
