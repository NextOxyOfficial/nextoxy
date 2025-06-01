<template>
	<LandingLayout>
		<CommonTopbar />
		<slot />
	</LandingLayout>
</template>

<script setup>
	const { user, jwtLogin } = useAuth();
	onMounted(() => {
		setTimeout(() => {
			console.log(user.value);
			if (!user.value) {
				jwtLogin();
			}
		}, 1000);
	});

	useHead({
		title: "NextOxy - Cloud Business Solutions.",
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
</script>
