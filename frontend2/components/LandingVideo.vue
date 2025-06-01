<template>
  <section class="bg-[#9c9b9b]/10 mt-0 py-16 px-2 md:px-4">
    <div class="max-w-7xl mx-auto">
      <div
        class="mx-auto place-self-center lg:col-span-7 max-w-[780px] z-10 text-center"
      >
        <h1
          class="mb-4 text-2xl font-semibold tracking-tight leading-tight md:text-5xl text-muted-700 dark:text-muted-300"
        >
          The Modern Community Platform
          <span class="text-primary-500">For Businesses</span>.
        </h1>
        <p
          class="mb-6 text-sm md:text-lg lg:mb-8 text-muted-700 dark:text-muted-300 text-center max-w-2xl mx-auto"
        >
          Our platform ensures that every order, payment, and inventory update
          occurs seamlessly, fostering trust at every touch-point.
        </p>
      </div>
      <div class="relative mt-0 video-wrapper max-w-4xl mx-auto h-[400px]">
        <!-- <img
          class="w-36 absolute left-[-10%] md:left-28 top-[-10%] md:top-20 z-0 rounded-2xl border border-slate-400/10 p-[3px] shadow"
          src="/static/frontend/landing/2.jpg"
          alt="mockup"
        />
        <img
          class="hidden md:block w-44 absolute right-5 top-24 z-0 rounded-2xl border border-slate-400/10 p-[3px] shadow"
          src="/static/frontend/landing/1.jpg"
          alt="mockup"
        />
        <img
          class="w-28 absolute right-[-10%] md:right-24 bottom-[-10%] md:bottom-20 z-0 rounded-2xl border border-slate-400/10 p-[3px] shadow"
          src="/static/frontend/landing/3.webp"
          alt="mockup"
        />
        <img
          class="hidden md:block w-32 absolute left-10 bottom-20 z-0 rounded-2xl border border-slate-400/10 p-[3px] shadow"
          src="/static/frontend/landing/4.jpeg"
          alt="mockup"
        /> -->
        <iframe
          class="mx-auto"
          src="https://www.youtube.com/embed/0JjEsw5pKJA?si=cC9w4Cn9EfUrqnPS"
          title="YouTube video player"
          frameborder="0"
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
          referrerpolicy="strict-origin-when-cross-origin"
          allowfullscreen
        ></iframe>
      </div>
    </div>
  </section>
</template>

<script setup></script>

<style scoped>
/* .center-img:hover img {
  filter: grayscale(0.5);
  opacity: 0.5;
  background: white;
  cursor: pointer;
}
.center-img .play {
  transition: all 0.2s;
  border: 1px solid rgb(185, 185, 185);
  height: 50px;
  width: 50px;
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
}
.center-img:hover .play {
  height: 60px;
  width: 60px;
  transition: all 0.2s;
  transform-origin: 33px;
} */

.video-wrapper {
  float: none;
  clear: both;
  width: 100%;
  position: relative;
  padding-bottom: 38.25%;
  padding-top: 25px;
  height: 0;
}
.video-wrapper iframe {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}
@media (max-width: 768px) {
  .video-wrapper {
    padding-bottom: 56.25%;
  }
}
</style>
