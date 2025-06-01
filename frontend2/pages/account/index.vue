<script setup>
	import { debounce } from "lodash";
	definePageMeta({
		layout: "dashboard",
	});
	const Api = useApi();

	const posts = ref("");
	const filter = ref("");
	async function getPosts() {
		var url = "/api/account/blog/?type=blog";
		if (filter.value) {
			url += `&search=${encodeURIComponent(filter.value)}`;
		}
		const res = await Api.get(url);
		console.log(res.data.results);
		posts.value = res.data;
	}
	getPosts();
	const debouncedGetPosts = debounce(getPosts, 1000);
	const loadMore = async (url) => {
		url = url.split("/api/");
		url = "/api/" + url[1];
		const res = await Api.get(url);
		posts.value.results = [...posts.value.results, ...res.data.results];
		posts.value.next = res.data.next;
	};

	const data = {
		personalInfo: {
			firstName: "Jane",
			lastName: "Doe",
			shortBio: "Frontend developer at Company",
			relations: "250K+ Users",
			projects: 8,
			socials: [
				{
					name: "Facebook",
					icon: "basil:facebook-solid",
					url: "https://www.facebook.com/nextoxyofficial/",
				},
				{
					name: "Dribbble",
					icon: "ph:dribbble-logo-duotone",
					url: "https://www.lyriczsoftwares.com/",
				},
			],
			picture: "https://tairo.cssninja.io/img/avatars/2.svg",
			badge: "https://tairo.cssninja.io/img/avatars/2.svg",
		},
	};
</script>

<template>
	<section>
		<div class="mx-auto w-full">
			<AccountFb />
			<div v-if="!data"></div>
			<div
				v-else
				class="relative w-full"
			>
				<div class="flex w-full flex-col">
					<div class="mx-auto w-full max-w-md text-center">
						<BaseHeading
							tag="h2"
							size="xl"
							weight="medium"
							class="mt-4"
						>
							Welcome Back
						</BaseHeading>
						<BaseParagraph
							size="sm"
							class="mb-3 mt-1"
						>
							Please Read Our Terms & Conditions Before Availing Our Services.
						</BaseParagraph>
						<div
							class="divide-muted-200 dark:divide-muted-800 flex items-center justify-center divide-x"
						>
							<div class="flex h-8 items-center gap-1 px-4">
								<Icon
									name="ph:circles-three-duotone"
									class="h-5 w-5"
								/>
								<BaseText size="sm">{{
									data?.personalInfo.relations
								}}</BaseText>
							</div>
							<div class="hidden h-8 items-center gap-1 px-4 sm:flex">
								<Icon
									name="ph:check-circle-duotone"
									class="h-5 w-5"
								/>
								<BaseText size="sm"
									>{{ data?.personalInfo.projects }} projects</BaseText
								>
							</div>
							<div class="flex h-8 items-center gap-2 px-4">
								<NuxtLink
									v-for="link in data?.personalInfo.socials"
									:key="link.name"
									:to="link.url"
									target="_blank"
									rel="noopener noreferrer"
									class="border-muted-200 hover:border-primary-500 dark:border-muted-700 dark:hover:border-primary-500 dark:bg-muted-800 hover:text-primary-500 flex h-10 w-10 items-center justify-center rounded-full border bg-white transition-colors duration-300"
								>
									<Icon
										:name="link.icon"
										class="h-4 w-4"
									/>
									<span class="sr-only">{{ link.name }}</span>
								</NuxtLink>
							</div>
						</div>
					</div>
				</div>

				<div
					class="ltablet:grid-cols-4 mx-auto mt-6 grid w-full grid-cols-2 gap-1 sm:grid-cols-4 lg:flex lg:justify-center lg:flex-wrap"
					style="justify-content: center"
				>
					<BaseCard
						shape="curved"
						elevated-hover
						class="hover:!border-primary-500 group border-2 lg:w-[210px]"
					>
						<NuxtLink
							to="/account/ecommerce"
							class="block p-6"
						>
							<div class="text-center">
								<Icon
									name="material-symbols:shopping-bag-outline-sharp"
									class="group-hover:text-primary-500 text-success-400 h-10 w-10 transition-all duration-300 group-hover:rotate-6"
								/>
								<BaseHeading
									tag="h3"
									size="sm"
									weight="semibold"
									class="mt-2 uppercase"
								>
									eCommerce & Landing Page
								</BaseHeading>
								<BaseText
									size="sm"
									class="min-h-[36px]"
								>
									Website & Lead Gen
								</BaseText>
							</div>
						</NuxtLink>
					</BaseCard>

					<BaseCard
						shape="curved"
						elevated-hover
						class="hover:!border-primary-500 group border-2 lg:w-[210px] hidden"
					>
						<NuxtLink
							to="#"
							class="block p-6"
						>
							<div class="text-center">
								<Icon
									name="solar:ruler-cross-pen-bold-duotone"
									class="group-hover:text-primary-500 text-success-400 h-10 w-10 transition-all duration-300 group-hover:rotate-6"
								/>
								<BaseHeading
									tag="h3"
									size="sm"
									weight="semibold"
									class="mt-2 uppercase"
								>
									Blog
								</BaseHeading>
								<BaseText
									size="sm"
									class="min-h-[36px]"
								>
									Coming Soon...
								</BaseText>
							</div>
						</NuxtLink>
					</BaseCard>
					<BaseCard
						shape="curved"
						elevated-hover
						class="hover:!border-primary-500 group border-2 lg:w-[210px] hidden"
					>
						<NuxtLink
							to="/account/services/domains"
							class="block p-6"
						>
							<div class="text-center">
								<Icon
									name="ph:users-four-duotone"
									class="group-hover:text-primary-500 text-success-400 h-10 w-10 transition-all duration-300 group-hover:rotate-6"
								/>
								<BaseHeading
									tag="h3"
									size="sm"
									weight="semibold"
									class="mt-2 uppercase"
								>
									Domain
								</BaseHeading>
								<BaseText
									size="sm"
									class="min-h-[36px]"
								>
									Purchase And Manage Domains
								</BaseText>
							</div>
						</NuxtLink>
					</BaseCard>
					<BaseCard
						shape="curved"
						elevated-hover
						class="hover:!border-primary-500 group border-2 lg:w-[210px]"
					>
						<NuxtLink
							to="/account/services/seo"
							class="block p-6"
						>
							<div class="text-center">
								<Icon
									name="ph:lock-open-duotone"
									class="group-hover:text-primary-500 text-success-400 h-10 w-10 transition-all duration-300 group-hover:rotate-6"
								/>
								<BaseHeading
									tag="h3"
									size="sm"
									weight="semibold"
									class="mt-2 uppercase"
								>
									SEO Marketing
								</BaseHeading>
								<BaseText
									size="sm"
									class="min-h-[36px]"
								>
									Order SEO Marketing Services
								</BaseText>
							</div>
						</NuxtLink>
					</BaseCard>
					<BaseCard
						shape="curved"
						elevated-hover
						class="hover:!border-primary-500 group border-2 lg:w-[210px]"
					>
						<NuxtLink
							to="/account/services/boosting"
							class="block p-6"
						>
							<div class="text-center">
								<Icon
									name="ph:note-duotone"
									class="group-hover:text-primary-500 text-success-400 h-10 w-10 transition-all duration-300 group-hover:rotate-6"
								/>
								<BaseHeading
									tag="h3"
									size="sm"
									weight="semibold"
									class="mt-2 uppercase"
								>
									Facebook Boosting
								</BaseHeading>
								<BaseText
									size="sm"
									class="min-h-[36px]"
								>
									Boost Your Facebook Page
								</BaseText>
							</div>
						</NuxtLink>
					</BaseCard>
					<BaseCard
						shape="curved"
						elevated-hover
						class="hover:!border-primary-500 group border-2 lg:w-[210px]"
					>
						<NuxtLink
							to="/account/services/graphic"
							class="block p-6"
						>
							<div class="text-center">
								<Icon
									name="ph:upload-duotone"
									class="group-hover:text-primary-500 text-success-400 h-10 w-10 transition-all duration-300 group-hover:rotate-6"
								/>
								<BaseHeading
									tag="h3"
									size="sm"
									weight="semibold"
									class="mt-2 uppercase"
								>
									Graphic Design
								</BaseHeading>
								<BaseText
									size="sm"
									class="min-h-[36px]"
								>
									Order Graphic Design Services
								</BaseText>
							</div>
						</NuxtLink>
					</BaseCard>
					<BaseCard
						shape="curved"
						elevated-hover
						class="hover:!border-primary-500 group border-2 lg:w-[210px]"
					>
						<NuxtLink
							to="/account/services/formation"
							class="block p-6"
						>
							<div class="text-center">
								<Icon
									name="fluent:building-bank-28-regular"
									class="group-hover:text-primary-500 text-success-400 h-10 w-10 transition-all duration-300 group-hover:rotate-6"
								/>
								<BaseHeading
									tag="h3"
									size="sm"
									weight="semibold"
									class="mt-2 uppercase"
								>
									UK & USA Business Formation
								</BaseHeading>
								<BaseText
									size="sm"
									class="min-h-[36px]"
								>
									UK & USA Business Registration Service
								</BaseText>
							</div>
						</NuxtLink>
					</BaseCard>
					<BaseCard
						shape="curved"
						elevated-hover
						class="hover:!border-primary-500 group border-2 lg:w-[210px]"
					>
						<a
							target="_blank"
							href="https://oxymanager.com"
							class="block p-6"
						>
							<div class="text-center">
								<div class="flex min-h-[40px] justify-center items-center">
									<img
										class="h-7 transition-all duration-300 group-hover:rotate-2 mx-auto"
										src="/static/frontend/images/ecommerce/oxymanager.svg"
										alt=""
										srcset=""
									/>
								</div>
								<BaseHeading
									tag="h3"
									size="sm"
									weight="semibold"
									class="mt-2 uppercase"
								>
									OxyManager
								</BaseHeading>
								<BaseText
									size="sm"
									class="min-h-[36px]"
								>
									POS & SMS Marketing
								</BaseText>
							</div>
						</a>
					</BaseCard>
					<BaseCard
						shape="curved"
						elevated-hover
						class="hover:!border-primary-500 group border-2 lg:w-[210px]"
					>
						<a
							target="_blank"
							href="https://nextdropshipping.com/"
							class="block p-6"
						>
							<div class="text-center">
								<div class="flex min-h-[40px] justify-center items-center">
									<img
										class="h-7 transition-all duration-300 group-hover:rotate-2 mx-auto"
										src="https://nextdropshipping.com/media/site_logo/imgs/nextdroplogo_2_FgAINnU.png"
										alt=""
										srcset=""
									/>
								</div>
								<BaseHeading
									tag="h3"
									size="sm"
									weight="semibold"
									class="mt-2 uppercase"
								>
									NextDropshipping
								</BaseHeading>
								<BaseText
									size="sm"
									class="min-h-[36px]"
								>
									Wholesale Marketplace
								</BaseText>
							</div>
						</a>
					</BaseCard>
					<BaseCard
						shape="curved"
						elevated-hover
						class="hover:!border-primary-500 group border-2 lg:w-[210px]"
					>
						<a
							target="_blank"
							href="https://academy.nextdropshipping.com/"
							class="block p-6"
						>
							<div class="text-center">
								<div class="flex min-h-[40px] justify-center items-center">
									<img
										class="h-7 transition-all duration-300 group-hover:rotate-2 mx-auto"
										src="https://nextdropshipping.com/media/site_logo/imgs/nextdroplogo_2_FgAINnU.png"
										alt=""
										srcset=""
									/>
								</div>
								<BaseHeading
									tag="h3"
									size="sm"
									weight="semibold"
									class="mt-2 uppercase"
								>
									NDS Academy
								</BaseHeading>
								<BaseText
									size="sm"
									class="min-h-[36px]"
								>
									Invest With NDS
								</BaseText>
							</div>
						</a>
					</BaseCard>
				</div>
			</div>
		</div>

		<!-- posts -->
		<nuxt-link
			target="_blank"
			to="/blog"
		>
			<img
				src="/static/frontend/images/accout-banner.jpg"
				class="hidden md:block mx-auto w-full object-cover mt-10 rounded-lg shadow-xl"
				alt=""
				srcset=""
			/>
			<img
				src="/static/frontend/images/account-banner-mobile.png"
				class="block md:hidden mx-auto w-full object-cover mt-10 rounded-lg shadow-xl"
				alt=""
				srcset=""
			/>
		</nuxt-link>

		<div class="my-16">
			<TairoContentWrapper>
				<template #left>
					<BaseInput
						v-model="filter"
						icon="lucide:search"
						shape="curved"
						placeholder="Search posts..."
						:classes="{
							wrapper: 'w-full sm:w-auto',
						}"
						@keyup="debouncedGetPosts"
					/>
				</template>
				<template #right> </template>
				<div>
					<div v-if="posts && posts?.results.length === 0">
						<BasePlaceholderPage
							title="No matching results"
							subtitle="Looks like we couldn't find any matching results for your search terms. Try other search terms."
						>
							<template #image>
								<img
									class="block dark:hidden"
									src="/static/img/illustrations/placeholders/flat/placeholder-search-6.svg"
									alt="Placeholder image"
								/>
								<img
									class="hidden dark:block"
									src="/static/img/illustrations/placeholders/flat/placeholder-search-6-dark.svg"
									alt="Placeholder image"
								/>
							</template>
						</BasePlaceholderPage>
					</div>
					<div v-else>
						<div
							class="ltablet:grid-cols-2 grid w-full gap-4 grid-cols-1 sm:grid-cols-2 lg:grid-cols-4"
						>
							<TransitionGroup
								enter-active-class="transform-gpu"
								enter-from-class="opacity-0 -translate-x-full"
								enter-to-class="opacity-100 translate-x-0"
								leave-active-class="absolute transform-gpu"
								leave-from-class="opacity-100 translate-x-0"
								leave-to-class="opacity-0 -translate-x-full"
							>
								<!-- <BaseCard
                  v-for="item in posts?.results"
                  :key="item.id"
                  shape="curved"
                  class="group p-3 cursor-pointer hover:shadow-lg flex gap-4"
                >
                  <nuxt-link :to="'/blog/' + item.id" class="relative w-2/5">
                    <img
                      :src="Api.baseURL + item.image"
                      class="h-full w-full rounded-lg object-cover"
                      v-if="item.image"
                    />
                    <img
                      v-else
                      src="https://via.placeholder.com/282x160"
                      class="h-full w-full rounded-lg object-cover"
                    />
                    <hr class="mt-5" />
                    <BaseTag
                      shape="full"
                      color="primary"
                      flavor="pastel"
                      size="sm"
                      class="absolute start-3 top-3 translate-y-1 opacity-0 transition-all duration-300 group-hover:translate-y-0 group-hover:opacity-100"
                      v-if="item.category"
                    >
                      {{ item.category.name }}
                    </BaseTag>
                  </nuxt-link>
                  <div class="flex-1 py-3 pr-4 w-3/5">
                    <div class="mb-6 mt-3">
                      <nuxt-link :to="'/blog/' + item.id">
                        <BaseHeading
                          tag="h2"
                          size="2xl"
                          weight="semibold"
                          lead="snug"
                          class="line-clamp-2 text-gray-800 dark:text-gray-100 my-2"
                        >
                          {{ item.title }}
                        </BaseHeading>
                      </nuxt-link>
                      <p class="flex items-center gap-1.5">
                        <Icon name="i-heroicons-calendar" />
                        {{ item.created_at }}
                      </p>
                      <p class="mb-4">{{ item.meta }}</p>
                      <div class="flex justify-between">
                        <p>
                          {{
                            item.category === null
                              ? "No category found!"
                              : item.category
                          }}
                        </p>
                        <p>{{ item.author }}</p>
                      </div>
                    </div>

                    <div class="mt-auto flex items-center gap-2 hidden">
                      <BaseAvatar
                        :src="item.author.avatar"
                        :text="item.author.initials"
                        size="xs"
                        class="bg-muted-500/20 text-muted-500"
                      />
                      <div class="leading-none">
                        <h4
                          class="text-muted-800 dark:text-muted-100 font-sans text-sm font-medium leading-tight"
                        >
                          {{ item.author.name }}
                        </h4>
                        <p class="text-muted-400 font-sans text-xs">
                          {{ item.published }}
                        </p>
                      </div>
                      <div class="ms-auto">
                        <BaseButtonAction to="#" shape="rounded">
                          <Icon name="lucide:edit-3" />
                          <span>Edit</span>
                        </BaseButtonAction>
                      </div>
                    </div>
                  </div>
                </BaseCard> -->

								<UCard
									class="text-center overflow-hidden bg-[#f1f1f1]"
									v-for="(blog, index) in posts?.results"
									:key="index"
									:ui="{
										header: {
											padding: 'px-0 py-0 sm:px-0',
										},
										body: {
											padding: 'px-0 py-0 sm:px-0 sm:p-0',
										},
									}"
								>
									<template #header>
										<div class="px-0">
											<img
												class="w-full h-40 bg-cover"
												:src="Api.baseURL + blog.image"
												:alt="blog.title"
											/>
										</div>
									</template>
									<div class="p-6 h-full">
										<h2
											class="text-base font-semibold uppercase text-[#022b46] dark:text-slate-400 h-12"
										>
											{{ blog.title.slice(0, 40) }}
										</h2>
										<p
											class="text-sm mb-5 text-[#022b46] dark:text-slate-400 h-10"
										>
											{{ blog.meta.slice(0, 60) }}
										</p>
										<ULink
											:to="'/blog/' + blog.id"
											active-class="text-primary"
											inactive-class="text-gray-500 dark:text-gray-400"
										>
											<PublicButton
												label="Read More"
												firstColor="bg-[#022b46]"
												secondColor="uppercase"
											/>
										</ULink>
									</div>
								</UCard>
							</TransitionGroup>
						</div>
						<div class="flex w-full justify-center">
							<BaseButton
								color="primary"
								@click="loadMore(posts.next)"
								v-if="posts && posts.next"
								>Load More</BaseButton
							>
						</div>
					</div>
				</div>
			</TairoContentWrapper>
		</div>
	</section>
</template>
