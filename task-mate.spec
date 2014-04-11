Summary:	Metapackage for MATE desktop environment
Name:		task-mate
Version:	1.8.0
Release:	2
Group:		Graphical desktop/GNOME
License:	GPLv2+
BuildArch:	noarch

Requires:	%{name}-minimal >= %{version}
Requires:	atril >= %{version}
Requires:	mate-applets >= %{version}
Requires:	mate-calc >= %{version}
Requires:	dconf-editor
Requires:	mate-dialogs >= %{version}
Requires:	engrampa >= %{version}
Requires:	eom >= %{version}
Requires:	mate-indicator-applet >= %{version}
Requires:	gnome-keyring >= %{version}
Requires:	mate-media >= %{version}
Requires:	mate-netspeed >= %{version}
Requires:	mate-screensaver >= %{version}
Requires:	mate-sensors-applet >= %{version}
Requires:	mate-system-monitor >= %{version}
Requires:	mate-system-tools >= %{version}
Requires:	pluma >= %{version}
Requires:	mate-terminal >= %{version}
Requires:	mate-utils >= %{version}
Requires:	mozo >= %{version}
Requires:	lightdm-gtk2-greeter
Requires:	lightdm
#Suggests:	mate-file-manager-sendto-pidgin >= %{version}
#Suggests:	mate-file-manager-sendto-upnpl >= %{version}

%description
This package is a meta-package, meaning that its purpose is to contain
dependencies for running the MATE.

%package minimal
Summary:	Minimal dependencies needed for MATE desktop 
Group:		Graphical desktop/GNOME

Requires:	caja >= %{version}
# MD mate made the switch, this really should be pulled by each pkg contains gschemas
Requires:	gsettings-desktop-schemas
Requires:	mate-backgrounds >= %{version}
Requires:	mate-control-center >= %{version}
Requires:	mate-icon-theme >= %{version}
Requires:	mate-notification-daemon >= %{version}
Requires:	mate-panel >= %{version}
Requires:	mate-polkit >= %{version}
Requires:	mate-power-manager >= %{version}
Requires:	mate-session-manager >= %{version}
Requires:	mate-themes >= %{version}
Requires:	marco >= %{version}
Requires:	preload
Requires:	task-pulseaudio
Requires:	task-x11
Requires:	libwnck

%description minimal
This package is a meta-package, meaning that its purpose is to contain
minimal dependencies for running a minimal MATE desktop environment.

%files

%files minimal

