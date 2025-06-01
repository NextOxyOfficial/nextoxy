<script setup lang="ts">
	definePageMeta({
		title: "Login",
		preview: {
			title: "Login 3",
			description: "For authentication and sign in",
			categories: ["layouts", "authentication"],
			src: "/img/screens/auth-login-3.png",
			srcDark: "/img/screens/auth-login-3-dark.png",
			order: 98,
		},
		layout: "landing",
	});

	const Api = useApi();

	const router = useRouter();
	const toaster = useToaster();

	const email = ref("");
	const message = ref("");
	const sending = ref(false);
	async function sendLink() {
		if (!email.value) {
			return;
		}
		sending.value = true;
		const res = await Api.get("/api/auth/reset/?email=" + email.value);
		message.value = res.data;
		setTimeout(() => {
			sending.value = false;
		}, 5000);
	}

	const reset = ref({
		pass1: "",
		pass2: "",
		error: "",
		success: "",
		otp: "",
	});
	async function resetPass() {
		reset.value.error = "";
		if (!reset.value.pass1 || !reset.value.pass2) {
			reset.value.error = "Please fill all fields";
			return;
		}
		if (reset.value.pass1 != reset.value.pass2) {
			reset.value.error = "Password does not match";
			return;
		}
		reset.value.otp = router.currentRoute.value.query.otp;
		console.log(reset.value);
		const res = await Api.post("/api/auth/reset/", reset.value);
		console.log(res);
		if (res.data == 200) {
			reset.value.success = "Reset Password Successful!";
		}
	}
</script>

<template>
	<div
		class="bg-muted-100 dark:bg-muted-900 relative w-full overflow-hidden mt-28"
	>
		<div class="flex w-full items-center justify-center">
			<div class="relative mx-auto w-full max-w-lg">
				<!--Form-->
				<BaseCard
					shape="curved"
					elevated
					class="py-6 px-2 me-auto ms-auto my-14 w-full"
				>
					<div class="me-auto ms-auto my-4 w-full max-w-md">
						<div class="text-center">
							<BaseHeading
								as="h2"
								size="3xl"
								weight="medium"
							>
								Reset Password!
							</BaseHeading>
							<BaseParagraph
								size="sm"
								class="text-muted-400 mb-6"
							>
								Reset your password.
							</BaseParagraph>
						</div>
						<div
							class="px-8 py-4"
							v-if="router.currentRoute.value.query.otp"
						>
							<div class="mb-4 space-y-4">
								<BaseInput
									v-model="reset.pass1"
									type="password"
									label="New Password"
									placeholder="Password"
								/>
								<BaseInput
									v-model="reset.pass2"
									type="password"
									label="Confirm New Password"
									placeholder="Password"
								/>
							</div>
							<p
								class="text-rose-500 p-1 text-center mb-2"
								v-if="reset.error"
							>
								{{ reset.error }}
							</p>
							<p
								class="text-green-500 p-1 text-center mb-2"
								v-if="reset.success"
							>
								{{ reset.success }}
							</p>
							<div class="mb-6">
								<BaseButton
									@click="resetPass"
									type="submit"
									color="primary"
									class="!h-12 w-full"
								>
									Reset password
								</BaseButton>
							</div>
						</div>
						<div
							class="px-8 py-4"
							v-else
						>
							<div class="mb-4 space-y-4">
								<BaseInput
									v-model="email"
									type="email"
									label="Email address"
									placeholder="Email address"
								/>
							</div>
							<p
								v-if="message == 404"
								class="text-rose-500 p-1 text-center mb-2"
							>
								No account is associated with this email.
							</p>
							<p
								v-if="message == 200"
								class="text-green-500 p-1 text-center mb-2"
							>
								Please check your email for instruction.
							</p>
							<div class="mb-6">
								<BaseButton
									@click="sendLink"
									type="submit"
									color="primary"
									class="!h-12 w-full"
									:disabled="sending"
								>
									Send Code
								</BaseButton>
							</div>
						</div>
					</div>
				</BaseCard>
			</div>
		</div>
	</div>
</template>
