cd /front_app
npm install
npm run dev
sleep 180 # Leave some time to `docker compose exec front bash` into the container if the dev server crashes
