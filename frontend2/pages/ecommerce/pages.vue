<template>
	<section class="relative z-10 overflow-hidden py-12">
		<div class="container mx-auto">
			<div
				class="border-b border-gray-200/10 pb-5 sm:flex sm:items-center sm:justify-between"
			>
				<CommonTitleIcon
					:filename="'pages-min.png'"
					:title="'Site Pages'"
				/>
				<div class="mt-3 sm:mt-0 sm:ml-4">
					<a
						@click="addPage"
						class="cursor-pointer inline-flex items-center rounded border border-transparent bg-primary-600 px-4 py-2 text-sm font-medium text-white shadow-sm hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2"
						>+ Add New Page</a
					>
				</div>
			</div>
			<BasePlaceload
				v-if="preloader"
				class="h-[50vh] w-full rounded opacity-35"
			/>
			<TairoFlexTable v-else>
				<template #header>
					<TairoFlexTableHeading
						class="max-w-[250px]"
						type="grow"
						>Page</TairoFlexTableHeading
					>
					<TairoFlexTableHeading type="grow"
						>Creation Date</TairoFlexTableHeading
					>
					<TairoFlexTableHeading type="stable"></TairoFlexTableHeading>
					<TairoFlexTableHeading type="stable"></TairoFlexTableHeading>
				</template>

				<TairoFlexTableRow
					v-for="page in pages.results"
					:key="page.id"
					shape="straight"
				>
					<TairoFlexTableCell
						type="grow"
						data-content="Member"
						class="max-w-[250px]"
					>
						<div class="flex items-center">
							<div class="ms-3 leading-none">
								<h4 class="font-sans text-sm font-medium">
									{{ page.title }}
								</h4>

								<p class="text-muted-400 font-sans text-xs font-normal">
									<a
										target="_blank"
										:href="
											'http://' + shop.name + '.nextoxy.com/page/' + page.slug
										"
										class="text-indigo-700 cursor-pointer"
										>pages/{{ page.slug }}</a
									>
								</p>
							</div>
						</div>
					</TairoFlexTableCell>

					<TairoFlexTableCell
						class="whitespace-nowrap"
						type="grow"
						data-content="Expertise"
						light
					>
						{{ page.created_at }}
					</TairoFlexTableCell>

					<TairoFlexTableCell
						type="stable"
						data-content="Actions"
					>
						<BaseButton
							@click="modifyPage(page)"
							color="primary"
							flavor="outline"
							shape="straight"
							class="scale-90"
						>
							Modify
						</BaseButton>
					</TairoFlexTableCell>
					<TairoFlexTableCell
						type="stable"
						data-content="Actions"
					>
						<BaseButton
							@click="deletePage(page.id)"
							color="primary"
							flavor="outline"
							shape="straight"
							class="scale-90"
						>
							Delete
						</BaseButton>
					</TairoFlexTableCell>
				</TairoFlexTableRow>
			</TairoFlexTable>
			<CommonOver :show="add">
				<DialogPanel
					class="pointer-events-auto relative w-screen max-w-6xl bg-white dark:bg-slate-800"
				>
					<TransitionChild
						as="template"
						enter="ease-in-out duration-500"
						enter-from="opacity-0"
						enter-to="opacity-100"
						leave="ease-in-out duration-500"
						leave-from="opacity-100"
						leave-to="opacity-0"
					>
						<div
							class="absolute top-0 left-1 md:-left-2 flex pt-1 pr-2 sm:-ml-10 sm:pr-4"
						>
							<span
								type="button"
								class="rounded-full shadow-xl cursor-pointer p-1 bg-white dark:bg-slate-800"
								@click="add = false"
							>
								<span class="sr-only">Close panel</span>
								<svg
									xmlns="http://www.w3.org/2000/svg"
									width="32"
									height="32"
									viewBox="0 0 24 24"
								>
									<path
										fill="currentColor"
										d="M20 6.91L17.09 4L12 9.09L6.91 4L4 6.91L9.09 12L4 17.09L6.91 20L12 14.91L17.09 20L20 17.09L14.91 12L20 6.91Z"
									/>
								</svg>
							</span>
						</div>
					</TransitionChild>
					<div
						class="flex h-full flex-col overflow-y-scroll py-6 shadow-xl"
						v-if="add"
					>
						<div class="px-4 sm:px-6">
							<DialogTitle
								class="font-semibold leading-6 text-gray-900 text-center"
								>Site Page</DialogTitle
							>
						</div>
						<div class="relative mt-6 flex-1 px-4 sm:px-6">
							<label
								for="title"
								class="block text-sm font-medium text-gray-700"
								>Page Title</label
							>
							<input
								type="text"
								name="title"
								id="title"
								@keyup="makeSlug"
								v-model="newPage.title"
								placeholder="Page Title"
								class="my-2 border px-2 py-2 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300/10 rounded-md"
							/>
							<label
								for="slug"
								class="block text-sm font-medium text-gray-700"
								>Page Slug</label
							>
							<input
								type="text"
								name="slug"
								id="slug"
								v-model="newPage.slug"
								placeholder="Page Slug"
								class="my-2 border px-2 py-2 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300/10 rounded-md"
							/>
							<CommonTiptap
								:content="newPage.content"
								@updateContent="
									(newVal) => {
										newPage.content = newVal;
									}
								"
							/>
							<button
								@click="saveContent"
								class="px-6 py-2 my-4 mr-2 bg-primary-500 rounded text-white"
							>
								Save Changes
							</button>
							<button
								@click="add = false"
								class="px-6 py-2 my-4 bg-slate-100 border="
							>
								Close
							</button>
						</div>
					</div>
				</DialogPanel>
			</CommonOver>
		</div>
	</section>
</template>

<script setup>
	import {
		Dialog,
		DialogPanel,
		DialogTitle,
		TransitionChild,
		TransitionRoot,
	} from "@headlessui/vue";
	import Editor from "@tinymce/tinymce-vue";
	definePageMeta({
		layout: "dashboard",
	});
	const preloader = useState("preloader");
	const { notifs } = useAuth();
	const { $swal } = useNuxtApp();
	const Api = useApi();
	const { shop } = useShop();
	const pages = ref("");
	async function getPages() {
		const response = await Api.get("/api/ecommerce/dash/pages");
		console.log(response);
		pages.value = response.data;
	}
	getPages();

	const add = ref(false);
	const newPage = ref({
		title: "",
		slug: "",
		content: "",
	});
	function modifyPage(page) {
		newPage.value = page;
		add.value = true;
	}
	function addPage() {
		newPage.value = {
			title: "",
			slug: "",
			content: "",
		};
		add.value = true;
	}
	function makeSlug() {
		newPage.value.slug = newPage.value.title
			.toLowerCase()
			.replace(/ /g, "-")
			.replace(/[^\w-]+/g, "");
	}
	async function saveContent() {
		if (!newPage.value.title || !newPage.value.slug || !newPage.value.content) {
			notifs.value.push({
				type: "error",
				title: "Error!",
				message: "Please fill all the fields",
			});
			return;
		}
		const response = await Api.post("/api/ecommerce/dash/pages", newPage.value);
		console.log(response);
		notifs.value.push({
			type: "success",
			message: "Page saved successfully",
		});
		getPages();
	}
	async function deletePage(id) {
		const response = await Api.del("/api/ecommerce/dash/pages?id=" + id);
		console.log(response);
		notifs.value.push({
			type: "success",
			message: "Page deleted successfully",
		});
		getPages();
	}
</script>

<style scoped></style>
