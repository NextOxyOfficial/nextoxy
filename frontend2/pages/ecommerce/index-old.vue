<script setup lang="ts">
import { toTypedSchema } from '@vee-validate/zod'
import { DatePicker } from 'v-calendar'
import { Field, useForm } from 'vee-validate'
import { z } from 'zod'
import { Calendar } from 'v-calendar'

import 'v-calendar/dist/style.css'
import '~/assets/css/vcalendar.css'

const preloader = useState('preloader')

definePageMeta({
    layout: 'dashboard'
})
const {shop, getShop}= useShop()
const Api = useApi()
// getShop()
const sparkLineOne = reactive(useSparkLineOne())
const sparkLineTwo = reactive(useSparkLineTwo())
const sparkLineThree = reactive(useSparkLineThree())
const sparkLineFour = reactive(useSparkLineFour())

const radialSalesRevenue = reactive(useRadialSalesRevenue())
const radialSmallOne = reactive(useRadialSmallOne())
const radialSmallTwo = reactive(useRadialSmallTwo())
const radialSmallThree = reactive(useRadialSmallThree())

function useSparkLineOne() {
  const { primary } = useTailwindColors()
  const height = 60
  const type = 'line'

  const options = {
    chart: {
      id: 'sparkline1',
      sparkline: {
        enabled: true,
      },
      group: 'sparklines',
    },
    grid: {
      padding: {
        top: 10,
        right: 0,
        bottom: 0,
        left: 0,
      },
    },
    stroke: {
      curve: 'smooth',
      width: [2],
    },
    markers: {
      size: 0,
    },
    yaxis: {
      min: 0,
      labels: {
        minWidth: 100,
      },
    },
    tooltip: {
      fixed: {
        enabled: true,
        position: 'right',
      },
      x: {
        show: false,
      },
    },
    colors: [primary.value],
  } as const

  const series = ref([
    {
      name: 'Sales',
      data: [2565, 6126, 4271, 5249, 2245, 4424, 1752],
    },
  ])

  return { height, type, options, series }
}

function useSparkLineTwo() {
  const { success } = useTailwindColors()
  const type = 'line'
  const height = 60

  const options = {
    chart: {
      id: 'sparkline2',
      sparkline: {
        enabled: true,
      },
      group: 'sparklines',
    },
    grid: {
      padding: {
        top: 10,
        right: 0,
        bottom: 0,
        left: 0,
      },
    },
    stroke: {
      curve: 'smooth',
      width: [2],
    },
    markers: {
      size: 0,
    },
    yaxis: {
      min: 0,
      labels: {
        minWidth: 100,
      },
    },
    tooltip: {
      fixed: {
        enabled: false,
        position: 'right',
      },
      x: {
        show: false,
      },
      y: {
        formatter: asKDollar,
      },
    },
    colors: [success.value],
  } as const

  const series = ref([
    {
      name: 'Income',
      data: [12.2, 14.5, 2.5, 47.5, 32.5, 44.5, 14.8],
    },
  ])

  return { height, type, options, series }
}

function useSparkLineThree() {
  const { info } = useTailwindColors()
  const height = 60
  const type = 'line'

  const options = {
    chart: {
      id: 'sparkline3',
      sparkline: {
        enabled: true,
      },
      group: 'sparklines',
    },
    grid: {
      padding: {
        top: 10,
        right: 0,
        bottom: 0,
        left: 0,
      },
    },
    stroke: {
      curve: 'smooth',
      width: [2],
    },
    markers: {
      size: 0,
    },
    tooltip: {
      fixed: {
        enabled: true,
        position: 'right',
      },
      x: {
        show: false,
      },
    },
    colors: [info.value],
    xaxis: {
      crosshairs: {
        width: 1,
      },
    },
    yaxis: {
      min: 0,
      labels: {
        minWidth: 100,
      },
    },
  } as const

  const series = ref([
    {
      name: 'New Orders',
      data: [4457, 4533, 7274, 3272, 5876, 3271, 4614],
    },
  ])

  return { height, type, options, series }
}

function useSparkLineFour() {
  const { danger } = useTailwindColors()
  const type = 'line'
  const height = 60

  const options = {
    chart: {
      id: 'sparkline4',
      sparkline: {
        enabled: true,
      },
      group: 'sparklines',
    },
    grid: {
      padding: {
        top: 10,
        right: 0,
        bottom: 0,
        left: 0,
      },
    },
    stroke: {
      curve: 'smooth',
      width: [2],
    },
    markers: {
      size: 0,
    },
    tooltip: {
      fixed: {
        enabled: true,
        position: 'right',
      },
      x: {
        show: false,
      },
    },
    colors: [danger.value],
    xaxis: {
      crosshairs: {
        width: 1,
      },
    },
    yaxis: {
      min: 0,
      labels: {
        minWidth: 100,
      },
    },
  } as const

  const series = ref([
    {
      name: 'Abandonned',
      data: [1412, 725, 427, 655, 145, 325, 197],
    },
  ])

  return { height, type, options, series }
}


function useRadialSalesRevenue() {
  const { primary } = useTailwindColors()
  const type = 'radialBar'
  const height = 155

  const options = {
    chart: {
      toolbar: {
        show: false,
      },
    },
    colors: [primary.value],
    plotOptions: {
      radialBar: {
        hollow: {
          size: '75%',
        },
        dataLabels: {
          show: true,
          name: {
            show: false,
            fontSize: '12px',
            fontFamily: 'Roboto, sans-serif',
            fontWeight: 400,
            offsetY: 5,
          },
          value: {
            show: true,
            fontWeight: 600,
            fontFamily: 'Roboto, sans-serif',
            fontSize: '16px',
            offsetY: 5,
          },
        },
      },
    },
    labels: ['Progress'],
  }

  const series = ref([65])

  return {
    type,
    height,
    options,
    series,
  }
}

function useRadialSmallOne() {
  const { primary } = useTailwindColors()
  const type = 'radialBar'
  const height = 100

  const options = {
    chart: {
      height: 100,
      type: 'radialBar',
      offsetY: -10,
      toolbar: {
        show: false,
      },
    },
    colors: [primary.value],
    plotOptions: {
      radialBar: {
        hollow: {
          size: '35%',
        },
        dataLabels: {
          show: false,
        },
      },
    },
    labels: [''],
  }

  const series = ref([31])

  return {
    type,
    height,
    options,
    series,
  }
}

function useRadialSmallTwo() {
  const { success } = useTailwindColors()
  const type = 'radialBar'
  const height = 100

  const options = {
    chart: {
      height: 100,
      type: 'radialBar',
      offsetY: -10,
      toolbar: {
        show: false,
      },
    },
    colors: [success.value],
    plotOptions: {
      radialBar: {
        hollow: {
          size: '35%',
        },
        dataLabels: {
          show: false,
        },
      },
    },
    labels: [''],
  }

  const series = ref([53])

  return {
    type,
    height,
    options,
    series,
  }
}

function useRadialSmallThree() {
  const { danger } = useTailwindColors()
  const type = 'radialBar'
  const height = 100

  const options = {
    chart: {
      height: 100,
      type: 'radialBar',
      offsetY: -10,
      toolbar: {
        show: false,
      },
    },
    colors: [danger.value],
    plotOptions: {
      radialBar: {
        hollow: {
          size: '35%',
        },
        dataLabels: {
          show: false,
        },
      },
    },
    labels: [''],
  }

  const series = ref([84])

  return {
    type,
    height,
    options,
    series,
  }
}


// all time 
const stats = ref([
  { id: 1, name: 'Total Products', stat: '0', href:'/ecommerce/products'},
  { id: 2, name: 'Total Customers', stat: '0',href:'/ecommerce/customers'},
  { id: 3, name: 'Total Orders', stat: '0',href:'/ecommerce/orders'},
  { id: 4, name: 'Order Value', stat: '0',href:'/ecommerce/orders'},
])
// date filtered 
const stats2 = ref([
  { id: 1, name: 'Products Added', stat: '0', },
  { id: 2, name: 'Customer Joined', stat: '0', },
  { id: 3, name: 'Order Placed', stat: '0', },
])
const stats3 = ref([
  { id: 1, name: 'Pending Order', stat: '0', },
  { id: 2, name: 'Completed Orders', stat: '0', },
  { id: 3, name: 'Cancelled Orders', stat: '0', },
])

  const recent_orders = ref('aa')
  const overviewType = ref('all')
  const fromDate = ref('')
  const toDate = ref('')
  async function getOverviewData(){
    if(overviewType.value == 'range' && !fromDate.value){
      return
    }
    if(overviewType.value == 'range' && !toDate.value){
      return
    }
    var body = {
      overviewType: overviewType.value,
      fromDate: fromDate.value,
      toDate: toDate.value
    }
    const {data} = await Api.post('/api/ecommerce/dash/overview', body)
    recent_orders.value = data.recent_orders
    stats.value[0].stat = data.stats[0].stat
    stats.value[1].stat = data.stats[1].stat
    stats.value[2].stat = data.stats[2].stat
    stats.value[3].stat = data.stats[3].stat

    stats2.value[0].stat = data.stats2[0].stat
    stats2.value[1].stat = data.stats2[1].stat
    stats2.value[2].stat = data.stats2[2].stat

    stats3.value[0].stat = data.stats3[0].stat
    stats3.value[1].stat = data.stats3[1].stat
    stats3.value[2].stat = data.stats3[2].stat
  }

const areaCustomers = ref({
  "active": false,
  "type": "bar",
  "height": 300,
  "options": {
    "chart": {
      "toolbar": {
        "show": false
      }
    },
    "colors": [
      "#8b5cf6",
      "#eb5e34",
      "#00cc00"
    ],
    "title": {
      "show": false,
      "align": "left"
    },
    "legend": {
      "show": true,
      "position": "top"
    },
    "dataLabels": {
      "enabled": false
    },
    "stroke": {
      "width": [
        0,
        0,
        0
      ],
      "curve": "smooth"
    },
    "xaxis": {
      "type": "datetime",
      "categories": [],
      "convertedCatToNumeric": false
    },
    "tooltip": {
      "x": {
        "format": "dd/MM/yy HH:mm"
      }
    }
  },
  "series": [
    {
      "name": "Total Sales",
      "data": []
    },
    {
      "name": "Pending Sales",
      "data": []
    },
    {
      "name": "Completed Sales",
      "data": []
    }
  ]
})
  getOverviewData()
    async function getChartData(){
    const {data} = await Api.get('/api/ecommerce/dash/chart')
    areaCustomers.value.options.xaxis.categories = data.labels
    areaCustomers.value.series[0].data = data.number_of_sales
    areaCustomers.value.series[1].data = data.pending_sales
    areaCustomers.value.series[2].data = data.complete_sales
    areaCustomers.value.active = true
  }
  getChartData()

  const zodSchema = z
  .object({
    event: z.object({
      startDateTime: z.date().nullable(),
      endDateTime: z.date().nullable(),
    }),
  })
  type FormInput = z.infer<typeof zodSchema>

const validationSchema = toTypedSchema(zodSchema)
const initialValues = computed<FormInput>(() => ({
  event: {
    startDateTime: null,
    endDateTime: null,
  },
}))

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
})
  const dates = ref({
    start: '',
    end: '',
  })
  const masks = ref({
    input: 'YYYY-MM-DD',
  })


// watch date change 

const filterChart = () => {
  console.log('event-create-success', values)
}
</script>

<template>
  <div>

    <div class="w-full" v-if="preloader">
      <div class="flex justify-between">
        <BaseCard shape="rounded" class="p-3 md:p-4 mb-2 max-w-[150px]" v-for="i in 4" :key="i">
          <div class="flex items-center">
            <div class="ms-3 grow space-y-2">
              <BasePlaceload class="h-3 w-[85%] rounded" />
            </div>
          </div>
        </BaseCard>
      </div>
      <div class="flex gap-1 flex-wrap">
        <BaseCard shape="rounded" class="px-4 md:px-6 py-12 mb-2 flex-1 max-w-[350px] min-w-[150px]" v-for="i in 4" :key="i">
          <div class="flex items-center">
            <BasePlaceload class="h-10 w-10 rounded-full" />

            <div class="ms-3 grow space-y-2">
              <BasePlaceload class="h-3 w-full rounded" />

              <BasePlaceload class="h-3 w-[85%] rounded" />
            </div>
          </div>
        </BaseCard>
      </div>
      <BaseCard shape="rounded" class="px-4 md:px-6 mb-2 py-12" v-for="i in 3" :key="i">
        <div class="flex items-center">
          <BasePlaceload class="h-10 w-10 rounded-full" />

          <div class="ms-3 grow space-y-2">
            <BasePlaceload class="h-3 w-full rounded" />

            <BasePlaceload class="h-3 w-[85%] rounded" />
          </div>
        </div>
      </BaseCard>
    </div>

    <span v-else>
      <!-- Header -->
      <div class="mb-2 flex flex-col justify-between md:flex-row md:items-center">
        <div
          class=" ltablet:max-w-full hidden md:flex max-w-[100%] md:max-w-[425px] flex-col items-center gap-4 text-center md:flex-row md:text-left lg:max-w-full"
        >
          <BaseAvatar src="/static/img/avatars/1.svg" size="lg" />
          <div>
            <BaseHeading as="h2" size="xl" weight="light" lead="tight" class="text-muted-800 dark:text-white">
              <span v-if="shop">Welcome back {{shop.name}}</span>
            </BaseHeading>
            <BaseParagraph>
              <span class="text-muted-500 dark:text-muted-400">
                Happy to see you again on your dashboard.
              </span>
            </BaseParagraph>
          </div>
        </div>
        <div
          class=" flex items-center justify-center gap-2 md:mt-0 md:justify-start"
        >
          <DatePicker
            v-model.range="dates"
            :masks="masks"
            :max-date="new Date()"
            mode="dateTime"
            hide-time-header
            trim-weeks
          >
            <template #default="{ inputValue, inputEvents }">
              <div class="w-full flex gap-1 max-w-[100vw] justify-center flex-wrap">
                <div class="relative grow max-w-[140px]">
                  <Field
                    v-slot="{
                      field,
                      errorMessage,
                      handleChange,
                      handleBlur,
                    }"
                    name="event.startDateTime"
                  >
                    <BaseInput
                      shape="rounded"
                      label="Start date"
                      icon="ph:calendar-blank-duotone"
                      :value="inputValue.start"
                      v-on="inputEvents.start"
                      :classes="{
                        input: '!h-11 !ps-11',
                        icon: '!h-11 !w-11',
                      }"
                      :model-value="field.value"
                      :error="errorMessage"
                      :disabled="isSubmitting"
                      type="text"
                      @update:model-value="handleChange"
                      @blur="handleBlur"
                      placeholder="Start Date"
                      autocomplete="off"
                    />
                  </Field>
                </div>
                <div class="relative grow max-w-[140px]">
                  <Field
                    v-slot="{
                      field,
                      errorMessage,
                      handleChange,
                      handleBlur,
                    }"
                    name="event.endDateTime"
                  >
                    <BaseInput
                      shape="rounded"
                      label="End date"
                      icon="ph:calendar-blank-duotone"
                      :value="inputValue.end"
                      v-on="inputEvents.end"
                      :classes="{
                        input: '!h-11 !ps-11',
                        icon: '!h-11 !w-11',
                      }"
                      :model-value="field.value"
                      :error="errorMessage"
                      :disabled="isSubmitting"
                      type="text"
                      @update:model-value="handleChange"
                      @blur="handleBlur"
                      placeholder="Select Date"
                      autocomplete="off"
                    />
                  </Field>
                </div>
                <div class="flex items-end">
                  <BaseButton @click="filterChart" color="primary" class="min-h-[43px]">Filter</BaseButton>
                </div>
              </div>
            </template>
          </DatePicker>
        </div>
      </div>
      <!-- Grid -->
      <div class="grid grid-cols-12 gap-1">
        <!-- Tile -->
        <div class="ptablet:col-span-6 col-span-12 sm:col-span-3">
          <BaseCard class="p-6">
            <div class="flex items-center justify-between">
              <BaseHeading
                as="h4"
                size="sm"
                weight="medium"
                lead="tight"
                class="text-muted-400 mb-1"
              >
                <span>Orders</span>
              </BaseHeading>
              <Icon
                name="ph:shopping-cart-duotone"
                class="text-primary-500 h-7 w-7"
              />
            </div>
            <div class="flex items-start justify-between gap-6 pt-2">
              <div class="grow">
                <span
                  class="text-muted-800 dark:text-muted-100 font-sans text-xl font-semibold"
                >
                  {{ stats[2].stat }}
                </span>
              </div>
              <div class="grow max-w-[150px]">
                <AddonApexcharts v-bind="sparkLineOne" />
              </div>
            </div>
          </BaseCard>
        </div>
        <!-- Tile -->
        <div class="ptablet:col-span-6 col-span-12 sm:col-span-3">
          <BaseCard class="p-6">
            <div class="flex items-center justify-between">
              <BaseHeading
                as="h4"
                size="sm"
                weight="medium"
                lead="tight"
                class="text-muted-400 mb-1"
              >
                <span>Sales Value</span>
              </BaseHeading>
              <Icon name="ph:money-duotone" class="text-success-500 h-7 w-7" />
            </div>
            <div class="flex items-start justify-between gap-6 pt-2">
              <div class="grow">
                <span
                  class="text-muted-800 dark:text-muted-100 font-sans text-xl font-semibold"
                >
                  ${{ stats[3].stat }}
                </span>
              </div>
              <div class="grow max-w-[150px]">
                <AddonApexcharts v-bind="sparkLineTwo" />
              </div>
            </div>
          </BaseCard>
        </div>
        <!-- Tile -->
        <div class="ptablet:col-span-6 col-span-12 sm:col-span-3 hidden md:block">
          <BaseCard class="p-6">
            <div class="flex items-center justify-between">
              <BaseHeading
                as="h4"
                size="sm"
                weight="medium"
                lead="tight"
                class="text-muted-400 mb-1"
              >
                <span>Products</span>
              </BaseHeading>
              <Icon name="ph:package-duotone" class="text-info-500 h-7 w-7" />
            </div>
            <div class="flex items-start justify-between gap-6 pt-2">
              <div class="grow">
                <span
                  class="text-muted-800 dark:text-muted-100 font-sans text-xl font-semibold"
                >
                  {{ stats[0].stat }}
                </span>
              </div>
              <div class="grow max-w-[150px]">
                <AddonApexcharts v-bind="sparkLineThree" />
              </div>
            </div>
          </BaseCard>
        </div>
        <!-- Tile -->
        <div class="ptablet:col-span-6 col-span-12 sm:col-span-3 hidden md:block">
          <BaseCard class="p-6">
            <div class="flex items-center justify-between">
              <BaseHeading
                as="h4"
                size="sm"
                weight="medium"
                lead="tight"
                class="text-muted-400 mb-1"
              >
                <span>Customers</span>
              </BaseHeading>
              <Icon name="ph:timer-duotone" class="text-danger-500 h-7 w-7" />
            </div>
            <div class="flex items-start justify-between gap-6 pt-2">
              <div class="grow">
                <span
                  class="text-muted-800 dark:text-muted-100 font-sans text-xl font-semibold"
                >
                  {{ stats[1].stat }}
                </span>
              </div>
              <div class="grow max-w-[150px]">
                <AddonApexcharts v-bind="sparkLineFour" />
              </div>
            </div>
          </BaseCard>
        </div>
        <!-- Chart -->
        <div class="relative col-span-12 md:col-span-7">
          <BaseCard class="p-0">
            <div class="mb-2 flex items-center justify-between p-4">
              <BaseHeading
                as="h3"
                size="md"
                weight="semibold"
                lead="tight"
                class="text-muted-800 dark:text-white"
              >
                <span>Last 7 Days Order</span>
              </BaseHeading>
              <NuxtLink
                to="#"
                class="bg-muted-100 hover:bg-muted-200 dark:bg-muted-700 dark:hover:bg-muted-900 text-primary-500 rounded-lg px-4 py-2 font-sans text-sm font-medium underline-offset-4 transition-colors duration-300 hover:underline"
              >
                Details
              </NuxtLink>
            </div>
            <div class="flex gap-8 hidden">
              <div>
                <span class="text-muted-400 font-sans text-xs">This month</span>
                <p class="text-primary-500 font-sans text-lg font-medium">
                  $75,689
                </p>
              </div>
              <div>
                <span class="text-muted-400 font-sans text-xs">Last month</span>
                <p
                  class="text-muted-800 dark:text-muted-100 font-sans text-lg font-medium"
                >
                  $59,724
                </p>
              </div>
              <div>
                <span class="text-muted-400 font-sans text-xs">Average</span>
                <p
                  class="text-muted-800 dark:text-muted-100 font-sans text-lg font-medium"
                >
                  $66,561
                </p>
              </div>
            </div>
            <span v-if="areaCustomers.active">
              <AddonApexcharts v-bind="areaCustomers" />
            </span>
          </BaseCard>
        </div>
        <!-- Column -->
        <div class="relative col-span-12 md:col-span-5">
          <div class="flex h-full flex-col gap-1">
            <!-- Charts -->
            <BaseCard class="flex-1 p-6">
              <div class="mb-6 flex items-center justify-between">
                <BaseHeading
                  as="h3"
                  size="md"
                  weight="semibold"
                  lead="tight"
                  class="text-muted-800 dark:text-white"
                >
                  <span>Order Stats</span>
                </BaseHeading>
              </div>
              <div class="flex justify-between gap-2">
                <div class="flex flex-1 flex-col gap-2 text-center">
                  <AddonApexcharts v-bind="radialSmallOne" />
                  <div class="-mt-6">
                    <BaseHeading
                      as="h5"
                      size="md"
                      weight="semibold"
                      lead="tight"
                      class="text-muted-800 dark:text-white"
                    >
                      <span>{{stats3[0].stat}}</span>
                    </BaseHeading>
                    <BaseParagraph size="xs">
                      <span class="text-muted-400">Pending Orders</span>
                    </BaseParagraph>
                  </div>
                </div>
                <div class="flex flex-1 flex-col gap-2 text-center">
                  <AddonApexcharts v-bind="radialSmallThree" />
                  <div class="-mt-6">
                    <BaseHeading
                      as="h5"
                      size="md"
                      weight="semibold"
                      lead="tight"
                      class="text-muted-800 dark:text-white"
                    >
                      <span>{{stats3[2].stat}}</span>
                    </BaseHeading>
                    <BaseParagraph size="xs">
                      <span class="text-muted-400">Cancelled Orders</span>
                    </BaseParagraph>
                  </div>
                </div>
                <div class="flex flex-1 flex-col gap-2 text-center">
                  <AddonApexcharts v-bind="radialSmallTwo" />
                  <div class="-mt-6">
                    <BaseHeading
                      as="h5"
                      size="md"
                      weight="semibold"
                      lead="tight"
                      class="text-muted-800 dark:text-white"
                    >
                      <span>{{stats3[1].stat}}</span>
                    </BaseHeading>
                    <BaseParagraph size="xs">
                      <span class="text-muted-400">Completed Orders</span>
                    </BaseParagraph>
                  </div>
                </div>
              </div>
            </BaseCard>
            <!-- Chart -->
            <BaseCard class="flex-1 px-6 py-2 flex flex-col justify-center">
              <div class="flex items-center justify-center">
                <div class="flex-1" v-if="recent_orders">
                  <BaseHeading
                    as="h3"
                    size="md"
                    weight="semibold"
                    lead="tight"
                    class="text-muted-800 mb-4 dark:text-white flex justify-between items-center"
                  >
                    <span>Recent Orders</span>
                    <nuxt-link class="text-xs text-blue-500" to="/ecommerce/orders">View All</nuxt-link>
                  </BaseHeading>
                  <BaseHeading
                    as="p"
                    size="xs"
                    weight="light"
                    lead="tight"
                    class="text-muted-600 mb-1 dark:text-white flex-1 flex gap-0"
                    v-for="order in recent_orders"
                    :key="order.id"
                  >
                    <span class="flex-1 border p-2 border-muted-400/20">{{order.created_at}}</span>
                    <span class="flex-1 border p-2 border-x-0 max-w-[100px] text-center border-muted-400/20">USD ${{order.total}}</span>
                    <span class="flex-1 max-w-[80px] text-right  border p-2 border-muted-400/20">{{order.status}}</span>
                  </BaseHeading>
                </div>
          
              </div>
            </BaseCard>
          </div>
        </div>
        <!-- Column -->
      </div>
    </span>
      <EcommerceSetup :state="true" />
  </div>
</template>
