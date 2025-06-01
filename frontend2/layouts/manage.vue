<template>
	<section
		class="flex max-w-[100vw]"
		v-if="user"
	>
		<div
			id="sidebar"
			class="fixed top-0 flex h-full w-64 flex-col border-r bg-white view"
		>
			<div class="flex h-14 items-center justify-center border-b relative">
				<div>NextOxy Management</div>
				<svg
					@click="toggleSidebar"
					class="absolute right-1 top-[50%] translate-y-[-50%] p-1 bg-slate-400/30 rounded cursor-pointer"
					xmlns="http://www.w3.org/2000/svg"
					width="26"
					height="26  "
					viewBox="0 0 24 24"
				>
					<path
						fill="currentColor"
						d="m18.54 9.88l-1.42-1.41L15 10.59l-2.12-2.12l-1.41 1.41L13.59 12l-2.12 2.12l1.41 1.42L15 13.41l2.12 2.13l1.42-1.42L16.41 12M2 12c0-2.79 1.64-5.2 4-6.32V3.5C2.5 4.76 0 8.09 0 12s2.5 7.24 6 8.5v-2.18C3.64 17.2 2 14.79 2 12m13-9c-4.96 0-9 4.04-9 9s4.04 9 9 9s9-4.04 9-9s-4.04-9-9-9m0 16c-3.86 0-7-3.14-7-7s3.14-7 7-7s7 3.14 7 7s-3.14 7-7 7Z"
					/>
				</svg>
			</div>
			<div class="flex-grow overflow-y-auto overflow-x-hidden">
				<ul class="flex flex-col space-y-1 py-4">
					<li>
						<nuxt-link
							to="/manage"
							class="relative flex h-11 flex-row items-center border-l-4 border-transparent pr-6 text-gray-600 hover:border-indigo-500 hover:bg-gray-50 hover:text-gray-800 focus:outline-none"
						>
							<span class="ml-4 inline-flex items-center justify-center">
								<svg
									class="h-5 w-5"
									fill="none"
									stroke="currentColor"
									viewBox="0 0 24 24"
									xmlns="http://www.w3.org/2000/svg"
								>
									<path
										stroke-linecap="round"
										stroke-linejoin="round"
										stroke-width="2"
										d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"
									></path>
								</svg>
							</span>
							<span class="ml-2 truncate text-sm tracking-wide">Dashboard</span>
						</nuxt-link>
					</li>
					<li>
						<nuxt-link
							to="/manage/sales"
							class="relative flex h-11 flex-row items-center border-l-4 border-transparent pr-6 text-gray-600 hover:border-indigo-500 hover:bg-gray-50 hover:text-gray-800 focus:outline-none text-violet-500"
						>
							<span
								class="ml-4 inline-flex items-center justify-center text-violet-500"
							>
								<svg
									xmlns="http://www.w3.org/2000/svg"
									width="23"
									height="23"
									viewBox="0 0 48 48"
								>
									<g
										fill="none"
										stroke="currentColor"
										stroke-linejoin="round"
										stroke-width="4"
									>
										<path d="M41 14L24 4L7 14v20l17 10l17-10V14Z" />
										<path
											stroke-linecap="round"
											d="M24 22v8m8-12v12m-16-4v4"
										/>
									</g>
								</svg>
							</span>
							<span class="ml-2 truncate text-sm tracking-wide">Sales</span>
						</nuxt-link>
					</li>
					<li>
						<nuxt-link
							to="/manage/sales"
							class="relative flex h-11 flex-row items-center border-l-4 border-transparent pr-6 text-gray-600 hover:border-indigo-500 hover:bg-gray-50 hover:text-gray-800 focus:outline-none text-violet-500"
						>
							<span
								class="ml-4 inline-flex items-center justify-center text-violet-500"
							>
								<svg
									xmlns="http://www.w3.org/2000/svg"
									width="23"
									height="23"
									viewBox="0 0 48 48"
								>
									<g
										fill="none"
										stroke="currentColor"
										stroke-linejoin="round"
										stroke-width="4"
									>
										<path d="M41 14L24 4L7 14v20l17 10l17-10V14Z" />
										<path
											stroke-linecap="round"
											d="M24 22v8m8-12v12m-16-4v4"
										/>
									</g>
								</svg>
							</span>
							<span class="ml-2 truncate text-sm tracking-wide"
								>Sales Chart</span
							>
						</nuxt-link>
					</li>
					<li>
						<nuxt-link
							to="/manage/products"
							class="relative flex h-11 flex-row items-center border-l-4 border-transparent pr-6 text-gray-600 hover:border-indigo-500 hover:bg-gray-50 hover:text-gray-800 focus:outline-none text-violet-500"
						>
							<span
								class="ml-4 inline-flex items-center justify-center text-violet-500"
							>
								<svg
									xmlns="http://www.w3.org/2000/svg"
									width="23"
									height="23"
									viewBox="0 0 48 48"
								>
									<g
										fill="none"
										stroke="currentColor"
										stroke-linejoin="round"
										stroke-width="4"
									>
										<path d="M41 14L24 4L7 14v20l17 10l17-10V14Z" />
										<path
											stroke-linecap="round"
											d="M24 22v8m8-12v12m-16-4v4"
										/>
									</g>
								</svg>
							</span>
							<span class="ml-2 truncate text-sm tracking-wide">Products</span>
						</nuxt-link>
					</li>
					<li>
						<nuxt-link
							to="/manage/employees"
							class="relative flex h-11 flex-row items-center border-l-4 border-transparent pr-6 text-gray-600 hover:border-indigo-500 hover:bg-gray-50 hover:text-gray-800 focus:outline-none text-violet-500"
						>
							<span
								class="ml-4 inline-flex items-center justify-center text-violet-500"
							>
								<svg
									xmlns="http://www.w3.org/2000/svg"
									width="23"
									height="23"
									viewBox="0 0 48 48"
								>
									<g
										fill="none"
										stroke="currentColor"
										stroke-linejoin="round"
										stroke-width="4"
									>
										<path d="M41 14L24 4L7 14v20l17 10l17-10V14Z" />
										<path
											stroke-linecap="round"
											d="M24 22v8m8-12v12m-16-4v4"
										/>
									</g>
								</svg>
							</span>
							<span class="ml-2 truncate text-sm tracking-wide">Employees</span>
						</nuxt-link>
					</li>
					<li>
						<nuxt-link
							to="/manage/customers"
							class="relative flex h-11 flex-row items-center border-l-4 border-transparent pr-6 text-gray-600 hover:border-indigo-500 hover:bg-gray-50 hover:text-gray-800 focus:outline-none text-violet-500"
						>
							<span
								class="ml-4 inline-flex items-center justify-center text-violet-500"
							>
								<svg
									xmlns="http://www.w3.org/2000/svg"
									width="23"
									height="23"
									viewBox="0 0 48 48"
								>
									<g
										fill="none"
										stroke="currentColor"
										stroke-linejoin="round"
										stroke-width="4"
									>
										<path d="M41 14L24 4L7 14v20l17 10l17-10V14Z" />
										<path
											stroke-linecap="round"
											d="M24 22v8m8-12v12m-16-4v4"
										/>
									</g>
								</svg>
							</span>
							<span class="ml-2 truncate text-sm tracking-wide">Customers</span>
						</nuxt-link>
					</li>
					<li>
						<nuxt-link
							to="/manage/shops"
							class="relative flex h-11 flex-row items-center border-l-4 border-transparent pr-6 text-gray-600 hover:border-indigo-500 hover:bg-gray-50 hover:text-gray-800 focus:outline-none"
						>
							<span class="ml-4 inline-flex items-center justify-center">
								<svg
									xmlns="http://www.w3.org/2000/svg"
									class="h-5 w-5"
									viewBox="0 0 24 24"
								>
									<path
										fill="currentColor"
										fill-rule="evenodd"
										d="M7.435 1.25h9.13c.57 0 1.054 0 1.453.041c.426.044.82.14 1.192.37c.371.23.633.539.863.9c.215.34.432.772.687 1.282l.016.033c.01.02.019.039.027.06l1.403 3.547c.168.423.353.95.407 1.488c.055.552-.02 1.183-.453 1.73a2.753 2.753 0 0 1-1.41.945v9.604H22a.75.75 0 0 1 0 1.5H2a.75.75 0 0 1 0-1.5h1.25v-9.604a2.754 2.754 0 0 1-1.41-.944c-.432-.548-.508-1.18-.453-1.73c.054-.54.24-1.066.406-1.489l1.404-3.548a.747.747 0 0 1 .027-.06l.016-.032c.255-.51.471-.943.687-1.282c.23-.361.492-.67.863-.9c.372-.23.766-.326 1.191-.37c.4-.041.884-.041 1.454-.041ZM18 10.887a2.75 2.75 0 0 0 1.25.76v9.603h-4v-2.782c0-.44 0-.82-.028-1.13c-.03-.33-.096-.656-.273-.963a2.251 2.251 0 0 0-.824-.824c-.307-.177-.633-.243-.962-.273c-.312-.028-.691-.028-1.13-.028h-.065c-.44 0-.82 0-1.13.028c-.33.03-.656.096-.963.273a2.25 2.25 0 0 0-.824.824c-.177.307-.243.633-.273.962c-.028.312-.028.691-.028 1.13v2.783h-4v-9.604A2.75 2.75 0 0 0 6 10.887a2.742 2.742 0 0 0 2 .863c.788 0 1.499-.331 2-.863a2.742 2.742 0 0 0 2 .863a2.74 2.74 0 0 0 2-.863a2.742 2.742 0 0 0 2 .863a2.74 2.74 0 0 0 2-.863ZM10.25 21.25h3.5V18.5c0-.481 0-.792-.022-1.027c-.02-.225-.055-.307-.079-.348a.75.75 0 0 0-.274-.274c-.04-.024-.123-.058-.348-.079A12.776 12.776 0 0 0 12 16.75c-.481 0-.792 0-1.027.022c-.225.02-.307.055-.348.079a.75.75 0 0 0-.274.274c-.024.04-.059.123-.079.348c-.021.235-.022.546-.022 1.027v2.75ZM6.75 9a1.25 1.25 0 0 0 2.5 0a.75.75 0 0 1 1.5 0a1.25 1.25 0 0 0 2.5 0a.75.75 0 0 1 1.5 0a1.25 1.25 0 0 0 2.5 0a.75.75 0 0 1 1.5 0a1.25 1.25 0 0 0 2.232.773c.114-.144.17-.342.138-.652c-.032-.322-.151-.688-.308-1.086L19.42 4.517c-.268-.535-.447-.89-.613-1.15c-.16-.252-.274-.361-.386-.43c-.111-.07-.26-.123-.557-.154c-.314-.032-.72-.033-1.336-.033H7.472c-.617 0-1.023 0-1.336.033c-.297.031-.446.085-.557.154c-.112.069-.226.178-.386.43c-.167.26-.345.615-.613 1.15L3.188 8.035c-.157.398-.276.764-.308 1.086c-.031.31.024.508.138.652A1.25 1.25 0 0 0 5.25 9a.75.75 0 0 1 1.5 0Z"
										clip-rule="evenodd"
									/>
								</svg>
							</span>
							<span class="ml-2 truncate text-sm tracking-wide">Shops</span>
							<span
								class="ml-auto rounded-full bg-red-50 px-2 py-0.5 text-xs font-medium tracking-wide text-red-500"
								v-if="overview"
								>{{ overview.shops }}</span
							>
						</nuxt-link>
					</li>
					<li>
						<nuxt-link
							to="/manage/services"
							class="relative flex h-11 flex-row items-center border-l-4 border-transparent pr-6 text-gray-600 hover:border-indigo-500 hover:bg-gray-50 hover:text-gray-800 focus:outline-none"
						>
							<span class="ml-4 inline-flex items-center justify-center">
								<svg
									xmlns="http://www.w3.org/2000/svg"
									class="h-5 w-5"
									viewBox="0 0 24 24"
								>
									<path
										fill="currentColor"
										fill-rule="evenodd"
										d="M7.435 1.25h9.13c.57 0 1.054 0 1.453.041c.426.044.82.14 1.192.37c.371.23.633.539.863.9c.215.34.432.772.687 1.282l.016.033c.01.02.019.039.027.06l1.403 3.547c.168.423.353.95.407 1.488c.055.552-.02 1.183-.453 1.73a2.753 2.753 0 0 1-1.41.945v9.604H22a.75.75 0 0 1 0 1.5H2a.75.75 0 0 1 0-1.5h1.25v-9.604a2.754 2.754 0 0 1-1.41-.944c-.432-.548-.508-1.18-.453-1.73c.054-.54.24-1.066.406-1.489l1.404-3.548a.747.747 0 0 1 .027-.06l.016-.032c.255-.51.471-.943.687-1.282c.23-.361.492-.67.863-.9c.372-.23.766-.326 1.191-.37c.4-.041.884-.041 1.454-.041ZM18 10.887a2.75 2.75 0 0 0 1.25.76v9.603h-4v-2.782c0-.44 0-.82-.028-1.13c-.03-.33-.096-.656-.273-.963a2.251 2.251 0 0 0-.824-.824c-.307-.177-.633-.243-.962-.273c-.312-.028-.691-.028-1.13-.028h-.065c-.44 0-.82 0-1.13.028c-.33.03-.656.096-.963.273a2.25 2.25 0 0 0-.824.824c-.177.307-.243.633-.273.962c-.028.312-.028.691-.028 1.13v2.783h-4v-9.604A2.75 2.75 0 0 0 6 10.887a2.742 2.742 0 0 0 2 .863c.788 0 1.499-.331 2-.863a2.742 2.742 0 0 0 2 .863a2.74 2.74 0 0 0 2-.863a2.742 2.742 0 0 0 2 .863a2.74 2.74 0 0 0 2-.863ZM10.25 21.25h3.5V18.5c0-.481 0-.792-.022-1.027c-.02-.225-.055-.307-.079-.348a.75.75 0 0 0-.274-.274c-.04-.024-.123-.058-.348-.079A12.776 12.776 0 0 0 12 16.75c-.481 0-.792 0-1.027.022c-.225.02-.307.055-.348.079a.75.75 0 0 0-.274.274c-.024.04-.059.123-.079.348c-.021.235-.022.546-.022 1.027v2.75ZM6.75 9a1.25 1.25 0 0 0 2.5 0a.75.75 0 0 1 1.5 0a1.25 1.25 0 0 0 2.5 0a.75.75 0 0 1 1.5 0a1.25 1.25 0 0 0 2.5 0a.75.75 0 0 1 1.5 0a1.25 1.25 0 0 0 2.232.773c.114-.144.17-.342.138-.652c-.032-.322-.151-.688-.308-1.086L19.42 4.517c-.268-.535-.447-.89-.613-1.15c-.16-.252-.274-.361-.386-.43c-.111-.07-.26-.123-.557-.154c-.314-.032-.72-.033-1.336-.033H7.472c-.617 0-1.023 0-1.336.033c-.297.031-.446.085-.557.154c-.112.069-.226.178-.386.43c-.167.26-.345.615-.613 1.15L3.188 8.035c-.157.398-.276.764-.308 1.086c-.031.31.024.508.138.652A1.25 1.25 0 0 0 5.25 9a.75.75 0 0 1 1.5 0Z"
										clip-rule="evenodd"
									/>
								</svg>
							</span>
							<span class="ml-2 truncate text-sm tracking-wide"
								>Service Orders</span
							>
						</nuxt-link>
					</li>
					<li>
						<a
							href="#"
							class="relative flex h-11 flex-row items-center border-l-4 border-transparent pr-6 text-gray-600 hover:border-indigo-500 hover:bg-gray-50 hover:text-gray-800 focus:outline-none"
						>
							<span class="ml-4 inline-flex items-center justify-center">
								<svg
									xmlns="http://www.w3.org/2000/svg"
									class="h-5 w-5"
									viewBox="0 0 48 48"
								>
									<g
										fill="none"
										stroke="currentColor"
										stroke-linejoin="round"
										stroke-width="4"
									>
										<path d="M44 14L24 4L4 14v20l20 10l20-10V14Z" />
										<path
											stroke-linecap="round"
											d="m4 14l20 10m0 20V24m20-10L24 24M34 9L14 19"
										/>
									</g>
								</svg>
							</span>
							<span class="ml-2 truncate text-sm tracking-wide"
								>Shop Products</span
							>
							<span
								class="ml-auto rounded-full bg-indigo-50 px-2 py-0.5 text-xs font-medium tracking-wide text-indigo-500"
								v-if="overview"
								>{{ overview.products }}</span
							>
						</a>
					</li>
					<li>
						<a
							href="#"
							class="relative flex h-11 flex-row items-center border-l-4 border-transparent pr-6 text-gray-600 hover:border-indigo-500 hover:bg-gray-50 hover:text-gray-800 focus:outline-none"
						>
							<span class="ml-4 inline-flex items-center justify-center">
								<svg
									xmlns="http://www.w3.org/2000/svg"
									class="h-5 w-5"
									viewBox="0 0 24 24"
								>
									<g fill="currentColor">
										<path
											fill-rule="evenodd"
											d="M14 7a1 1 0 0 0-1 1v8a1 1 0 0 0 1 1h4a1 1 0 0 0 1-1V8a1 1 0 0 0-1-1h-4Zm3 2h-2v6h2V9Z"
											clip-rule="evenodd"
										/>
										<path
											d="M6 7a1 1 0 0 0 0 2h4a1 1 0 1 0 0-2H6Zm0 4a1 1 0 1 0 0 2h4a1 1 0 1 0 0-2H6Zm-1 5a1 1 0 0 1 1-1h4a1 1 0 1 1 0 2H6a1 1 0 0 1-1-1Z"
										/>
										<path
											fill-rule="evenodd"
											d="M4 3a3 3 0 0 0-3 3v12a3 3 0 0 0 3 3h16a3 3 0 0 0 3-3V6a3 3 0 0 0-3-3H4Zm16 2H4a1 1 0 0 0-1 1v12a1 1 0 0 0 1 1h16a1 1 0 0 0 1-1V6a1 1 0 0 0-1-1Z"
											clip-rule="evenodd"
										/>
									</g>
								</svg>
							</span>
							<span class="ml-2 truncate text-sm tracking-wide">Websites</span>
							<span
								class="ml-auto rounded-full bg-red-50 px-2 py-0.5 text-xs font-medium tracking-wide text-red-500"
								>0</span
							>
						</a>
					</li>
					<li>
						<a
							href="#"
							class="relative flex h-11 flex-row items-center border-l-4 border-transparent pr-6 text-gray-600 hover:border-indigo-500 hover:bg-gray-50 hover:text-gray-800 focus:outline-none"
						>
							<span class="ml-4 inline-flex items-center justify-center">
								<svg
									xmlns="http://www.w3.org/2000/svg"
									class="h-5 w-5 opacity-90"
									viewBox="0 0 24 24"
								>
									<path
										fill="currentColor"
										d="M12.526 11.695c1.84-.382 3.367-2.044 3.367-4.478c0-2.604-1.9-4.97-5.615-4.97H0v19.506h10.6c3.75 0 5.683-2.341 5.683-5.292c-.009-2.426-1.646-4.444-3.757-4.766zm-8.37-5.793h5.207c1.407 0 2.28.849 2.28 2.044c0 1.255-.881 2.044-2.28 2.044H4.155zM9.54 18.098H4.155v-4.444h5.386c1.61 0 2.484.992 2.484 2.222c.009 1.399-.932 2.222-2.484 2.222zM21.396 2.28c-1.255 0-2.315 1.052-2.315 2.307s.882 2.103 1.993 2.103c.238 0 .467-.025.56-.085c-.238 1.052-1.315 2.282-2.256 2.782l1.611 1.314C22.796 9.422 24 7.462 24 5.266c0-1.9-1.23-2.985-2.604-2.985Z"
									/>
								</svg>
							</span>
							<span class="ml-2 truncate text-sm tracking-wide">Blogs</span>
							<span
								class="ml-auto rounded-full bg-red-50 px-2 py-0.5 text-xs font-medium tracking-wide text-red-500"
								>0</span
							>
						</a>
					</li>
					<li class="px-5">
						<div class="flex h-8 flex-row items-center">
							<div class="text-sm font-light tracking-wide text-gray-500">
								Others
							</div>
						</div>
					</li>
					<li>
						<nuxt-link
							to="/manage/no-blog"
							class="relative flex h-11 flex-row items-center border-l-4 border-transparent pr-6 text-gray-600 hover:border-indigo-500 hover:bg-gray-50 hover:text-gray-800 focus:outline-none"
						>
							<span class="ml-4 inline-flex items-center justify-center">
								<svg
									class="h-5 w-5"
									fill="none"
									stroke="currentColor"
									viewBox="0 0 24 24"
									xmlns="http://www.w3.org/2000/svg"
								>
									<path
										stroke-linecap="round"
										stroke-linejoin="round"
										stroke-width="2"
										d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-3 7h3m-3 4h3m-6-4h.01M9 16h.01"
									></path>
								</svg>
							</span>
							<span class="ml-2 truncate text-sm tracking-wide"
								>NextOxy Blogs</span
							>
						</nuxt-link>
					</li>
					<li>
						<nuxt-link
							to="/manage/no-blog-add/new"
							class="relative flex h-11 flex-row items-center border-l-4 border-transparent pr-6 text-gray-600 hover:border-indigo-500 hover:bg-gray-50 hover:text-gray-800 focus:outline-none"
						>
							<span class="ml-4 inline-flex items-center justify-center">
								<svg
									class="h-5 w-5"
									fill="none"
									stroke="currentColor"
									viewBox="0 0 24 24"
									xmlns="http://www.w3.org/2000/svg"
								>
									<path
										stroke-linecap="round"
										stroke-linejoin="round"
										stroke-width="2"
										d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-3 7h3m-3 4h3m-6-4h.01M9 16h.01"
									></path>
								</svg>
							</span>
							<span class="ml-2 truncate text-sm tracking-wide"
								>Add new Post</span
							>
						</nuxt-link>
					</li>
					<li>
						<nuxt-link
							to="/manage/tickets"
							class="relative flex h-11 flex-row items-center border-l-4 border-transparent pr-6 text-gray-600 hover:border-indigo-500 hover:bg-gray-50 hover:text-gray-800 focus:outline-none"
						>
							<span class="ml-4 inline-flex items-center justify-center">
								<svg
									class="h-5 w-5"
									fill="none"
									stroke="currentColor"
									viewBox="0 0 24 24"
									xmlns="http://www.w3.org/2000/svg"
								>
									<path
										stroke-linecap="round"
										stroke-linejoin="round"
										stroke-width="2"
										d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-3 7h3m-3 4h3m-6-4h.01M9 16h.01"
									></path>
								</svg>
							</span>
							<span class="ml-2 truncate text-sm tracking-wide"
								>Support Tickets</span
							>
						</nuxt-link>
					</li>
					<li>
						<nuxt-link
							to="/manage/orders"
							class="relative flex h-11 flex-row items-center border-l-4 border-transparent pr-6 text-gray-600 hover:border-indigo-500 hover:bg-gray-50 hover:text-gray-800 focus:outline-none"
						>
							<span class="ml-4 inline-flex items-center justify-center">
								<svg
									class="h-5 w-5"
									fill="none"
									stroke="currentColor"
									viewBox="0 0 24 24"
									xmlns="http://www.w3.org/2000/svg"
								>
									<path
										stroke-linecap="round"
										stroke-linejoin="round"
										stroke-width="2"
										d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-3 7h3m-3 4h3m-6-4h.01M9 16h.01"
									></path>
								</svg>
							</span>
							<span class="ml-2 truncate text-sm tracking-wide">Orders</span>
						</nuxt-link>
					</li>
					<li>
						<a
							href="#"
							class="relative flex h-11 flex-row items-center border-l-4 border-transparent pr-6 text-gray-600 hover:border-indigo-500 hover:bg-gray-50 hover:text-gray-800 focus:outline-none"
						>
							<span class="ml-4 inline-flex items-center justify-center">
								<svg
									class="h-5 w-5"
									fill="none"
									stroke="currentColor"
									viewBox="0 0 24 24"
									xmlns="http://www.w3.org/2000/svg"
								>
									<path
										stroke-linecap="round"
										stroke-linejoin="round"
										stroke-width="2"
										d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z"
									></path>
								</svg>
							</span>
							<span class="ml-2 truncate text-sm tracking-wide">All Users</span>
							<span
								class="ml-auto rounded-full bg-green-50 px-2 py-0.5 text-xs font-medium tracking-wide text-green-500"
								v-if="overview"
								>{{ overview.accounts }}</span
							>
						</a>
					</li>
					<li class="px-5">
						<div class="flex h-8 flex-row items-center">
							<div class="text-sm font-light tracking-wide text-gray-500">
								Settings
							</div>
						</div>
					</li>
					<li>
						<a
							href="#"
							class="relative flex h-11 flex-row items-center border-l-4 border-transparent pr-6 text-gray-600 hover:border-indigo-500 hover:bg-gray-50 hover:text-gray-800 focus:outline-none"
						>
							<span class="ml-4 inline-flex items-center justify-center">
								<svg
									class="h-5 w-5"
									fill="none"
									stroke="currentColor"
									viewBox="0 0 24 24"
									xmlns="http://www.w3.org/2000/svg"
								>
									<path
										stroke-linecap="round"
										stroke-linejoin="round"
										stroke-width="2"
										d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"
									></path>
									<path
										stroke-linecap="round"
										stroke-linejoin="round"
										stroke-width="2"
										d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"
									></path>
								</svg>
							</span>
							<span class="ml-2 truncate text-sm tracking-wide">Settings</span>
						</a>
					</li>
					<li>
						<a
							href="#"
							class="relative flex h-11 flex-row items-center border-l-4 border-transparent pr-6 text-gray-600 hover:border-indigo-500 hover:bg-gray-50 hover:text-gray-800 focus:outline-none"
						>
							<span class="ml-4 inline-flex items-center justify-center">
								<svg
									class="h-5 w-5"
									fill="none"
									stroke="currentColor"
									viewBox="0 0 24 24"
									xmlns="http://www.w3.org/2000/svg"
								>
									<path
										stroke-linecap="round"
										stroke-linejoin="round"
										stroke-width="2"
										d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1"
									></path>
								</svg>
							</span>
							<span class="ml-2 truncate text-sm tracking-wide">Logout</span>
						</a>
					</li>
				</ul>
			</div>
		</div>

		<main
			id="main"
			class="flex-1 px-1 md:px-4 w-full"
		>
			<div class="flex h-14 items-center justify-between border-b">
				<svg
					@click="toggleSidebar"
					class="cursor-pointer"
					xmlns="http://www.w3.org/2000/svg"
					width="24"
					height="24"
					viewBox="0 0 24 24"
				>
					<g
						fill="none"
						stroke="currentColor"
						stroke-linecap="round"
						stroke-width="2"
					>
						<path
							stroke-dasharray="15"
							stroke-dashoffset="15"
							d="M4 5H17"
						>
							<animate
								fill="freeze"
								attributeName="stroke-dashoffset"
								dur="0.2s"
								values="15;0"
							/>
						</path>
						<path
							stroke-dasharray="12"
							stroke-dashoffset="12"
							d="M4 10H14"
						>
							<animate
								fill="freeze"
								attributeName="stroke-dashoffset"
								begin="0.2s"
								dur="0.2s"
								values="12;0"
							/>
						</path>
						<path
							stroke-dasharray="18"
							stroke-dashoffset="18"
							d="M4 15H20"
						>
							<animate
								fill="freeze"
								attributeName="stroke-dashoffset"
								begin="0.4s"
								dur="0.2s"
								values="18;0"
							/>
						</path>
						<path
							stroke-dasharray="15"
							stroke-dashoffset="15"
							d="M4 20H17"
						>
							<animate
								fill="freeze"
								attributeName="stroke-dashoffset"
								begin="0.6s"
								dur="0.2s"
								values="15;0"
							/>
						</path>
					</g>
				</svg>
				<div>NextOxy Management Panel</div>
			</div>
			<slot />
		</main>
	</section>
	<section
		v-else
		class=""
		style="
			min-height: 100vh;
			display: flex;
			justify-content: center;
			align-items: center;
			padding: 10px;
			flex-direction: column;
			background-color: rgba(248, 227, 135, 0.267);
		"
	>
		<div
			class="flex justify-center items-center my-6 gap-2 border border-orange-400 p-2 text-orange-400 font-bold text-4xl"
		>
			<svg
				xmlns="http://www.w3.org/2000/svg"
				width="32"
				height="32"
				viewBox="0 0 14 14"
			>
				<g
					fill="none"
					stroke="currentColor"
					stroke-linecap="round"
					stroke-linejoin="round"
				>
					<rect
						width="10"
						height="8"
						x="2"
						y="5.5"
						rx="1"
					/>
					<path d="M10.5 5.5V4a3.5 3.5 0 0 0-7 0v1.5" />
					<circle
						cx="7"
						cy="9.5"
						r=".5"
					/>
				</g>
			</svg>
			403
		</div>
		<div
			class="alert alert-warning mt-30 text-center p-6 bg-orange-300"
			role="alert"
		>
			You Do Not Have Permission To Access This Page!
			<nuxt-link class="text-blue-500">Login First</nuxt-link>
		</div>
		<div class="mx-auto w-full max-w-lg lg:w-120 p-10 lg:px-[70px]">
			<div class="mt-0">
				<div class="mt-6">
					<form class="space-y-6">
						<div>
							<label
								for="email"
								class="block text-sm font-medium text-slate-900"
								>Email address</label
							>
							<div class="mt-1">
								<input
									v-model="logindata.email"
									id="email"
									name="email"
									type="text"
									autocomplete="email"
									required=""
									class="block w-full appearance-none rounded-md border border-gray-300 px-3 py-2 placeholder-gray-400 shadow-sm focus:border-indigo-500 focus:outline-none focus:ring-indigo-500 sm:text-sm dark:text-gray-600"
								/>
							</div>
						</div>

						<div class="space-y-1">
							<label
								for="password"
								class="block text-sm font-medium text-slate-900"
								>Password</label
							>
							<div class="mt-1">
								<input
									v-model="logindata.password"
									id="password"
									name="password"
									type="password"
									autocomplete="current-password"
									required=""
									class="block w-full appearance-none rounded-md border border-gray-300 px-3 py-2 placeholder-gray-400 shadow-sm focus:border-indigo-500 focus:outline-none focus:ring-indigo-500 sm:text-sm dark:text-gray-600"
								/>
							</div>
						</div>

						<div class="flex items-center justify-between">
							<div class="flex items-center">
								<input
									id="remember-me"
									name="remember-me"
									type="checkbox"
									class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-500"
								/>
								<label
									for="remember-me"
									class="ml-2 block text-sm text-gray-900"
									>Remember me</label
								>
							</div>

							<div class="text-sm">
								<nuxt-link
									to="/public/auth/reset"
									class="font-medium text-indigo-600 hover:text-indigo-500"
									>Forgot your passwords?</nuxt-link
								>
							</div>
						</div>
						<p
							class="text-rose-500"
							v-if="logindata.error"
						>
							{{ logindata.error }}
						</p>

						<div>
							<button
								v-if="!logindata.loading"
								@click.prevent="loginUser"
								class="w-full p-3 mt-3 rounded block text-center"
							>
								Sign in
							</button>
							<button
								v-else
								@click.prevent="loginUser"
								class="w-full p-3 mt-3 rounded flex justify-center text-center"
							>
								<svg
									xmlns="http://www.w3.org/2000/svg"
									width="22"
									height="22"
									viewBox="0 0 24 24"
								>
									<path
										fill="currentColor"
										d="M12,1A11,11,0,1,0,23,12,11,11,0,0,0,12,1Zm0,19a8,8,0,1,1,8-8A8,8,0,0,1,12,20Z"
										opacity=".25"
									/>
									<path
										fill="currentColor"
										d="M10.14,1.16a11,11,0,0,0-9,8.92A1.59,1.59,0,0,0,2.46,12,1.52,1.52,0,0,0,4.11,10.7a8,8,0,0,1,6.66-6.61A1.42,1.42,0,0,0,12,2.69h0A1.57,1.57,0,0,0,10.14,1.16Z"
									>
										<animateTransform
											attributeName="transform"
											dur="0.75s"
											repeatCount="indefinite"
											type="rotate"
											values="0 12 12;360 12 12"
										/>
									</path>
								</svg>
							</button>
						</div>
					</form>
				</div>

				<div class="relative mt-8">
					<div
						class="absolute inset-0 flex items-center"
						aria-hidden="true"
					>
						<div class="w-full border-t border-gray-300" />
					</div>
					<div class="relative flex justify-center text-sm">
						<span class="bg-white rounded px-2 text-gray-500"
							>Don't have An Account?</span
						>
					</div>
				</div>
				<div class="text-center mt-1">
					<nuxt-link
						to="/public/auth/register"
						class="text-indigo-600 flex items-center justify-center gap-1 hover:text-indigo-500 cp-btn-2 font-bold"
						><svg
							class="w-6"
							xmlns="http://www.w3.org/2000/svg"
							width="32"
							height="32"
							viewBox="0 0 24 24"
						>
							<path
								fill="currentColor"
								d="M21.5 9h-5l1.86-1.86A7.991 7.991 0 0 0 12 4c-4.42 0-8 3.58-8 8c0 1.83.61 3.5 1.64 4.85c1.22-1.4 3.51-2.35 6.36-2.35c2.85 0 5.15.95 6.36 2.35A7.945 7.945 0 0 0 20 12h2c0 5.5-4.5 10-10 10S2 17.5 2 12S6.5 2 12 2c3.14 0 5.95 1.45 7.78 3.72L21.5 4v5M12 20c1.9 0 3.64-.66 5-1.76c-.64-1.01-2.55-1.74-5-1.74s-4.36.73-5 1.74c1.36 1.1 3.1 1.76 5 1.76m0-14c1.93 0 3.5 1.57 3.5 3.5S13.93 13 12 13s-3.5-1.57-3.5-3.5S10.07 6 12 6m0 2c-.83 0-1.5.67-1.5 1.5S11.17 11 12 11s1.5-.67 1.5-1.5S12.83 8 12 8Z"
							/>
						</svg>
						Create New Account</nuxt-link
					>
				</div>
			</div>
		</div>
	</section>
</template>

<script setup>
	const Api = useApi();
	const { login, jwtLogin, logout, user, isAuthenticated } = useAuth();
	const logindata = reactive({
		email: "",
		password: "",
		loading: false,
		error: "",
	});
	async function loginUser() {
		logindata.loading = true;
		logindata.error = "";
		const res = await login(logindata.email, logindata.password);
		console.log(res);
		if (res) {
			console.log("login success");
		} else {
			logindata.error = "Invalid Email or Password!";
		}
		logindata.loading = false;
	}
	const toggleSidebar = () => {
		const sidebar = document.getElementById("sidebar");
		sidebar.classList.toggle("hide");
		const main = document.getElementById("main");
		main.classList.toggle("view");
	};

	const overview = useState("manage-overview");
	getOverview();
	async function getOverview() {
		const { data } = await Api.get("/api/office/manage/overview");
		overview.value = data;
	}
</script>

<style scoped>
	.router-link-active {
		background-color: #f9fafb;
		border-left: 3px solid #6366f1;
	}
	#sidebar {
		left: 0;
		transition: all 0.5s ease;
	}

	#main {
		transition: all 0.5s ease;
		margin-left: 255px;
	}
	#sidebar.hide {
		left: -450px;
	}
	#main.view {
		transition: all 0.5s ease;
		margin-left: 0px;
	}
	@media screen and (max-width: 768px) {
		#sidebar {
			left: -420px;
		}
		#main {
			margin-left: 0px;
		}
		#sidebar.hide {
			left: 0px;
		}
		#main.view {
			margin-left: 0px;
		}
	}
</style>
