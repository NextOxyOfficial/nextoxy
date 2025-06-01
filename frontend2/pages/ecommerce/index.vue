<script setup>
	definePageMeta({
		layout: "dashboard",
	});
	const { shop, getShop } = useShop();
	const Api = useApi();

	const preloader = useState("preloader");
	const shopData = ref("");
	const overviewType = ref({ id: 1, name: "Today" });
	const fromDate = ref("");
	const toDate = ref("");

	const dummyChatData = ref([
		{
			name: "Completed Sales",
			data: [],
		},
		{
			name: "Sales value",
			data: [],
		},
	]);
	const areaExpenses = ref(useAreaExpenses(dummyChatData.value));

	async function getOverviewData() {
		if (overviewType.value.name == "range" && !fromDate.value) {
			return;
		}
		if (overviewType.value.name == "range" && !toDate.value) {
			return;
		}
		var body = {
			overviewType: overviewType.value.name,
			fromDate: fromDate.value,
			toDate: toDate.value,
		};
		const { data } = await Api.post("/api/ecommerce/dash/overview", body);
		shopData.value = data;
		areaExpenses.value = useAreaExpenses(data.series);
	}
	getOverviewData();

	watch(overviewType, (newX) => {
		getOverviewData();
	});

	const orders = ref();
	const getOrders = async () => {
		const response = await Api.get("/api/ecommerce/dash/orders?limit=3");
		orders.value = response.data;
	};
	getOrders();

	const filter = [
		{
			id: 0,
			name: "All Time",
		},
		{
			id: 1,
			name: "Today",
		},
		{
			id: 2,
			name: "Yesterday",
		},
		{
			id: 3,
			name: "This Week",
		},
		{
			id: 4,
			name: "Last Week",
		},
		{
			id: 5,
			name: "This Month",
		},
		{
			id: 6,
			name: "Last Month",
		},
		{
			id: 7,
			name: "Custom Date",
		},
	];
	function useAreaExpenses(series) {
		const { primary } = useTailwindColors();
		const type = "area";
		const height = 320;

		const options = {
			chart: {
				foreColor: "#999",
				stacked: true,
				toolbar: {
					show: false,
				},
				dropShadow: {
					enabled: true,
					enabledSeries: [0],
					top: -2,
					left: 2,
					blur: 5,
					opacity: 0.06,
				},
			},
			colors: ["#1FFFB4", primary.value, "#39c922"],
			stroke: {
				curve: "smooth",
				width: 3,
			},
			title: {
				text: "",
				align: "left",
			},
			dataLabels: {
				enabled: false,
			},
			markers: {
				size: 0,
				strokeColor: "#fff",
				strokeWidth: 3,
				strokeOpacity: 1,
				hover: {
					size: 6,
				},
			},
			xaxis: {
				type: "datetime",
				axisBorder: {
					show: false,
				},
				axisTicks: {
					show: false,
				},
			},
			yaxis: {
				labels: {
					offsetX: 0,
					offsetY: -5,
				},
				tooltip: {
					enabled: true,
				},
			},
			grid: {
				show: false,
				padding: {
					left: -5,
					right: 5,
				},
			},
			tooltip: {
				x: {
					format: "dd MMM yyyy",
				},
			},
			legend: {
				position: "top",
				horizontalAlign: "left",
			},
			fill: {
				type: "solid",
				fillOpacity: 0.7,
			},
		};

		return {
			type,
			height,
			options,
			series,
		};
	}

	const auth = useAuth();

	const steps = ref([]);
	// const completed = ref(0);
	async function getSteps() {
		var res = await Api.get("/api/ecommerce/dash/steps");
		steps.value = res.data;
		console.log(steps.value, 333);
		// completed.value = steps.value?.data?.filter(
		//   (item) => item.status === "complete"
		// );
	}

	getSteps();
</script>

<template>
	<div class="relative">
		<div
			class="w-full"
			v-if="preloader"
		>
			<div class="flex gap-1 md:gap-3 flex-wrap">
				<BaseCard
					shape="rounded"
					class="px-4 md:px-6 py-8 md:py-20 mb-2 flex-1 md:max-w-[50%] min-w-[150px] flex flex-col justify-around"
					v-for="i in 2"
					:key="i"
				>
					<div
						class="flex items-center my-2"
						v-for="i in 2"
						:key="i"
					>
						<BasePlaceload class="h-10 w-10 rounded-full" />

						<div class="ms-3 grow space-y-2">
							<BasePlaceload class="h-3 w-full rounded" />

							<BasePlaceload class="h-3 w-[85%] rounded" />
						</div>
					</div>
				</BaseCard>
			</div>
			<BaseCard
				shape="rounded"
				class="px-4 md:px-6 mb-2 py-12"
				v-for="i in 3"
				:key="i"
			>
				<div class="flex items-center">
					<BasePlaceload class="h-10 w-10 rounded-full" />

					<div class="ms-3 grow space-y-2">
						<BasePlaceload class="h-3 w-full rounded" />

						<BasePlaceload class="h-3 w-[85%] rounded" />
					</div>
				</div>
			</BaseCard>
		</div>

		<p class="text-2xl font-semibold mb-5">
			Good Day! {{ auth?.user?.first_name }}
		</p>
		<h2 class="text-2xl mb-3 font-semibold">Let's setup your store!</h2>
		<div class="mb-10 bg-green-100 dark:bg-muted-800 rounded-xl p-8">
			<div
				class="flex items-center gap-6 mb-4 last-of-type:mb-0"
				v-for="(step, index) in steps.data"
				:key="index"
			>
				<UIcon
					name="i-heroicons-check-circle-solid"
					v-if="step.status === 'complete'"
					class="text-primary text-3xl"
				/>
				<UIcon
					name="i-icon-park-outline:loading-one"
					class="text-3xl"
					dynamic
					v-else
				/>
				<NuxtLink
					v-if="step.status === 'current'"
					:to="step.href"
					class="lowercase first-letter:uppercase text-sm"
				>
					{{ step.name }}
					<UBadge
						color="primary"
						variant="solid"
						size="md"
						v-if="step.status === 'current'"
						>Fix</UBadge
					>
				</NuxtLink>
				<p
					v-else
					class="lowercase first-letter:uppercase text-sm"
				>
					{{ step.name }}
				</p>
			</div>
		</div>
		<div
			:class="{ 'opacity-0': preloader }"
			class="flex flex-col gap-6"
		>
			<BaseCard
				class="ltablet:flex-row flex flex-col-reverse gap-y-10 px-2 py-4 md:py-10 sm:px-10 lg:flex-row"
				v-if="shopData.stats"
			>
				<div class="ltablet:w-3/5 w-full lg:w-3/5">
					<div class="mb-4 sm:mb-4 flex items-center justify-between">
						<BaseHeading
							as="h3"
							size="md"
							weight="semibold"
							lead="tight"
							class="text-muted-800 dark:text-white"
						>
							<span>My Store</span>
						</BaseHeading>
						<div></div>
					</div>
					<div
						class="ltablet:pe-12 flex flex-col gap-y-4 sm:flex-row sm:gap-x-8 lg:pe-12"
					>
						<div class="grid w-full gap-[3px] sm:gap-4 md:px-6 grid-cols-2">
							<DemoCreditCardCustom
								:balance="shopData.stats.orders"
								ending-number="Orders"
								type="visa"
								:active="true"
							/>
							<DemoCreditCardCustom
								:balance="shop.currency + shopData.stats.total"
								ending-number="Sales Value"
								type="visa"
								:active="false"
							/>
							<DemoCreditCardCustom
								:balance="shopData.stats.products"
								ending-number="Products Added"
								type="visa"
								:active="false"
							/>
							<DemoCreditCardCustom
								:balance="shopData.stats.customers"
								ending-number="Customer Joined"
								type="visa"
								:active="false"
							/>
						</div>
					</div>
				</div>
				<div class="ltablet:w-2/5 w-full lg:w-2/5">
					<div
						class="ltablet:ps-12 ltablet:border-l border-muted-200 dark:border-muted-700 flex h-full flex-col lg:border-l lg:ps-12"
					>
						<div class="mb-4 flex items-center justify-between">
							<BaseHeading
								as="h4"
								size="md"
								weight="semibold"
								lead="tight"
								class="text-muted-800 dark:text-white hidden sm:block"
							>
								<span>Accounting</span>
							</BaseHeading>
							<div
								class="ltablet:max-w-[230px] w-full sm:max-w-[260px] grow flex gap-1"
							>
								<BaseListbox
									v-model="overviewType"
									label="Select Date"
									:items="filter"
									:properties="{
										value: 'id',
										label: 'name',
										sublabel: '',
									}"
									hide-label
								/>
								<TairoPopover
									size="sm"
									orientation="end"
									v-if="overviewType.name == 'Custom Date'"
								>
									<BaseButton
										class="text-muted-500 flex items-center border mt-6 !px-1"
									>
										<Icon
											name="material-symbols-light:calendar-month-outline"
											class="h-8 w-8"
										/>
									</BaseButton>

									<template #content>
										<div class="p-2">
											<BaseInput
												v-model="fromDate"
												shape="rounded"
												label="From Date"
												placeholder="Ex: username"
												type="date"
												@change="getOverviewData"
											/>
											<BaseInput
												v-model="toDate"
												shape="rounded"
												label="To Date"
												placeholder="Ex: username"
												type="date"
												@change="getOverviewData"
											/>
										</div>
									</template>
								</TairoPopover>
							</div>
						</div>
						<div
							class="ptablet:flex ptablet:items-end ptablet:justify-between ptablet:mt-10 mt-auto"
						>
							<div class="ptablet:mb-0 mb-6 leading-relaxed">
								<span class="text-muted-500 block font-sans text-sm">
									Completeds
								</span>
								<span
									class="text-muted-800 dark:text-muted-100 block font-sans text-3xl font-semibold"
								>
									{{ shop.currency }}{{ shopData.stats.complete_total }} ({{
										shopData.stats.complete_orders
									}}
									orders)
								</span>
							</div>
							<div class="flex items-center gap-[10px] sm:gap-4">
								<div class="card-balance-stat">
									<div
										class="text-muted-500 mb-1 font-sans text-xs font-medium uppercase"
									>
										<span>Pending</span>
									</div>
									<div class="flex items-center gap-2">
										<div
											class="bg-muted-100 flex h-10 w-10 items-center justify-center rounded-full"
										>
											<Icon
												name="lucide:arrow-right"
												class="text-success-500 h-4 w-4 -rotate-45"
											/>
										</div>
										<div
											class="text-muted-500 dark:text-muted-500 font-sans text-sm"
										>
											<span
												>{{ shop.currency
												}}{{ shopData.stats.pending_total }} ({{
													shopData.stats.pending_orders
												}}
												orders)</span
											>
										</div>
									</div>
								</div>
								<div class="card-balance-stat">
									<div
										class="text-muted-500 mb-1 font-sans text-xs font-medium uppercase"
									>
										<span>Cancelled</span>
									</div>
									<div class="flex items-center gap-2">
										<div
											class="bg-muted-100 flex h-10 w-10 items-center justify-center rounded-full"
										>
											<Icon
												name="lucide:arrow-right"
												class="text-danger-500 h-4 w-4 rotate-45"
											/>
										</div>
										<div
											class="text-muted-500 dark:text-muted-500 font-sans text-sm"
										>
											<span
												>{{ shop.currency
												}}{{ shopData.stats.cancelled_total }} ({{
													shopData.stats.cancelled_orders
												}}
												orders)</span
											>
										</div>
									</div>
								</div>
							</div>
						</div>
					</div>
				</div>
			</BaseCard>
			<BaseMessage
				v-if="shop.shop_message"
				type="info"
				shape="rounded"
				class="flex-1 items-start"
				icon
			>
				<span>{{ shop.shop_message }}</span>
				<nuxt-link
					class="font-bold text-blue-500"
					:to="shop_message_link"
					v-if="shop.shop_message_link"
				>
					Learn More</nuxt-link
				>
			</BaseMessage>
			<BaseCard
				class="ltablet:flex-row !bg-muted-50 dark:!bg-muted-800 flex flex-col gap-y-10 px-2 py-4 md:py-10 sm:px-10 lg:flex-row"
			>
				<div
					class="ltablet:w-3/5 ltablet:border-r border-muted-300 dark:border-muted-700 w-full lg:w-3/5 lg:border-r"
				>
					<div class="mb-4 flex items-center justify-between sm:pe-12">
						<BaseHeading
							as="h4"
							size="md"
							weight="semibold"
							lead="tight"
							class="text-muted-800 dark:text-white hidden sm:block"
						>
							<span>Summary</span>
						</BaseHeading>
						<div
							class="ltablet:max-w-[230px] w-full sm:max-w-[260px] grow flex gap-1 hidden"
						>
							<BaseListbox
								v-model="overviewType"
								label="Select Date"
								:items="filter"
								:properties="{
									value: 'id',
									label: 'name',
									sublabel: '',
								}"
								hide-label
							/>
							<TairoPopover
								size="sm"
								orientation="end"
								v-if="overviewType.name == 'Custom Date'"
							>
								<BaseButton
									class="text-muted-500 flex items-center border mt-6 !px-1"
								>
									<Icon
										name="material-symbols-light:calendar-month-outline"
										class="h-8 w-8"
									/>
								</BaseButton>

								<template #content>
									<div class="p-2">
										<BaseInput
											v-model="fromDate"
											shape="rounded"
											label="From Date"
											placeholder="Ex: username"
											type="date"
											@change="getOverviewData"
										/>
										<BaseInput
											v-model="toDate"
											shape="rounded"
											label="To Date"
											placeholder="Ex: username"
											type="date"
											@change="getOverviewData"
										/>
									</div>
								</template>
							</TairoPopover>
						</div>
					</div>
					<div class="flex h-full w-full flex-col gap-16 sm:flex-row">
						<!-- Monthly Summary -->
						<div class="shrink-0 hidden">
							<div
								class="border-muted-300 divide-muted-300 dark:border-muted-700 dark:divide-muted-700 flex flex-col divide-y rounded-lg border"
							>
								<div class="p-4">
									<div
										class="text-muted-500 mb-1 font-sans text-xs font-medium uppercase"
									>
										<span>Profit</span>
									</div>
									<div class="text-success-500 font-sans text-sm font-semibold">
										<span>+ {{ formatPrice(2324.12) }}</span>
									</div>
								</div>
								<div class="p-4">
									<div
										class="text-muted-500 mb-1 font-sans text-xs font-medium uppercase"
									>
										<span>Sold</span>
									</div>
									<div class="text-primary-500 font-sans text-sm font-semibold">
										<span>{{ formatPrice(1509.27) }}</span>
									</div>
								</div>
							</div>
						</div>
						<!-- Chart -->
						<div class="ltablet:pe-12 flex h-full grow flex-col lg:pe-12">
							<div class="my-auto">
								<AddonApexcharts v-bind="areaExpenses" />
							</div>
						</div>
					</div>
				</div>
				<div class="ltablet:w-2/5 w-full lg:w-2/5">
					<div class="ltablet:ps-12 h-full lg:ps-12">
						<div class="flex h-full w-full flex-col">
							<div class="mb-6 flex items-center justify-between">
								<BaseHeading
									as="h3"
									size="md"
									weight="semibold"
									lead="tight"
									class="text-muted-800 mb-6 dark:text-white"
								>
									<span>Recent Orders</span>
								</BaseHeading>
							</div>
							<div
								class="my-auto"
								v-if="orders && orders.results"
							>
								<div
									class="space-y-4"
									v-if="orders.results.length > 0"
								>
									<!-- Item -->
									<div
										class="flex items-center gap-2"
										v-for="order in orders.results"
										:key="order.id"
									>
										<BaseIconBox
											class="bg-success-500/10 text-success-500"
											size="md"
											shape="full"
										>
											<Icon
												name="material-symbols-light:shopping-basket-sharp"
												class="h-5 w-5"
											/>
										</BaseIconBox>
										<div>
											<BaseHeading
												as="h4"
												size="sm"
												weight="medium"
												lead="tight"
												class="text-muted-800 dark:text-white"
											>
												<span>{{ shop.currency }}{{ order.total }}</span>
											</BaseHeading>
											<BaseParagraph
												size="xs"
												class="text-muted-500"
											>
												<span>{{ order.created_at }}</span>
											</BaseParagraph>
										</div>
										<div class="ms-auto">
											<span
												class="text-muted-800 dark:text-muted-100 font-sans text-sm font-semibold"
											>
												{{ order.status }}
											</span>
										</div>
									</div>
								</div>
								<div
									class="flex w-full flex-col justify-center items-center"
									v-else
								>
									<Icon
										name="solar:notification-unread-bold-duotone"
										class="text-primary-500 h-20 w-20"
									/>
									<BaseHeading
										as="p"
										size="xl"
										weight="thin"
										class="text-muted-800 dark:text-white"
									>
										You don't have any orders!
									</BaseHeading>
								</div>
								<div class="mt-6 flex items-center gap-2">
									<BaseButton
										to="/ecommerce/orders"
										color="primary"
										class="w-full"
									>
										<span>View Orders</span>
									</BaseButton>
								</div>
							</div>
						</div>
					</div>
				</div>
			</BaseCard>
		</div>
	</div>
</template>
