Name:     v4l2loopback
Version:  0.12.5
Release:  1%{?dist}
Summary:  Tools to create Video4Linux loopback devices
Group:    System Environment/Kernel
License:  GPLv2
URL:      https://github.com/umlaeute/v4l2loopback
Source0:  https://github.com/umlaeute/v4l2loopback/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch: noarch

Requires: %{name}-kmod = %{version}
Requires: bash
Requires: gstreamer1
Requires: v4l-utils
Requires: which

BuildRequires:  help2man
BuildRequires:  make


%description
Allows creating “virtual video devices” which normal (v4l2) applications will read these devices as if they were ordinary video devices.


%package dkms
Summary:  Kernel module to create Video4Linux loopback devices
Requires: dkms >= 2.2
Provides: %{name}-kmod = %{version}


%description dkms
Allows creating “virtual video devices” which normal (v4l2) applications will read these devices as if they were ordinary video devices.


%post dkms
%{_prefix}/lib/dkms/common.postinst %{name} %{version}


%preun dkms
if [ $1 -ne 1 ]; then
  dkms remove -m %{name} -v %{version} --all --rpm_safe_upgrade || :
fi


%prep
%autosetup


%build
# v4l2loopback is a shell script


%install
if [ "$RPM_BUILD_ROOT" != "/" ]; then
  rm -rf $RPM_BUILD_ROOT
fi
mkdir -p "${RPM_BUILD_ROOT}%{_usrsrc}"
cp -r ../%{name}-%{version} "${RPM_BUILD_ROOT}%{_usrsrc}/"

make install-utils install-man DESTDIR="$RPM_BUILD_ROOT" PREFIX=%{_prefix} BINDIR=%{_bindir} MANDIR=%{_mandir}


%files
%doc AUTHORS NEWS README.md
%{_bindir}/%{name}*
%{_mandir}/man1/*.1*


%files dkms
%{_usrsrc}/%{name}-%{version}
