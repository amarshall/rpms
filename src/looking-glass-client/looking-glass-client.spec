%define reponame LookingGlass

Name:           looking-glass-client
Version:        B1
Release:        1%{?dist}
Summary:        Allows sharing video-out from Kernel-based Virtual Machine with GPU passthrough

License:        GPLv2.0
URL:            https://looking-glass.hostfission.com
Source0:        https://github.com/gnif/%{reponame}/archive/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz

BuildRequires:  binutils-devel
BuildRequires:  cmake
BuildRequires:  egl-wayland-devel
BuildRequires:  fontconfig-devel
BuildRequires:  gcc
BuildRequires:  libX11-devel
BuildRequires:  libXfixes-devel
BuildRequires:  libXi-devel
BuildRequires:  make
BuildRequires:  mesa-libEGL-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libGLES-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  nettle-devel
BuildRequires:  SDL2-devel
BuildRequires:  SDL2_ttf-devel
BuildRequires:  spice-protocol
BuildRequires:  wayland-devel


%description
Allows the use of a KVM (Kernel-based Virtual Machine) configured for VGA PCI
Pass-through without an attached physical monitor


%prep
%autosetup -n %{reponame}-%{version}


%build
cd client
%cmake . -DENABLE_BACKTRACE=0
%make_build


%install
cd client
%make_install

%files
%license LICENSE
%doc README.md
%{_bindir}/looking-glass-client
