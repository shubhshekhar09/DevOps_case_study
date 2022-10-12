FROM node:12.18.1
ENV NODE_ENV=production

WORKDIR /app

COPY ["node/package.json", "node/package-lock.json*", "./"]

RUN npm install --production

COPY node/ .

CMD [ "node", "server.js" ]