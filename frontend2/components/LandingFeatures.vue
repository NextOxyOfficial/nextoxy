<template>
  <div class="dark:bg-muted-900 bg-white py-24">
    <div class="mx-auto w-full max-w-7xl px-4">
      <div class="mb-12 max-w-2xl">
        <BaseText
          as="p"
          size="sm"
          class="text-primary-500 mb-2 uppercase tracking-wider"
          >There's more</BaseText
        >
        <BaseHeading
          as="h2"
          size="2xl"
          weight="light"
          lead="tight"
          class="text-muted-800 md:!text-4xl md:!leading-tight mx-auto mb-4 dark:text-white"
        >
          Developer friendly
        </BaseHeading>
        <BaseParagraph
          size="sm"
          class="text-muted-500 dark:text-muted-100 mx-auto mb-4 md:!text-lg"
        >
          NextOxy is renowned for being developer-friendly. With a supportive
          and collaborative environment, NextOxy empowers its developers to
          unleash their creativity and expertise. The company provides the
          necessary resources, tools, and a culture that fosters growth and
          innovation, making it an ideal workplace for developers.
        </BaseParagraph>
      </div>
      <div class="ltablet:grid-cols-3 grid gap-8 sm:grid-cols-2 lg:grid-cols-3">
        <LandingFeaturesTile
          title="Django"
          icon="vscode-icons:file-type-django"
        >
          Python web framework for building scalable and secure web
          applications.
        </LandingFeaturesTile>
        <LandingFeaturesTile title="PostgreSQL" icon="logos:postgresql">
          Open-source relational database management system.
        </LandingFeaturesTile>
        <LandingFeaturesTile
          title="Django Rest Framework"
          icon="devicon-plain:djangorest"
        >
          Powerful toolkit for building RESTful APIs with Django framework.
        </LandingFeaturesTile>
        <LandingFeaturesTile title="Nuxt" icon="simple-icons:nuxtdotjs">
          Nuxt is the latest version of the Nuxt.js framework, a powerful SSR
          vue framework.
        </LandingFeaturesTile>
        <LandingFeaturesTile
          title="Tailwind CSS"
          icon="simple-icons:tailwindcss"
        >
          Tailwind CSS is a utility-first CSS framework for rapidly building
          custom user interfaces.
        </LandingFeaturesTile>
        <LandingFeaturesTile title="Typescript" icon="file-icons:typescript">
          Typescript is a typed superset of javascript that compiles to plain
          JS.
        </LandingFeaturesTile>
        <LandingFeaturesTile title="Vite" icon="simple-icons:vite">
          Vite is a next generation frontend tool for frontend development.
        </LandingFeaturesTile>
        <LandingFeaturesTile title="Node LTS" icon="teenyicons:nodejs-solid">
          Node 18 is one of the latest versions of Node.js, a powerful
          javascript server engine.
        </LandingFeaturesTile>
        <LandingFeaturesTile title="Pnpm" icon="file-icons:pnpm">
          Pnpm is a fast, disk space efficient package manager for the npm and
          Yarn registries.
        </LandingFeaturesTile>
        <LandingFeaturesTile title="Eslint" icon="file-icons:eslint">
          Eslint is a tool for identifying and reporting on patterns found in
          JavaScript code.
        </LandingFeaturesTile>
        <LandingFeaturesTile title="Prettier" icon="simple-icons:prettier">
          Prettier is an opinionated code formatter. It enforces a consistent
          code style.
        </LandingFeaturesTile>
        <LandingFeaturesTile title="Icones.js" icon="ph:lightning-duotone">
          Icones.js is a library that allows you to use any icon from any icon
          library.
        </LandingFeaturesTile>
      </div>

      <!-- <div class="mt-16 flex items-center justify-center">
        <BaseButton
          to="https://go.cssninja.io/buy-tairo"
          shape="curved"
          color="primary"
        >
          Get Tairo Dashboard System
        </BaseButton>
      </div> -->
    </div>
  </div>
</template>
