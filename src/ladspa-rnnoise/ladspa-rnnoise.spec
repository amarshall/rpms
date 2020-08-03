%define commit 34003bd9ab1509708eab61ef458feaae23327495
%define __cmake_in_source_build 1

Name:      ladspa-rnnoise
Version:   0.9.git.1.%{commit}
Release:   1%{?dist}
Summary:   RNNoise LADSPA plugin
License:   GPLv3+
URL:       https://github.com/werman/noise-suppression-for-voice
Source0:   https://github.com/werman/noise-suppression-for-voice/archive/%{commit}.tar.gz

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: ladspa-devel
BuildRequires: make

Requires: ladspa

%description
A real-time noise suppression plugin for voice based on Xiph’s RNNoise.


%prep
%autosetup -n noise-suppression-for-voice-%{commit}

# Replace bundled header with packaged header
%{__rm} ./src/ladspa_plugin/ladspa.h
ln -s /usr/include/ladspa.h ./src/ladspa_plugin/ladspa.h


%build
%cmake -DBUILD_LV2_PLUGIN=OFF -DBUILD_VST_PLUGIN=OFF .
%make_build


%install
%make_install


%files
%doc README.md
%license LICENSE
%{_libdir}/ladspa/*.so
