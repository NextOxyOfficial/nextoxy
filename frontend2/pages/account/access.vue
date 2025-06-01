<script setup lang="ts">
definePageMeta({
    layout: 'dashboard',
})

const route = useRoute()
const router = useRouter()
const page = computed(() => parseInt((route.query.page as string) ?? '1'))

const filter = ref('')
const perPage = ref(12)

watch([filter, perPage], () => {
  router.push({
    query: {
      page: undefined,
    },
  })
})

const query = computed(() => {
  return {
    filter: filter.value,
    perPage: perPage.value,
    page: page.value,
  }
})

const data = {
  "total": 15,
  "data": [
    {
      "id": "1",
      "slug": "delivery-app-project",
      "name": "Emplyee One",
      "dueDate": "August 2020",
      "updated": "3m ago",
      "image": "/img/apps/1.jpg",
      "completed": 75,
      "recent": false,
      "category": "UI/UX Design",
      "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quid iudicant sensus? Primum quid tu dicis breve? Etiam beatissimum? Ne discipulum abducam, times.",
      "meta": {
        "sprintPerWeek": 2,
        "monthDuration": 3,
        "budgetType": "Fixed"
      },
      "owner": {
        "id": 7,
        "avatar": "/img/avatars/3.svg",
        "badge": "/img/stacks/reactjs.svg",
        "role": "Frontend Developer",
        "bio": "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod.",
        "name": "Clarke G.",
        "text": "CG"
      },
      "team": [
        {
          "id": 27,
          "src": "/img/avatars/24.svg",
          "badge": "/img/stacks/illustrator.svg",
          "role": "UI/UX Designer",
          "bio": "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod.",
          "tooltip": "Carmen E.",
          "data-nui-tooltip": "Carmen E.",
          "text": "CE"
        },
        {
          "id": 15,
          "src": "/img/avatars/15.svg",
          "badge": "/img/stacks/js.svg",
          "role": "Fullstack Developer",
          "bio": "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod.",
          "tooltip": "Josh C.",
          "data-nui-tooltip": "Josh C.",
          "text": "JC"
        },
        {
          "id": 12,
          "src": "/img/avatars/12.svg",
          "badge": "/img/stacks/csharp.svg",
          "role": "Backend Developer",
          "bio": "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod.",
          "tooltip": "Marjory L.",
          "data-nui-tooltip": "Marjory L.",
          "text": "ML"
        }
      ],
      "files": [
        {
          "id": 0,
          "name": "company-ux-guide.pdf",
          "icon": "/img/icons/files/pdf.svg",
          "size": "4.7MB",
          "version": "1.5.2",
          "uploaded": "2 weeks ago",
          "author": {
            "name": "Hermann M.",
            "picture": "/img/avatars/16.svg"
          }
        },
        {
          "id": 1,
          "name": "tech-summit-expenses.xlsx",
          "icon": "/img/icons/files/sheet.svg",
          "size": "34KB",
          "version": "1.1.3",
          "uploaded": "3 days ago",
          "author": {
            "name": "Clarissa M.",
            "picture": "/img/avatars/5.svg"
          }
        },
        {
          "id": 2,
          "name": "project-outline.docx",
          "icon": "/img/icons/files/doc-2.svg",
          "size": "77KB",
          "version": "1.0.0",
          "uploaded": "5 days ago",
          "author": {
            "name": "Clark D.",
            "picture": "/img/avatars/3.svg"
          }
        },
        {
          "id": 3,
          "name": "ux-presentation.pptx",
          "icon": "/img/icons/files/ppt.svg",
          "size": "2.3MB",
          "version": "1.0.0",
          "uploaded": "2 weeks ago",
          "author": {
            "name": "Terry S.",
            "picture": "/img/avatars/11.svg"
          }
        },
        {
          "id": 4,
          "name": "website-homepage-redesign.ai",
          "icon": "/img/icons/files/ai.svg",
          "size": "4.8MB",
          "version": "1.0.0",
          "uploaded": "2 weeks ago",
          "author": {
            "name": "Lana E.",
            "picture": "/img/avatars/4.svg"
          }
        },
        {
          "id": 5,
          "name": "interns-ux-rampup.docx",
          "icon": "/img/icons/files/doc-2.svg",
          "size": "1.8MB",
          "version": "1.2.0",
          "uploaded": "3 days ago",
          "author": {
            "name": "Howard L.",
            "picture": "/img/avatars/20.svg"
          }
        }
      ],
      "tools": [
        {
          "name": "Sketch",
          "description": "Design Software",
          "icon": "/img/stacks/sketch.svg"
        },
        {
          "name": "Illustrator",
          "description": "Design Software",
          "icon": "/img/stacks/illustrator.svg"
        },
        {
          "name": "Photoshop",
          "description": "Design Software",
          "icon": "/img/stacks/photoshop.svg"
        }
      ],
      "stacks": [
        {
          "name": "Html5",
          "description": "Design Software",
          "icon": "/img/stacks/html5.svg"
        },
        {
          "name": "Javascript",
          "description": "Programming Language",
          "icon": "/img/stacks/js.svg"
        },
        {
          "name": "Vue",
          "description": "Design Software",
          "icon": "/img/stacks/vuejs.svg"
        }
      ],
      }]}
</script>

<template>
  <div>
    <TairoContentWrapper>
      <template #left>
        <BaseInput
          v-model="filter"
          icon="lucide:search"
          shape="curved"
          placeholder="Filter projects..."
          :classes="{
            wrapper: 'w-full sm:w-auto',
          }"
        />
      </template>
      <template #right>
        <BaseButton shape="curved" class="w-full sm:w-32">Settings</BaseButton>
        <BaseButton shape="curved" color="primary" class="w-full sm:w-32">
          <Icon name="lucide:plus" class="h-4 w-4" />
          <span>Create</span>
        </BaseButton>
      </template>
      <div>
        <div v-if="!pending && data?.data.length === 0">
          <BasePlaceholderPage
            title="No matching results"
            subtitle="Looks like we couldn't find any matching results for your search terms. Try other search terms."
          >
            <template #image>
              <img
                class="block dark:hidden"
                src="/img/illustrations/placeholders/flat/placeholder-search-7.svg"
                alt="Placeholder image"
              />
              <img
                class="hidden dark:block"
                src="/img/illustrations/placeholders/flat/placeholder-search-7-dark.svg"
                alt="Placeholder image"
              />
            </template>
          </BasePlaceholderPage>
        </div>
        <div v-else>
          <div
            class="ltablet:grid-cols-3 grid w-full gap-4 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4"
          >
            <TransitionGroup
              enter-active-class="transform-gpu"
              enter-from-class="opacity-0 -translate-x-full"
              enter-to-class="opacity-100 translate-x-0"
              leave-active-class="absolute transform-gpu"
              leave-from-class="opacity-100 translate-x-0"
              leave-to-class="opacity-0 -translate-x-full"
            >
              <BaseCard
                v-for="item in data?.data"
                :key="item.id"
                shape="curved"
                class="p-6"
              >
                <div class="mb-3 flex items-center justify-center">
                  <BaseAvatar
                    :src="item.owner.avatar"
                    :badge-src="item.image"
                    shape="curved"
                    size="lg"
                    :data-nui-tooltip="item.owner.name"
                    class="bg-muted-500/20 text-muted-500"
                  />
                </div>
                <div class="my-4 flex flex-col items-center justify-between">
                  <div class="text-center" :data-nui-tooltip="item.name">
                    <h4
                      class="text-muted-800 dark:text-muted-100 line-clamp-1 font-sans text-base font-medium"
                    >
                      {{ item.name }}
                    </h4>
                    <div
                      class="text-muted-400 flex items-center justify-center gap-1"
                    >
                      <Icon name="ph:calendar-blank-duotone" class="h-4 w-4" />
                      <p class="font-sans text-sm">
                        {{ item.dueDate }}
                      </p>
                    </div>
                  </div>
                  <div class="my-4">
                    <BaseAvatarGroup
                      size="xs"
                      :limit="2"
                      :avatars="item.team"
                    />
                  </div>
                </div>
                <div class="flex items-center gap-2">
                  <BaseButton shape="curved" class="w-full">Admin</BaseButton>
                  <BaseButton shape="curved" class="w-full">
                    Manage
                  </BaseButton>
                </div>
              </BaseCard>
            </TransitionGroup>
          </div>
          <div class="mt-6">
            <BasePagination
              :total-items="data?.total ?? 0"
              :item-per-page="perPage"
              :current-page="page"
              shape="curved"
            />
          </div>
        </div>
      </div>
    </TairoContentWrapper>
  </div>
</template>
