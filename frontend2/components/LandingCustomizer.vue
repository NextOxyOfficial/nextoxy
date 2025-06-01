<script setup lang="ts">
const selectedStyle = ref("classic");
const toggled = ref(false);

watch(selectedStyle, (value) => {
  if (value) {
    toggled.value = true;
    const timeout = setTimeout(() => {
      toggled.value = false;
      clearTimeout(timeout);
    }, 1750);
  }
});
const list = ["classic", "corporate", "smart", "creative"];
let currentIndex = 0;

const changeStyle = () => {
  selectedStyle.value = list[currentIndex];
  currentIndex = (currentIndex + 1) % list.length;
};

const interval = setInterval(changeStyle, 2000);

// Clear the interval when the component is unmounted to avoid memory leaks
onUnmounted(() => {
  clearInterval(interval);
});
</script>

<template>
  <div class="dark:bg-muted-900 overflow-hidden bg-white">
    <div class="mx-auto w-full max-w-7xl px-4">
      <div
        class="flex w-full flex-col-reverse items-center justify-between gap-6 sm:flex-row"
        aria-hidden="true"
      ></div>
    </div>
  </div>
</template>

<style scoped>
.gridlines {
  background-image: url(/img/illustrations/gridlines.svg);
}

.dark .gridlines {
  background-image: url(/img/illustrations/gridlines-predark.svg);
}

.shuriken-1 {
  animation: shurikenFirst 0.75s 0s forwards;
}

.shuriken-2 {
  top: 190px;
  transform: translateX(-20px);
  animation: shurikenSecond 0.5s 0s forwards;
}
.shuriken-3 {
  top: 110px;
  transform: translateX(-20px) rotate(20deg);
  animation: shurikenThird 1.75s 0s forwards;
}
@keyframes shurikenFirst {
  0% {
    transform: translateX(0);
    opacity: 0;
  }
  10% {
    opacity: 1;
  }
  100% {
    transform: translateX(600px);
    opacity: 0;
  }
}

@keyframes shurikenSecond {
  0% {
    transform: translateX(0);
    opacity: 0;
  }
  10% {
    opacity: 1;
  }
  100% {
    transform: translateX(500px);
    opacity: 0;
  }
}

@keyframes shurikenThird {
  0% {
    transform: translateX(0);
    opacity: 0;
  }
  10% {
    opacity: 1;
  }
  100% {
    transform: translateX(400px);
    opacity: 0;
  }
}
</style>
