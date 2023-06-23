import os
import subprocess

# LAMP bileşenlerinin kurulumu
subprocess.run(["sudo", "apt", "install", "-y", "apache2", "php7.4", "php7.4-curl", "php7.4-zip", "php7.4-gd", "php7.4-intl", "php7.4-pear", "php7.4-imagick", "php-bz2", "php7.4-imap", "php-memcache", "php7.4-pspell", "php7.4-tidy", "php7.4-xmlrpc", "php7.4-xsl", "php7.4-mbstring", "php7.4-ldap", "php-cas", "php-apcu", "libapache2-mod-php7.4", "php7.4-mysql", "mariadb-server"])




# Apache ve MariaDB'nin durumunu kontrol etme
subprocess.run(["sudo", "systemctl", "status", "apache2"])
subprocess.run(["sudo", "systemctl", "status", "mariadb"])


subprocess.run(["sudo", "mkdir", "-p", "/var/www/html/glpi"])
subprocess.run(["sudo", "chown", "-R", "www-data:www-data", "/var/www/html/glpi"])

# Firewall'da 80 ve 443 portlarını açma
subprocess.run(["sudo", "ufw", "allow", "80"])
subprocess.run(["sudo", "ufw", "allow", "443"])

# MariaDB root şifresini ayarlama
subprocess.run(["sudo", "mysql_secure_installation"])

# GLPI veritabanı ve kullanıcı oluşturma
subprocess.run(["sudo", "mysql", "-u", "root", "-p", "-e", "CREATE DATABASE glpidb;"])
subprocess.run(["sudo", "mysql", "-u", "root", "-p", "-e", "GRANT ALL PRIVILEGES ON glpidb.* TO username@your_host IDENTIFIED BY 'password';"])
subprocess.run(["sudo", "mysql", "-u", "root", "-p", "-e", "FLUSH PRIVILEGES;"])

# GLPI'nin indirilmesi ve kurulumu
subprocess.run(["cd", "/tmp/"])
subprocess.run(["wget", "https://github.com/glpi-project/glpi/releases/download/9.5.5/glpi-9.5.5.tgz"])
subprocess.run(["tar", "-xvf", "glpi-9.5.5.tgz"])
subprocess.run(["sudo", "mv", "glpi", "/var/www/html/"])
subprocess.run(["sudo", "chmod", "755", "-R", "/var/www/html/"])
subprocess.run(["sudo", "chown", "www-data:www-data", "-R", "/var/www/html/"])

# Apache VirtualHost yapılandırması
glpi_conf = """
<VirtualHost *:80>
   ServerAdmin username@your_host
   DocumentRoot /var/www/html/glpi
   ServerName your_host

   <Directory /var/www/html/glpi>
        Options FollowSymLinks
        AllowOverride All
        Require all granted
   </Directory>

   ErrorLog ${APACHE_LOG_DIR}/your_host_error.log
   CustomLog ${APACHE_LOG_DIR}/your_host_access.log combined
</VirtualHost>
"""

with open("/etc/apache2/sites-available/glpi.conf", "w") as f:
    f.write(glpi_conf)

subprocess.run(["sudo", "ln", "-s", "/etc/apache2/sites-available/glpi.conf", "/etc/apache2/sites-enabled/glpi.conf"])
subprocess.run(["sudo", "a2enmod", "rewrite"])
subprocess.run(["sudo", "systemctl", "restart", "apache2"])

print("GLPI kurulumu tamamlandı.")
