<template>
	<section class="max-w-3xl mx-auto">
		<BaseCard
			shape="rounded"
			class="p-6"
		>
			<BaseHeading
				as="h4"
				size="lg"
				weight="semibold"
				class="text-muted-800 dark:text-white my-2"
			>
				Open New Ticket
			</BaseHeading>
			<p>Contact with NextOxy</p>
			<br />
			<BaseTextarea
				v-model="newMsg.subject"
				label="Subject"
				shape="rounded"
				placeholder="Write a subject..."
				rows="2"
				size="sm"
				class="mb-3"
				autogrow
			/>
			<BaseTextarea
				v-model="newMsg.message"
				rows="10"
				class="mb-3"
				label="Message"
				shape="rounded"
				placeholder="Write a message..."
				color-focus
			/>
			<BaseInputFile
				@change="imageUploaded"
				shape="rounded"
				label="Attachment"
			/>
			<BaseButtonAction
				@click="openTicket"
				class="mt-4"
				shape="rounded"
				color="primary"
				>Submit Ticket</BaseButtonAction
			>
		</BaseCard>
	</section>
</template>

<script setup>
	definePageMeta({
		layout: "dashboard",
	});
	const Api = useApi();
	const newMsg = ref({
		subject: "",
		message: "",
		image: "",
	});
	async function openTicket() {
		console.log(newMsg.value);
		const { data } = Api.post("/api/auth/tickets/", newMsg.value);
		console.log(data);
		navigateTo("/support");
	}
	function imageUploaded(e) {
		let reader = new FileReader();
		reader.onload = function () {
			newMsg.value.image = reader.result;
		};
		reader.readAsDataURL(e.target.files[0]);
	}
</script>

<style scoped></style>
