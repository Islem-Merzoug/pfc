FROM node:16.5.0-alpine as build
WORKDIR /app
COPY package.json .
RUN npm install 
COPY . .
RUN npm run build

FROM nginx
COPY --from=build /app/build /var/www
# COPY --from=build /app/build /user/share/nginx/html
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx/nginx.conf /etc/nginx/nginx.conf
# EXPOSE 80
# CMD ["nginx", "-g", "daemon off;"]
