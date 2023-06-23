<!DOCTYPE html>
<html>

<body>
  <h1>GLPI Installation</h1>

  <h2>Description</h2>
  <p>This project contains a script that automates the installation process of GLPI, an IT asset management and service desk software. The script installs the required LAMP (Linux, Apache, MySQL/MariaDB, PHP) components, configures the necessary settings, creates the database and user, downloads and installs GLPI, and sets up the Apache VirtualHost.</p>

  <h2>Prerequisites</h2>
  <ul>
    <li>Linux operating system</li>
    <li>Apache2 web server</li>
    <li>PHP 7.4</li>
    <li>MariaDB</li>
    <li><code>wget</code> command-line tool</li>
  </ul>

  <h2>Installation</h2>
  <ol>
    <li>Clone the project repository:</li>
  </ol>
  <pre><code>git clone https://github.com/your-username/glpi-installation.git</code></pre>

  <ol start="2">
    <li>Change into the project directory:</li>
  </ol>
  <pre><code>cd glpi-installation</code></pre>

  <ol start="3">
    <li>Run the installation script:</li>
  </ol>
  <pre><code>python install_glpi.py</code></pre>

  <h2>Usage</h2>
  <p>The installation script can be executed by running the <code>install_glpi.py</code> file using Python.</p>
  <pre><code>python install_glpi.py</code></pre>
  <p>Make sure to modify the script according to your specific requirements before running it.</p>

  <h2>Configuration</h2>
  <p>Before running the installation script, you may need to modify the following variables:</p>
  <ul>
    <li><code>username</code>: Replace with your desired username for the database user.</li>
    <li><code>your_host</code>: Replace with the hostname or IP address of your server.</li>
    <li><code>password</code>: Replace with your desired password for the database user.</li>
  </ul>

  <h2>License</h2>
  <p>This project is licensed under the <a href="LICENSE">MIT License</a>.</p>

  <h2>Acknowledgments</h2>
  <p><a href="https://glpi-project.org/">GLPI Project</a> for providing the GLPI software.</p>

  <p>Please note that this README file provides an overview of the project and assumes some prior knowledge of the LAMP stack and server administration.</p>
</body>
</html>

