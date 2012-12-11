Summary:	Metapackage for MATE desktop environment
Name:		task-mate
Version:	1.4.0
Release:	1
Group:		Graphical desktop/GNOME
License:	GPLv2+
BuildArch:	noarch

Requires:	%{name}-minimal >= %{version}
Requires:	atril >= %{version}
Requires:	caja-sendto-bluetooth >= %{version}
Requires:	ffmpegthumbnailer-caja >= %{version}
Requires:	mate-applets >= %{version}
Requires:	mate-bluetooth >= %{version}
Requires:	mate-calc >= %{version}
Requires:	mate-conf-editor >= %{version}
Requires:	mate-dialogs >= %{version}
# should be engrampa
Requires:	mate-file-archiver >= %{version}
Requires:	mate-file-manager-gksu >= %{version}
Requires:	mate-file-manager-image-converter >= %{version}
Requires:	mate-file-manager-open-terminal >= %{version}
# should be eom
Requires:	mate-image-viewer >= %{version}
Requires:	mate-indicator-applet >= %{version}
Requires:	mate-keyring >= %{version}
Requires:	mate-media >= %{version}
Requires:	mate-netspeed >= %{version}
Requires:	mate-notification-daemon >= %{version}
Requires:	mate-screensaver >= %{version}
Requires:	mate-sensors-applet >= %{version}
Requires:	mate-system-monitor >= %{version}
Requires:	mate-system-tools >= %{version}
# should be pluma
Requires:	mate-text-editor >= %{version}
Requires:	mate-terminal >= %{version}
Requires:	mate-utils >= %{version}
Requires:	mozo >= %{version}
#Requires:	python-mate-desktop >= %{version}
#Requires:	python-mate-keyring >= %{version}
#Requires:	python-mate-marco >= %{version}
#Requires:	python-mate-wnck >= %{version}
#Requires:	python-matevfs >= %{version}
#Suggests:	caja-filesharing
#Suggests:	caja-sendto-evolution
#Suggests:	gucharmap
Suggests:	gdm-220
Suggests:	mate-file-manager-sendto-pidginl >= %{version}
Suggests:	mate-file-manager-sendto-upnpl >= %{version}

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




%changelog
* Wed Jun 13 2012 Matthew Dawkins <mattydaw@mandriva.org> 1.2.0-2
+ Revision: 805484
- rebuild adding more requires for functionality

* Fri Jun 08 2012 Matthew Dawkins <mattydaw@mandriva.org> 1.2.0-1
+ Revision: 803437
- imported package task-mate

