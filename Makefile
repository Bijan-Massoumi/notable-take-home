target:
	cd ./calendar; npm install; npm run-script build  --silent
	cp -r ./calendar/build ./server

compile:
	cd ./calendar; npm run-script build  --silent
	cp -r ./calendar/build ./server

