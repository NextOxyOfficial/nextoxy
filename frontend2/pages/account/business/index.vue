<template>
	<div class="py-5">
		<div
			shape="rounded"
			class="mx-auto max-w-2xl px-1 md:px-3 lg:px-5 rounded min-h-[85vh]"
		>
			<!-- ====== Table Grid Section Start -->
			<BaseButton
				class="ml-4"
				color="success"
				size="sm"
				to="/account"
				flavor="pastel"
			>
				<Icon
					name="ph:arrow-fat-lines-left-thin"
					class="h-4 w-4 mr-1"
				/>
				Back to services
			</BaseButton>

			<section class="">
				<div class="mx-auto px-1 md:px-4 sm:container">
					<div class="my-3">
						<div
							class="w-full flex items-center justify-between flex-wrap whitespace-nowrap gap-3"
						>
							<h2 class="mb-2 sm:text-2xl font-semibold text-[18px]">
								Your sites
							</h2>
							<nuxt-link to="/account/ecommerce/create">
								<BaseButton
									class="ml-4"
									color="primary"
									size="sm"
									flavor="pastel"
								>
									<Icon
										name="solar:shop-2-broken"
										class="h-4 w-4 mr-1"
									/>
									Create New Site
								</BaseButton>
							</nuxt-link>
						</div>
						<p class="text-body-color text-base mt-4 sm:mt-3">
							Create as many sites you want
						</p>
					</div>
					<BasePlaceload
						v-if="preloader"
						class="h-[170px] w-full rounded opacity-35"
					/>
					<BaseCard
						v-else
						shape="curved"
						class="flex flex-wrap mb-2 !bg-white/70 dark:!bg-slate-800/20"
						v-for="site in ecommerceList"
						:key="site.email"
					>
						<div class="w-full">
							<div
								class="shadow-card relative items-center rounded-lg p-3 flex flex-wrap gap-2 md:gap-6"
							>
								<div
									class="mb-4 w-full max-w-[80px] md:max-w-[120px] overflow-hidden rounded sm:mb-0 relative"
								>
									<p class="text-xs p-1 bg-white top-1 left-1 rounded border">
										<span
											v-if="site.active"
											class="text-lime-600 font-bold"
											>• Active</span
										>
										<span
											v-else
											class="text-rose-600"
											>• Inactive</span
										>
									</p>
									<img
										v-if="site.logo"
										:src="Api.baseURL + site.logo"
										alt="table grid"
										class="aspect-square h-full w-full object-contain"
									/>
									<img
										v-else
										src="/static/frontend/images/account/shop-manage.png"
										alt="table grid"
										class="aspect-square h-full w-full object-contain"
									/>
								</div>
								<div class="w-full flex-1 border-l pl-3 md:pl-6">
									<BaseHeading
										as="h4"
										size="sm"
										weight="semibold"
										lead="tight"
										class="text-muted-800 mb-1 dark:text-white"
										>{{ site.name }}</BaseHeading
									>
									<BaseParagraph
										size="xs"
										lead="tight"
										class="text-muted-500 my-1 mb-4"
										>Created: {{ site.created_at }}</BaseParagraph
									>
									<div
										class="text-body-color text-sm flex gap-1 flex-wrap hidden"
										v-if="site.domains.length"
									>
										<span
											v-for="domain in site.domains"
											class="text-sm inline text-blue-500 border-r pr-1"
										>
											<a
												:href="'https://' + domain.domain + '.nextoxy.com'"
												v-if="domain.subdomain"
												href=""
												target="_blank"
												>{{ domain.domain }}.nextoxy.com</a
											>
											<a
												:href="'https://' + domain.domain"
												v-else
												href=""
												target="_blank"
												>{{ domain.domain }}</a
											>
										</span>
									</div>
									<div
										class="flex gap-2 my-2 flex-wrap whitespace-nowrap justify-start items-center sm:mt-3"
									>
										<BaseButton
											color="primary"
											size="xs"
											@click="selectedSite(site.id)"
										>
											<a class="flex items-center text-xs py-2 px-3">
												Manage
												<svg
													xmlns="http://www.w3.org/2000/svg"
													width="16"
													height="16"
													viewBox="0 0 24 24"
												>
													<path
														fill="currentColor"
														d="M6.4 18L5 16.6L14.6 7H6V5h12v12h-2V8.4Z"
													/>
												</svg>
											</a>
										</BaseButton>
										<BaseButton
											color="danger"
											flavor="pastel"
											size="xs"
											@click="openModal(site)"
										>
											<a class="flex items-center text-xs py-2 px-3">
												<svg
													class="cursor-pointer"
													xmlns="http://www.w3.org/2000/svg"
													width="16"
													height="16"
													viewBox="0 0 24 24"
												>
													<path
														fill="currentColor"
														d="M7 21q-.825 0-1.413-.588T5 19V6H4V4h5V3h6v1h5v2h-1v13q0 .825-.588 1.413T17 21H7ZM17 6H7v13h10V6ZM9 17h2V8H9v9Zm4 0h2V8h-2v9ZM7 6v13V6Z"
													/>
												</svg>
												Delete
											</a>
										</BaseButton>
									</div>
								</div>
							</div>
						</div>
					</BaseCard>
				</div>
				<!-- popup -->
				<TransitionRoot
					appear
					:show="isCreatorOpen"
					as="template"
				>
					<Dialog
						as="div"
						@close="closeModal"
						class="relative z-10"
					>
						<TransitionChild
							as="template"
							enter="duration-300 ease-out"
							enter-from="opacity-0"
							enter-to="opacity-100"
							leave="duration-200 ease-in"
							leave-from="opacity-100"
							leave-to="opacity-0"
						>
							<div class="fixed inset-0 bg-black bg-opacity-25" />
						</TransitionChild>

						<div class="fixed inset-0 overflow-y-auto">
							<div
								class="flex min-h-full items-center justify-center p-4 text-center"
							>
								<TransitionChild
									as="template"
									enter="duration-300 ease-out"
									enter-from="opacity-0 scale-95"
									enter-to="opacity-100 scale-100"
									leave="duration-200 ease-in"
									leave-from="opacity-100 scale-100"
									leave-to="opacity-0 scale-95"
								>
									<DialogPanel
										class="w-full max-w-md transform overflow-hidden rounded-2xl bg-white dark:bg-slate-900 p-6 text-left align-middle shadow-xl transition-all"
									>
										<DialogTitle
											as="h3"
											class="text-lg font-medium leading-6"
										>
											Delete "{{ deleteShop.name }}"
										</DialogTitle>
										<div class="mt-2">
											<p class="text-sm my-1 text-muted-500">
												Are you sure? You can't undo this action afterwards.
											</p>
											<p class="text-sm my-1 text-muted-500">
												🚨 This will permanently delete the shop and all of its
												data!
											</p>
											<br />
											<BaseInput
												v-model="deleteShop.confirm_name"
												shape="rounded"
												:label="
													'Please Type `' + deleteShop.name + '` To Confirm'
												"
												placeholder="Shop Name"
											/>
											<br />
											<div class="flex items-center gap-1 flex-wrap">
												<BaseCheckbox
													class="my-2"
													v-model="deleteShop.confirm_checkbox"
													label="I agree to the"
													shape="straight"
													color="danger"
												/>
												<nuxt-link
													to="/terms-of-service"
													class="text-blue-500"
													>Deletion Terms.</nuxt-link
												>
											</div>
										</div>

										<div class="mt-4 flex gap-2">
											<BaseButton
												@click="confirmDelete"
												v-if="
													deleteShop.confirm_checkbox &&
													deleteShop.name == deleteShop.confirm_name
												"
												color="danger"
												flavor="pastel"
												>Confirm & Delete</BaseButton
											>
											<BaseButton
												v-else
												class="opacity-50"
												color="danger"
												flavor="pastel"
												>Confirm & Delete</BaseButton
											>
											<BaseButton
												@click="closeModal"
												color="default"
												flavor="pastel"
												>Cancel</BaseButton
											>
										</div>
									</DialogPanel>
								</TransitionChild>
							</div>
						</div>
					</Dialog>
				</TransitionRoot>
			</section>

			<!-- ====== Table Grid Section End -->

			<div
				:class="{ 'opacity-0': preloader }"
				class="text-center p-10 border rounded"
				v-if="ecommerceList && ecommerceList.length == 0"
			>
				<svg
					class="mx-auto h-12 w-12 text-gray-400"
					fill="none"
					viewBox="0 0 24 24"
					stroke="currentColor"
					aria-hidden="true"
				>
					<path
						vector-effect="non-scaling-stroke"
						stroke-linecap="round"
						stroke-linejoin="round"
						stroke-width="2"
						d="M9 13h6m-3-3v6m-9 1V7a2 2 0 012-2h6l2 2h6a2 2 0 012 2v8a2 2 0 01-2 2H5a2 2 0 01-2-2z"
					/>
				</svg>
				<h3 class="mt-2 text-sm font-medium text-gray-900">No Shop Yet!</h3>
				<p class="mt-1 text-sm text-gray-500">
					Get started by creating a new website.
				</p>
				<div class="mt-6">
					<nuxt-link
						to="/account/ecommerce/create"
						class="px-2 py-1 flex justify-center gap-1 items-center"
					>
						<svg
							xmlns="http://www.w3.org/2000/svg"
							width="22"
							height="22"
							viewBox="0 0 24 24"
						>
							<path
								fill="currentColor"
								d="M13 7h-2v4H7v2h4v4h2v-4h4v-2h-4V7zm-1-5C6.48 2 2 6.48 2 12s4.48 10 10 10s10-4.48 10-10S17.52 2 12 2zm0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8s8 3.59 8 8s-3.59 8-8 8z"
							/>
						</svg>
						Create New Site
					</nuxt-link>
				</div>
			</div>
		</div>
	</div>
</template>

<script setup>
	const Api = useApi();
	const preloader = useState("preloader");
	definePageMeta({
		layout: "dashboard",
	});
	const { getShop } = useShop();
	const ecommerceList = ref([]);
	function getEcommerceList() {
		Api.get("/api/account/business/").then((res) => {
			ecommerceList.value = res.data;
		});
	}
	getEcommerceList();

	async function selectedSite(id) {
		console.log("s", id);
		const activeEcommerce = useCookie("ecommerce");
		activeEcommerce.value = id;
		const activeBlog = useCookie("blog");
		activeBlog.value = "";
		const activeWebsite = useCookie("website");
		activeWebsite.value = "";
		await getShop();
		navigateTo("/ecommerce");
	}

	// const navbarOpen = ref(false);

	//   // navbar
	//   window.onscroll = function() {myFunction()};
	//   var navbar = document.getElementById("navbar");
	//   if(navbar){
	//     var sticky = navbar.offsetTop;
	//   }
	//   function myFunction() {
	//     if (!navbar){
	//       navbar = document.getElementById("navbar");
	//       if(navbar){
	//         sticky = navbar.offsetTop;
	//       }
	//     }
	//     if (window.pageYOffset >= sticky && navbar) {
	//       navbar.classList.add("sticky")
	//     } else {
	//       navbar.classList.remove("sticky");
	//     }
	//   }

	import { ref } from "vue";
	import {
		TransitionRoot,
		TransitionChild,
		Dialog,
		DialogPanel,
		DialogTitle,
	} from "@headlessui/vue";

	const isCreatorOpen = ref(false);

	const deleteShop = ref("");
	function closeModal() {
		deleteShop.value = "";
		isCreatorOpen.value = false;
	}
	function openModal(shop) {
		deleteShop.value = shop;
		isCreatorOpen.value = true;
	}
	const toaster = useToaster();
	function confirmDelete() {
		console.log(deleteShop.value.id);
		Api.get("/api/account/ecommerce/?delete=" + deleteShop.value.id).then(
			(res) => {
				ecommerceList.value = res.data;
				closeModal();
				toaster.show({
					title: "Shop Deletion Successful.",
					message: "Your Shop Has Been Deleted Successfully",
					color: "success",
					icon: "lucide:check",
					closable: true,
				});
			}
		);
	}
</script>

<style scoped>
	.stripe:nth-child(odd) {
		background-color: #f3f3f380;
	}
</style>
