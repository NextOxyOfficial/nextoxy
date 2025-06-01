<template>
  <section>
    <section v-if="youtube" class="">
      <div x-show="modalOpen" x-transition class="fixed left-0 top-0 flex h-full min-h-screen w-full items-center justify-center bg-black bg-opacity-50 px-4 py-5 z-[99999]">
        <div class="bg-slate-900 relative w-full max-w-[420px] rounded-[20px] px-7 py-9 text-center">
          <div class="mx-auto mb-5 flex h-20 w-20 items-center justify-center rounded-full bg-white bg-opacity-10 text-white" >
            <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><path fill="currentColor" d="M6 20v-2h12v2Zm-2-3q-.825 0-1.412-.587Q2 15.825 2 15V6q0-.825.588-1.412Q3.175 4 4 4h16q.825 0 1.413.588Q22 5.175 22 6v9q0 .825-.587 1.413Q20.825 17 20 17Zm6-3l5.5-3.5L10 7Z"/></svg>
          </div>
          <input class="border-primary my-1 w-full cursor-pointer rounded-md border bg-slate-800 py-3 px-5 text-base text-slate-200 transition hover:bg-opacity-90" id="url" type="text" v-model="url" placeholder="Video url" min="320" max="1024" >
          <div class="flex gap-1">
            <input class="border-primary my-1 w-full cursor-pointer rounded-md border bg-slate-800 py-3 px-5 text-base text-slate-200 transition hover:bg-opacity-90" id="width" type="number" v-model="width" placeholder="width" min="320" max="1024" >
            <input class="border-primary my-1 w-full cursor-pointer rounded-md border bg-slate-800 py-3 px-5 text-base text-slate-200 transition hover:bg-opacity-90" id="height" ype="number" v-model="height" placeholder="width" min="320" max="1024" >
          </div>
          <a @click="addVideo" class="hover:text-primary w-full inline-block rounded-lg border border-white px-[50px] py-3 text-center text-base font-medium text-white transition cursor-pointer bg-black hover:bg-slate-800"> Insert Video </a>

          <button @click="youtube = false" class="hover:text-primary absolute right-6 top-6 flex h-7 w-7 items-center justify-center rounded-full bg-white bg-opacity-10 text-white transition">
            <svg width="10" height="10" viewBox="0 0 13 13" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M6.4917 7.65579L11.106 12.2645C11.2545 12.4128 11.4715 12.5 11.6738 12.5C11.8762 12.5 12.0931 12.4128 12.2416 12.2645C12.5621 11.9445 12.5623 11.4317 12.2423 11.1114C12.2422 11.1113 12.2422 11.1113 12.2422 11.1113C12.242 11.1111 12.2418 11.1109 12.2416 11.1107L7.64539 6.50351L12.2589 1.91221L12.2595 1.91158C12.5802 1.59132 12.5802 1.07805 12.2595 0.757793C11.9393 0.437994 11.4268 0.437869 11.1064 0.757418C11.1063 0.757543 11.1062 0.757668 11.106 0.757793L6.49234 5.34931L1.89459 0.740581L1.89396 0.739942C1.57364 0.420019 1.0608 0.420019 0.740487 0.739944C0.42005 1.05999 0.419837 1.57279 0.73985 1.89309L6.4917 7.65579ZM6.4917 7.65579L1.89459 12.2639L1.89395 12.2645C1.74546 12.4128 1.52854 12.5 1.32616 12.5C1.12377 12.5 0.906853 12.4128 0.758361 12.2645L1.1117 11.9108L0.758358 12.2645C0.437984 11.9445 0.437708 11.4319 0.757539 11.1116C0.757812 11.1113 0.758086 11.111 0.75836 11.1107L5.33864 6.50287L0.740487 1.89373L6.4917 7.65579Z" class="fill-current stroke-current" />
            </svg>
          </button>
        </div>
      </div>
    </section>
    <!-- ====== Modal Section End -->
    <!-- ====== Modal Section Start -->
    <section v-if="image" class="">
      <div x-show="modalOpen" x-transition class="fixed left-0 top-0 flex h-full min-h-screen w-full items-center justify-center bg-black bg-opacity-50 px-4 py-5 z-[99999]">
        <div class="bg-slate-900 relative w-full max-w-[820px] rounded-[20px] px-7 py-9 text-center">
          <div class="mx-auto mb-5 flex h-20 w-20 items-center justify-center rounded-full bg-white bg-opacity-10 text-white" >
            <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><path fill="currentColor" d="M18 9q-.425 0-.713-.288T17 8V7h-1q-.425 0-.713-.288T15 6q0-.425.288-.713T16 5h1V4q0-.425.288-.713T18 3q.425 0 .713.288T19 4v1h1q.425 0 .713.288T21 6q0 .425-.288.713T20 7h-1v1q0 .425-.288.713T18 9ZM7 17h10q.3 0 .45-.275t-.05-.525l-2.75-3.675q-.15-.2-.4-.2t-.4.2L11.25 16L9.4 13.525q-.15-.2-.4-.2t-.4.2l-2 2.675q-.2.25-.05.525T7 17Zm-2 4q-.825 0-1.413-.588T3 19V5q0-.825.588-1.413T5 3h8q.425 0 .713.288T14 4v3q0 .425.288.713T15 8h1v1q0 .425.288.713T17 10h3q.425 0 .713.288T21 11v8q0 .825-.588 1.413T19 21H5Z"/></svg>
          </div>
          <div class="mb-14 w-full">
            <div class="flex flex-wrap bg-slate-800 text-slate-200 rounded">
              <a @click="openTab = false" :class="{'bg-slate-700':!openTab}" class="rounded-l border-primary text-primary px-4 py-2 text-sm font-medium md:text-base lg:px-6 lg:py-3 cursor-pointer"> My Media </a>
              <a @click="openTab = 2" :class="{'bg-slate-700':openTab == 2}" class="border-primary text-primary px-4 py-2 text-sm font-medium md:text-base lg:px-6 lg:py-3 cursor-pointer"> Upload </a>
              <a @click="openTab = 3" :class="{'bg-slate-700':openTab == 3}" class="border-primary text-primary px-4 py-2 text-sm font-medium md:text-base lg:px-6 lg:py-3 cursor-pointer"> Url </a>
            </div>
            {{url}}
            <div class="" v-if="openTab == false">
              <div class="flex gap-2 my-2" v-if="mediafiles && mediafiles.results">
                <span v-for="mf in mediafiles.results" @click="url = Api.baseURL + mf.file">
                  <img class="w-[130px] h-[130px] object-cover rounded cursor-pointer" :class="{'border': url == Api.baseURL + mf.file}" :src="Api.baseURL + mf.file" alt="">
                </span>
              </div>
            </div>
            <div class="" v-if="openTab == 2">
              <input class="border-primary my-1 w-full cursor-pointer rounded-md border bg-slate-800 py-3 px-5 text-base text-slate-200 transition hover:bg-opacity-90" id="upload-media-file" type="file" placeholder="Image url" min="320" max="1024" >
            </div>
            <div class="" v-if="openTab == 3">
              <input class="border-primary my-1 w-full cursor-pointer rounded-md border bg-slate-800 py-3 px-5 text-base text-slate-200 transition hover:bg-opacity-90" id="url" type="text" v-model="url" placeholder="Image url" min="320" max="1024" >
            </div>
          </div>


          <div class="flex gap-1 max-w-[400px]">
            <input class="border-primary my-1 w-full cursor-pointer rounded-md border bg-slate-800 py-3 px-5 text-base text-slate-200 transition hover:bg-opacity-90" id="width" type="number" v-model="width" placeholder="Width In Pixel" min="320" max="1024" >
            <input class="border-primary my-1 w-full cursor-pointer rounded-md border bg-slate-800 py-3 px-5 text-base text-slate-200 transition hover:bg-opacity-90" id="height" ype="number" v-model="height" placeholder="Height In Pixel" min="320" max="1024" >
          </div>
          <a @click="addImage" class="hover:text-primary mt-10 inline-block rounded-lg border border-white px-[50px] py-3 text-center text-base font-medium text-white transition cursor-pointer bg-black hover:bg-slate-800"> Insert Image </a>

          <button @click="image = false" class="hover:text-primary absolute right-6 top-6 flex h-7 w-7 items-center justify-center rounded-full bg-white bg-opacity-10 text-white transition">
            <svg width="10" height="10" viewBox="0 0 13 13" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M6.4917 7.65579L11.106 12.2645C11.2545 12.4128 11.4715 12.5 11.6738 12.5C11.8762 12.5 12.0931 12.4128 12.2416 12.2645C12.5621 11.9445 12.5623 11.4317 12.2423 11.1114C12.2422 11.1113 12.2422 11.1113 12.2422 11.1113C12.242 11.1111 12.2418 11.1109 12.2416 11.1107L7.64539 6.50351L12.2589 1.91221L12.2595 1.91158C12.5802 1.59132 12.5802 1.07805 12.2595 0.757793C11.9393 0.437994 11.4268 0.437869 11.1064 0.757418C11.1063 0.757543 11.1062 0.757668 11.106 0.757793L6.49234 5.34931L1.89459 0.740581L1.89396 0.739942C1.57364 0.420019 1.0608 0.420019 0.740487 0.739944C0.42005 1.05999 0.419837 1.57279 0.73985 1.89309L6.4917 7.65579ZM6.4917 7.65579L1.89459 12.2639L1.89395 12.2645C1.74546 12.4128 1.52854 12.5 1.32616 12.5C1.12377 12.5 0.906853 12.4128 0.758361 12.2645L1.1117 11.9108L0.758358 12.2645C0.437984 11.9445 0.437708 11.4319 0.757539 11.1116C0.757812 11.1113 0.758086 11.111 0.75836 11.1107L5.33864 6.50287L0.740487 1.89373L6.4917 7.65579Z" class="fill-current stroke-current" />
            </svg>
          </button>
        </div>
      </div>
    </section>
    <!-- ====== Modal Section End -->


    <floating-menu class="floating-menu" :editor="editor" :tippy-options="{ duration: 100, theme: 'light' }" v-if="editor">
        <button @click="editor.chain().focus().toggleHeading({ level: 1 }).run();">
            <!-- H1 -->
            <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m16 10l3-1v10M3 5v7m0 0v7m0-7h8m0-7v7m0 0v7"/></svg>
        </button>
        <button @click="editor.chain().focus().toggleHeading({ level: 2 }).run();">
          <!-- H2 -->
          <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12.5V12a3 3 0 0 1 3-3h.172a2.828 2.828 0 0 1 2 4.829L15 19h6M3 5v7m0 0v7m0-7h8m0-7v7m0 0v7"/></svg>
        </button>
        <button @click="editor.chain().focus().toggleHeading({ level: 3 }).run();">
          <!-- H3 -->
          <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 9h6l-4 4h1a3 3 0 1 1-2.83 3.998M3 5v7m0 0v7m0-7h8m0-7v7m0 0v7"/></svg>
        </button>
        <button @click="editor.chain().focus().toggleHeading({ level: 4 }).run();">
          <!-- H4 -->
          <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m18 9l-2.5 8H20m0 0h1m-1 0v-3m0 3v2M3 5v7m0 0v7m0-7h8m0-7v7m0 0v7"/></svg>
        </button>
        <button @click="editor.chain().focus().toggleHeading({ level: 5 }).run();">
          <!-- H5 -->
          <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 9h-4l-1.25 5.016a2.998 2.998 0 0 1 3.555-.717a3 3 0 1 1-3.555 4.685M3 5v7m0 0v7m0-7h8m0-7v7m0 0v7"/></svg>
        </button>
        <button @click="editor.chain().focus().toggleHeading({ level: 6 }).run();">
          <!-- H6 -->
          <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.402 14.525A2.974 2.974 0 0 0 16.5 18.6a3.01 3.01 0 0 0 4.099-1.092a2.973 2.973 0 0 0-1.099-4.075a3.01 3.01 0 0 0-4.098 1.092Zm0 0L19 8M3 5v7m0 0v7m0-7h8m0-7v7m0 0v7"/></svg>
        </button>
        <button @click="editor.chain().focus().toggleBulletList().run()" :class="{ 'is-active': editor.isActive('bulletList') }">
          <!-- List -->
          <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><path fill="currentColor" d="M6.983 19H4v-1h1.989v-.5h-.994v-1h.995V16H4v-1h2.983v4ZM21 18H9.069v-2H21v2ZM6.983 14H4v-.9L5.79 11H4v-1h2.983v.9L5.193 13h1.79v1ZM21 13H9.069v-2H21v2ZM6.486 9h-.995V6H4.5V5h1.986v4ZM21 8H9.069V6H21v2Z"/></svg>
        </button>
        <button @click="editor.chain().focus().toggleOrderedList().run()" :class="{ 'is-active': editor.isActive('bulletList') }">
          <!-- Bullet List -->
          <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><path fill="currentColor" d="M20 18H8v-2h12v2ZM6 18H4v-2h2v2Zm14-5H8v-2h12v2ZM6 13H4v-2h2v2Zm14-5H8.023V6H20v2ZM6 8H4V6h2v2Z"/></svg>
        </button>
        <button @click="editor.chain().focus().toggleCodeBlock().run()" :class="{ 'is-active': editor.isActive('codeBlock') }">
            <!-- toggleCodeBlock -->
            <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m15 7l5 5l-5 5m-6 0l-5-5l5-5"/></svg>
        </button>
        <button @click="editor.chain().focus().toggleBlockquote().run()" :class="{ 'is-active': editor.isActive('bulletList') }">
          <!-- quote -->
          <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><g fill="currentColor"><path fill-rule="evenodd" d="M20 5H4v14h16V5ZM4 3a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V5a2 2 0 0 0-2-2H4Z" clip-rule="evenodd"/><path d="M9.067 9.196h3l-2.134 5.608h-3l2.134-5.608Zm5 0h3l-2.134 5.608h-3l2.134-5.608Z"/></g></svg>
        </button>
        <button @click="editor.chain().focus().setHorizontalRule().run()">
            <!-- setHorizontalRule -->
            <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 1024 1024"><path fill="currentColor" d="M904 476H120c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h784c4.4 0 8-3.6 8-8v-56c0-4.4-3.6-8-8-8z"/></svg>
        </button>
        <button @click="youtube = true" class="tippy" data-template="youtube">
          <!-- youtube  -->
          <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><path fill="currentColor" d="M2.5 4.5h19c.84 0 1.5.65 1.5 1.5v11.5c0 .85-.66 1.5-1.5 1.5h-19c-.85 0-1.5-.65-1.5-1.5V6c0-.85.65-1.5 1.5-1.5m7.21 4V15l5.71-3.3l-5.71-3.2M17.25 21H6.65c-.3 0-.5-.2-.5-.5s.2-.5.5-.5h10.7c.3 0 .5.2.5.5s-.3.5-.6.5Z"/></svg>
        </button>
        <button @click="image = true" class="tippy" data-template="youtube">
          <!-- image  -->
          <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><path fill="currentColor" d="M5 21q-.825 0-1.413-.588T3 19V5q0-.825.588-1.413T5 3h14q.825 0 1.413.588T21 5v14q0 .825-.588 1.413T19 21H5Zm2-4h10q.3 0 .45-.275t-.05-.525l-2.75-3.675q-.15-.2-.4-.2t-.4.2L11.25 16L9.4 13.525q-.15-.2-.4-.2t-.4.2l-2 2.675q-.2.25-.05.525T7 17Zm1.5-7q.625 0 1.063-.438T10 8.5q0-.625-.438-1.063T8.5 7q-.625 0-1.063.438T7 8.5q0 .625.438 1.063T8.5 10Z"/></svg>
        </button>
    </floating-menu>
    <bubble-menu class="floating-menu" :editor="editor" :tippy-options="{ duration: 100, theme: 'light' }" v-if="editor" >        
        <template v-if="!editor.isActive('image')">
          <button @click="editor.chain().focus().toggleHeading({ level: 1 }).run();" :class="{ 'is-active': editor.isActive('heading', { level: 1 }) }">
              <!-- H1 -->
              <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m16 10l3-1v10M3 5v7m0 0v7m0-7h8m0-7v7m0 0v7"/></svg>
          </button>
          <button @click="editor.chain().focus().toggleHeading({ level: 2 }).run()" :class="{ 'is-active': editor.isActive('heading', { level: 2 }) }">
            <!-- H2 -->
            <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12.5V12a3 3 0 0 1 3-3h.172a2.828 2.828 0 0 1 2 4.829L15 19h6M3 5v7m0 0v7m0-7h8m0-7v7m0 0v7"/></svg>
          </button>
          <button @click="editor.chain().focus().toggleHeading({ level: 3 }).run()" :class="{ 'is-active': editor.isActive('heading', { level: 3 }) }">
            <!-- H3 -->
            <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 9h6l-4 4h1a3 3 0 1 1-2.83 3.998M3 5v7m0 0v7m0-7h8m0-7v7m0 0v7"/></svg>
          </button>
          <button @click="editor.chain().focus().toggleHeading({ level: 4 }).run()" :class="{ 'is-active': editor.isActive('heading', { level: 4 }) }">
            <!-- H4 -->
            <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m18 9l-2.5 8H20m0 0h1m-1 0v-3m0 3v2M3 5v7m0 0v7m0-7h8m0-7v7m0 0v7"/></svg>
          </button>
          <button @click="editor.chain().focus().toggleHeading({ level: 5 }).run()" :class="{ 'is-active': editor.isActive('heading', { level: 5 }) }">
            <!-- H5 -->
            <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 9h-4l-1.25 5.016a2.998 2.998 0 0 1 3.555-.717a3 3 0 1 1-3.555 4.685M3 5v7m0 0v7m0-7h8m0-7v7m0 0v7"/></svg>
          </button>
          <button @click="editor.chain().focus().toggleHeading({ level: 6 }).run()" :class="{ 'is-active': editor.isActive('heading', { level: 6 }) }">
            <!-- H6 -->
            <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.402 14.525A2.974 2.974 0 0 0 16.5 18.6a3.01 3.01 0 0 0 4.099-1.092a2.973 2.973 0 0 0-1.099-4.075a3.01 3.01 0 0 0-4.098 1.092Zm0 0L19 8M3 5v7m0 0v7m0-7h8m0-7v7m0 0v7"/></svg>
          </button>
          <button @click="editor.chain().focus().toggleBulletList().run()" :class="{ 'is-active': editor.isActive('bulletList') }">
            <!-- List -->
            <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><path fill="currentColor" d="M6.983 19H4v-1h1.989v-.5h-.994v-1h.995V16H4v-1h2.983v4ZM21 18H9.069v-2H21v2ZM6.983 14H4v-.9L5.79 11H4v-1h2.983v.9L5.193 13h1.79v1ZM21 13H9.069v-2H21v2ZM6.486 9h-.995V6H4.5V5h1.986v4ZM21 8H9.069V6H21v2Z"/></svg>
          </button>
          <button @click="editor.chain().focus().toggleOrderedList().run()" :class="{ 'is-active': editor.isActive('orderedList') }">
            <!-- Bullet List -->
            <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><path fill="currentColor" d="M20 18H8v-2h12v2ZM6 18H4v-2h2v2Zm14-5H8v-2h12v2ZM6 13H4v-2h2v2Zm14-5H8.023V6H20v2ZM6 8H4V6h2v2Z"/></svg>
          </button>
          <button @click="editor.chain().focus().toggleCodeBlock().run()" :class="{ 'is-active': editor.isActive('codeBlock') }">
              <!-- toggleCodeBlock -->
              <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m15 7l5 5l-5 5m-6 0l-5-5l5-5"/></svg>
          </button>
          <button @click="editor.chain().focus().toggleBlockquote().run()" :class="{ 'is-active': editor.isActive('blockquote') }">
            <!-- quote -->
            <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><g fill="currentColor"><path fill-rule="evenodd" d="M20 5H4v14h16V5ZM4 3a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V5a2 2 0 0 0-2-2H4Z" clip-rule="evenodd"/><path d="M9.067 9.196h3l-2.134 5.608h-3l2.134-5.608Zm5 0h3l-2.134 5.608h-3l2.134-5.608Z"/></g></svg>
          </button>
          <button @click="editor.chain().focus().toggleBold().run()" :class="{ 'is-active': editor.isActive('bold') }">
              <!-- bold -->
              <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 12h4.5M8 12V5h4.5a3.5 3.5 0 1 1 0 7M8 12v7h5.5a3.5 3.5 0 1 0 0-7h-1"/></svg>
          </button>
          <button @click="editor.chain().focus().toggleItalic().run()" :class="{ 'is-active': editor.isActive('italic') }">
              <!-- italic -->
              <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 19h2m0 0h2m-2 0l4-14m-2 0h2m0 0h2"/></svg>
          </button>
          <button @click="editor.chain().focus().toggleUnderline().run()" :class="{ 'is-active': editor.isActive('underline') }">
            <!-- toggleUnderline -->
            <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 19h12M8 5v6a4 4 0 0 0 8 0V5"/></svg>
          </button>
          <button @click="editor.chain().focus().toggleStrike().run()" :class="{ 'is-active': editor.isActive('strike') }">
              <!-- strike -->
              <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 1024 1024"><path fill="currentColor" d="M952 474H569.9c-10-2-20.5-4-31.6-6c-15.9-2.9-22.2-4.1-30.8-5.8c-51.3-10-82.2-20-106.8-34.2c-35.1-20.5-52.2-48.3-52.2-85.1c0-37 15.2-67.7 44-89c28.4-21 68.8-32.1 116.8-32.1c54.8 0 97.1 14.4 125.8 42.8c14.6 14.4 25.3 32.1 31.8 52.6c1.3 4.1 2.8 10 4.3 17.8c.9 4.8 5.2 8.2 9.9 8.2h72.8c5.6 0 10.1-4.6 10.1-10.1v-1c-.7-6.8-1.3-12.1-2-16c-7.3-43.5-28-81.7-59.7-110.3c-44.4-40.5-109.7-61.8-188.7-61.8c-72.3 0-137.4 18.1-183.3 50.9c-25.6 18.4-45.4 41.2-58.6 67.7c-13.5 27.1-20.3 58.4-20.3 92.9c0 29.5 5.7 54.5 17.3 76.5c8.3 15.7 19.6 29.5 34.1 42H72c-4.4 0-8 3.6-8 8v60c0 4.4 3.6 8 8 8h433.2c2.1.4 3.9.8 5.9 1.2c30.9 6.2 49.5 10.4 66.6 15.2c23 6.5 40.6 13.3 55.2 21.5c35.8 20.2 53.3 49.2 53.3 89c0 35.3-15.5 66.8-43.6 88.8c-30.5 23.9-75.6 36.4-130.5 36.4c-43.7 0-80.7-8.5-110.2-25c-29.1-16.3-49.1-39.8-59.7-69.5c-.8-2.2-1.7-5.2-2.7-9c-1.2-4.4-5.3-7.5-9.7-7.5h-79.7c-5.6 0-10.1 4.6-10.1 10.1v1c.2 2.3.4 4.2.6 5.7c6.5 48.8 30.3 88.8 70.7 118.8c47.1 34.8 113.4 53.2 191.8 53.2c84.2 0 154.8-19.8 204.2-57.3c25-18.9 44.2-42.2 57.1-69c13-27.1 19.7-57.9 19.7-91.5c0-31.8-5.8-58.4-17.8-81.4c-5.8-11.2-13.1-21.5-21.8-30.8H952c4.4 0 8-3.6 8-8v-60a8 8 0 0 0-8-7.9z"/></svg>
          </button>
          <button @click="editor.chain().focus().setTextAlign('left').run()" :class="{ 'is-active': editor.isActive({ textAlign: 'left' }) }">
              <!-- left -->
              <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 18h10M4 14h16M4 10h10M4 6h16"/></svg>
          </button>
          <button @click="editor.chain().focus().setTextAlign('center').run()" :class="{ 'is-active': editor.isActive({ textAlign: 'center' }) }">
             <!-- center -->
             <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 18H7m13-4H4m13-4H7m13-4H4"/></svg>
          </button>
          <button @click="editor.chain().focus().setTextAlign('right').run()" :class="{ 'is-active': editor.isActive({ textAlign: 'right' }) }">
              <!-- right -->
              <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 18H10m10-4H4m16-4H10m10-4H4"/></svg>
          </button>
          <button @click="editor.chain().focus().setTextAlign('justify').run()" :class="{ 'is-active': editor.isActive({ textAlign: 'justify' }) }">
              <!-- justify -->
              <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 18H4m16-4H4m16-4H4m16-4H4"/></svg>
          </button>
          <button @click="editor.chain().focus().unsetTextAlign().run()">
              <!-- unsetTextAlign -->
              <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 1024 1024"><path fill="currentColor" fill-rule="evenodd" d="M880 112c17.7 0 32 14.3 32 32v736c0 17.7-14.3 32-32 32H144c-17.7 0-32-14.3-32-32V144c0-17.7 14.3-32 32-32Zm-40 72H184v656h656V184ZM640.013 338.826c.023.007.042.018.083.059l45.02 45.019c.04.04.05.06.058.083a.118.118 0 0 1 0 .07c-.007.022-.018.041-.059.082L557.254 512l127.861 127.862a.268.268 0 0 1 .05.06l.009.023a.118.118 0 0 1 0 .07c-.007.022-.018.041-.059.082l-45.019 45.02c-.04.04-.06.05-.083.058a.118.118 0 0 1-.07 0c-.022-.007-.041-.018-.082-.059L512 557.254L384.14 685.115c-.042.041-.06.052-.084.059a.118.118 0 0 1-.07 0c-.022-.007-.041-.018-.082-.059l-45.02-45.019a.199.199 0 0 1-.058-.083a.118.118 0 0 1 0-.07c.007-.022.018-.041.059-.082L466.745 512l-127.86-127.86a.268.268 0 0 1-.05-.061l-.009-.023a.118.118 0 0 1 0-.07c.007-.022.018-.041.059-.082l45.019-45.02c.04-.04.06-.05.083-.058a.118.118 0 0 1 .07 0c.022.007.041.018.082.059L512 466.745l127.862-127.86c.04-.041.06-.052.083-.059a.118.118 0 0 1 .07 0Z"/></svg>
          </button>
          <input type="color" @input="editor.chain().focus().setColor($event.target.value).run()" :value="editor.getAttributes('textStyle').color">
          <input type="color" @input="editor.chain().focus().toggleHighlight({ color: $event.target.value }).run()" :value="editor.getAttributes('highlight').color">
          <button @click="setLink" :class="{ 'is-active': editor.isActive('link') }">
            <!-- setLink -->
            <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><path fill="currentColor" d="M10.59 13.41c.41.39.41 1.03 0 1.42c-.39.39-1.03.39-1.42 0a5.003 5.003 0 0 1 0-7.07l3.54-3.54a5.003 5.003 0 0 1 7.07 0a5.003 5.003 0 0 1 0 7.07l-1.49 1.49c.01-.82-.12-1.64-.4-2.42l.47-.48a2.982 2.982 0 0 0 0-4.24a2.982 2.982 0 0 0-4.24 0l-3.53 3.53a2.982 2.982 0 0 0 0 4.24m2.82-4.24c.39-.39 1.03-.39 1.42 0a5.003 5.003 0 0 1 0 7.07l-3.54 3.54a5.003 5.003 0 0 1-7.07 0a5.003 5.003 0 0 1 0-7.07l1.49-1.49c-.01.82.12 1.64.4 2.43l-.47.47a2.982 2.982 0 0 0 0 4.24a2.982 2.982 0 0 0 4.24 0l3.53-3.53a2.982 2.982 0 0 0 0-4.24a.973.973 0 0 1 0-1.42Z"/></svg>
          </button>
          <button @click="editor.chain().focus().unsetLink().run()" v-if="editor.isActive('link')">
            <!-- unsetLink -->
            <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><path fill="currentColor" d="M2 5.27L3.28 4L20 20.72L18.73 22l-4.83-4.83l-2.61 2.61a5.003 5.003 0 0 1-7.07 0a5.003 5.003 0 0 1 0-7.07l1.49-1.49c-.01.82.12 1.64.4 2.43l-.47.47a2.982 2.982 0 0 0 0 4.24a2.982 2.982 0 0 0 4.24 0l2.62-2.6l-1.62-1.61c-.01.24-.11.49-.29.68c-.39.39-1.03.39-1.42 0A4.973 4.973 0 0 1 7.72 11L2 5.27m10.71-1.05a5.003 5.003 0 0 1 7.07 0a5.003 5.003 0 0 1 0 7.07l-1.49 1.49c.01-.82-.12-1.64-.4-2.42l.47-.48a2.982 2.982 0 0 0 0-4.24a2.982 2.982 0 0 0-4.24 0l-3.33 3.33l-1.41-1.42l3.33-3.33m.7 4.95c.39-.39 1.03-.39 1.42 0a4.999 4.999 0 0 1 1.23 5.06l-1.78-1.77c-.05-.68-.34-1.35-.87-1.87a.973.973 0 0 1 0-1.42Z"/></svg>
          </button>
          <select name="" id="" :value="editor.getAttributes('textStyle').fontFamily" @change="editor.chain().focus().setFontFamily($event.target.value).run()">
            <option value="">No Font</option>
            <option value="Inter">Inter</option>
            <option value="Comic Sans MS, Comic Sans">Comic Sans MS</option>
            <option value="cursive">Cursive</option>
            <option value="monospace">Monospace</option>
            <option value="serif">Serif</option>
          </select>
        </template>
    </bubble-menu>
    <editor-content :editor="editor" />
  </section>
</template>

<script setup>
    // imports 
    import tippy from 'tippy.js';
    import 'tippy.js/dist/tippy.css';
    import 'tippy.js/themes/light.css';
    import StarterKit from '@tiptap/starter-kit'
    import { Editor, EditorContent, FloatingMenu, BubbleMenu } from '@tiptap/vue-3'

    import Text from '@tiptap/extension-text'
    import FontFamily from '@tiptap/extension-font-family'
    import TextAlign from '@tiptap/extension-text-align'
    import { Color } from '@tiptap/extension-color'
    import TextStyle from '@tiptap/extension-text-style'
    import Highlight from '@tiptap/extension-highlight'
    import Link from '@tiptap/extension-link'
    import Underline from '@tiptap/extension-underline'
    import Youtube from '@tiptap/extension-youtube'
    import Image from '@tiptap/extension-image'

    const editor = ref(null)
    const youtube = ref(false)
    const image = ref(false)
    const openTab = ref(false)
    const height = ref(300)
    const width = ref(300)
    const url = ref('')
    const mediafiles = ref(null)
    const Api = useApi()

    const props = defineProps({
        content: String,
        mediaUrl: String,
    })

    onMounted(() => {
        editor.value = new Editor({
        extensions: [
          StarterKit,
          TextAlign.configure({
            types: ['heading', 'paragraph'],
          }),
          Color,
          Text,
          FontFamily,
          Underline,
          TextStyle,
          Image,
          Highlight.configure({ multicolor: true }),
          Link.configure({ openOnClick: false, }),
          Youtube.configure({ controls: false, }),
        ],
        content: props.content,
        onUpdate: () =>{
          emitContent()
        }
      })
      setTimeout(() => {
        getMediaFiles()
      }, 1000);
    })
    const emit = defineEmits(['updateContent'])
    const emitContent = () => {
        emit('updateContent', editor.value.getHTML());
    }
    const setLink = () => {
        const previousUrl = editor.value.getAttributes('link').href
        const url = window.prompt('URL', previousUrl)

        // cancelled
        if (url === null) {
        return
        }

        // empty
        if (url === '') {
        editor.value
            .chain()
            .focus()
            .extendMarkRange('link')
            .unsetLink()
            .run()

        return
        }

        // update link
        editor.value
        .chain()
        .focus()
        .extendMarkRange('link')
        .setLink({ href: url })
        .run()
    }
    const addVideo = () => {
        editor.value.commands.setYoutubeVideo({
        src: url.value,
        width: Math.max(320, parseInt(width.value, 10)) || 640,
        height: Math.max(180, parseInt(height.value, 10)) || 480,
        })
        youtube.value = false
        url.value = ''
    }
    const addImage = () => {
        if(openTab.value == 2){
        var input = document.getElementById('upload-media-file')
        var file = input.files[0]
        var reader = new FileReader()
        reader.readAsDataURL(file)
        reader.onload = () => {         
            console.log(reader.result);
            const formData = []
            formData.push(reader.result)
            Api.post(props.mediaUrl, formData)
            .then((res) => {
                getMediaFiles()
            })
            .catch((err) => {
                console.log(err)
            })
            openTab.value = false;
            url.value = ''
            return;
        }


        // editor.value.chain().focus().setImage({ src: reader.result }).run()
        }else{
        editor.value.chain().focus().setImage({ src: url.value }).run()
        image.value = false
        url.value = ''
        }
    }
    const getMediaFiles = () => {
        Api.get(props.mediaUrl)
        .then((res) => {
            mediafiles.value = res.data
        })
        .catch((err) => {
            console.log(err)
        })
    }

</script>

<style scoped>
</style>


<style>
.tiptap img, .tiptap iframe{
    max-width: 100%;
    max-height: 500px;
    margin: auto;
}
.tiptap a{
    color: #007bff;
}
.tiptap.ProseMirror{
    min-height: 500px;
    padding: 5px;
    /* background: #fffffffb !important; */
    margin-bottom: 10px;
    border: none;
    outline: none;
}

.tiptap ol{
    list-style: circle !important;
    margin-left: 20px;
}
.tiptap ul{
    list-style: auto !important;
    margin-left: 20px;
}
.tiptap p{
    margin: 0px;
}
.tiptap blockquote{
    margin: 0px;
    padding: 0px;
    border-left: 3px solid #ccc;
    margin-left: 10px;
    padding-left: 10px;
}
.tiptap pre{
    margin: 0px;
    padding: 0px;
    background: #f5f5f5;
    border-radius: 5px;
    padding: 10px;
    margin-bottom: 10px;
}

.tiptap pre code{
    background: none;
    padding: 0px;
    margin: 0px;
}
.tiptap code{
    background: #f5f5f5;
    padding: 2px;
    border-radius: 5px;
    margin: 0px;
}
.tiptap hr{
  border: none;
    border-top: 1px solid #ccc;
    margin: 10px 0px;
}
.tiptap mark{
    padding: 5px;
    border-radius: 5px;
    margin: 0px;
}



</style>

<style>
.floating-menu{
    width: 100%;
    flex-wrap: wrap;
    display: flex;
    gap: 0px;
}
.floating-menu button.is-active{
    background: #cad8f1;
}
.floating-menu button{
  background-color: transparent;
    border: none;
    padding: 7px;
    margin: 0px;
    border-radius: 5px;
    cursor: pointer;
    outline: none;
    color: rgb(58, 58, 58);
    display: inline;
    border-right: none;
    border: 1px solid rgba(133, 133, 133, 0.1);
    border-radius: 0px;
}
.floating-menu input[type="color"] {
    padding: 1px;
    background-color: transparent;
    margin: 0px;
    border-radius: 0px;
    cursor: pointer;
    outline: none;
    display: inline;
    border-right: none;
    border: 1px solid rgba(133, 133, 133, 0.1);
    width: 38px;
    height: 40px;
}
.floating-menu select{
    padding: 1px;
    background-color: transparent;
    margin: 0px;
    border-radius: 0px;
    cursor: pointer;
    outline: none;
    display: inline;
    border-right: none;
    border: 1px solid rgba(133, 133, 133, 0.1);
    width: 100px;
    height: 40px;
}
.floating-menu button:hover{
    background: #7774745b;
}
.floating-menu button svg{
    width: 22px;
    height: 22px;
}
</style>