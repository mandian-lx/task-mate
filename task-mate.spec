Summary:	Metapackage for MATE desktop environment
Name:		task-mate
Version:	1.2.0
Release:	2
Group:		Graphical desktop/GNOME
License:	GPLv2+
BuildArch:	noarch

Requires:	%{name}-minimal
Requires:	atril
Requires:	caja-sendto-bluetooth
Requires:	ffmpegthumbnailer-caja
Requires:	mate-applets
Requires:	mate-bluetooth
Requires:	mate-calc
Requires:	mate-conf-editor
Requires:	mate-dialogs
# should be engrampa
Requires:	mate-file-archiver
Requires:	mate-file-manager-gksu
Requires:	mate-file-manager-image-converter
Requires:	mate-file-manager-open-terminal
# should be eom
Requires:	mate-image-viewer
Requires:	mate-indicator-applet
Requires:	mate-keyring
Requires:	mate-media
Requires:	mate-netspeed
Requires:	mate-notification-daemon
Requires:	mate-screensaver
Requires:	mate-sensors-applet
Requires:	mate-system-monitor
Requires:	mate-system-tools
# should be pluma
Requires:	mate-text-editor
Requires:	mate-terminal
Requires:	mate-utils
Requires:	mozo
Requires:	python-mate-desktop
Requires:	python-mate-keyring
Requires:	python-mate-marco
Requires:	python-mate-wnck
Requires:	python-matevfs
#Suggests:	caja-filesharing
#Suggests:	caja-sendto-evolution
#Suggests:	gucharmap
Suggests:	gdm-220
Suggests:	mate-file-manager-sendto-pidgin
Suggests:	mate-file-manager-sendto-upnp

%description
This package is a meta-package, meaning that its purpose is to contain
dependencies for running the MATE.

%package minimal
Summary:	Minimal dependencies needed for MATE desktop 
Group:		Graphical desktop/GNOME

Requires:	mate-backgrounds
Requires:	mate-control-center
# should be caja
Requires:	mate-file-manager
Requires:	mate-icon-theme
Requires:	mate-panel
Requires:	mate-power-manager
Requires:	mate-session-manager
Requires:	mate-themes
# should be marco
Requires:	mate-window-manager
Requires:	preload
Requires:	task-pulseaudio
Requires:	task-x11

%description minimal
This package is a meta-package, meaning that its purpose is to contain
minimal dependencies for running a minimal MATE desktop environment.

%files

%files minimal


