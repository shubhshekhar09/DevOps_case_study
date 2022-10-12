
## Nginx Configuration
``` mkdir nginx```  #Done
## SSL Configuration
```
mkdir ssl 
cd ssl

openssl req -x509 -sha256 -nodes -days 365 -newkey rsa:2048 -subj '/O=devops Inc./CN=devops.com' -keyout devops.com.key -out devops.com.crt

openssl req -out devops.com.csr -newkey rsa:2048 -nodes -keyout devops.com.key -subj "/CN=devops.com/O=some organization"
openssl x509 -req -sha256 -days 365 -CA devops.com.crt -CAkey devops.com.key -set_serial 0 -in devops.com.csr -out devops.com.crt ```