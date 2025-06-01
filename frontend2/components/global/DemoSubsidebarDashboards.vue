<script setup>
	const { shop } = useShop();
	const navigation = [
		{
			name: "Store Front",
			children: [
				{
					name: "Dashboard",
					icon: "solar:pie-chart-2-broken",
					to: "/ecommerce",
					exact: true,
				},
				{
					name: "Products",
					icon: "solar:shop-2-broken",
					to: "/ecommerce/products",
				},
				{
					name: "Orders",
					icon: "solar:cart-check-broken",
					to: "/ecommerce/orders",
				},
				{
					name: "Customers",
					icon: "solar:users-group-rounded-broken",
					to: "/ecommerce/customers",
				},
				{
					name: "Leads",
					icon: "solar:user-id-broken",
					to: "/ecommerce/leads",
				},
				{
					name: "Custom Invoice",
					icon: "solar:document-broken",
					to: "/ecommerce/custom-invoice",
				},
				{
					name: "Coupon/Gift Cards",
					icon: "solar:ticket-sale-broken",
					to: "/ecommerce/giftcards",
				},
			],
		},
		{
			name: "Site Settings",
			children: [
				{
					name: "Site Settings",
					icon: "solar:settings-broken",
					to: "/ecommerce/settings",
				},
				{
					name: "Subscriptions",
					icon: "solar:card-broken",
					to: "/ecommerce/subscription",
				},
				{
					name: "Themes",
					icon: "solar:documents-minimalistic-broken",
					to: "/ecommerce/themes",
				},
				{
					name: "Plugins",
					icon: "solar:widget-add-broken",
					to: "/ecommerce/plugins",
				},
				{
					name: "Pages",
					icon: "solar:document-broken",
					to: "/ecommerce/pages",
				},
				{
					name: "Domain & DNS",
					icon: "solar:cursor-square-broken",
					to: "/ecommerce/domain",
				},
				{
					name: "Tags & Keywords",
					icon: "solar:tag-broken",
					to: "/ecommerce/tags",
				},
				{
					name: "Customization",
					icon: "solar:ruler-pen-broken",
					to: "/ecommerce/customize",
				},
				{
					name: "Shipping Charges",
					icon: "mdi:truck-fast-outline",
					to: "/ecommerce/shipping",
				},
				// {
				//   name: 'Mailing',
				//   icon: 'solar:mailbox-broken',
				//   to: '/ecommerce/mailing',
				// },
				{
					name: "Subscribers",
					icon: "solar:users-group-two-rounded-broken",
					to: "/ecommerce/subscribers",
				},
			],
		},
		{
			name: "Desk",
			children: [
				{
					name: "Customer Support",
					icon: "solar:headphones-round-broken",
					to: "/ecommerce/customer_support",
				},
				{
					name: "Reviews",
					icon: "solar:hand-stars-broken",
					to: "/ecommerce/reviews",
				},
			],
		},
	];

	function getNavigation() {
		// if (shop.value && shop.value.package) {
		// 	if (shop.value.package.id == 5) return navigationLp;
		// }
		return navigation;
	}
</script>

<template>
	<TairoSubsidebar>
		<template #header>
			<TairoSubsidebarHeader />
		</template>
		<DashboardProgressSteps />
		<TairoSubsidebarMenu :navigation="getNavigation()" />
	</TairoSubsidebar>
</template>
