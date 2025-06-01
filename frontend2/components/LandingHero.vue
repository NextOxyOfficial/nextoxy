<script setup>
const { y } = useNinjaWindowScroll();

const gaugePersonal = reactive(useGaugePersonal());

function useGaugePersonal() {
  const { primary } = useTailwindColors();
  const type = "radialBar";
  const height = 220;

  const options = {
    title: {
      text: undefined,
    },
    chart: {
      sparkline: {
        enabled: true,
      },
      toolbar: {
        show: false,
      },
    },
    colors: [primary.value],
    plotOptions: {
      radialBar: {
        startAngle: -90,
        endAngle: 90,
        track: {
          background: "#e7e7e7",
          strokeWidth: "97%",
          margin: 5, // margin is in pixels
          dropShadow: {
            enabled: false,
            top: 2,
            left: 0,
            color: "#999",
            opacity: 1,
            blur: 2,
          },
        },
        hollow: {
          margin: 0,
          size: "35%",
        },
        dataLabels: {
          name: {
            show: false,
          },
          value: {
            offsetY: -2,
            fontSize: "22px",
          },
        },
      },
    },
    fill: {
      type: "gradient",
      gradient: {
        shade: "light",
        shadeIntensity: 0.1,
        inverseColors: false,
        opacityFrom: 1,
        opacityTo: 1,
        stops: [0, 50, 53, 91],
      },
    },
    labels: ["Average Results"],
  };

  const series = ref([76]);

  return {
    type,
    height,
    options,
    series,
  };
}
const slider = ref(1);
setInterval(() => {
  if (slider.value === 3) {
    slider.value = 1;
  } else {
    slider.value = slider.value + 1;
  }
}, 5000);

const isLoaded = ref(false);

onMounted(() => {
  setTimeout(() => {
    isLoaded.value = true;
  }, 5000);
});
</script>

<template>
  <div
    class="dark:to-muted-900 relative overflow-hidden bg-gradient-to-b from-transparent to-white hero pb-32 pt-24 md:pt-52 min-h-screen"
  >
    <!-- <div class="gridlines absolute inset-x-0 z-10 -mt-8 py-20"></div> -->
    <!-- <div class="absolute inset-x-0 z-20 -mt-24 py-20">
      <div
        class="mt-12 grid grid-cols-2 -space-x-52 opacity-60 dark:opacity-50 2xl:mx-auto 2xl:max-w-6xl"
      ></div>
    </div> -->
    <!-- <video
      class="absolute w-full h-screen object-cover left-0 top-0 opacity-[25%]"
      src="/static/frontend/hero.webm"
      autoplay
      loop
    ></video> -->
    <div
      class="mx-auto w-full max-w-7xl xl:max-w-[1600px] px-4 relative z-10"
      v-if="slider === 1"
    >
      <div class="flex flex-col md:flex-row gap-10">
        <div class="w-full md:w-[45%] slide-in-right">
          <div class="relative z-30">
            <BaseHeading
              as="h1"
              size="4xl"
              weight="bold"
              lead="tight"
              class="text-muted-800 dark:text-white mb-12 max-w-4xl md:!text-6xl md:!leading-tight"
            >
              Go live with
              <span class="text-primary-500"> Instant Theme setup</span> no
              coding<br />skill is needed
            </BaseHeading>
            <BaseParagraph as="p" size="lg" class="mb-6 dark:text-white">
              Get Your Free Package Now!</BaseParagraph
            >
            <BaseButton
              shape="curved"
              color="primary"
              to="https://nextoxy.com/auth/signup/"
              shadow="hover"
              class="!h-12 w-44"
            >
              Register NOW!
            </BaseButton>
          </div>
        </div>
        <div class="w-full md:w-[55%] slide-in-left">
          <img
            src="/static/frontend/images/slider3.png"
            class="block md:ml-auto md:w-[88%]"
          />
        </div>
      </div>
    </div>
    <div
      class="mx-auto w-full max-w-7xl xl:max-w-[1600px] px-4 relative z-10"
      v-if="slider === 2"
    >
      <div class="flex flex-col md:flex-row gap-10">
        <div class="sm:w-1/2 slide-in-right">
          <div class="relative z-30">
            <BaseHeading
              as="h1"
              size="4xl"
              weight="bold"
              lead="tight"
              class="text-muted-800 dark:text-white mb-12 max-w-4xl md:!text-6xl md:!leading-tight"
            >
              <span class="text-primary-500"
                >Simplest & Fastest <br />
                Checkout</span
              >
              For Global <br />
              Buyers Increases <br />
              Your
              <span class="text-primary-500">Sales</span>
            </BaseHeading>
            <BaseParagraph as="p" size="lg" class="mb-6 dark:text-white">
              Get Your Free Package Now!</BaseParagraph
            >
            <BaseButton
              shape="curved"
              color="primary"
              to="https://nextoxy.com/auth/signup/"
              shadow="hover"
              class="!h-12 w-44"
            >
              Register NOW!
            </BaseButton>
          </div>
        </div>
        <div class="sm:w-1/2 slide-in-left">
          <img
            src="/static/frontend/images/slider1.png"
            class="block ml-auto"
          />
        </div>
      </div>
    </div>
    <div
      class="mx-auto w-full max-w-7xl xl:max-w-[1600px] px-4 relative z-10"
      v-if="slider === 3"
    >
      <div class="flex flex-col md:flex-row gap-10">
        <div class="w-full md:w-[45%] slide-in-right">
          <div class="relative z-30">
            <BaseHeading
              as="h1"
              size="4xl"
              weight="bold"
              lead="tight"
              class="text-muted-800 dark:text-white mb-12 max-w-4xl md:!text-6xl md:!leading-tight"
            >
              Start Your eCommerce <br />
              Journey In
              <span class="text-primary-500"
                >Less Than <br />
                5 Minutes</span
              >
            </BaseHeading>
            <BaseParagraph as="p" size="lg" class="mb-6 dark:text-white">
              Get Your Free Package Now!</BaseParagraph
            >
            <BaseButton
              shape="curved"
              color="primary"
              to="https://nextoxy.com/auth/signup/"
              shadow="hover"
              class="!h-12 w-44"
            >
              Register NOW!
            </BaseButton>
          </div>
        </div>
        <div class="w-full md:w-[55%] slide-in-left">
          <img
            src="/static/frontend/images/slider2.png"
            class="block ml-auto"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.gridlines {
  background-image: url(/static/img/illustrations/gridlines.svg);
}

.dark .gridlines {
  background-image: url(/static/img/illustrations/gridlines-dark.svg);
}

.hero {
  /* background-image: url(/static/frontend/images/slider_bg.png); */
  background-color: #a7d6ff;
  background-size: cover;
  background-position: center center;
  background-repeat: no-repeat;
}
@keyframes slideInLeft {
  from {
    transform: translateX(100%);
    opacity: 0;
  }
  to {
    transform: translateX(0);
    opacity: 1;
  }
}
@keyframes slideInRight {
  from {
    transform: translateX(-100%);
    opacity: 0;
  }
  to {
    transform: translateX(0);
    opacity: 1;
  }
}

.slide-in-left {
  animation: slideInLeft 0.5s forwards; /* 0.5s is the duration of the animation */
}
.slide-in-right {
  animation: slideInRight 0.5s forwards;
}
</style>
