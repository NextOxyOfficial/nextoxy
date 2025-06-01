<script setup lang="ts">
	import { Menu, MenuButton, MenuItem, MenuItems } from "@headlessui/vue";
	const { user } = useAuth();
	const Api = useApi();
	const notifs = ref();
	async function getNotifs() {
		const res = await $fetch(
			Api.baseURL + "/api/auth/notifications/?acc_id=" + user.value.id
		);
		console.log(res);
		notifs.value = res;
		if (user.value.notifications != 0) {
			setTimeout(() => {
				user.value.notifications = 0;
			}, 3000);
		}
	}
</script>

<template>
	<div class="group inline-flex items-center justify-center text-right">
		<Menu
			as="div"
			class="relative h-9 w-9 text-left"
			v-slot="{ close }"
		>
			<MenuButton as="div">
				<button
					type="button"
					class="relative group-hover:ring-muted-200 dark:group-hover:ring-muted-700 dark:ring-offset-muted-900 inline-flex h-9 w-9 items-center justify-center rounded-full ring-1 ring-transparent transition-all duration-300 group-hover:ring-offset-4"
					@click="getNotifs"
				>
					<div
						class="absolute bg-rose-400 text-[9px] w-4 h-4 rounded-full text-white flex justify-center items-center top-0 right-0"
						v-if="user && user.notifications > 0"
					>
						<span>{{ user.notifications }}</span>
					</div>
					<span
						class="border-muted-200 dark:border-muted-700 dark:bg-muted-800 flex h-9 w-9 items-center justify-center rounded-full border bg-white"
					>
						<Icon
							name="ph:bell-duotone"
							class="text-muted-400 h-5 w-5"
						/>
					</span>
				</button>
			</MenuButton>

			<Transition
				enter-active-class="transition duration-100 ease-out"
				enter-from-class="transform scale-95 opacity-0"
				enter-to-class="transform scale-100 opacity-100"
				leave-active-class="transition duration-75 ease-in"
				leave-from-class="transform scale-100 opacity-100"
				leave-to-class="transform scale-95 opacity-0"
			>
				<MenuItems
					class="divide-muted-100 border-muted-200 dark:divide-muted-700 dark:border-muted-700 dark:bg-muted-800 absolute end-0 mt-2 w-72 origin-top-right divide-y rounded-md border bg-white shadow-lg focus:outline-none"
					v-if="user"
				>
					<div class="p-4">
						<div class="relative flex items-center justify-between">
							<h4
								class="font-heading text-muted-500 dark:text-muted-200 text-xs uppercase"
							>
								Notifications
							</h4>
							<span class="font-alt text-primary-500 text-sm font-semibold">
								<span>{{ user.notifications }} Unread</span>
							</span>
						</div>
					</div>
					<div
						class="p-4 flex flex-col gap-1 items-center justify-center"
						v-if="!notifs"
					>
						<UIcon
							name="i-svg-spinners:bars-fade"
							dynamic
						/>
						<span class="opacity-50">Loading Notifications</span>
					</div>
					<div
						class="p-4"
						v-else-if="notifs.length == 0"
					>
						<BaseHeading
							as="h6"
							size="sm"
							class="text-muted-400 text-center"
						>
							You Have O Notifications
						</BaseHeading>
					</div>
					<div
						class="p-4"
						v-else
					>
						<MenuItem
							v-for="n in notifs"
							as="div"
							v-slot="{ active }"
						>
							<NuxtLink
								to="#"
								class="group flex w-full items-center rounded-md p-2 text-sm transition-colors duration-300"
								:class="[
									active
										? 'bg-muted-100 dark:bg-muted-700  text-primary-500'
										: 'text-muted-500',
									n.unread
										? 'bg-muted-50 dark:bg-muted-600  text-primary-400'
										: 'text-muted-400',
								]"
								@click.passive="close"
							>
								<div
									class="relative inline-flex h-9 w-9 items-center justify-center rounded-full bg-red-300/10"
								>
									<Icon
										name="ph:bell-duotone"
										class="text-muted-400 h-5 w-5"
									/>
								</div>
								<div class="ms-2">
									<h6
										class="font-heading text-muted-800 text-xs font-semibold leading-tight dark:text-white"
									>
										{{ n.content }}
									</h6>
									<p class="text-muted-400 font-sans text-xs">
										{{ n.created_at }}
									</p>
								</div>
							</NuxtLink>
						</MenuItem>
					</div>
				</MenuItems>
			</Transition>
		</Menu>
	</div>
</template>
