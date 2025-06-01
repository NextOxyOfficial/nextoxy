<template>
	<div>
		<!-- ====== Table Section Start -->
		<BaseCard
			shape="rounded"
			class="py-2"
		>
			<div class="w-full flex flex-wrap justify-between my-4 mb-6">
				<div class="px-4">
					<CommonTitleIcon
						:filename="'review-min.png'"
						:title="'Customer Reviews & Feedbacks'"
					/>
				</div>
				<span></span>
			</div>
			<BasePlaceload
				v-if="preloader"
				class="h-[50vh] w-full rounded opacity-35"
			/>
			<div
				class="container mx-auto"
				v-else
			>
				<div class="-mx-4 flex flex-wrap">
					<div class="w-full px-4">
						<div class="max-w-full overflow-x-auto">
							<table class="w-full table-auto">
								<thead>
									<tr class="text-left">
										<th
											class="text-dark min-w-[300px] py-4 pl-11 pr-4 text-base font-medium uppercase"
										>
											Email
										</th>
										<th
											class="text-dark min-w-[280px] px-4 py-4 text-base font-medium uppercase"
										>
											Date
										</th>
										<th
											class="text-dark min-w-[140px] px-4 py-4 text-base font-medium uppercase"
										>
											Type
										</th>
										<th
											class="text-dark min-w-[140px] px-4 py-4 text-base font-medium uppercase text-center"
										>
											Action
										</th>
									</tr>
								</thead>
								<tbody v-if="subscribers">
									<tr v-for="subscriber in subscribers.results">
										<td class="border-t p-4 pl-11">
											<p class="text-body-color text-sm">
												{{ subscriber.email }}
											</p>
										</td>
										<td class="border-t p-4">
											<p class="text-body-color text-sm">
												{{ subscriber.created_at }}
											</p>
										</td>
										<td class="border-t p-4">
											<span
												class="inline-flex items-center justify-center rounded-full bg-[#34D399] bg-opacity-[15%] px-4 py-2 text-xs font-semibold text-[#34D399]"
											>
												SOI
											</span>
										</td>
										<td class="border-t text-center">
											<button
												@click="deleteSub(subscriber.id)"
												class="text-primary border-primary hover:shadow rounded border px-5 py-2 text-sm font-medium"
											>
												Remove
											</button>
										</td>
									</tr>
								</tbody>
							</table>
						</div>
					</div>
				</div>
			</div>
		</BaseCard>
		<!-- ====== Table Section End -->
	</div>
</template>

<script setup>
	definePageMeta({
		layout: "dashboard",
	});
	const preloader = useState("preloader");
	const Api = useApi();
	const { notifs } = useAuth();
	const subscribers = ref("");
	const getSubscribers = async () => {
		const { data } = await Api.get("/api/ecommerce/dash/subscribers");
		subscribers.value = data;
	};
	onMounted(() => {
		getSubscribers();
	});
	function deleteSub(id) {
		Api.del(`/api/ecommerce/dash/subscribers?id=${id}`);
		getSubscribers();
		notifs.value.push({
			type: "success",
			message: "Subscriber removed successfully",
		});
	}
</script>

<style scoped></style>
