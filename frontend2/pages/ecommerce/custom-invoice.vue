<script setup lang="ts">
	import { debounce } from "lodash";
	definePageMeta({
		layout: "dashboard",
	});
	const preloader = useState("preloader");

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

	const Api = useApi();
	const customers = ref([]);
	const getCustomers = async () => {
		const { data } = await Api.get("/api/ecommerce/dash/customers");
		customers.value = data;
	};
	getCustomers();
	const loadMore = async (url) => {
		var url = url.split("/api/ecommerce/dash/customers");
		url = url[url.length - 1];
		const response = await Api.get("/api/ecommerce/dash/customers" + url);
		customers.value.results = customers.value.results.concat(
			response.data.results
		);
		customers.value.next = response.data.next;
	};
	const search = ref("");
	const searchOrder = async () => {
		const response = await Api.get(
			"/api/ecommerce/dash/customers?search=" + search.value
		);
		customers.value = response.data;
		filter.value = true;
	};
	const debouncedSearchOrder = debounce(searchOrder, 1000);

	function statusColor(itemStatus: string) {
		switch (itemStatus) {
			case "online":
				return "success";
			case "working":
				return "info";
			case "suspended":
				return "warning";
			default:
				break;
		}
	}

	const selected = ref("");
	const isModalOpen = ref(false);
	function closeModal() {
		isModalOpen.value = false;
	}
	function openModal(item) {
		isModalOpen.value = true;
		selected.value = JSON.parse(JSON.stringify(item));
	}

	async function UpdateCustomer() {
		selected.value.message = "";
		if (selected.value.new_pass || selected.value.confirm_pass) {
			if (!selected.value.new_pass || !selected.value.confirm_pass) {
				selected.value.message = "All Fields Are Required";
				selected.value.class = "warning";
				return;
			}
			if (selected.value.new_pass.length < 5) {
				selected.value.message = "New passwords are too short";
				selected.value.class = "warning";
				return;
			}
			if (selected.value.new_pass != selected.value.confirm_pass) {
				selected.value.message = "New passwords does not match";
				selected.value.class = "warning";
				return;
			}
		}
		const { data } = await Api.post(
			"/api/ecommerce/dash/customers",
			selected.value
		);
		selected.value.class = data.class;
		selected.value.message = data.message;
		getCustomers();
	}
	async function DeleteCustomer() {
		selected.value.message = "";
		const { data } = await Api.del(
			"/api/ecommerce/dash/customers?id=" + selected.value.id
		);
		selected.value.class = data.class;
		selected.value.message = data.message;
		getCustomers();
		setTimeout(() => {
			closeModal();
		}, 2000);
	}
</script>

<template>
	<div>
		<!-- Modal component -->
		<TairoModal
			:open="isModalOpen"
			size="lg"
			@close="closeModal"
		>
			<template #header>
				<!-- Header -->
				<div
					class="flex w-full items-center justify-between p-4 md:p-6 mb-0 !pb-0"
				>
					<h3
						class="font-heading text-muted-900 text-lg font-medium leading-6 dark:text-white"
					>
						Update Customer Details
					</h3>

					<BaseButtonClose @click="closeModal" />
				</div>
			</template>

			<!-- Body -->
			<div
				class="p-4 md:p-6"
				v-if="selected"
			>
				<div class="mx-auto w-full">
					<p class="p-2 w-full text-center">{{ selected.name }}</p>
					<hr class="my-3" />
					<div class="grid gap-6 w-full md:grid-cols-2">
						<BaseInput
							v-model="selected.email"
							shape="rounded"
							type="email"
							label="Email Address"
							placeholder="Your email..."
							icon="lucide:mail"
						/>
						<BaseInput
							v-model="selected.phone"
							shape="rounded"
							type="text"
							label="Phone Number"
							placeholder="Phone..."
							icon="lucide:phone"
						/>
						<BaseInput
							v-model="selected.new_pass"
							shape="rounded"
							type="password"
							label="New Password"
							placeholder="New Password..."
							icon="lucide:key-round"
						/>
						<BaseInput
							v-model="selected.confirm_pass"
							shape="rounded"
							type="password"
							label="Confirm New Password"
							placeholder="Confirm New Password..."
							icon="lucide:key-round"
						/>
					</div>
				</div>
				<BaseMessage
					class="mt-4"
					:type="selected.class"
					v-if="selected.message"
					>{{ selected.message }}</BaseMessage
				>
			</div>

			<template #footer>
				<!-- Footer -->
				<div class="p-4 md:p-6 w-full">
					<div class="flex w-full gap-x-2 justify-between items-center">
						<BaseButton
							color="danger"
							flavor="pastel"
							@click="DeleteCustomer"
							>Delete</BaseButton
						>
						<span class="flex gap-2 items-center">
							<BaseButton @click="closeModal">Close</BaseButton>
							<BaseButton
								color="primary"
								flavor="solid"
								@click="UpdateCustomer"
								>Update</BaseButton
							>
						</span>
					</div>
				</div>
			</template>
		</TairoModal>

		<TairoContentWrapper>
			<template #left>
				<BaseInput
					v-model="search"
					icon="lucide:search"
					shape="full"
					placeholder="Find By Name Or Email..."
					:classes="{
						wrapper: 'w-full sm:w-auto',
					}"
					@keyup="debouncedSearchOrder"
				/>
			</template>
			<template #right>
				<BaseButton
					class="w-full sm:w-32 hidden"
					shape="full"
					>Manage</BaseButton
				>
				<BaseButton
					color="primary"
					shape="full"
					class="w-full sm:w-32 hidden"
				>
					<Icon
						name="lucide:plus"
						class="h-4 w-4"
					/>
					<span>Add User</span>
				</BaseButton>
			</template>
			<BasePlaceload
				v-if="preloader"
				class="h-[50vh] w-full rounded opacity-35"
			/>
			<div v-else>
				<div
					v-if="
						customers && customers.results && customers.results.length === 0
					"
					class="mt-28"
				>
					<BasePlaceholderPage title="Invoice list will be appeared here">
						<template #image>
							<img
								class="block dark:hidden"
								src="/static/frontend/images/no-customer.png"
								alt="Placeholder image"
							/>
							<img
								class="hidden dark:block"
								src="/static/frontend/images/no-customer.png"
								alt="Placeholder image"
							/>
						</template>
					</BasePlaceholderPage>
				</div>
				<div
					v-else
					class="pt-6"
				>
					<TransitionGroup
						enter-active-class="transform-gpu"
						enter-from-class="opacity-0 -translate-x-full"
						enter-to-class="opacity-100 translate-x-0"
						leave-active-class="absolute transform-gpu"
						leave-from-class="opacity-100 translate-x-0"
						leave-to-class="opacity-0 -translate-x-full"
					>
						<DemoFlexTableRow
							v-for="(item, index) in customers.results"
							:key="index"
							shape="straight"
							condensed
							spaced
						>
							<template #start>
								<DemoFlexTableStart
									label="user"
									:hide-label="index > 0"
									:title="item.name"
									:subtitle="'ID: ' + item.id"
									avatar="/static/img/avatars/6.svg"
									badge=""
								/>
							</template>
							<template #end>
								<DemoFlexTableCell
									label="Email"
									:hide-label="index > 0"
									class="w-full sm:w-40"
								>
									<p
										class="text-muted-500 dark:text-muted-400 font-sans text-sm"
									>
										{{ item.email }}
									</p>
								</DemoFlexTableCell>
								<DemoFlexTableCell
									label="Phone"
									:hide-label="index > 0"
									class="w-full sm:w-40"
								>
									<span
										class="text-muted-500 dark:text-muted-400 font-sans text-sm"
									>
										{{ item.phone }}
									</span>
								</DemoFlexTableCell>
								<DemoFlexTableCell
									label="Join"
									:hide-label="index > 0"
									class="w-full sm:w-16"
								>
									<BaseTag
										color="success"
										flavor="pastel"
										shape="full"
										>Active</BaseTag
									>
								</DemoFlexTableCell>
								<DemoFlexTableCell
									label="relations"
									:hide-label="index > 0"
									tablet-hidden
									class="w-full sm:w-[160px] text-xs text-muted-500"
								>
									{{ item.user.date_joined }}
								</DemoFlexTableCell>
								<DemoFlexTableCell
									label="action"
									:hide-label="index > 0"
								>
									<BaseButtonAction
										color="muted"
										@click="openModal(item)"
									>
										<span>Edit</span>
									</BaseButtonAction>
								</DemoFlexTableCell>
							</template>
						</DemoFlexTableRow>
					</TransitionGroup>
				</div>
				<div class="flex items-center justify-center my-2">
					<BaseButton
						shape="rounded"
						class="flex w-[200px] justify-center"
						@click="loadMore(customers.next)"
						v-if="customers && customers.next"
					>
						Load More
					</BaseButton>
				</div>
			</div>
		</TairoContentWrapper>
	</div>
</template>
