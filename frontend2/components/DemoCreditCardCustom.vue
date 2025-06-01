<script setup lang="ts">
	const props = withDefaults(
		defineProps<{
			type?: string;
			endingNumber?: any;
			balance?: any;
			active: boolean;
		}>(),
		{
			type: "",
			endingNumber: 0,
			balance: 0,
		}
	);
</script>

<template>
	<div
		role="button"
		class="xs:w-[240px] relative flex w-[290px] max-w-full cursor-pointer flex-col overflow-hidden rounded-xl p-5 transition-all duration-300 lg:w-full"
		:class="[
			props.active ? 'bg-primary-700' : 'bg-muted-200 dark:bg-muted-900',
		]"
	>
		<div
			class="absolute -bottom-5 -end-5 h-[70px] w-[70px] rounded-full bg-white opacity-30 dark:opacity-10"
		></div>

		<div class="mt-auto">
			<span
				class="block font-sans text-lg font-semibold"
				:class="
					props.active ? 'text-white' : 'text-muted-800 dark:text-muted-200'
				"
			>
				{{ props.balance }}
			</span>
			<span
				class="block font-sans text-sm"
				:class="
					props.active ? 'text-white' : 'text-muted-500 dark:text-muted-400'
				"
			>
				{{ props.endingNumber }}
			</span>
		</div>
	</div>
</template>
