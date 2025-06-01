<template>
	<div>
		<h5 class="my-2 font-bold">What are you trying to setup?</h5>
		<p class="text-sm">
			In this question, we aim to understand your objective for setup,
			specifically in the context of software account registration. Tell us what
			you're trying to achieve with the registration process and the features
			you wish to enable for users.
		</p>
		<div class="checkboxes my-3 mt-8 flex gap-1 flex-wrap">
			<div
				class="flex-1 border pl-4 flex gap-1 justify-start items-center cursor-pointer rounded"
			>
				<input
					v-model="businessType"
					value="eCommerce"
					type="radio"
					name="type"
					id="ec"
					class=""
				/>
				<label
					for="ec"
					class="cursor-pointer text-sm w-full p-3 md:p-6"
					>eCommerce</label
				>
			</div>
			<div
				class="flex-1 border pl-4 flex gap-1 justify-start items-center cursor-pointer rounded"
				:class="{ 'border-purple-500': businessType == 'ec' }"
			>
				<input
					v-model="businessType"
					value="eCommerce(Single Product)"
					type="radio"
					name="type"
					id="ec"
					class=""
				/>
				<label
					for="ec"
					class="cursor-pointer text-sm w-full p-3 md:p-6"
					>eCommerce(Single Product)</label
				>
			</div>
			<div
				class="flex-1 border pl-4 flex gap-1 justify-start items-center cursor-pointer rounded"
				:class="{ 'border-purple-500': businessType == 'ec' }"
			>
				<input
					v-model="businessType"
					value="Landing Page"
					type="radio"
					name="type"
					id="ec"
					class=""
				/>
				<label
					for="ec"
					class="cursor-pointer text-sm w-full p-3 md:p-6"
					>Landing Page</label
				>
			</div>
		</div>
	</div>
</template>

<script setup>
	const businessType = ref();
</script>

<style scoped>
	.radio-item input[type="radio"]:checked + label:after {
		border-radius: 11px;
		width: 12px;
		height: 12px;
		position: absolute;
		top: 9px;
		left: 10px;
		content: " aaa";
		display: block;
		background: #749cc4;
	}
</style>
