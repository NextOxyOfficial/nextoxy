<template>
	<section>
		<div>
			<div
				class=""
				v-if="!add"
			>
				<div
					class="mb-3 border-b border-gray-200 pb-5 flex-wrap items-center flex gap-1 justify-center md:justify-between"
				>
					<CommonTitleIcon
						:filename="'fast-delivery-min.png'"
						:title="'Shipping & Delivery'"
					/>
					<BaseButton
						color="primary"
						@click="form = true"
					>
						<Icon
							name="material-symbols:add"
							class="me-1 h-4 w-4"
						/>
						<span>Add Profile</span>
					</BaseButton>
				</div>
				<BasePlaceload
					v-if="preloader"
					class="h-[20vh] w-full rounded opacity-35"
				/>
				<div
					class="my-6"
					v-else
				>
					<dl class="mt-3 flex flex-wrap gap-1">
						<BaseCard
							shape="curved"
							class="p-3 w-full md:w-auto"
							v-for="profile in profiles"
							:key="profile.id"
						>
							<div class="flex w-full items-center gap-2">
								<Icon
									name="fa6-solid:truck-fast"
									class="me-2 block h-8 w-8"
								/>
								<div>
									<BaseHeading
										tag="h3"
										size="sm"
										weight="medium"
									>
										{{ profile.name }}
										<span
											class="text-xs border border-slate-500/50 px-1 rounded-md font-base"
											>Active</span
										>
									</BaseHeading>
									<BaseParagraph
										size="xs"
										class="text-muted-400"
									>
										<span>{{ profile.created_at }}</span>
									</BaseParagraph>
								</div>
								<div class="ms-auto">
									<BaseDropdown
										flavor="context"
										label="Dropdown"
										orientation="end"
										size="md"
										class="z-20"
										shape="curved"
									>
										<BaseDropdownItem
											@click="rename = JSON.parse(JSON.stringify(profile))"
											title="Rename"
											text="Rename Shipping Profile"
										>
											<template #start>
												<Icon
													name="ph:share-duotone"
													class="me-2 block h-5 w-5"
												/>
											</template>
										</BaseDropdownItem>
										<BaseDropdownDivider />
										<BaseDropdownItem
											@click="add = profile"
											title="Manage"
											text="Modify Shipping Profile"
										>
											<template #start>
												<Icon
													name="ph:share-duotone"
													class="me-2 block h-5 w-5"
												/>
											</template>
										</BaseDropdownItem>
										<BaseDropdownDivider />
										<BaseDropdownItem
											@click="deleteProfile(profile.id)"
											title="Delete"
											text="Delete Shipping Profile"
										>
											<template #start>
												<Icon
													name="ph:trash-duotone"
													class="me-2 block h-5 w-5"
												/>
											</template>
										</BaseDropdownItem>
									</BaseDropdown>
								</div>
							</div>
						</BaseCard>
					</dl>
				</div>
			</div>
			<div
				class="my-5"
				v-else
			>
				<div
					class="mb-3 border-b border-gray-200 pb-5 sm:flex sm:items-center sm:justify-between items-center"
				>
					<BaseButton
						color="primary"
						@click="add = false"
					>
						<Icon
							name="lucide:arrow-left"
							class="me-1 h-4 w-4"
						/>
						<span>Back</span>
					</BaseButton>
					<h3 class="text-lg font-medium leading-6">{{ add.name }}</h3>
				</div>
				<EcommerceFormsShipping :profile="add" />
			</div>
			<BaseCard
				shape="rounded"
				class="mb-4 justify-start gap-2 border-b border-gray-200 px-4 py-3 sm:flex sm:items-center"
				v-if="form"
			>
				<input
					v-model="newProfile.name"
					type="text"
					class="block w-full max-w-xs rounded-md border border-gray-300 px-3 py-2 shadow-sm focus:border-indigo-500 focus:outline-none focus:ring-indigo-500 sm:text-sm my-2"
					placeholder="Profile Name"
				/>
				<button
					@click="addProfile"
					type="button"
					class="inline-flex items-center rounded-md border border-transparent bg-indigo-600 px-4 py-2 text-sm font-medium text-white shadow-sm hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2 mr-1 md:mr-0"
				>
					+ Add
				</button>
				<button
					@click="form = false"
					type="button"
					class="inline-flex items-center rounded-md border bg-slate-100 px-4 py-2 text-sm font-medium text-slate-700 shadow hover:bg-slate-200 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2"
				>
					Cancel
				</button>
			</BaseCard>
			<BaseCard
				shape="rounded"
				class="mb-4 justify-start gap-2 border-b border-gray-200 px-4 py-3 sm:flex sm:items-center"
				v-if="rename"
			>
				<input
					v-model="rename.name"
					type="text"
					class="block w-full max-w-xs rounded-md border border-gray-300 px-3 py-2 shadow-sm focus:border-indigo-500 focus:outline-none focus:ring-indigo-500 sm:text-sm"
					placeholder="Profile Name"
				/>
				<button
					@click="renameProfile"
					type="button"
					class="inline-flex items-center rounded-md border border-transparent bg-indigo-600 px-4 py-2 text-sm font-medium text-white shadow-sm hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2"
				>
					Rename Profile
				</button>
				<button
					@click="deleteProfile(rename.id)"
					type="button"
					class="inline-flex items-center rounded-md border bg-slate-100 px-4 py-2 text-sm font-medium text-slate-700 shadow hover:bg-slate-200 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2"
				>
					Delete
				</button>
				<button
					@click="rename = ''"
					type="button"
					class="inline-flex items-center rounded-md border bg-slate-100 px-4 py-2 text-sm font-medium text-slate-700 shadow hover:bg-slate-200 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2"
				>
					Cancel
				</button>
			</BaseCard>
		</div>
	</section>
</template>

<script setup>
	definePageMeta({
		layout: "dashboard",
	});
	const preloader = useState("preloader");
	const Api = useApi();
	const { $swal } = useNuxtApp();

	const profiles = ref([]);
	const getProfiles = async () => {
		const { data } = await Api.get("/api/ecommerce/dash/shipping");
		profiles.value = data;
		console.log(data);
	};
	getProfiles();
	const add = ref(false);
	const form = ref(false);
	const newProfile = ref({
		name: "",
	});
	const addProfile = async () => {
		const res = await Api.post(
			"/api/ecommerce/dash/shipping",
			newProfile.value
		);
		getProfiles();
		form.value = false;
		newProfile.value.name = "";
	};

	const rename = ref("");
	const renameProfile = async () => {
		const res = await Api.put("/api/ecommerce/dash/shipping", rename.value);
		getProfiles();
		rename.value = "";
	};
	const deleteProfile = async (id) => {
		const res = await Api.del("/api/ecommerce/dash/shipping?id=" + id);
		getProfiles();
		rename.value = "";
	};
</script>

<style scoped></style>
