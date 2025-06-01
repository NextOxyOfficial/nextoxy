<template>
	<section class="container mx-auto my-2">
		<div class="flex gap-1">
			<div class="grp flex-1">
				<label for="title">Post Title</label>
				<input
					v-model="post.title"
					type="text"
					id="title"
					name="title"
					placeholder="Title"
					class="block p-2 border w-full rounded"
				/>
			</div>
			<div class="grp">
				<label for="title">Type</label>
				<select
					name=""
					v-model="post.type"
					class="block p-2 h-[43px] border w-full rounded"
				>
					<option value="blog">Blog</option>
					<option value="documentation">Documentation</option>
					<option value="help_center">Help Center</option>
				</select>
			</div>
			<div
				class="flex-1 max-w-[300px]"
				v-if="cats"
			>
				<label for="title">Select Category</label>
				<select
					v-model="post.category__name"
					class="block p-[10px] border w-full rounded"
				>
					<option value="">Select Category</option>
					<option
						v-for="cat in cats"
						:key="cat.id"
						:value="cat.name"
					>
						{{ cat.name }}
					</option>
				</select>
			</div>
		</div>
		<div class="flex gap-1 my-4">
			<div class="grp">
				<label for="title">Post Author Name</label>
				<input
					v-model="post.author"
					type="text"
					id="title"
					name="title"
					placeholder="Title"
					class="block p-2 border w-full rounded"
				/>
			</div>
			<div class="grp flex-1 max-w-[500px]">
				<img
					:src="Api.baseURL + post.image"
					v-if="post.image"
					alt=""
					class="max-w-[300px]"
					srcset=""
				/>
				<label for="title">Featured Image</label>
				<input
					@change="imageAdded"
					type="file"
					id="title"
					name="title"
					placeholder="Title"
					class="block p-2 h-[43px] border w-full rounded"
				/>
			</div>
		</div>

		<div class="w-full">
			<CommonTiptap
				:content="post.content"
				@updateContent="
					(newVal) => {
						post.content = newVal;
					}
				"
			/>
		</div>

		<div class="my-3 flex justify-end">
			<button
				@click="
					Api.post('/api/account/blog/', post).then((response) => {
						$router.push({ path: '/manage/no-blog' });
					})
				"
				class="btn bg-blue-500 text-white rounded px-3 py-2"
			>
				Publish
			</button>
		</div>
	</section>
</template>

<script setup>
	const Api = useApi();
	definePageMeta({
		layout: "manage",
	});
	const post = ref({
		id: "",
		type: "blog",
		title: "",
		content: "",
		category__name: "",
		image: "",
		author: "NextOxy",
	});

	const route = useRouter();
	const id = route.currentRoute.value.params.id;
	if (id != "new") {
		Api.get(`/api/account/blog/?id=${id}`)
			.then((response) => {
				post.value.id = response.data["id"];
				post.value.title = response.data["title"];
				post.value.content = response.data["content"];
				if (response.data["category"])
					post.value.category__name = response.data["category"]["name"];
				post.value.image = response.data["image"];
			})
			.catch((error) => {
				console.log(error);
			});
	} else {
		post.value.content = "<p>Hello World</p>";
	}

	const handleUpdateContent = (updatedContent) => {
		post.value.content = updatedContent;
	};
	const cats = ref("");
	const getCats = () => {
		Api.get("/api/account/blog_categories/")
			.then((response) => {
				cats.value = response.data;
			})
			.catch((error) => {
				console.log(error);
			});
	};
	getCats();
	const imageAdded = (e) => {
		const file = e.target.files[0];
		const reader = new FileReader();
		reader.readAsDataURL(file);
		reader.onload = () => {
			post.value.image = reader.result;
		};
	};
</script>

<style scoped></style>
