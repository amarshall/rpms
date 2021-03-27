%global version0 1.6-rc2

Name:           sway
Version:        1.6
Release:        0.rc2.1%{?dist}
Summary:        i3-compatible window manager for Wayland
License:        MIT
URL:            https://github.com/swaywm/sway
Source0:        %{url}/releases/download/%{version0}/%{name}-%{version0}.tar.gz
Source1:        %{url}/releases/download/%{version0}/%{name}-%{version0}.tar.gz.sig
# 0FDE7BE0E88F5E48: emersion <contact@emersion.fr>
Source2:        https://emersion.fr/.well-known/openpgpkey/hu/dj3498u4hyyarh35rkjfnghbjxug6b19#/gpgkey-0FDE7BE0E88F5E48.gpg

BuildRequires:  gcc-c++
BuildRequires:  gnupg2
BuildRequires:  meson >= 0.53.0
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(json-c) >= 0.13
BuildRequires:  pkgconfig(libevdev)
BuildRequires:  pkgconfig(libinput) >= 1.6.0
BuildRequires:  pkgconfig(libpcre)
BuildRequires:  pkgconfig(libsystemd) >= 239
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(scdoc)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.14
BuildRequires:  pkgconfig(wlroots) >= 0.13.0
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xkbcommon)
# Dmenu is the default launcher in sway
Recommends:     dmenu
# In addition, xargs is recommended for use in such a launcher arrangement
Recommends:     findutils
# Install configs and scripts for better integration with systemd user session
Recommends:     sway-systemd

Requires:       swaybg
# By default the Fedora background is used
Recommends:     desktop-backgrounds-compat

# Lack of graphical drivers may hurt the common use case
Recommends:     mesa-dri-drivers
# Minimal installation doesn't include Qt Wayland backend
Recommends:     (qt5-qtwayland if qt5-qtbase-gui)
Recommends:     (qt6-qtwayland if qt6-qtbase-gui)

# dmenu (as well as rxvt any many others) requires XWayland on Sway
Requires:       xorg-x11-server-Xwayland
# Sway binds the terminal shortcut to one specific terminal. In our case alacritty
Recommends:     alacritty
# grim is the recommended way to take screenshots on sway 1.0+
Recommends:     grim

%description
Sway is a tiling window manager supporting Wayland compositor protocol and
i3-compatible configuration.

%package -n     grimshot
Summary:        Helper for screenshots within sway
Requires:       grim
Requires:       jq
Requires:       slurp
Requires:       /usr/bin/wl-copy
Recommends:     /usr/bin/notify-send

%description -n grimshot
Grimshot is an easy to use screenshot tool for sway. It relies on grim,
slurp and jq to do the heavy lifting, and mostly provides an easy to use
interface.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install
# Set Fedora background as default background
sed -i "s|^output \* bg .*|output * bg /usr/share/backgrounds/default.png fill|" %{buildroot}%{_sysconfdir}/sway/config
# Create directory for extra config snippets
install -d -m755 -pv %{buildroot}%{_sysconfdir}/sway/config.d

# install contrib/grimshot tool
scdoc <contrib/grimshot.1.scd >%{buildroot}%{_mandir}/man1/grimshot.1
install -D -m755 -pv contrib/grimshot %{buildroot}%{_bindir}/grimshot

%files
%license LICENSE
%doc README.md
%dir %{_sysconfdir}/sway
%dir %{_sysconfdir}/sway/config.d
%config(noreplace) %{_sysconfdir}/sway/config
%{_mandir}/man1/sway*
%{_mandir}/man5/*
%{_mandir}/man7/*
%{_bindir}/sway
%{_bindir}/swaybar
%{_bindir}/swaymsg
%{_bindir}/swaynag
%{_datadir}/wayland-sessions/sway.desktop
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_sway*
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/sway*
%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d
%{_datadir}/fish/vendor_completions.d/sway*
%{_datadir}/backgrounds/sway

%files -n grimshot
%{_bindir}/grimshot
%{_mandir}/man1/grimshot.1*
