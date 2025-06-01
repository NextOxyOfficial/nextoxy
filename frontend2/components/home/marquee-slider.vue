<template>
	<div class="mx-auto">
		<div class="text-center mt-12">
			<BaseHeading
				as="h1"
				class="text-2xl font-semibold md:!text-5xl"
			>
				Pre-Made Inner Pages That Serve <br />
				Your Purpose
			</BaseHeading>
			<section id="marquee">
				<div class="max-w-none">
					<div class="pic-container">
						<div class="pic">
							<img
								src="/static/frontend/images/img1.png"
								alt="img"
								class="h-[450px]"
							/>
						</div>
						<div class="pic">
							<img
								src="/static/frontend/images/img2.png"
								alt="img"
								class="h-[450px]"
							/>
						</div>
						<div class="pic">
							<img
								src="/static/frontend/images/img3.png"
								alt="img"
								class="h-[450px]"
							/>
						</div>
						<div class="pic">
							<img
								src="/static/frontend/images/img4.png"
								alt="img"
								class="h-[450px]"
							/>
						</div>
						<div class="pic">
							<img
								src="/static/frontend/images/img5.png"
								alt="img"
								class="h-[450px]"
							/>
						</div>
						<div class="pic">
							<img
								src="/static/frontend/images/img6.png"
								alt="img"
								class="h-[450px]"
							/>
						</div>
						<div class="pic">
							<img
								src="/static/frontend/images/img7.png"
								alt="img"
								class="h-[450px]"
							/>
						</div>
						<div class="pic">
							<img
								src="/static/frontend/images/img8.png"
								alt="img"
								class="h-[450px]"
							/>
						</div>
					</div>
				</div>
			</section>
		</div>
	</div>
</template>

<script setup></script>

<style scoped>
	#marquee {
		padding: 50px 0px;
		width: 100%;
	}

	#marquee .container {
		overflow: hidden;
		width: 100%;
	}

	#marquee .pic-container {
		display: flex;
		animation: marquee 10s infinite linear;
		gap: 12px;
	}

	#marquee .pic-container .pic {
		flex-basis: 25%;
		flex-shrink: 0;
	}

	#marquee img {
		width: 100%;
		object-fit: cover;
		border: 1px solid rgba(238, 231, 231, 0.9);
	}

	@media (max-width: 1024px) {
		#marquee .pic-container .pic {
			flex-basis: 25%;
		}
	}

	@media (max-width: 768px) {
		#marquee .pic-container .pic {
			flex-basis: 33.33%;
		}
	}

	@keyframes marquee {
		0% {
			transform: translateX(0);
		}
		100% {
			transform: translateX(-100%);
		}
	}

	@media (max-width: 1024px) {
		@keyframes marquee {
			0% {
				transform: translateX(0);
			}
			100% {
				transform: translateX(-125%);
			}
		}
	}

	@media (max-width: 768px) {
		@keyframes marquee {
			0% {
				transform: translateX(0);
			}
			100% {
				transform: translateX(-186.65%);
			}
		}
	}
</style>
