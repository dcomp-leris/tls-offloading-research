# NGINX Docker Image with kTLS Support

This Dockerfile is used to build a Docker image for NGINX, a high-performance web server, with the option to enable or disable kTLS (Kernel Transport Layer Security) support during the image build.

## Usage

### Build the Docker Image

To build the Docker image, you can use the following command:

```bash
docker build -t nginx-ktls --build-arg KTLS_ENABLED=true .
```

- Set the `KTLS_ENABLED` argument to `true` to enable kTLS support, or `false` to disable it.

### Run the Docker Container

After building the image, you can run a Docker container from it with the following command:

```bash
docker run -d -p 8443:8383 --name nginx-container nginx-ktls
```

- This command starts a container named `nginx-container` based on the `nginx-ktls` image.
- Port `8443` on the host is mapped to port `8383` inside the container, allowing you to access NGINX on port `8383` of your host machine.

### NGINX Configuration

- Depending on whether kTLS is enabled or disabled, NGINX will use different configuration files:
  - When `KTLS_ENABLED=true`, NGINX will use `nginx_ktls.conf`.
  - When `KTLS_ENABLED=false`, NGINX will use `nginx_noktls.conf`.

You can customize these configuration files to suit your specific needs.

## SSL Certificates

- This Docker image generates a self-signed SSL certificate during the build process.
- The certificate files are stored in `/etc/ssl/private/nginx-selfsigned.key` and `/etc/ssl/certs/nginx-selfsigned.crt`.
- You can replace these files with your own SSL certificate files for production use.

## NGINX Data

- The image creates sample data files of various sizes in the `/data` directory.
- These files can be used for testing NGINX's data-serving capabilities.

## Additional Information

- NGINX version: 1.21.4
- OpenSSL version: 3.0.0

Feel free to customize this Dockerfile and NGINX configuration files to meet your specific requirements.


## License

This software is released under the [BSD-3 License](https://opensource.org/license/bsd-3-clause/). You are free to use, modify, and distribute this software, provided that you include the original copyright notice and disclaimers. The BSD-3 License is a permissive open-source license that encourages collaboration and innovation. It grants you the freedom to adapt this software to your needs while respecting the original author's contributions. Feel free to contribute to the project or build upon it for your own projects. Please review the LICENSE file on the root of this repo for the full terms and conditions of this license.
