// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
    devtools: { enabled: false },
    css: ["~/assets/styles/main.scss"],
    ssr: false,
    telemetry: false,
});
