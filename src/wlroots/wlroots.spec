%global commit0 d9cae04ffc3140408f2604eeff7d4776fe8d9548
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global commitdate 20200321

# Version of the .so library
%global abi_ver 7

Name:           wlroots
Version:        0.13.0
Release:        0.1.%{commitdate}git%{shortcommit0}%{?dist}
Summary:        A modular Wayland compositor library

# Source files/overall project licensed as MIT, but
# - LGPLv2.1+
#   * protocol/idle.xml
#   * protocol/server-decoration.xml
# Those files are processed to C-compilable files by the
# `wayland-scanner` binary during build and don't alter
# the main license of the binaries linking with them by
# the underlying licenses.
License:        MIT
URL:            https://github.com/swaywm/%{name}
Source0:        %{url}/archive/%{commit0}.zip

# this file is a modification of examples/meson.build so as to:
# - make it self-contained
# - only has targets for examples known to compile well (cf. "examples) global)
Source3:        examples.meson.build

BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  meson >= 0.54.0
# FIXME: wlroots require `pkgconfig(egl)`, but assumes mesa provides it
# (and uses it's extension header `<EGL/eglmesaext.h>).
# Upstream is working on not needing that: https://github.com/swaywm/wlroots/issues/1899
# Until it is fixed, pull mesa-libEGL-devel manually
BuildRequires:  (mesa-libEGL-devel if libglvnd-devel < 1:1.3.2)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gbm) >= 17.1.0
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(libdrm) >= 2.4.95
BuildRequires:  pkgconfig(libinput) >= 1.9.0
BuildRequires:  pkgconfig(libsystemd) >= 237
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.17
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(wayland-server) >= 1.18
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xcb-renderutil)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xwayland)

# only select examples are supported for being readily compilable (see SOURCE3)
%global examples \
    cat multi-pointer output-layout pointer rotation screencopy simple tablet touch

%description
%{summary}.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} == %{version}-%{release}
# FIXME: See the rationale above for this require; remove when no longer needed
Requires:       (mesa-libEGL-devel if libglvnd-devel < 1:1.3.2)
# not required per se, so not picked up automatically by RPM
Recommends:     pkgconfig(xcb-icccm)
# for examples
Suggests:       gcc
Suggests:       meson >= 0.51.2
Suggests:       pkgconfig(libpng)

%description    devel
Development files for %{name}.


%prep
%autosetup -p1 -n %{name}-%{commit0}


%build
MESON_OPTIONS=(
    # Disable options requiring extra/unpackaged dependencies
    -Dexamples=false
    -Dxcb-errors=disabled
    -Dlibseat=disabled
    # select systemd logind provider
    -Dlogind-provider=systemd

%ifarch s390x
    # Disable -Werror on s390x: https://github.com/swaywm/wlroots/issues/2018
    -Dwerror=false
%endif
)

%{meson} "${MESON_OPTIONS[@]}"
%{meson_build}


%install
%{meson_install}

EXAMPLES=( %{examples} )  # Normalize whitespace by creating an array
for example in "${EXAMPLES[@]}"; do
    install -pm0644 -Dt '%{buildroot}/%{_pkgdocdir}/examples' examples/"${example}".[ch]
done
install -pm0644 -D '%{SOURCE3}' '%{buildroot}/%{_pkgdocdir}/examples/meson.build'


%check
%{meson_test}


%files
%license LICENSE
%doc README.md
%doc %dir %{_pkgdocdir}
%{_libdir}/lib%{name}.so.%{abi_ver}*


%files  devel
%doc %{_pkgdocdir}/examples
%{_includedir}/wlr
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
