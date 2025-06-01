<template>
	<div
		class="bg-white dark:bg-slate-700 shadow p-4 rounded my-2 overflow-x-scroll"
	>
		<div class="hidden">
			<div class="flex justify-between items-center">
				<label
					for="price"
					class="block text-sm font-medium leading-6 text-gray-900"
					>Select Products</label
				>
				<SwitchGroup
					as="div"
					class="flex items-center justify-between my-2 gap-2"
				>
					<span class="flex flex-grow flex-col">
						<SwitchLabel
							as="span"
							class="text-sm font-medium text-gray-900"
							passive
							>All Products</SwitchLabel
						>
					</span>
					<Switch
						v-model="enabled"
						:class="[
							enabled ? 'bg-indigo-600' : 'bg-gray-200',
							'relative inline-flex h-6 w-11 flex-shrink-0 cursor-pointer rounded-full border-2 border-transparent transition-colors duration-200 ease-in-out focus:outline-none',
						]"
					>
						<span
							aria-hidden="true"
							:class="[
								enabled ? 'translate-x-5' : 'translate-x-0',
								'pointer-events-none inline-block h-5 w-5 transform rounded-full  shadow ring-0 transition duration-200 ease-in-out',
							]"
						/>
					</Switch>
				</SwitchGroup>
			</div>

			<small
				class="my-4"
				v-if="enabled"
				>All products Selected</small
			>
			<small
				class="my-4"
				v-else
				>No Products Added</small
			>
			<div
				class="relative mt-2 rounded-md shadow-sm"
				v-if="!enabled"
			>
				<div
					class="pointer-events-none absolute inset-y-0 left-0 flex items-center pl-3"
				>
					<span class="text-gray-500 sm:text-sm">
						<svg
							xmlns="http://www.w3.org/2000/svg"
							width="22"
							height="22"
							viewBox="0 0 2048 2048"
						>
							<path
								fill="currentColor"
								d="m960 120l832 416v1040l-832 415l-832-415V536l832-416zm625 456L960 264L719 384l621 314l245-122zM960 888l238-118l-622-314l-241 120l625 312zM256 680v816l640 320v-816L256 680zm768 1136l640-320V680l-640 320v816z"
							/>
						</svg>
					</span>
				</div>
				<input
					type="text"
					name="users"
					id="users"
					class="finder block w-full rounded-md border-0 py-1.5 pl-10 pr-20 text-gray-900 ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 sm:text-sm sm:leading-6"
					placeholder="Find with product name or id"
				/>
				<div
					class="absolute right-0 top-15 flex items-center border p-2 z-20 shadow-lg w-full"
				>
					<div class="results">
						<p class="">aa</p>
					</div>
				</div>
			</div>
		</div>
		<div
			class="my-6 min-w-[800px]"
			v-if="profile.data"
		>
			<div class="flex justify-end my-2">
				<BaseButton
					color="primary"
					@click="saveData()"
				>
					<span>Save All</span>
				</BaseButton>
			</div>
			<div
				class="flex justify-between items-center px-6 py-4 font-sm text-gray-800 bg-slate-100 rounded-t"
			>
				<label
					for="price"
					class="font-sm flex justify-center items-center gap-1"
				>
					Country
					<svg
						xmlns="http://www.w3.org/2000/svg"
						width="13"
						height="13"
						viewBox="0 0 24 24"
					>
						<path
							fill="currentColor"
							d="M6.23 20.23L8 22l10-10L8 2L6.23 3.77L14.46 12z"
						/>
					</svg>
					State
					<svg
						xmlns="http://www.w3.org/2000/svg"
						width="13"
						height="13"
						viewBox="0 0 24 24"
					>
						<path
							fill="currentColor"
							d="M6.23 20.23L8 22l10-10L8 2L6.23 3.77L14.46 12z"
						/>
					</svg>
					City
				</label>
				<div class="flex gap-2">
					<div class="w-[182px]">Shipping Charges</div>
					<div class="w-[200px]">Delivery Time</div>
					<p class="">Action</p>
				</div>
			</div>
			<div
				class="flex justify-end items-center px-[1px] border-b py-4 text-sm text-gray-700 gap-6"
			>
				<h6 class="mr-6">Set Default:</h6>
				<div class="flex gap-6">
					<div class="flex gap-1 items-center justify-center">
						<svg
							xmlns="http://www.w3.org/2000/svg"
							width="18"
							height="18"
							viewBox="0 0 24 24"
						>
							<path
								d="M12 2a10 10 0 0 1 10 10a10 10 0 0 1-10 10A10 10 0 0 1 2 12A10 10 0 0 1 12 2m0 2a8 8 0 0 0-8 8a8 8 0 0 0 8 8a8 8 0 0 0 8-8a8 8 0 0 0-8-8m-1 13v-1H9v-2h4v-1h-3a1 1 0 0 1-1-1V9a1 1 0 0 1 1-1h1V7h2v1h2v2h-4v1h3a1 1 0 0 1 1 1v3a1 1 0 0 1-1 1h-1v1h-2z"
								fill="currentColor"
							/>
						</svg>
						<input
							v-model="profile.data.default.charge"
							type="number"
							name=""
							id=""
							class="w-[145px] rounded border px-2 text-sm py-1"
							placeholder="Shipping Charge"
						/>
					</div>
					<div class="flex items-center gap-1">
						<svg
							xmlns="http://www.w3.org/2000/svg"
							width="18"
							height="18"
							viewBox="0 0 24 24"
						>
							<path
								fill="currentColor"
								d="M12 20a8 8 0 0 0 8-8a8 8 0 0 0-8-8a8 8 0 0 0-8 8a8 8 0 0 0 8 8m0-18a10 10 0 0 1 10 10a10 10 0 0 1-10 10C6.47 22 2 17.5 2 12A10 10 0 0 1 12 2m.5 5v5.25l4.5 2.67l-.75 1.23L11 13V7h1.5Z"
							/>
						</svg>
						<input
							v-model="profile.data.default.from"
							type="number"
							name=""
							id=""
							class="w-20 rounded border px-2 text-sm py-1"
							placeholder="From"
						/>
						<input
							v-model="profile.data.default.to"
							type="number"
							name=""
							id=""
							class="w-20 rounded border px-2 text-sm py-1"
							placeholder="To"
						/>
						<p class="text-xs">Days</p>
					</div>
				</div>
				<span
					class="px-2 py-0 inline-block m-2 text-slate-700 rounded bg-slate-500/20 hover:shadow"
				>
					<svg
						class="m-1"
						xmlns="http://www.w3.org/2000/svg"
						width="18"
						height="18"
						viewBox="0 0 24 24"
					>
						<g
							fill="none"
							stroke="currentColor"
							stroke-linecap="round"
							stroke-linejoin="round"
							stroke-width="2"
						>
							<path
								d="M18.37 2.63L14 7l-1.59-1.59a2 2 0 0 0-2.82 0L8 7l9 9l1.59-1.59a2 2 0 0 0 0-2.82L17 10l4.37-4.37a2.12 2.12 0 1 0-3-3Z"
							/>
							<path d="M9 8c-2 3-4 3.5-7 4l8 10c2-1 6-5 6-7m-1.5 2.5L4.5 15" />
						</g>
					</svg>
				</span>
			</div>
			<div class="countries">
				<!-- countries  -->
				<div
					class="stripe"
					v-for="country in countries"
					:key="country.id"
				>
					<div
						class="country border border-gray-50 my-1 p-[1px] cursor-pointer hover:shadow-sm rounded flex justify-between items-center"
						:class="{
							'text-shadow': country == activeCountry,
							active: country == activeCountry,
						}"
					>
						<h6
							class="flex text-sm items-center gap-1 cursor-pointer flex-1"
							@click="
								activeCountry = activeCountry === country ? null : country
							"
						>
							<svg
								class="h-6"
								v-if="country == activeCountry"
								xmlns="http://www.w3.org/2000/svg"
								width="32"
								height="32"
								viewBox="0 0 24 24"
							>
								<path
									fill="currentColor"
									d="M19 12.998H5v-2h14z"
								/>
							</svg>
							<svg
								class="h-6"
								v-else
								xmlns="http://www.w3.org/2000/svg"
								width="32"
								height="32"
								viewBox="0 0 24 24"
							>
								<path
									fill="currentColor"
									d="M18 12.998h-5v5a1 1 0 0 1-2 0v-5H6a1 1 0 0 1 0-2h5v-5a1 1 0 0 1 2 0v5h5a1 1 0 0 1 0 2z"
								/>
							</svg>
							{{ country.name }}
						</h6>
						<div class="flex gap-6">
							<div class="flex gap-6">
								<div class="flex gap-1 items-center justify-center">
									<svg
										xmlns="http://www.w3.org/2000/svg"
										width="18"
										height="18"
										viewBox="0 0 24 24"
									>
										<path
											d="M12 2a10 10 0 0 1 10 10a10 10 0 0 1-10 10A10 10 0 0 1 2 12A10 10 0 0 1 12 2m0 2a8 8 0 0 0-8 8a8 8 0 0 0 8 8a8 8 0 0 0 8-8a8 8 0 0 0-8-8m-1 13v-1H9v-2h4v-1h-3a1 1 0 0 1-1-1V9a1 1 0 0 1 1-1h1V7h2v1h2v2h-4v1h3a1 1 0 0 1 1 1v3a1 1 0 0 1-1 1h-1v1h-2z"
											fill="currentColor"
										/>
									</svg>
									<input
										v-model="country.charge"
										:placeholder="profile.data.default.charge"
										type="number"
										name=""
										id=""
										class="w-[145px] rounded border px-2 text-sm py-1"
										placeholder="Shipping Charge"
									/>
								</div>
								<div class="flex items-center gap-1">
									<svg
										xmlns="http://www.w3.org/2000/svg"
										width="18"
										height="18"
										viewBox="0 0 24 24"
									>
										<path
											fill="currentColor"
											d="M12 20a8 8 0 0 0 8-8a8 8 0 0 0-8-8a8 8 0 0 0-8 8a8 8 0 0 0 8 8m0-18a10 10 0 0 1 10 10a10 10 0 0 1-10 10C6.47 22 2 17.5 2 12A10 10 0 0 1 12 2m.5 5v5.25l4.5 2.67l-.75 1.23L11 13V7h1.5Z"
										/>
									</svg>
									<input
										v-model="country.from"
										:placeholder="profile.data.default.from"
										type="number"
										name=""
										id=""
										class="w-20 rounded border px-2 text-sm py-1"
										placeholder="From"
									/>
									<input
										v-model="country.to"
										:placeholder="profile.data.default.to"
										type="number"
										name=""
										id=""
										class="w-20 rounded border px-2 text-sm py-1"
										placeholder="To"
									/>
									<p class="text-xs">Days</p>
								</div>
							</div>
							<span
								class="px-2 py-0 inline-block m-2 text-slate-700 rounded bg-slate-500/20 hover:shadow"
							>
								<svg
									class="m-1"
									xmlns="http://www.w3.org/2000/svg"
									width="18"
									height="18"
									viewBox="0 0 24 24"
								>
									<g
										fill="none"
										stroke="currentColor"
										stroke-linecap="round"
										stroke-linejoin="round"
										stroke-width="2"
									>
										<path
											d="M18.37 2.63L14 7l-1.59-1.59a2 2 0 0 0-2.82 0L8 7l9 9l1.59-1.59a2 2 0 0 0 0-2.82L17 10l4.37-4.37a2.12 2.12 0 1 0-3-3Z"
										/>
										<path
											d="M9 8c-2 3-4 3.5-7 4l8 10c2-1 6-5 6-7m-1.5 2.5L4.5 15"
										/>
									</g>
								</svg>
							</span>
						</div>
					</div>
					<div v-if="country == activeCountry">
						<!-- states  -->
						<div
							class="stripe"
							v-for="state in states"
							:key="state.id"
						>
							<div
								class="state ml-4 border border-slate-100 cursor-pointer my-1 p-[1px] hover:shadow-sm rounded flex justify-between items-center"
								:class="{
									'text-shadow': state == activeState,
									active: state == activeState,
								}"
							>
								<h6
									class="flex text-base items-center gap-1 cursor-pointer flex-1"
									@click="activeState = activeState === state ? null : state"
								>
									<svg
										class="h-5"
										v-if="state == activeState"
										xmlns="http://www.w3.org/2000/svg"
										width="32"
										height="32"
										viewBox="0 0 24 24"
									>
										<path
											fill="currentColor"
											d="M19 12.998H5v-2h14z"
										/>
									</svg>
									<svg
										class="h-5"
										v-else
										xmlns="http://www.w3.org/2000/svg"
										width="32"
										height="32"
										viewBox="0 0 24 24"
									>
										<path
											fill="currentColor"
											d="M18 12.998h-5v5a1 1 0 0 1-2 0v-5H6a1 1 0 0 1 0-2h5v-5a1 1 0 0 1 2 0v5h5a1 1 0 0 1 0 2z"
										/>
									</svg>
									{{ state.name }}
								</h6>
								<div class="flex gap-6">
									<div class="flex gap-6">
										<div class="flex gap-1 items-center justify-center">
											<svg
												xmlns="http://www.w3.org/2000/svg"
												width="18"
												height="18"
												viewBox="0 0 24 24"
											>
												<path
													d="M12 2a10 10 0 0 1 10 10a10 10 0 0 1-10 10A10 10 0 0 1 2 12A10 10 0 0 1 12 2m0 2a8 8 0 0 0-8 8a8 8 0 0 0 8 8a8 8 0 0 0 8-8a8 8 0 0 0-8-8m-1 13v-1H9v-2h4v-1h-3a1 1 0 0 1-1-1V9a1 1 0 0 1 1-1h1V7h2v1h2v2h-4v1h3a1 1 0 0 1 1 1v3a1 1 0 0 1-1 1h-1v1h-2z"
													fill="currentColor"
												/>
											</svg>
											<input
												v-model="state.charge"
												:placeholder="
													activeCountry.charge || profile.data.default.charge
												"
												type="number"
												name=""
												id=""
												class="w-[145px] rounded border px-2 text-sm py-1"
												placeholder="Shipping Charge"
											/>
										</div>
										<div class="flex items-center gap-1">
											<svg
												xmlns="http://www.w3.org/2000/svg"
												width="18"
												height="18"
												viewBox="0 0 24 24"
											>
												<path
													fill="currentColor"
													d="M12 20a8 8 0 0 0 8-8a8 8 0 0 0-8-8a8 8 0 0 0-8 8a8 8 0 0 0 8 8m0-18a10 10 0 0 1 10 10a10 10 0 0 1-10 10C6.47 22 2 17.5 2 12A10 10 0 0 1 12 2m.5 5v5.25l4.5 2.67l-.75 1.23L11 13V7h1.5Z"
												/>
											</svg>
											<input
												v-model="state.from"
												:placeholder="
													activeCountry.from || profile.data.default.from
												"
												type="number"
												name=""
												id=""
												class="w-20 rounded border px-2 text-sm py-1"
												placeholder="From"
											/>
											<input
												v-model="state.to"
												:placeholder="
													activeCountry.to || profile.data.default.to
												"
												type="number"
												name=""
												id=""
												class="w-20 rounded border px-2 text-sm py-1"
												placeholder="To"
											/>
											<p class="text-xs">Days</p>
										</div>
									</div>
									<span
										class="px-2 py-0 inline-block m-2 text-slate-700 rounded bg-slate-500/20 hover:shadow"
									>
										<svg
											class="m-1"
											xmlns="http://www.w3.org/2000/svg"
											width="18"
											height="18"
											viewBox="0 0 24 24"
										>
											<g
												fill="none"
												stroke="currentColor"
												stroke-linecap="round"
												stroke-linejoin="round"
												stroke-width="2"
											>
												<path
													d="M18.37 2.63L14 7l-1.59-1.59a2 2 0 0 0-2.82 0L8 7l9 9l1.59-1.59a2 2 0 0 0 0-2.82L17 10l4.37-4.37a2.12 2.12 0 1 0-3-3Z"
												/>
												<path
													d="M9 8c-2 3-4 3.5-7 4l8 10c2-1 6-5 6-7m-1.5 2.5L4.5 15"
												/>
											</g>
										</svg>
									</span>
								</div>
							</div>
							<div v-if="state == activeState">
								<!-- cities  -->
								<div
									class="stripe"
									v-for="city in cities"
									:key="city.id"
								>
									<div
										class="city ml-8 border border-slate-100 my-1 p-[1px] hover:shadow-sm rounded flex justify-between items-center"
									>
										<h6
											class="flex text-base items-center gap-1 cursor-pointer"
										>
											<svg
												class="h-5"
												xmlns="http://www.w3.org/2000/svg"
												width="32"
												height="32"
												viewBox="0 0 24 24"
											>
												<path
													fill="currentColor"
													d="M12 12q.825 0 1.413-.588T14 10q0-.825-.588-1.413T12 8q-.825 0-1.413.588T10 10q0 .825.588 1.413T12 12Zm0 9.625q-.2 0-.4-.075t-.35-.2Q7.6 18.125 5.8 15.362T4 10.2q0-3.75 2.413-5.975T12 2q3.175 0 5.588 2.225T20 10.2q0 2.4-1.8 5.163t-5.45 5.987q-.15.125-.35.2t-.4.075Z"
												/>
											</svg>
											{{ city.name }}
										</h6>
										<div class="flex gap-6">
											<div class="flex gap-6">
												<div class="flex gap-1 items-center justify-center">
													<svg
														xmlns="http://www.w3.org/2000/svg"
														width="18"
														height="18"
														viewBox="0 0 24 24"
													>
														<path
															d="M12 2a10 10 0 0 1 10 10a10 10 0 0 1-10 10A10 10 0 0 1 2 12A10 10 0 0 1 12 2m0 2a8 8 0 0 0-8 8a8 8 0 0 0 8 8a8 8 0 0 0 8-8a8 8 0 0 0-8-8m-1 13v-1H9v-2h4v-1h-3a1 1 0 0 1-1-1V9a1 1 0 0 1 1-1h1V7h2v1h2v2h-4v1h3a1 1 0 0 1 1 1v3a1 1 0 0 1-1 1h-1v1h-2z"
															fill="currentColor"
														/>
													</svg>
													<input
														v-model="city.charge"
														:placeholder="
															activeState.charge ||
															activeCountry.charge ||
															profile.data.default.charge
														"
														type="number"
														name=""
														id=""
														class="w-[145px] rounded border px-2 text-sm py-1"
														placeholder="Shipping Charge"
													/>
												</div>
												<div class="flex items-center gap-1">
													<svg
														xmlns="http://www.w3.org/2000/svg"
														width="18"
														height="18"
														viewBox="0 0 24 24"
													>
														<path
															fill="currentColor"
															d="M12 20a8 8 0 0 0 8-8a8 8 0 0 0-8-8a8 8 0 0 0-8 8a8 8 0 0 0 8 8m0-18a10 10 0 0 1 10 10a10 10 0 0 1-10 10C6.47 22 2 17.5 2 12A10 10 0 0 1 12 2m.5 5v5.25l4.5 2.67l-.75 1.23L11 13V7h1.5Z"
														/>
													</svg>
													<input
														v-model="city.from"
														:placeholder="
															activeState.from ||
															activeCountry.from ||
															profile.data.default.from
														"
														type="number"
														name=""
														id=""
														class="w-20 rounded border px-2 text-sm py-1"
														placeholder="From"
													/>
													<input
														v-model="city.to"
														:placeholder="
															activeState.to ||
															activeCountry.to ||
															profile.data.default.to
														"
														type="number"
														name=""
														id=""
														class="w-20 rounded border px-2 text-sm py-1"
														placeholder="To"
													/>
													<p class="text-xs">Days</p>
												</div>
											</div>
											<span
												class="px-2 py-0 inline-block m-2 text-slate-700 rounded bg-slate-500/20 hover:shadow"
											>
												<svg
													class="m-1"
													xmlns="http://www.w3.org/2000/svg"
													width="18"
													height="18"
													viewBox="0 0 24 24"
												>
													<g
														fill="none"
														stroke="currentColor"
														stroke-linecap="round"
														stroke-linejoin="round"
														stroke-width="2"
													>
														<path
															d="M18.37 2.63L14 7l-1.59-1.59a2 2 0 0 0-2.82 0L8 7l9 9l1.59-1.59a2 2 0 0 0 0-2.82L17 10l4.37-4.37a2.12 2.12 0 1 0-3-3Z"
														/>
														<path
															d="M9 8c-2 3-4 3.5-7 4l8 10c2-1 6-5 6-7m-1.5 2.5L4.5 15"
														/>
													</g>
												</svg>
											</span>
										</div>
									</div>
								</div>
							</div>
						</div>
					</div>
				</div>
				<div class="flex justify-end my-2">
					<BaseButton
						color="primary"
						@click="saveData()"
					>
						<span>Save All</span>
					</BaseButton>
				</div>
			</div>
		</div>
	</div>
</template>

<script setup>
	import { Switch, SwitchGroup, SwitchLabel } from "@headlessui/vue";
	const Api = useApi();
	const { notifs } = useAuth();
	const enabled = ref(true);
	const props = defineProps({
		profile: {
			type: String,
			default: false,
		},
	});

	console.log(props.profile);
	onMounted(() => {
		getProfileData();
		getCountries();
	});

	async function getProfileData() {
		const { data } = await Api.get(
			"/api/ecommerce/dash/shipping-data?id=" + props.profile.id
		);
		console.log(data);
		props.profile.data = data.data;
		if (!props.profile.data.default) {
			props.profile.data.default = {
				charge: 0,
				from: 0,
				to: 0,
			};
		}
	}

	// country city state
	const countries = ref([]);
	const activeCountry = ref("");
	const getCountries = async () => {
		const response = await Api.get("/api/utils/countries/");
		countries.value = response.data;
		// set values
		for (let name in props.profile.data) {
			var value = props.profile.data[name];
			for (let i = 0; i < countries.value.length; i++) {
				const country = countries.value[i];
				if (country.name == name) {
					country.charge = value.charge;
					country.from = value.from;
					country.to = value.to;
				}
			}
		}
	};
	// watch activeCountry
	watch(activeCountry, (val) => {
		if (val) {
			getStates(val.name);
		}
	});

	const states = ref("");
	const activeState = ref("");
	const getStates = async (name) => {
		const response = await Api.get(`/api/utils/states/?country=${name}`);
		console.log(response);
		states.value = response.data;
		// set values
		for (let name in props.profile.data) {
			var value = props.profile.data[name];
			for (let i = 0; i < states.value.length; i++) {
				const state = states.value[i];
				if (state.name == name) {
					state.charge = value.charge;
					state.from = value.from;
					state.to = value.to;
				}
			}
		}
	};
	// watch activeState
	watch(activeState, (val) => {
		if (val) {
			getCities(val.name);
		}
	});

	const cities = ref("");
	const getCities = async (name) => {
		const response = await Api.get(
			`/api/utils/cities/?state=${name}&country=${activeCountry.value.name}`
		);
		cities.value = response.data;
		console.log(response);
		// set values
		for (let name in props.profile.data) {
			var value = props.profile.data[name];
			for (let i = 0; i < cities.value.length; i++) {
				const city = cities.value[i];
				if (city.name == name) {
					city.charge = value.charge;
					city.from = value.from;
					city.to = value.to;
				}
			}
		}
	};

	async function saveData() {
		const data = {
			id: props.profile.id,
			data: props.profile.data,
		};
		countries.value.forEach((country) => {
			if (country.charge && country.from && country.to) {
				props.profile.data[country.name] = {
					charge: country.charge,
					from: country.from,
					to: country.to,
				};
			}
		});

		if (states.value) {
			states.value.forEach((state) => {
				if (state.charge && state.from && state.to) {
					props.profile.data[state.name] = {
						charge: state.charge,
						from: state.from,
						to: state.to,
					};
				}
			});
		}

		if (cities.value) {
			cities.value.forEach((city) => {
				if (city.charge && city.from && city.to) {
					props.profile.data[city.name] = {
						charge: city.charge,
						from: city.from,
						to: city.to,
					};
				}
			});
		}

		if (
			props.profile.data.default.charge &&
			props.profile.data.default.from &&
			props.profile.data.default.to
		) {
			props.profile.data.default = {
				charge: props.profile.data.default.charge,
				from: props.profile.data.default.from,
				to: props.profile.data.default.to,
			};
		}

		const response = await Api.post(
			"/api/ecommerce/dash/shipping-data?id=" + props.profile.id,
			{ data: props.profile.data }
		);
		console.log(response);
		getProfileData();
		notifs.value.push({
			type: "success",
			message: "Shipping data saved successfully",
		});
	}
</script>

<style scoped>
	.country.active,
	.state.active {
		background-color: #e1e1e191;
	}
	.stripe:nth-child(odd) {
		background-color: #ffffff2f;
	}

	.stripe:nth-child(even) {
		background-color: #f9fafb00;
	}
</style>
