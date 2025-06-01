<template>
	<section>
		<div
			class="fixed left-1 bottom-1 z-[9999999] w-screen max-w-[400px] flex flex-col gap-1"
		>
			<UAlert
				class="auto-hide capitalize"
				:class="n.type"
				:description="n.message"
				:title="n.type"
				v-for="n in notifs"
				:key="n.type"
				:close-button="{
					icon: 'i-heroicons-x-mark-20-solid',
					color: 'gray',
					variant: 'link',
					padded: false,
				}"
				@load="closeNotif(n)"
				@close="closeNotif(n)"
			/>
		</div>
		<TairoSidebarLayout v-if="user">
			<!-- <span>{{loading}} {{preloader}} {{useState('preloader')}}</span> -->
			<slot />
		</TairoSidebarLayout>
		<Icon
			v-else
			name="svg-spinners:blocks-wave"
			class="text-muted-500 opacity-30 h-14 w-14 fixed left-[50%] top-[50%]"
		/>
	</section>
</template>

<script setup>
	const { currentName } = useSidebar();
	const { shop, getShop } = useShop();
	const route = useRoute();
	const { user, jwtLogin, notifs } = useAuth();
	onMounted(() => {
		setTimeout(() => {
			console.log(user.value);
			if (!useCookie("jwt").value) {
				navigateTo("/auth/login");
			} else if (!user.value) {
				jwtLogin();
			}
		}, 1000);
	});

	watch(
		() => route.fullPath,
		async () => {
			setTimeout(() => {
				setSidebar();
			}, 100);
		}
	);
	async function setSidebar() {
		if (route.fullPath.startsWith("/account")) {
			if (currentName.value != "Account") {
				currentName.value = "Account";
			}
		} else if (route.fullPath.startsWith("/support")) {
			if (currentName.value != "Support") {
				currentName.value = "Support";
			}
		} else if (route.fullPath.startsWith("/ecommerce")) {
			if (currentName.value != "eCommerce") {
				await getShop();
				currentName.value = "eCommerce";
			} else {
				if (!shop.value) {
					getShop();
				}
			}
		}
	}
	setSidebar();

	const loading = useState("loading");
	const preloader = useState("preloader");
	preloader.value = false;

	const timer = ref(0);
	function myRecursiveFunction() {
		timer.value += 1;
		if (timer.value > 1 && loading.value == false) {
			preloader.value = false;
			timer.value = 0;
		} else {
			setTimeout(myRecursiveFunction, 500);
		}
	}

	watch(
		() => loading.value,
		async () => {
			if (loading.value == true) {
				preloader.value = true;
				timer.value = 0;
				myRecursiveFunction();
			}
		}
	);
	useHead({
		title: "NextOxy Dashboard",
		viewport: "width=device-width, initial-scale=1, maximum-scale=1",
		charset: "utf-8",
		meta: [
			{
				name: "description",
				content:
					"AI-Powered Technology eCommerce & Dropshipping Startup made simple. NextOxy's all-in-one workspace allows you to effortlessly manage every aspect of your ecommerce and dropshipping business from a single platform.",
			},
		],
		link: [
			{
				rel: "icon",
				type: "image/png",
				href: "/static/frontend/images/favicon.png",
			},
		],
		script: [
			{
				src: "https://translate.google.com/translate_a/element.js?cb=google_translate_element",
				body: true,
				defer: false,
			},
		],
	});
	// twak to
	var Tawk_API = Tawk_API || {},
		Tawk_LoadStart = new Date();
	(function () {
		var s1 = document.createElement("script"),
			s0 = document.getElementsByTagName("script")[0];
		s1.async = true;
		s1.src = "https://embed.tawk.to/65509825958be55aeaaed27e/1hf1d4lg5";
		s1.charset = "UTF-8";
		s1.setAttribute("crossorigin", "*");
		s0.parentNode.insertBefore(s1, s0);
	})();

	// notifs
	function closeNotif(n) {
		console.log(n, notifs);
		notifs.value.splice(n, 1);
	}
</script>

// for toaster
<style>
	#nt-container {
		position: fixed;
		z-index: 99999;
		bottom: 10px;
		right: 10px;
	}
</style>

<style scoped>
	.auto-hide {
		animation: fadeOut 5s forwards;
		animation-delay: 5s; /* Wait for 5 seconds before starting the animation */
	}

	/* Define the fadeOut animation */
	@keyframes fadeOut {
		from {
			opacity: 1;
		}
		to {
			opacity: 0;
			display: none;
		}
	}
	.auto-hide.success {
		background-color: rgb(73, 150, 50);
		color: white;
	}
	.auto-hide.warning {
		background-color: rgb(206, 240, 128);
		color: white;
	}
	.auto-hide.error {
		background-color: rgb(240, 163, 128);
		color: white;
	}
</style>
