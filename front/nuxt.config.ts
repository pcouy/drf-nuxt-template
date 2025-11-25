// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: false },
  css: ["assets/styles/main.scss"],
  ssr: false,
  telemetry: false,
  compatibilityDate: '2025-07-15',
  modules: ['@nuxt/content', '@nuxt/eslint'],
  vite: {
      server: {
          allowedHosts: ["front"],
      },
  },
  runtimeConfig: {
      apiRoot: '/api/',
  },
})
