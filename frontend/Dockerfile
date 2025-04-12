FROM node:18-alpine

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

# Add OpenSSL compatibility fix
ENV NODE_OPTIONS=--openssl-legacy-provider

RUN npm run build

# Serve static files
RUN npm install -g serve

CMD ["serve", "-s", "build"]