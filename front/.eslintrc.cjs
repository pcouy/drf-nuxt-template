module.exports = {
    env: {
        browser: true,
        es2021: true,
    },
    parser: "vue-eslint-parser",
    extends: ["@nuxt/eslint-config", "plugin:prettier/recommended"],
    overrides: [
        {
            files: ["composables/*.{js,ts}"],
            rules: {
                "no-undef": "off",
            },
        },
    ],
};
