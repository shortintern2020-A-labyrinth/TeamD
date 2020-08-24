# ビルド環境
FROM node:lts-alpine as build-stage
WORKDIR /code
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build
RUN npm run generate
RUN npm install --save @nuxtjs/auth

# 本番環境
FROM nginx:stable-alpine as production-stage
COPY --from=build-stage /code/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
