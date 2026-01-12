/ [Home](index.md)

## Lima - Linux Machines (on MacOS)


### Installation Commands
```
brew update
brew install lima
```


### Version Check
```
limactl --version
limactl version 2.0.3
```


### List VM Instances
```
limactl list

NAME            STATUS     SSH                VMTYPE    ARCH       CPUS    MEMORY    DISK      DIR
default         Running    127.0.0.1:55058    vz        aarch64    4       4GiB      100GiB    ~/.lima/default
ubuntu-20.04    Running    127.0.0.1:55585    vz        aarch64    4       4GiB      100GiB    ~/.lima/ubuntu-20.04
```


### Stop VM Instance
```
limactl stop ubuntu-20.04

INFO[0000] Sending SIGINT to hostagent process 78861
INFO[0000] Waiting for the host agent and the driver processes to shut down
INFO[0000] [hostagent] Received SIGINT, shutting down the host agent
INFO[0000] [hostagent] Shutting down the host agent
INFO[0000] [hostagent] Shutting down VZ
INFO[0002] [hostagent] [VZ] - vm state change: stopped
ERRO[0002] [hostagent] accept tcp 127.0.0.1:55585: use of closed network connection
INFO[0003] Waiting for the instance to shut down
INFO[0004] The instance ubuntu-20.04 has shut down
```

### Delete VM Instance
```
limactl delete ubuntu-20.04

INFO[0000] The vz driver process seems already stopped
INFO[0000] The host agent process seems already stopped
INFO[0000] Removing *.pid *.sock *.tmp under "/Users/csp/.lima/ubuntu-20.04"
INFO[0000] Deleted "ubuntu-20.04" ("/Users/csp/.lima/ubuntu-20.04")
```

### Force Delete VM Instance
```
limactl delete --force default

INFO[0000] Sending SIGKILL to the vz driver process 78334
INFO[0000] Sending SIGKILL to the host agent process 78334
INFO[0000] Removing *.pid *.sock *.tmp under "/Users/csp/.lima/default"
INFO[0000] Removing "/Users/csp/.lima/default/default_ep.sock"
INFO[0000] Removing "/Users/csp/.lima/default/default_fd.sock"
INFO[0000] Removing "/Users/csp/.lima/default/ha.pid"
INFO[0000] Removing "/Users/csp/.lima/default/ha.sock"
INFO[0000] Removing "/Users/csp/.lima/default/ssh.sock"
INFO[0000] Removing "/Users/csp/.lima/default/vz.pid"
INFO[0000] Deleted "default" ("/Users/csp/.lima/default")
```


### Verify Empty Instance List
```
limactl list
WARN[0000] No instance found. Run `limactl create` to create an instance.
```


```
limactl info

{
    "version": "2.0.3",
    "templates": [
        {
            "name": "_default/mounts",
            "location": "/opt/homebrew/share/lima/templates/_default/mounts.yaml"
        },
        {
            "name": "_images/almalinux-10",
            "location": "/opt/homebrew/share/lima/templates/_images/almalinux-10.yaml"
        },
        {
            "name": "_images/almalinux-8",
            "location": "/opt/homebrew/share/lima/templates/_images/almalinux-8.yaml"
        },
        {
            "name": "_images/almalinux-9",
            "location": "/opt/homebrew/share/lima/templates/_images/almalinux-9.yaml"
        },
        {
            "name": "_images/almalinux-kitten-10",
            "location": "/opt/homebrew/share/lima/templates/_images/almalinux-kitten-10.yaml"
        },
        {
            "name": "_images/alpine",
            "location": "/opt/homebrew/share/lima/templates/_images/alpine.yaml"
        },
        {
            "name": "_images/alpine-iso",
            "location": "/opt/homebrew/share/lima/templates/_images/alpine-iso.yaml"
        },
        {
            "name": "_images/archlinux",
            "location": "/opt/homebrew/share/lima/templates/_images/archlinux.yaml"
        },
        {
            "name": "_images/centos-stream-10",
            "location": "/opt/homebrew/share/lima/templates/_images/centos-stream-10.yaml"
        },
        {
            "name": "_images/centos-stream-9",
            "location": "/opt/homebrew/share/lima/templates/_images/centos-stream-9.yaml"
        },
        {
            "name": "_images/debian-11",
            "location": "/opt/homebrew/share/lima/templates/_images/debian-11.yaml"
        },
        {
            "name": "_images/debian-12",
            "location": "/opt/homebrew/share/lima/templates/_images/debian-12.yaml"
        },
        {
            "name": "_images/debian-13",
            "location": "/opt/homebrew/share/lima/templates/_images/debian-13.yaml"
        },
        {
            "name": "_images/fedora",
            "location": "/opt/homebrew/share/lima/templates/_images/fedora.yaml"
        },
        {
            "name": "_images/fedora-41",
            "location": "/opt/homebrew/share/lima/templates/_images/fedora-41.yaml"
        },
        {
            "name": "_images/fedora-42",
            "location": "/opt/homebrew/share/lima/templates/_images/fedora-42.yaml"
        },
        {
            "name": "_images/fedora-43",
            "location": "/opt/homebrew/share/lima/templates/_images/fedora-43.yaml"
        },
        {
            "name": "_images/opensuse-leap",
            "location": "/opt/homebrew/share/lima/templates/_images/opensuse-leap.yaml"
        },
        {
            "name": "_images/opensuse-leap-15",
            "location": "/opt/homebrew/share/lima/templates/_images/opensuse-leap-15.yaml"
        },
        {
            "name": "_images/opensuse-leap-16",
            "location": "/opt/homebrew/share/lima/templates/_images/opensuse-leap-16.yaml"
        },
        {
            "name": "_images/oraclelinux-10",
            "location": "/opt/homebrew/share/lima/templates/_images/oraclelinux-10.yaml"
        },
        {
            "name": "_images/oraclelinux-8",
            "location": "/opt/homebrew/share/lima/templates/_images/oraclelinux-8.yaml"
        },
        {
            "name": "_images/oraclelinux-9",
            "location": "/opt/homebrew/share/lima/templates/_images/oraclelinux-9.yaml"
        },
        {
            "name": "_images/rocky-10",
            "location": "/opt/homebrew/share/lima/templates/_images/rocky-10.yaml"
        },
        {
            "name": "_images/rocky-8",
            "location": "/opt/homebrew/share/lima/templates/_images/rocky-8.yaml"
        },
        {
            "name": "_images/rocky-9",
            "location": "/opt/homebrew/share/lima/templates/_images/rocky-9.yaml"
        },
        {
            "name": "_images/ubuntu",
            "location": "/opt/homebrew/share/lima/templates/_images/ubuntu.yaml"
        },
        {
            "name": "_images/ubuntu-20.04",
            "location": "/opt/homebrew/share/lima/templates/_images/ubuntu-20.04.yaml"
        },
        {
            "name": "_images/ubuntu-22.04",
            "location": "/opt/homebrew/share/lima/templates/_images/ubuntu-22.04.yaml"
        },
        {
            "name": "_images/ubuntu-24.04",
            "location": "/opt/homebrew/share/lima/templates/_images/ubuntu-24.04.yaml"
        },
        {
            "name": "_images/ubuntu-24.10",
            "location": "/opt/homebrew/share/lima/templates/_images/ubuntu-24.10.yaml"
        },
        {
            "name": "_images/ubuntu-25.04",
            "location": "/opt/homebrew/share/lima/templates/_images/ubuntu-25.04.yaml"
        },
        {
            "name": "_images/ubuntu-25.10",
            "location": "/opt/homebrew/share/lima/templates/_images/ubuntu-25.10.yaml"
        },
        {
            "name": "_images/ubuntu-lts",
            "location": "/opt/homebrew/share/lima/templates/_images/ubuntu-lts.yaml"
        },
        {
            "name": "almalinux",
            "location": "/opt/homebrew/share/lima/templates/almalinux.yaml"
        },
        {
            "name": "almalinux-10",
            "location": "/opt/homebrew/share/lima/templates/almalinux-10.yaml"
        },
        {
            "name": "almalinux-8",
            "location": "/opt/homebrew/share/lima/templates/almalinux-8.yaml"
        },
        {
            "name": "almalinux-9",
            "location": "/opt/homebrew/share/lima/templates/almalinux-9.yaml"
        },
        {
            "name": "almalinux-kitten",
            "location": "/opt/homebrew/share/lima/templates/almalinux-kitten.yaml"
        },
        {
            "name": "almalinux-kitten-10",
            "location": "/opt/homebrew/share/lima/templates/almalinux-kitten-10.yaml"
        },
        {
            "name": "alpine",
            "location": "/opt/homebrew/share/lima/templates/alpine.yaml"
        },
        {
            "name": "alpine-iso",
            "location": "/opt/homebrew/share/lima/templates/alpine-iso.yaml"
        },
        {
            "name": "apptainer",
            "location": "/opt/homebrew/share/lima/templates/apptainer.yaml"
        },
        {
            "name": "apptainer-rootful",
            "location": "/opt/homebrew/share/lima/templates/apptainer-rootful.yaml"
        },
        {
            "name": "archlinux",
            "location": "/opt/homebrew/share/lima/templates/archlinux.yaml"
        },
        {
            "name": "buildkit",
            "location": "/opt/homebrew/share/lima/templates/buildkit.yaml"
        },
        {
            "name": "centos-stream",
            "location": "/opt/homebrew/share/lima/templates/centos-stream.yaml"
        },
        {
            "name": "centos-stream-10",
            "location": "/opt/homebrew/share/lima/templates/centos-stream-10.yaml"
        },
        {
            "name": "centos-stream-9",
            "location": "/opt/homebrew/share/lima/templates/centos-stream-9.yaml"
        },
        {
            "name": "debian",
            "location": "/opt/homebrew/share/lima/templates/debian.yaml"
        },
        {
            "name": "debian-12",
            "location": "/opt/homebrew/share/lima/templates/debian-12.yaml"
        },
        {
            "name": "debian-13",
            "location": "/opt/homebrew/share/lima/templates/debian-13.yaml"
        },
        {
            "name": "default",
            "location": "/opt/homebrew/share/lima/templates/default.yaml"
        },
        {
            "name": "docker",
            "location": "/opt/homebrew/share/lima/templates/docker.yaml"
        },
        {
            "name": "docker-rootful",
            "location": "/opt/homebrew/share/lima/templates/docker-rootful.yaml"
        },
        {
            "name": "experimental/alsa",
            "location": "/opt/homebrew/share/lima/templates/experimental/alsa.yaml"
        },
        {
            "name": "experimental/debian-sid",
            "location": "/opt/homebrew/share/lima/templates/experimental/debian-sid.yaml"
        },
        {
            "name": "experimental/gentoo",
            "location": "/opt/homebrew/share/lima/templates/experimental/gentoo.yaml"
        },
        {
            "name": "experimental/opensuse-tumbleweed",
            "location": "/opt/homebrew/share/lima/templates/experimental/opensuse-tumbleweed.yaml"
        },
        {
            "name": "experimental/rke2",
            "location": "/opt/homebrew/share/lima/templates/experimental/rke2.yaml"
        },
        {
            "name": "experimental/u7s",
            "location": "/opt/homebrew/share/lima/templates/experimental/u7s.yaml"
        },
        {
            "name": "experimental/ubuntu-26.04",
            "location": "/opt/homebrew/share/lima/templates/experimental/ubuntu-26.04.yaml"
        },
        {
            "name": "experimental/ubuntu-next",
            "location": "/opt/homebrew/share/lima/templates/experimental/ubuntu-next.yaml"
        },
        {
            "name": "experimental/vnc",
            "location": "/opt/homebrew/share/lima/templates/experimental/vnc.yaml"
        },
        {
            "name": "experimental/wsl2",
            "location": "/opt/homebrew/share/lima/templates/experimental/wsl2.yaml"
        },
        {
            "name": "faasd",
            "location": "/opt/homebrew/share/lima/templates/faasd.yaml"
        },
        {
            "name": "fedora",
            "location": "/opt/homebrew/share/lima/templates/fedora.yaml"
        },
        {
            "name": "fedora-41",
            "location": "/opt/homebrew/share/lima/templates/fedora-41.yaml"
        },
        {
            "name": "fedora-42",
            "location": "/opt/homebrew/share/lima/templates/fedora-42.yaml"
        },
        {
            "name": "fedora-43",
            "location": "/opt/homebrew/share/lima/templates/fedora-43.yaml"
        },
        {
            "name": "k0s",
            "location": "/opt/homebrew/share/lima/templates/k0s.yaml"
        },
        {
            "name": "k3s",
            "location": "/opt/homebrew/share/lima/templates/k3s.yaml"
        },
        {
            "name": "k8s",
            "location": "/opt/homebrew/share/lima/templates/k8s.yaml"
        },
        {
            "name": "linuxbrew",
            "location": "/opt/homebrew/share/lima/templates/linuxbrew.yaml"
        },
        {
            "name": "opensuse",
            "location": "/opt/homebrew/share/lima/templates/opensuse.yaml"
        },
        {
            "name": "opensuse-leap",
            "location": "/opt/homebrew/share/lima/templates/opensuse-leap.yaml"
        },
        {
            "name": "opensuse-leap-15",
            "location": "/opt/homebrew/share/lima/templates/opensuse-leap-15.yaml"
        },
        {
            "name": "opensuse-leap-16",
            "location": "/opt/homebrew/share/lima/templates/opensuse-leap-16.yaml"
        },
        {
            "name": "oraclelinux",
            "location": "/opt/homebrew/share/lima/templates/oraclelinux.yaml"
        },
        {
            "name": "oraclelinux-10",
            "location": "/opt/homebrew/share/lima/templates/oraclelinux-10.yaml"
        },
        {
            "name": "oraclelinux-8",
            "location": "/opt/homebrew/share/lima/templates/oraclelinux-8.yaml"
        },
        {
            "name": "oraclelinux-9",
            "location": "/opt/homebrew/share/lima/templates/oraclelinux-9.yaml"
        },
        {
            "name": "podman",
            "location": "/opt/homebrew/share/lima/templates/podman.yaml"
        },
        {
            "name": "podman-rootful",
            "location": "/opt/homebrew/share/lima/templates/podman-rootful.yaml"
        },
        {
            "name": "rocky",
            "location": "/opt/homebrew/share/lima/templates/rocky.yaml"
        },
        {
            "name": "rocky-10",
            "location": "/opt/homebrew/share/lima/templates/rocky-10.yaml"
        },
        {
            "name": "rocky-8",
            "location": "/opt/homebrew/share/lima/templates/rocky-8.yaml"
        },
        {
            "name": "rocky-9",
            "location": "/opt/homebrew/share/lima/templates/rocky-9.yaml"
        },
        {
            "name": "ubuntu",
            "location": "/opt/homebrew/share/lima/templates/ubuntu.yaml"
        },
        {
            "name": "ubuntu-20.04",
            "location": "/opt/homebrew/share/lima/templates/ubuntu-20.04.yaml"
        },
        {
            "name": "ubuntu-22.04",
            "location": "/opt/homebrew/share/lima/templates/ubuntu-22.04.yaml"
        },
        {
            "name": "ubuntu-24.04",
            "location": "/opt/homebrew/share/lima/templates/ubuntu-24.04.yaml"
        },
        {
            "name": "ubuntu-24.10",
            "location": "/opt/homebrew/share/lima/templates/ubuntu-24.10.yaml"
        },
        {
            "name": "ubuntu-25.04",
            "location": "/opt/homebrew/share/lima/templates/ubuntu-25.04.yaml"
        },
        {
            "name": "ubuntu-25.10",
            "location": "/opt/homebrew/share/lima/templates/ubuntu-25.10.yaml"
        },
        {
            "name": "ubuntu-lts",
            "location": "/opt/homebrew/share/lima/templates/ubuntu-lts.yaml"
        }
    ],
    "defaultTemplate": {
        "base": [
            {
                "url": "template:_images/ubuntu"
            },
            {
                "url": "template:_default/mounts"
            }
        ],
        "minimumLimaVersion": "2.0.0",
        "vmOpts": {
            "qemu": {
                "cpuType": null,
                "minimumVersion": null
            },
            "vz": {
                "diskImageFormat": null,
                "rosetta": {
                    "binfmt": null,
                    "enabled": null
                }
            }
        },
        "os": "Linux",
        "arch": "aarch64",
        "cpus": 4,
        "memory": "4GiB",
        "disk": "100GiB",
        "mountInotify": false,
        "ssh": {
            "localPort": 0,
            "loadDotSSHPubKeys": false,
            "forwardAgent": false,
            "forwardX11": false,
            "forwardX11Trusted": false
        },
        "firmware": {
            "legacyBIOS": false
        },
        "audio": {
            "device": ""
        },
        "video": {
            "display": "none",
            "vnc": {}
        },
        "upgradePackages": false,
        "containerd": {
            "system": false,
            "user": true,
            "archives": [
                {
                    "location": "https://github.com/containerd/nerdctl/releases/download/v2.2.1/nerdctl-full-2.2.1-linux-amd64.tar.gz",
                    "arch": "x86_64",
                    "digest": "sha256:cf4720a290f098f1a66d34a1b2e1d3736c9014fceca737861fb7a069c66c01c2"
                },
                {
                    "location": "https://github.com/containerd/nerdctl/releases/download/v2.2.1/nerdctl-full-2.2.1-linux-arm64.tar.gz",
                    "arch": "aarch64",
                    "digest": "sha256:2c4b97312acd41c4dfe80db6e82592367b3862b5db4c51ce67a6d79bf6ee00ee"
                }
            ]
        },
        "guestInstallPrefix": "/usr/local",
        "hostResolver": {
            "enabled": true,
            "ipv6": false
        },
        "propagateProxyEnv": true,
        "caCerts": {
            "removeDefaults": false
        },
        "rosetta": {},
        "plain": false,
        "timezone": "America/Toronto",
        "nestedVirtualization": false,
        "user": {
            "name": "csp",
            "comment": "Raja CSP Raman",
            "home": "/home/csp.linux",
            "shell": "/bin/bash",
            "uid": 501
        }
    },
    "limaHome": "/Users/csp/.lima",
    "vmTypes": [
        "krunkit",
        "qemu",
        "vz"
    ],
    "vmTypesEx": {
        "krunkit": {
            "location": "/opt/homebrew/Cellar/lima/2.0.3/libexec/lima/lima-driver-krunkit"
        },
        "qemu": {
            "location": "internal"
        },
        "vz": {
            "location": "internal"
        }
    },
    "guestAgents": {
        "aarch64": {
            "location": "/opt/homebrew/share/lima/lima-guestagent.Linux-aarch64.gz"
        }
    },
    "shellEnvBlock": [
        "BASH*",
        "DISPLAY",
        "DYLD_*",
        "EUID",
        "FPATH",
        "GID",
        "GROUP",
        "HOME",
        "HOSTNAME",
        "LD_*",
        "LOGNAME",
        "OLDPWD",
        "PATH",
        "PWD",
        "SHELL",
        "SHLVL",
        "SSH_*",
        "TERM",
        "TERMINFO",
        "TMPDIR",
        "UID",
        "USER",
        "XAUTHORITY",
        "XDG_*",
        "ZDOTDIR",
        "ZSH*",
        "_*"
    ],
    "hostOS": "darwin",
    "hostArch": "aarch64",
    "identityFile": "/Users/csp/.lima/_config/user",
    "plugins": [
        {
            "name": "mcp",
            "path": "/opt/homebrew/Cellar/lima/2.0.3/libexec/lima/limactl-mcp"
        }
    ],
    "libexecPaths": [
        "/opt/homebrew/Cellar/lima/2.0.3/libexec/lima"
    ],
    "sharePaths": [
        "/opt/homebrew/share/lima",
        "/opt/homebrew/Cellar/lima/2.0.3/share/lima"
    ]
}
```