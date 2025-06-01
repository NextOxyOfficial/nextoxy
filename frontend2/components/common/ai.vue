<template>
    <section class="fixed bottom-2 right-2 z-[998]" :class="{'expanded':expand}">
      <!-- ====== Chat Box Section Start -->
      <section class="bg-gray-2 py-2 animate__animated animate__bounceInRight" v-if="chatView">
        <div class="mx-auto md:container">
          <div class="area border-stroke mx-auto max-w-[97vw] w-[530px] h-[650px] rounded-[10px] border bg-slate-100 shadow-2xl flex flex-col">
            <div class="border-stroke flex items-center justify-between border-b p-2 px-4 bg-white">
              <div class="flex items-center flex-1">
                <div class="relative mr-4 h-[56px] w-full max-w-[56px] rounded-full">
                  <img src="https://nextoxy.com/media/plugins/robotxt.png" alt="avatar" class="h-full w-full rounded-full object-cover object-center" />
                  <span class="bg-success absolute bottom-[2px] right-0 inline-block h-[14px] w-[14px] rounded-full border-2 border-white"></span>
                </div>
                <div>
                  <h5 class="text-black font-bold">OxyBot</h5>
                  <p class="text-body-color text-lime-600 text-sm">Online</p>
                  <p class="text-body-color text-sm">Ask me anything about everything!</p>
                </div>
              </div>
              <div>
                <div class="relative flex items-center">
                  <a @click="expand = !expand" class="text-body-color cursor-pointer" v-if="!expand">
                    <svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9 9L4 4m0 0v4m0-4h4m7 5l5-5m0 0v4m0-4h-4M9 15l-5 5m0 0v-4m0 4h4m7-5l5 5m0 0v-4m0 4h-4"/></svg>
                  </a>
                  <a @click="expand = !expand" class="text-body-color cursor-pointer" v-else>
                    <svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 9h4V5M3 3l6 6m-4 6h4v4m-6 2l6-6m10-6h-4V5m0 4l6-6m-2 12h-4v4m0-4l6 6"/></svg>
                  </a>
                  <a @click="chatView = !chatView" class="text-yellow-900 cursor-pointer mr-2">
                    <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" viewBox="0 0 24 24"><path fill="currentColor" d="M18.3 5.71a.996.996 0 0 0-1.41 0L12 10.59L7.11 5.7A.996.996 0 1 0 5.7 7.11L10.59 12L5.7 16.89a.996.996 0 1 0 1.41 1.41L12 13.41l4.89 4.89a.996.996 0 1 0 1.41-1.41L13.41 12l4.89-4.89c.38-.38.38-1.02 0-1.4z"/></svg>
                  </a>
                  <div @click.outside="openDropDown = false" class="hidden shadow-card absolute right-0 top-full z-40 w-[200px] space-y-1 rounded bg-white p-2">
                    <a class="text-body-color hover:bg-gray-2 w-full rounded px-3 py-2 text-left text-sm">Edit</a>
                    <a class="text-body-color hover:bg-gray-2 w-full rounded px-3 py-2 text-left text-sm">Delete</a>
                  </div>
                </div>
              </div>
            </div>
            <div class="chat-list1 px-[30px] max-h-[540px] flex-1 flex justify-between flex-col">
              <div class="chat-list2 flex-1 max-h-[440px] overflow-y-scroll py-1 no-scrollbar" id="chat-box">
                  <template v-for="chat in chats">
                      <div class="chat w-full max-w-[270px]" v-if="chat.type == 'response'">
                          <div class="relative">
                          <div class="relative mb-1 ml-4 rounded-[10px] rounded-bl-none bg-[#EBECF2] px-4 py-[10px]">
                              <span class="absolute -left-3 bottom-0 text-[#EBECF2]">
                              <svg width="13" height="13" viewBox="0 0 13 13" fill="none" xmlns="http://www.w3.org/2000/svg">
                                  <path d="M0 13H13V0L0 13Z" fill="currentColor" />
                              </svg>
                              </span>
                              <p class="text-body-color text-base">{{ chat.message }}</p>
                          </div>
                          <p class="text-body-color ml-5 text-sm">18:03</p>
                          </div>
                      </div>
      
                      <div class="chat ml-auto w-full max-w-[270px]" v-if="chat.type == 'prompt'">
                          <div class="relative">
                          <div class="bg-green-400 relative mb-1 mr-4 rounded-[10px] rounded-br-none px-4 py-[10px]">
                              <span class="text-green-400 absolute -right-3 bottom-0">
                              <svg width="13" height="13" viewBox="0 0 13 13" fill="none" xmlns="http://www.w3.org/2000/svg">
                                  <path d="M9.53674e-07 -5.68248e-07L3.85426e-07 13L13 13L9.53674e-07 -5.68248e-07Z" fill="currentColor" />
                              </svg>
                              </span>
                              <p class="text-base text-white">{{ chat.message }}</p>
                          </div>
                          <p class="text-body-color ml-5 flex items-center justify-end text-right text-sm">
                              18:03
                              <span class="text-green-400 inline-block pl-1">
                              <svg width="24" height="14" viewBox="0 0 24 14" fill="none" xmlns="http://www.w3.org/2000/svg">
                                  <path fill-rule="evenodd" clip-rule="evenodd" d="M12.0791 3.08687C12.307 3.31468 12.307 3.68402 12.0791 3.91183L5.66248 10.3285C5.43467 10.5563 5.06533 10.5563 4.83752 10.3285L1.92085 7.41183C1.69305 7.18402 1.69305 6.81468 1.92085 6.58687C2.14866 6.35906 2.51801 6.35906 2.74581 6.58687L5.25 9.09106L11.2542 3.08687C11.482 2.85906 11.8513 2.85906 12.0791 3.08687Z" fill="currentColor" />
                                  <path fill-rule="evenodd" clip-rule="evenodd" d="M22.0791 3.08687C22.307 3.31468 22.307 3.68402 22.0791 3.91183L15.6625 10.3285C15.4347 10.5563 15.0653 10.5563 14.8375 10.3285L11.9209 7.41183C11.693 7.18402 11.693 6.81468 11.9209 6.58687C12.1487 6.35906 12.518 6.35906 12.7458 6.58687L15.25 9.09106L21.2542 3.08687C21.482 2.85906 21.8513 2.85906 22.0791 3.08687Z" fill="currentColor" />
                              </svg>
                              </span>
                          </p>
                          </div>
                      </div>
                  </template>
              </div>

              <!-- send area  -->
              <div class="relative">
                <!-- indicator -->
                <div class="absolute left-0 -top-[30px] w-full text-sm text-slate-500 flex justify-center items-center gap-2" v-if="busy">
                  <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24"><circle cx="4" cy="12" r="3" fill="currentColor"><animate id="svgSpinners3DotsScale0" attributeName="r" begin="0;svgSpinners3DotsScale1.end-0.25s" dur="0.75s" values="3;.2;3"/></circle><circle cx="12" cy="12" r="3" fill="currentColor"><animate attributeName="r" begin="svgSpinners3DotsScale0.end-0.6s" dur="0.75s" values="3;.2;3"/></circle><circle cx="20" cy="12" r="3" fill="currentColor"><animate id="svgSpinners3DotsScale1" attributeName="r" begin="svgSpinners3DotsScale0.end-0.45s" dur="0.75s" values="3;.2;3"/></circle></svg>
                  <small>{{ text }}</small>
                </div>
                <input @keydown.enter="send" type="text" v-model="newPrompt.message" placeholder="Type something here..." class="border placeholder-body-color shadow-chat-box  h-[58px] w-full rounded-[10px] bg-white pl-[60px] pr-[100px] text-base text-black outline-none" />
                <a class="absolute left-6 top-1/2 -translate-y-1/2">
                  <svg width="18" height="18" viewBox="0 0 18 18" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path fill-rule="evenodd" clip-rule="evenodd" d="M6.87866 0.878664C7.44126 0.316065 8.20431 0 8.99995 0C9.79558 0 10.5586 0.316065 11.1212 0.878664C11.6838 1.44126 11.9999 2.20431 11.9999 2.99995V8.99984C11.9999 9.79548 11.6838 10.5585 11.1212 11.1211C10.5586 11.6837 9.79558 11.9998 8.99995 11.9998C8.20431 11.9998 7.44126 11.6837 6.87866 11.1211C6.31606 10.5585 6 9.79548 6 8.99984V2.99995C6 2.20431 6.31606 1.44126 6.87866 0.878664ZM8.99995 1.49997C8.60213 1.49997 8.2206 1.65801 7.93931 1.93931C7.65801 2.2206 7.49997 2.60213 7.49997 2.99995V8.99984C7.49997 9.39766 7.65801 9.77918 7.93931 10.0605C8.2206 10.3418 8.60213 10.4998 8.99995 10.4998C9.39777 10.4998 9.77929 10.3418 10.0606 10.0605C10.3419 9.77918 10.4999 9.39766 10.4999 8.99984V2.99995C10.4999 2.60213 10.3419 2.2206 10.0606 1.93931C9.77929 1.65801 9.39776 1.49997 8.99995 1.49997Z" fill="#AAAAAA" />
                    <path fill-rule="evenodd" clip-rule="evenodd" d="M3.74999 6.75C4.16419 6.75 4.49997 7.08578 4.49997 7.49999V8.99996C4.49997 10.1934 4.97407 11.338 5.81797 12.1819C6.66187 13.0258 7.80644 13.4999 8.99989 13.4999C10.1933 13.4999 11.3379 13.0258 12.1818 12.1819C13.0257 11.338 13.4998 10.1934 13.4998 8.99996V7.49999C13.4998 7.08578 13.8356 6.75 14.2498 6.75C14.664 6.75 14.9998 7.08578 14.9998 7.49999V8.99996C14.9998 10.5912 14.3677 12.1173 13.2425 13.2425C12.1173 14.3677 10.5912 14.9999 8.99989 14.9999C7.40862 14.9999 5.88253 14.3677 4.75733 13.2425C3.63213 12.1173 3 10.5912 3 8.99996V7.49999C3 7.08578 3.33578 6.75 3.74999 6.75Z" fill="#AAAAAA" />
                    <path fill-rule="evenodd" clip-rule="evenodd" d="M8.99974 13.5C9.41395 13.5 9.74973 13.8358 9.74973 14.25V17.2499C9.74973 17.6641 9.41395 17.9999 8.99974 17.9999C8.58554 17.9999 8.24976 17.6641 8.24976 17.2499V14.25C8.24976 13.8358 8.58554 13.5 8.99974 13.5Z" fill="#AAAAAA" />
                    <path fill-rule="evenodd" clip-rule="evenodd" d="M5.25 17.25C5.25 16.8358 5.58578 16.5 5.99999 16.5H11.9999C12.4141 16.5 12.7499 16.8358 12.7499 17.25C12.7499 17.6642 12.4141 18 11.9999 18H5.99999C5.58578 18 5.25 17.6642 5.25 17.25Z" fill="#AAAAAA" />
                  </svg>
                </a>
                <div class="absolute right-4 top-1/2 inline-flex -translate-y-1/2 items-center justify-end space-x-4 sm:right-6">
                  <a>
                    <svg width="18" height="18" viewBox="0 0 18 18" fill="none" xmlns="http://www.w3.org/2000/svg">
                      <path fill-rule="evenodd" clip-rule="evenodd" d="M11.8343 1.79099C11.2371 1.79099 10.6644 2.02821 10.2421 2.45048L3.34977 9.34286C2.64605 10.0466 2.25071 11.001 2.25071 11.9962C2.25071 12.9914 2.64605 13.9459 3.34977 14.6496C4.05349 15.3533 5.00793 15.7487 6.00314 15.7487C6.99835 15.7487 7.9528 15.3533 8.65651 14.6496L15.5489 7.75723C15.8418 7.46434 16.3166 7.46434 16.6095 7.75723C16.9024 8.05011 16.9024 8.52498 16.6095 8.81787L9.71716 15.7102C8.73214 16.6953 7.39617 17.2486 6.00314 17.2486C4.61012 17.2486 3.27414 16.6953 2.28913 15.7102C1.30411 14.7252 0.750732 13.3893 0.750732 11.9962C0.750732 10.6032 1.30411 9.26723 2.28913 8.28222L9.18151 1.38983C9.88507 0.686273 10.8393 0.291016 11.8343 0.291016C12.8293 0.291016 13.7835 0.686272 14.4871 1.38983C15.1906 2.0934 15.5859 3.04763 15.5859 4.04262C15.5859 5.03761 15.1906 5.99184 14.4871 6.6954L7.58719 13.5878C7.16509 14.0099 6.59259 14.247 5.99564 14.247C5.39869 14.247 4.8262 14.0099 4.40409 13.5878C3.98198 13.1657 3.74485 12.5932 3.74485 11.9962C3.74485 11.3993 3.98198 10.8268 4.40409 10.4047L10.7718 4.04448C11.0648 3.75176 11.5397 3.75204 11.8324 4.0451C12.1251 4.33816 12.1249 4.81303 11.8318 5.10574L5.46473 11.4653C5.32412 11.6061 5.24482 11.7972 5.24482 11.9962C5.24482 12.1954 5.32393 12.3863 5.46473 12.5271C5.60554 12.6679 5.79651 12.7471 5.99564 12.7471C6.19477 12.7471 6.38575 12.6679 6.52655 12.5271L13.4264 5.63476C13.8485 5.21253 14.0859 4.63965 14.0859 4.04262C14.0859 3.44545 13.8487 2.87274 13.4264 2.45048C13.0042 2.02821 12.4315 1.79099 11.8343 1.79099Z" fill="#AAAAAA" />
                    </svg>
                  </a>
                  <button @click="send" class="bg-green-400 flex h-9 w-9 items-center justify-center rounded-md hover:bg-opacity-90">
                    <svg width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg">
                      <g clip-path="url(#clip0_2992_698)">
                        <path fill-rule="evenodd" clip-rule="evenodd" d="M15.1969 0.803654C15.4898 1.09655 15.4898 1.57142 15.1969 1.86431L7.86358 9.19765C7.57069 9.49054 7.09582 9.49054 6.80292 9.19765C6.51003 8.90476 6.51003 8.42988 6.80292 8.13699L14.1363 0.803654C14.4292 0.510761 14.904 0.510761 15.1969 0.803654Z" fill="white" />
                        <path fill-rule="evenodd" clip-rule="evenodd" d="M15.1969 0.803675C15.4006 1.0074 15.4697 1.30983 15.3745 1.58177L10.7078 14.9151C10.6062 15.2054 10.3378 15.4042 10.0305 15.4167C9.72324 15.4292 9.43946 15.253 9.31456 14.9719L6.76505 9.23554L1.02865 6.68603C0.747641 6.56114 0.571344 6.27736 0.583879 5.9701C0.596415 5.66284 0.795243 5.39437 1.08549 5.29278L14.4188 0.626112C14.6908 0.530932 14.9932 0.599947 15.1969 0.803675ZM3.36656 6.08363L7.63786 7.98198C7.80753 8.05739 7.9432 8.19306 8.01861 8.36273L9.91697 12.634L13.4441 2.55648L3.36656 6.08363Z" fill="white" />
                      </g>
                      <defs>
                        <clipPath id="clip0_2992_698">
                          <rect width="16" height="16" fill="white" />
                        </clipPath>
                      </defs>
                    </svg>
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
      <!-- ====== Chat Box Section End -->
      <div class="flex justify-end items-center gap-3 z-[999]">
        <span class="hidden font-bold text-right text-indigo-500 text-lg" style="text-shadow: 0px 0px 2px white;">
          Heyyy! I'm Your <br>
          <span class="text-slate-900">Virtual AI Assistant</span>
        </span>
        <span class="bg-white rounded-full shadow-2xl cursor-pointer"  @click="chatView = !chatView">
          <img src="https://nextoxy.com/media/plugins/robotxt.png" alt="avatar" class="h-20 w-20 p-4 object-cover object-center transition-all" />
        </span>
      </div>
    </section>
</template>

<script setup>
const Api = useApi()
const chats = ref([])
const chatView = ref(false)
const expand = ref(false)
const newPrompt = ref({
    'type': 'prompt',
    'message': '',
})
const busy = ref(false)

async function send(){
    busy.value = true
    chats.value.push(JSON.parse(JSON.stringify(newPrompt.value)))
    setTimeout(() => {
        const chatBox = document.getElementById('chat-box')
        chatBox.scrollTop = chatBox.scrollHeight
    }, 100)
    let prompt = JSON.stringify(newPrompt.value.message)
    newPrompt.value.message = ''
    restartWaitingMessage()
    const response = await Api.get('/api/office/ai/?prompt='+prompt)
    busy.value = false
    chats.value.push({
        'type': 'response',
        'message': response.data
    })
    setTimeout(() => {
        const chatBox = document.getElementById('chat-box')
        chatBox.scrollTop = chatBox.scrollHeight
    }, 100)
}

// response indicator 
const textList = [
  "Please wait while I'm thinking",
  "I found something",
  "Almost done",
  "Taking a bit longer as I've found some more nice ideas",
  "Friend, How about you visit NextOxy features while I'm writing?",
  "Oh, My response is long"
]
const text = ref(textList[0])
const index = ref(0)
const interval = ref(null)
const start = () => {
  interval.value = setInterval(() => {
    index.value++
    if (index.value === textList.length) {
      index.value = 0
    }
    text.value = textList[index.value]
  }, 4000)
}
const stop = () => {
  clearInterval(interval.value)
}
function restartWaitingMessage(){
  index.value = 0
  stop()
  start()
}





</script>

<style scoped>
.no-scrollbar::-webkit-scrollbar {
    display: none;
  }
  .expanded{
    width: 100vw;
    left: 10px;
    right: 10px;
  }
  .expanded .area{
    width: 100%;
    height: 700px;
    left: 0;
    right: 0;
  }
  .expanded .chat-list1{
    max-height: 600px;
  }
  .expanded .chat-list2{
    max-height: 100vh;
  }
  .expanded .chat{
    max-width: 600px;
  }
</style>