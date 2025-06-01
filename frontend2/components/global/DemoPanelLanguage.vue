<script setup>
const { close } = usePanels()
    useHead({
        script: [
            { src: 'https://translate.google.com/translate_a/element.js?cb=google_translate_element', body: true, defer: false },
        ]
    })
    function initGoogle() {
      new google.translate.TranslateElement({pageLanguage: 'en'}, 'google_translate_element');
      clearInterval(googleInterval);
    }
    let googleInterval = setInterval(() => {
        if (typeof google != 'undefined') {
            initGoogle();
        }
    }, 1000);
</script>

<template>
  <div
    class="border-muted-200 dark:border-muted-700 dark:bg-muted-800 border bg-white"
  >
    <div class="flex h-16 w-full items-center justify-between px-10">
      <h2
        class="font-heading text-muted-700 text-lg font-semibold dark:text-white"
      >
        Select language
      </h2>
      <button
        type="button"
        class="text-muted-400 hover:bg-muted-100 hover:text-muted-600 dark:hover:bg-muted-700 flex h-10 w-10 items-center justify-center rounded-full transition-colors duration-300 dark:hover:text-white"
        @click="close"
      >
        <Icon name="feather:chevron-right" class="h-6 w-6" />
      </button>
    </div>

    <div class="relative h-[calc(100%_-_64px)] w-full px-10">
      <div class="w-full py-6">
         <div  class="translate-google pl-4 bg-" id="google_translate_element"></div>
      </div>

      <div>
        <img
          src="/static/img/illustrations/translation.svg"
          class="mx-auto w-full max-w-[280px] dark:hidden"
          alt="illustration"
        />
        <img
          src="/static/img/illustrations/translation-dark.svg"
          class="mx-auto hidden w-full max-w-[280px] dark:block"
          alt="illustration"
        />
      </div>
    </div>
  </div>
</template>


<style>
#google_translate_element select{
  width: 100%;
  padding: 5px;
  border: 2px solid #80808061;
  border-radius: 3px;
  background: white;
}
#google_translate_element {
    height: 38px;
    overflow: hidden;
    width: 100%;
}
iframe.skiptranslate{
  display: none !important;
}
body{
  top: 0px !important;
}
</style>