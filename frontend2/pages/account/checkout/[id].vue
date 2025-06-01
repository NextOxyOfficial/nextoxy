<script setup lang="ts">
definePageMeta({
    layout: 'dashboard'
})
const Api = useApi()
const {user} = useAuth()
const cardInfo = ref({
  billing_first_name: '',
  billing_last_name: '',
  billing_email: '',
  billing_phone_number: '',
  billing_address: '',
  billing_city: '',
  billing_state: '',
  billing_country: '',
})

const selectedMethod = ref('stripe')
const termsApproval = ref(false)

const route = useRoute()
const invoiceId = route.params.id
const inv = ref('')
async function getInv() {
    const res = await Api.get('/api/account/invoices?id='+invoiceId)
    inv.value = res.data
    selectedMethod.value = inv.value.payment_method
}
getInv()

const payBtn = ref('Pay Now')

function makePayment(){
  var url = '/api/account/stripe/pay/'+invoiceId
  if (inv.value.payment_method == 'sp'){
    url = '/api/account/sp/pay/'+invoiceId
  }
  if (inv.value.payment_method == 'paypal'){
    url = '/api/account/paypal/pay/'+invoiceId
  }
  Api.get(url)
  .then(response => {
    console.log(response.data)
    // check if "url" data, then redirect to url 
    if('url' in response.data){
        window.location.href = response.data.url
    }

  })
}

const payError = ref('')
async function payNow() {
  if(!termsApproval.value){
    payError.value = 'You must agree to our terms & conditions'
    return;
  }
    payBtn.value = 'Saving Data...'
    var data = {
        billing_first_name: user.value.billing_first_name,
        billing_last_name: user.value.billing_last_name,
        billing_email: user.value.billing_email,
        billing_phone_number: user.value.billing_phone_number,
        billing_address: user.value.billing_address,
        billing_city: user.value.billing_city,
        billing_state: user.value.billing_state,
        billing_country: user.value.billing_country,
        method: selectedMethod.value,
    }
    const res = await Api.post('/api/account/invoices?id='+invoiceId,data)
    inv.value = res.data
    selectedMethod.value = inv.value.payment_method
    console.log(inv.value);
    payBtn.value = 'Processing...'
    makePayment()
}
</script>

<template>
  <form class="grid w-full gap-8 md:grid-cols-2 lg:grid-cols-3" v-if="inv && user">
    <div class="lg:col-span-2">
      <BaseCard>
        <div
          class="border-muted-200 dark:border-muted-700 flex items-center justify-between gap-4 border-b px-8 py-5"
        >
          <div>
            <BaseHeading as="h3" size="sm" weight="medium">
              Payment method
            </BaseHeading>
            <BaseText size="xs" class="text-muted-400"
              >Select a payment method</BaseText
            >
          </div>
          <div class="ms-auto">
            <BaseButtonAction @click.prevent="$router.back()">
              <Icon name="lucide:arrow-left" class="h-3 w-3" />
              <span>Cancel</span>
            </BaseButtonAction>
          </div>
        </div>
        <form class="border-muted-200 dark:border-muted-700 flex items-center justify-between gap-4 border-b px-8 py-5">
            <div class="grid grid-cols-12 gap-4 w-full">
                <div class="col-span-12 md:col-span-6">
                    <BaseInput
                        v-model="user.billing_first_name"
                        label="First name"
                    />
                </div>
                <div class="col-span-12 md:col-span-6">
                    <BaseInput
                        v-model="user.billing_last_name"
                        label="Last name"

                    />
                </div>
                <div class="col-span-12 md:col-span-6">
                    <BaseInput
                        v-model="user.billing_email"
                        label="Email"

                    />
                </div>
                <div class="col-span-12 md:col-span-6">
                    <BaseInput
                        v-model="user.billing_phone_number"
                        label="Phone number"

                    />
                </div>
                <div class="col-span-12 md:col-span-6">
                    <BaseInput
                        v-model="user.billing_address"
                        label="Address"

                    />
                </div>
                <div class="col-span-12 md:col-span-6">
                    <BaseInput
                        v-model="user.billing_city"
                        label="City"

                    />
                </div>
                <div class="col-span-12 md:col-span-6">
                    <BaseInput
                        v-model="user.billing_state"
                        label="State"

                    />
                </div>
                <div class="col-span-12 md:col-span-6">
                    <BaseInput
                        v-model="user.billing_country"
                        label="Country"

                    />
                </div>

            </div>
        </form>
        <div>
          <div
            role="button"
            class="flex cursor-pointer items-center px-8 py-5"
            :class="
              selectedMethod === 'paypal'
                ? 'bg-muted-50 dark:bg-muted-900/60'
                : ''
            "
            @click="selectedMethod = 'paypal'"
          >
            <div
              class="dark:border-muted-800 h-4 w-4 rounded-full border-2 border-white ring-2 transition-colors"
              :class="
                selectedMethod === 'paypal'
                  ? 'bg-primary-600 ring-primary-600'
                  : 'ring-muted-400'
              "
            ></div>
            <label class="ms-4 text-sm font-medium cursor-pointer">PayPal</label>
          </div>
          <div
            v-if="selectedMethod === 'paypal'"
            class="flex flex-wrap items-center justify-between gap-4 p-8 pt-4"
          >
            <div class="max-w-xs">
              <BaseHeading as="h3" size="md" weight="medium" class="mb-2">
                Pay with PayPal
              </BaseHeading>
              <BaseParagraph size="sm" class="text-muted-400">
                After clicking on "start subscription", you will be redirected
                to PayPal website to complete your purchase securely.
              </BaseParagraph>
            </div>
            <div class="grow">
              <BaseCard
                shape="curved"
                elevated
                class="mx-auto flex max-w-[280px] items-center justify-center px-8 py-16"
              >
                <Icon name="logos:paypal" class="h-12 w-12" />
              </BaseCard>
            </div>
          </div>
        </div>
        <div class="border-muted-200 dark:border-muted-700 border-t">
          <div
            role="button"
            class="flex cursor-pointer items-center px-8 py-5"
            :class="
              selectedMethod === 'stripe' ? 'bg-muted-50 dark:bg-muted-900/60' : ''
            "
            @click="selectedMethod = 'stripe'"
          >
            <div
              class="dark:border-muted-800 h-4 w-4 rounded-full border-2 border-white ring-2"
              :class="
                selectedMethod === 'stripe'
                  ? 'bg-primary-600 ring-primary-600'
                  : 'ring-muted-400'
              "
            ></div>
            <label class="ms-4 text-sm font-medium flex w-full gap-3 cursor-pointer">
                <p>Debit/Credit Card - Worldwide</p>
                <svg viewBox="0 0 60 25" xmlns="http://www.w3.org/2000/svg" height="20" class="UserLogo variant-- "><title>Stripe logo</title><path fill="var(--userLogoColor, #0A2540)" d="M59.64 14.28h-8.06c.19 1.93 1.6 2.55 3.2 2.55 1.64 0 2.96-.37 4.05-.95v3.32a8.33 8.33 0 0 1-4.56 1.1c-4.01 0-6.83-2.5-6.83-7.48 0-4.19 2.39-7.52 6.3-7.52 3.92 0 5.96 3.28 5.96 7.5 0 .4-.04 1.26-.06 1.48zm-5.92-5.62c-1.03 0-2.17.73-2.17 2.58h4.25c0-1.85-1.07-2.58-2.08-2.58zM40.95 20.3c-1.44 0-2.32-.6-2.9-1.04l-.02 4.63-4.12.87V5.57h3.76l.08 1.02a4.7 4.7 0 0 1 3.23-1.29c2.9 0 5.62 2.6 5.62 7.4 0 5.23-2.7 7.6-5.65 7.6zM40 8.95c-.95 0-1.54.34-1.97.81l.02 6.12c.4.44.98.78 1.95.78 1.52 0 2.54-1.65 2.54-3.87 0-2.15-1.04-3.84-2.54-3.84zM28.24 5.57h4.13v14.44h-4.13V5.57zm0-4.7L32.37 0v3.36l-4.13.88V.88zm-4.32 9.35v9.79H19.8V5.57h3.7l.12 1.22c1-1.77 3.07-1.41 3.62-1.22v3.79c-.52-.17-2.29-.43-3.32.86zm-8.55 4.72c0 2.43 2.6 1.68 3.12 1.46v3.36c-.55.3-1.54.54-2.89.54a4.15 4.15 0 0 1-4.27-4.24l.01-13.17 4.02-.86v3.54h3.14V9.1h-3.13v5.85zm-4.91.7c0 2.97-2.31 4.66-5.73 4.66a11.2 11.2 0 0 1-4.46-.93v-3.93c1.38.75 3.1 1.31 4.46 1.31.92 0 1.53-.24 1.53-1C6.26 13.77 0 14.51 0 9.95 0 7.04 2.28 5.3 5.62 5.3c1.36 0 2.72.2 4.09.75v3.88a9.23 9.23 0 0 0-4.1-1.06c-.86 0-1.44.25-1.44.9 0 1.85 6.29.97 6.29 5.88z" fill-rule="evenodd"></path></svg>
            </label>
          </div>
          <div
            v-if="selectedMethod === 'stripe'"
            class="grid grid-cols-1 md:grid-cols-2 gap-4 p-8 pt-4"
          >
            <div class="flex items-center">
              <div class="max-w-xs">
                <BaseHeading as="h3" size="md" weight="medium" class="mb-2">
                    Pay with Debit/Credit card
                </BaseHeading>
                <BaseParagraph size="sm" class="text-muted-400">
                    Millions of companies of all sizes use Stripe online and in person to astripeept payments, send payouts, automate financial processes, and ultimately grow revenue.
                </BaseParagraph>
                </div>
            </div>
            <div class="mt-6">
              <DemoCreditCardReal
                :name="cardInfo.name"
                :number="cardInfo.number"
                :expiry-month="cardInfo.expiryMonth"
                :expiry-year="cardInfo.expiryYear"
                :cvc="cardInfo.cvc"
              />
            </div>
          </div>
        </div>
        <div class="border-muted-200 dark:border-muted-700 border-t">
          <div
            role="button"
            class="flex cursor-pointer items-center px-8 py-5"
            :class="
              selectedMethod === 'sp' ? 'bg-muted-50 dark:bg-muted-900/60' : ''
            "
            @click="selectedMethod = 'sp'"
          >
            <div
              class="dark:border-muted-800 h-4 w-4 rounded-full border-2 border-white ring-2"
              :class="
                selectedMethod === 'sp'
                  ? 'bg-primary-600 ring-primary-600'
                  : 'ring-muted-400'
              "
            ></div>
            <label class="ms-4 text-sm font-medium flex w-full gap-3 items-center cursor-pointer">
                <p>Mobile Banking/Debit/Credit Card - BD</p>
                <img class="h-6" src="/static/frontend/images/sp-logo.png" alt="" srcset="">
            </label>
          </div>
          <div
            v-if="selectedMethod === 'sp'"
            class="grid grid-cols-1 md:grid-cols-2 gap-4 p-8 pt-4"
          >
            <div class="flex items-center">
              <div class="max-w-xs">
                <BaseHeading as="h3" size="md" weight="medium" class="mb-2">
                    Pay with Mobile Banking Debit/Credit card
                </BaseHeading>
                <BaseParagraph size="sm" class="text-muted-400">
                  Experience seamless transactions with ShurjoPay, your trusted payment method. Pay effortlessly using mobile banking or debit/credit cards."
                </BaseParagraph>
                </div>
            </div>
            <div class="mt-6">
              <DemoCreditCardReal
                :name="cardInfo.name"
                :number="cardInfo.number"
                :expiry-month="cardInfo.expiryMonth"
                :expiry-year="cardInfo.expiryYear"
                :cvc="cardInfo.cvc"
              />
            </div>
          </div>
        </div>
      </BaseCard>
    </div>
    <div>
      <BaseCard class="pb-6">
        <div class="border-muted-200 dark:border-muted-700 border-b px-8 py-5">
          <BaseHeading as="h3" size="sm" weight="medium">
            Order Summary
          </BaseHeading>
          <BaseText size="xs" class="text-muted-400"
            >Check your order details</BaseText
          >
        </div>
        <div class="mt-4 px-8 pb-1">
          <div class="flex items-end justify-between">
            <BaseHeading as="h3" size="sm" weight="medium" lead="none">
              Order
            </BaseHeading>
            <BaseText size="sm" class="text-muted-800 dark:text-muted-100">
              <span class="font-base uppercase">{{inv.note}}</span>
            </BaseText>
          </div>
        </div>

        <div
          class="border-muted-200 dark:border-muted-700 mt-4 border-t px-8 pt-5"
        >
          <div class="flex items-end justify-between">
            <BaseHeading as="h3" size="sm" weight="medium" lead="none">
              Amount To Pay (USD)
            </BaseHeading>
            <BaseText size="md" class="text-muted-800 dark:text-muted-100">
              <span class="font-semibold">${{inv.amount}}</span>
            </BaseText>
          </div>
        </div>
        <div class="my-4 flex items-start gap-2 px-8 text-sm pt-4">
          <BaseCheckbox
            v-model="termsApproval"
            color="primary"
            shape="full"
            :classes="{
              label: 'relative top-0.5 text-xs',
            }"
          />
          <p class="w-full max-w-md -mt-1">
            Please agree to the 
            <a target="_blank" href="/terms-of-service" class="underline text-primary-500 hover:no">Terms of Service</a>,
            <a target="_blank" href="/privacy-policy" class="underline text-primary-500 hover:no">Privacy Policy</a> &
            <a target="_blank" href="/refund-policy" class="underline text-primary-500 hover:no">Refund Policy</a>.
          </p>
        </div>
        <p class="my-2 text-rose-500 px-8" v-if="payError">{{payError}}</p>
        <div class="flex flex-col px-8 pt-4">
          <BaseButton @click="payNow" color="primary" class="!h-12 w-full" v-if="payBtn == 'Pay Now'">{{payBtn}}</BaseButton>
          <BaseButton color="primary" class="!h-12 w-full flex gap-2" v-else>
            <Icon  name="svg-spinners:90-ring-with-bg" class="h-4 w-4" />
            {{payBtn}}
          </BaseButton>
        </div>
      </BaseCard>
    </div>
  </form>
</template>
