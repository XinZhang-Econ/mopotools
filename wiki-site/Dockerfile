# Build stage: compile the Quartz static site from wiki/ content
FROM node:20-alpine AS builder

WORKDIR /app

# Install Quartz
RUN git clone --depth 1 https://github.com/jackyzha0/quartz.git .
RUN npm ci

# Copy wiki content (injected by Cloud Build)
COPY wiki/ content/

# Copy MoPoTools Quartz config
COPY wiki-site/quartz.config.ts .

# Build static site
RUN npx quartz build

# Serve stage: lightweight nginx to serve the compiled site
FROM nginx:alpine AS runner

COPY --from=builder /app/public /usr/share/nginx/html

# Custom nginx config for SPA-style routing used by Quartz
COPY wiki-site/nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 8080
CMD ["nginx", "-g", "daemon off;"]
