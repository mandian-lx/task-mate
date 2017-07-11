Summary:	Metapackage for MATE desktop environment
Name:		task-mate
Version:	1.18.0
Release:	1
Group:		Graphical desktop/Other
License:	GPLv2+
BuildArch:	noarch

Requires:	%{name}-minimal >= %{version}
Requires:	atril >= %{version}
Requires:	dconf-editor
Requires:	engrampa >= %{version}
Requires:	eom >= %{version}
Requires:	gnome-keyring #>= %{version}
Requires:	lightdm
Requires:	lightdm-gtk3-greeter
Requires:	mate-applets >= %{version}
Requires:	mate-calc >= %{version}
Requires:	mate-indicator-applet >= %{version}
Requires:	mate-media >= %{version}
Requires:	matemixer-backend-pulse >= %{version}
Requires:	mate-screensaver >= %{version}
Requires:	mate-sensors-applet >= %{version}
Requires:	mate-system-monitor >= %{version}
Requires:	mate-terminal >= %{version}
Requires:	mate-user-guide >= %{version}
Requires:	mate-utils >= %{version}
Requires:	mozo >= %{version}
Requires:	pluma >= %{version}
Requires:	yelp
#Suggests:	mate-file-manager-sendto-pidgin >= %{version}
#Suggests:	mate-file-manager-sendto-upnpl >= %{version}

%description
This package is a meta-package, meaning that its purpose is to contain
dependencies for running the MATE.

#---------------------------------------------------------------------------

%package minimal
Summary:	Minimal dependencies needed for MATE desktop 
Group:		Graphical desktop/Other

# MD mate made the switch, this really should be pulled by each pkg contains gschemas
#Requires:	gsettings-desktop-schemas
Requires:	caja >= %{version}
Requires:	libwnck3
Requires:	mate-backgrounds >= %{version}
Requires:	mate-control-center >= %{version}
Requires:	mate-icon-theme >= %{version}
Requires:	mate-notification-daemon >= %{version}
Requires:	mate-panel >= %{version}
Requires:	mate-polkit >= %{version}
Requires:	mate-power-manager >= %{version}
Requires:	mate-session-manager >= %{version}
Requires:	mate-themes >= 3.22 #%{version}
Requires:	marco >= %{version}
#Requires:	openmandriva-mate-config  >= %{version}
Requires:	preload
Requires:	task-pulseaudio
Requires:	task-x11

%description minimal
This package is a meta-package, meaning that its purpose is to contain
minimal dependencies for running a minimal MATE desktop environment.

#---------------------------------------------------------------------------

%files

%files minimal

