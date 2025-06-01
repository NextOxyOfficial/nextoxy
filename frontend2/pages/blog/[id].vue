<template>
	<section class="mx-auto w-full max-w-7xl px-4 pt-36">
		<BaseCard
			shape="rounded"
			class="p-6"
			v-if="post"
		>
			<BaseHeading
				as="h1"
				size="xl"
				weight="semibold"
				lead="tight"
				class="text-muted-800 mb-2 dark:text-white"
			>
				{{ post.title }}
			</BaseHeading>
			<small>{{ post.created_at }}</small>

			<img
				:src="Api.baseURL + post.image"
				class="w-full max-w-[900px] max-h-[500px] mx-auto my-4"
				alt=""
				srcset=""
			/>
			<div
				class="blog-content prose lg:prose-xl"
				v-html="post.content"
			></div>
		</BaseCard>
	</section>
</template>

<script setup>
	definePageMeta({
		title: "The Nuxt & Tailwind CSS dashboard system",
		description:
			"Nuxt & Tailwind CSS dashboard system template that comes with 100+ prebuilt pages and 40+ custom UI components.",
		breadcrumb: {
			label: "Tairo",
		},
		layout: "landing",
	});
	const Api = useApi();
	const router = useRoute();
	const post = ref("");
	async function getPosts() {
		const res = await Api.get("/api/account/blog/?id=" + router.params.id);
		post.value = res.data;
	}
	getPosts();
</script>

<style>
	.blog-content p {
		margin-top: 8px;
		margin-bottom: 8px;
		line-height: 28px;
	}
	.blog-content h1 {
		font-size: 2em; /* Adjust the size as needed */
	}

	.blog-content h2 {
		font-size: 1.5em; /* Adjust the size as needed */
	}

	.blog-content h3 {
		font-size: 1.17em; /* Adjust the size as needed */
	}

	.blog-content h4 {
		font-size: 1em; /* Adjust the size as needed */
	}

	.blog-content h5 {
		font-size: 0.83em; /* Adjust the size as needed */
	}

	.blog-content h6 {
		font-size: 0.67em; /* Adjust the size as needed */
	}
</style>
