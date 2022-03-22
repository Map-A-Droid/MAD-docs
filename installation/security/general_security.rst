.. _sec_sec_gen:

General Security Advice
========================

Here is some security advice that is not only related to MAD but to servers and software hosting in general.

- Don't run MAD inside a webhosted directory like :code:`/var/www/html`.
- MAD does not need root privileges to run. Start it as a normal user. The only programs that need root are your webserver and your database.
- Don't use the same or similar passwords. A `password manager <https://keepass.info/>`_ can be useful for that.
- Use SSL whenever it's possible. Why? Read `this <https://howhttps.works/why-do-we-need-https/>`_.

Firewall
^^^^^^^^^

It's always a good idea to open as few ports as possible. In MADs case that's only 22 for SSH (even that is not 100% necessary in some cases), 80 and 443 for a Webserver if you are proxying everything. Read more about :code:`iptables` `here <https://www.hostinger.com/tutorials/iptables-tutorial>`_.

SSH Authentication
^^^^^^^^^^^^^^^^^^^

Follow this `guide <https://www.howtogeek.com/443156/the-best-ways-to-secure-your-ssh-server/>`_ and install `fail2ban <https://www.techrepublic.com/article/how-to-install-fail2ban-on-ubuntu-server-18-04/>`_.
