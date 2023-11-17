
```
sudo systemd-nspawn \
-bD / \
--volatile=no \
--bind-ro=~ .Xauthority \
--bind=/run/user/1000 \
--bind=/tmp/.X11-unix \
--bind=/dev/shm \
--bind=/dev/dri \
--bind=/run/dbus/system_bus_socket \
--bind=~
```


> Written with [StackEdit](https://stackedit.io/).
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE3NTI2OTgzMzJdfQ==
-->