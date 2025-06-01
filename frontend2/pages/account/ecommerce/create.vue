<script setup>
	import { TransitionRoot } from "@headlessui/vue";
	const Api = useApi();
	definePageMeta({
		layout: "dashboard",
	});
	const step = ref(1);
	const newShopData = ref({
		shopName: "",
	});

	function registerWithShopName(shopName) {
		console.log(shopName);
		newShopData.value.shopName = shopName;
		Api.post("/api/account/ecommerce/", newShopData.value);
		step.value++;
	}
</script>
<style scoped>
	.fade-in-sec {
		animation: fadein 5s;
	}
	@keyframes fadein {
		0% {
			opacity: 0;
		}
		99% {
			opacity: 0;
		}
		100% {
			opacity: 1;
		}
	}
</style>
<template>
	<div class="flex gap-2 min-h-[97vh]">
		<div class="flex-1 py-6">
			<div
				class="min-h-[70vh] overflow-hidden mx-auto w-full max-w-2xl lg:w-120 p-10px-8 py-12"
			>
				<img
					class="h-8 w-auto"
					src="/static/frontend/images/home/logo.png"
					alt="Your Company"
				/>

				<div class="flex justify-center my-4 mt-8 gap-1">
					<span
						class="bg-gray-100 border flex-1 h-3 inline-block rounded-full"
						:class="{ 'bg-purple-500': step == 1 }"
					></span>
					<span
						class="bg-gray-100 border flex-1 h-3 inline-block rounded-full"
						:class="{ 'bg-purple-500': step == 2 }"
					></span>
					<span
						class="bg-gray-100 border flex-1 h-3 inline-block rounded-full"
						:class="{ 'bg-purple-500': step == 3 }"
					></span>
					<span
						class="bg-gray-100 border flex-1 h-3 inline-block rounded-full"
						:class="{ 'bg-purple-500': step == 4 }"
					></span>
					<span
						class="bg-gray-100 border flex-1 h-3 inline-block rounded-full"
						:class="{ 'bg-purple-500': step == 5 }"
					></span>
				</div>
				<TransitionRoot
					:show="step == 5"
					enter="transition-all duration-300"
					enter-from="opacity-0 pl-64"
					enter-to="opacity-100"
					leave="transition-opacity duration-0"
					leave-from="opacity-100"
					leave-to="opacity-0"
				>
					<AccountEcommerceStep5 @registerWithShopName="registerWithShopName" />
				</TransitionRoot>
				<TransitionRoot
					:show="step == 4"
					enter="transition-all duration-300"
					enter-from="opacity-0 pl-64"
					enter-to="opacity-100"
					leave="transition-opacity duration-0"
					leave-from="opacity-100"
					leave-to="opacity-0"
				>
					<AccountEcommerceStep4 @registerWithShopName="registerWithShopName" />
				</TransitionRoot>
				<TransitionRoot
					:show="step == 3"
					enter="transition-all duration-300"
					enter-from="opacity-0 pl-64"
					enter-to="opacity-100"
					leave="transition-opacity duration-0"
					leave-from="opacity-100"
					leave-to="opacity-0"
				>
					<AccountEcommerceStep3 />
				</TransitionRoot>
				<TransitionRoot
					:show="step == 2"
					enter="transition-all duration-300"
					enter-from="opacity-0 pl-64"
					enter-to="opacity-100"
					leave="transition-opacity duration-0"
					leave-from="opacity-100"
					leave-to="opacity-0"
				>
					<AccountEcommerceStep2 />
				</TransitionRoot>
				<TransitionRoot
					:show="step == 1"
					enter="transition-all duration-300"
					enter-from="opacity-0 pl-64"
					enter-to="opacity-100"
					leave="transition-opacity duration-0"
					leave-from="opacity-100"
					leave-to="opacity-0"
				>
					<AccountEcommerceStep1 />
				</TransitionRoot>
				<div class="flex justify-between mt-12">
					<nuxt-link
						to="/account/ecommerce"
						class="px-10 py-3 mt-5 light opacity-80 bg-white border border-dashed text-slate-700 rounded"
						v-if="step == 1"
						>Cancel</nuxt-link
					>
					<button
						@click="step--"
						class="px-10 py-3 mt-5 light opacity-80 bg-white border border-dashed text-slate-700 rounded"
						v-if="step != 1"
					>
						Back
					</button>
					<span
						class="opacity-0"
						v-else
					></span>
					<button
						@click="step++"
						class="px-10 py-3 mt-5 bg-purple-600 text-white rounded"
						v-if="step < 4"
					>
						Next
					</button>
					<nuxt-link
						to="/account/ecommerce"
						class="px-10 py-3 mt-5 bg-purple-600 text-white rounded fade-in-sec"
						v-if="step == 5"
						>Complete</nuxt-link
					>
				</div>
			</div>
		</div>
	</div>
</template>
