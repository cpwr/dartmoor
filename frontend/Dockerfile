FROM debian:latest AS build-env

# Install flutter dependencies
RUN apt-get update 
RUN apt-get install -y curl git wget unzip libgconf-2-4 gdb libstdc++6 libglu1-mesa fonts-droid-fallback lib32stdc++6 python3
RUN apt-get clean

# Clone the flutter repo
RUN git clone https://github.com/flutter/flutter.git /usr/local/flutter

# Set flutter path
# RUN /usr/local/flutter/bin/flutter doctor -v
ENV PATH="/usr/local/flutter/bin:/usr/local/flutter/bin/cache/dart-sdk/bin:${PATH}"

# Run flutter doctor
RUN flutter doctor -v

# Update flutter
RUN flutter channel stable
RUN flutter upgrade

# Enable flutter web
RUN flutter config --enable-web
RUN flutter config --no-analytics

# Copy files to container and build
RUN mkdir /app/
COPY . /app/
WORKDIR /app/
RUN flutter build web

FROM nginx
COPY ./nginx-site.conf /etc/nginx/conf.d/default.conf
COPY --from=build-env /app/build/web /usr/share/nginx/html