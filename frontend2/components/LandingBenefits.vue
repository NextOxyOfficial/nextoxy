<template>
  <div class="dark:bg-muted-900 bg-white pb-24">
    <div class="mx-auto w-full max-w-7xl px-4">
      <div class="mb-10 max-w-2xl">
        <BaseText
          size="sm"
          as="p"
          class="text-primary-500 mb-2 text-[0.65rem] uppercase tracking-wider"
          >We back you up</BaseText
        >
        <BaseHeading
          as="h2"
          size="2xl"
          weight="light"
          lead="tight"
          class="text-muted-800 mx-auto mb-4 dark:text-white md:!text-4xl md:!leading-tight"
        >
          Our 24/7 Dedicated Customers Support Team!
        </BaseHeading>
        <BaseParagraph
          size="sm"
          class="text-muted-500 dark:text-muted-100 mx-auto mb-4 md:!text-lg md:!leading-tight"
        >
          We understand the importance of providing exceptional customer support
          to our clients. That's why we offer a 24/7 dedicated customer support
          team that is always ready to assist you with any issues or concerns.
        </BaseParagraph>
      </div>
      <div class="ptablet:grid-cols-2 grid gap-6 sm:grid-cols-3">
        <LandingLayersBox
          title="Customer Support"
          icon="streamline:interface-help-customer-support-4-customer-headset-help-phone-support"
          to="/"
          color="indigo"
        >
          <a class="text-indigo-500" href="mailto:support@nextoxy.com"
            >support@nextoxy.com</a
          >
          <br />
          NextOxy provides exceptional customer support, offering timely
          assistance, knowledgeable staff, and efficient problem-solving,
          commited to ensuring customer satisfaction and builds trust with
          clients.
        </LandingLayersBox>
        <LandingLayersBox
          title="Finance"
          icon="fa6-brands:github"
          to="/"
          color="purple"
        >
          <a class="text-indigo-500" href="mailto:finance@nextoxy.com"
            >finance@nextoxy.com</a
          >
          <br />
          NextOxy's finance solutions empower businesses with robust financial
          management tools, enabling efficient budgeting, accurate forecasting,
          streamlined invoicing, and comprehensive reporting.
        </LandingLayersBox>
        <LandingLayersBox
          title="Business Oppertunities"
          icon="fa6-brands:discord"
          to="/"
        >
          <a class="text-indigo-500" href="mailto:bizopp@nextoxy.com"
            >bizopp@nextoxy.com</a
          >
          <br />
          NextOxy helps businesses unlock new opportunities. Their software
          equips organizations with the knowledge to make informed strategic
          decisions and capitalize on emerging business prospects.
        </LandingLayersBox>
      </div>
    </div>
  </div>
</template>
