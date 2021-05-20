%global debug_package %{nil}

Name: scream
Version: 3.6
Release: 1%{?dist}
Summary: Scream audio receiver using Pulseaudio, ALSA, or stdout as audio output

License: MS-PL
URL: https://github.com/duncanthrax/scream/tree/master/Receivers/unix
Source0: https://github.com/duncanthrax/scream/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: alsa-lib-devel
BuildRequires: cmake
BuildRequires: gcc
BuildRequires: make
BuildRequires: pulseaudio-libs-devel

%description
Scream audio receiver using Pulseaudio, ALSA, or stdout as audio output.

%prep
%autosetup

%build
cd Receivers/unix
mkdir build
cd build
cmake ..
make

%install
mkdir -p %{buildroot}/%{_bindir}
install -p -m 0755 Receivers/unix/build/%{name} %{buildroot}/%{_bindir}/

%files
%{_bindir}/scream
