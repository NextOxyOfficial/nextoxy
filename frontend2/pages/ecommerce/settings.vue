<script setup lang="ts">
	definePageMeta({
		layout: "dashboard",
	});
	const preloader = useState("preloader");
	const tabs = [
		"General",
		"Menu",
		"Category",
		"Brands",
		"Socials",
		"Refund Policy",
		"Privacy Policy",
		"Terms & Conditions",
	];
	const selectedTab = ref(tabs[0]);
</script>
<template>
	<div>
		<div class="mx-auto flex w-full max-w-4xl flex-col">
			<div class="relative mx-auto w-full">
				<div
					class="border-b border-gray-200 pb-4 px-0 my-4 flex justify-between"
				>
					<CommonTitleIcon
						:filename="'settings-min.png'"
						:title="'Shop Settings'"
					/>
					<span></span>
				</div>
				<div class="w-full">
					<!-- Tabs -->
					<div class="lg:hidden">
						<label
							for="selected-tab"
							class="sr-only"
							>Select a tab</label
						>
						<select
							id="selected-tab"
							name="selected-tab"
							class="mt-1 block w-full rounded-md border py-2 pl-3 pr-10 text-base border-purple-500 focus:outline-none focus:ring-purple-500 sm:text-sm"
							v-model="selectedTab"
						>
							<option
								v-for="tab in tabs"
								:value="tab"
								:key="tab"
								:selected="tab == selectedTab"
							>
								{{ tab }}
							</option>
						</select>
					</div>
					<div class="hidden lg:block mb-3">
						<div class="border-slate-500/50">
							<nav class="-mb-px flex justify-start cursor-pointer gap-[1px]">
								<a
									@click="selectedTab = tab"
									v-for="tab in tabs"
									:key="tab"
									:href="tab.href"
									class="bg-violet-400/10 rounded px-4 py-2"
									:class="[
										tab == selectedTab
											? 'border-purple-500 text-purple-600'
											: 'border-transparent text-violet-500 hover:border-gray-300',
										'whitespace-nowrap border-b-2 font-medium text-sm',
									]"
									>{{ tab }}</a
								>
							</nav>
						</div>
					</div>

					<BasePlaceload
						v-if="preloader"
						class="h-[50vh] w-full rounded opacity-35"
					/>
					<section :class="{ 'opacity-0': preloader }">
						<ClientOnly>
							<EcommerceSettingsGeneral v-if="selectedTab == 'General'" />
							<EcommerceSettingsCategory v-if="selectedTab == 'Category'" />
							<EcommerceSettingsMenu v-if="selectedTab == 'Menu'" />
							<EcommerceSettingsBrands v-if="selectedTab == 'Brands'" />
							<EcommerceSettingsSocials v-if="selectedTab == 'Socials'" />
							<EcommerceSettingsStaffMembers
								v-if="selectedTab == 'Staff Members'"
							/>
							<EcommerceSettingsRefundPolicy
								v-if="selectedTab == 'Refund Policy'"
							/>
							<EcommerceSettingsPrivacyPolicy
								v-if="selectedTab == 'Privacy Policy'"
							/>
							<EcommerceSettingsTermsConditions
								v-if="selectedTab == 'Terms & Conditions'"
							/>
						</ClientOnly>
					</section>
				</div>
			</div>
		</div>
	</div>
</template>
