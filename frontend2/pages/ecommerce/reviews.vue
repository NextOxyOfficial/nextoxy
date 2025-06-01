<script setup lang="ts">
	definePageMeta({
		layout: "dashboard",
	});
	const preloader = useState("preloader");
	const Api = useApi();
	const route = useRoute();
	const router = useRouter();
	const page = computed(() => parseInt((route.query.page as string) ?? "1"));

	const filter = ref("");
	const perPage = ref(10);

	watch([filter, perPage], () => {
		router.push({
			query: {
				page: undefined,
			},
		});
	});

	const query = computed(() => {
		return {
			filter: filter.value,
			perPage: perPage.value,
			page: page.value,
		};
	});

	const revs = ref("");
	async function getRevs() {
		const res = await Api.get("/api/ecommerce/dash/reviews");
		revs.value = res.data;
	}
	getRevs();
	const loadMore = async (url) => {
		url = url.split("/api/");
		url = "/api/" + url[1];
		const res = await Api.get(url);
		revs.value.results = [...revs.value.results, ...res.data.results];
		revs.value.next = res.data.next;
	};
</script>

<template>
	<div>
		<TairoContentWrapper>
			<template #left>
				<BaseInput
					v-model="filter"
					icon="lucide:search"
					placeholder="Filter users..."
					:classes="{
						wrapper: 'w-full sm:w-auto',
					}"
				/>
			</template>
			<template #right>
				<BaseSelect
					v-model="perPage"
					placeholder="Items per page"
					label=""
					:classes="{
						wrapper: 'w-full sm:w-40',
					}"
				>
					<option :value="10">10 per page</option>
					<option :value="25">25 per page</option>
					<option :value="50">50 per page</option>
					<option :value="100">100 per page</option>
				</BaseSelect>
			</template>
			<BasePlaceload
				v-if="preloader"
				class="h-[50vh] w-full rounded opacity-35"
			/>
			<div v-else>
				<div v-if="revs && revs?.results.length === 0">
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
					<div class="ltablet:grid-cols-2 grid w-full gap-4 lg:grid-cols-2">
						<TransitionGroup
							enter-active-class="transform-gpu"
							enter-from-class="opacity-0 -translate-x-full"
							enter-to-class="opacity-100 translate-x-0"
							leave-active-class="absolute transform-gpu"
							leave-from-class="opacity-100 translate-x-0"
							leave-to-class="opacity-0 -translate-x-full"
						>
							<BaseCard
								v-for="item in revs?.results"
								:key="item.id"
							>
								<div
									class="border-muted-200 dark:border-muted-700 flex flex-col items-center border-b p-6 sm:flex-row"
								>
									<div class="flex flex-col items-center gap-3 sm:flex-row">
										<Icon
											name="solar:user-rounded-bold-duotone"
											class="me-1 h-12 w-12"
										/>
										<div class="text-center leading-none sm:text-left">
											<h4
												class="text-muted-800 dark:text-muted-100 font-sans text-base font-medium"
											>
												{{ item.customer.name }}
											</h4>
											<p class="text-muted-400 font-sans text-sm">
												{{ item.review }}
											</p>
										</div>
									</div>
								</div>
								<div
									class="border-muted-200 dark:border-muted-700 flex flex-col items-center border-b p-6 sm:flex-row"
								>
									<div class="flex flex-col items-center gap-3 sm:flex-row">
										<div class="flex items-center">
											<Icon
												name="solar:box-bold-duotone"
												class="me-1 h-12 w-12"
											/>
										</div>
										<div class="text-center leading-none sm:text-left">
											<h4
												class="text-muted-800 dark:text-muted-100 font-sans text-base font-medium"
											>
												{{ item.product.name }}
											</h4>
											<p class="text-muted-400 font-sans text-sm">
												SKU: {{ item.product.sku }}
											</p>
										</div>
									</div>
								</div>
								<div
									class="flex flex-col items-center justify-between px-6 py-4 sm:flex-row"
								>
									<div class="w-full grow space-y-1 sm:w-auto sm:max-w-[260px]">
										<div class="flex items-center justify-between">
											<div>
												<span class="text-muted-400 font-sans text-sm">
													{{ item.rating }} Star
												</span>
											</div>
										</div>
										<div>
											<span class="text-muted-400 font-sans text-sm">
												{{ item.created_at }}
											</span>
										</div>
									</div>
									<div class="mt-4 w-full sm:mt-0 sm:w-auto">
										<BaseButton class="w-full sm:w-auto"> Delete </BaseButton>
									</div>
								</div>
							</BaseCard>
						</TransitionGroup>
					</div>
					<div class="flex w-full justify-center">
						<button
							class="p-1 px-3 my-4 bg-yellow-600 rounded"
							@click="loadMore(revs.next)"
							v-if="revs && revs.next"
						>
							Load More
						</button>
					</div>
				</div>
			</div>
		</TairoContentWrapper>
	</div>
</template>
