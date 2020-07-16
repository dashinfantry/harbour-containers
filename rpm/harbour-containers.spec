# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       harbour-containers

# >> macros
# << macros

Summary:    sailfish-containers LXC Silica UI
Version:    0.3
Release:    4
Group:      Qt/Qt
License:    LICENSE
URL:        http://example.org/
Source0:    %{name}-%{version}.tar.bz2
Source100:  harbour-containers.yaml
Requires:   sailfishsilica-qt5 >= 0.10.9
Requires:   lxc-templates-desktop
Requires:   python3-gobject
Requires:   dbus-python3
Requires:   nemo-qml-plugin-dbus-qt5
Requires:   qxdisplay
Requires:   sailfish-polkit-agent
BuildRequires:  pkgconfig(sailfishapp) >= 1.0.2
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  desktop-file-utils

%description
Short description of my Sailfish OS Application


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%qmake5 

make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre

# << install pre
%qmake5_install

# >> install post
chmod +x  %{buildroot}/usr/share/%{name}/service/daemon.py
chmod +x  %{buildroot}/usr/share/%{name}/scripts/host/*.sh
chmod +x  %{buildroot}/usr/share/%{name}/scripts/guest/*.sh
chmod +x  %{buildroot}/usr/share/%{name}/scripts/guest/setups/*.sh

# << install post

desktop-file-install --delete-original       \
  --dir %{buildroot}%{_datadir}/applications             \
   %{buildroot}%{_datadir}/applications/*.desktop

%files
%defattr(-,root,root,-)
%{_bindir}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/*/apps/%{name}.png
/etc/dbus-1/system.d/org.sailfishcontainers.daemon.conf
/usr/share/dbus-1/system-services/org.sailfishcontainers.daemon.service
/etc/systemd/system/sailfish-containers.service
/usr/share/polkit-1/actions/org.sailfishcontainers.daemon.policy
# >> files
# << files
