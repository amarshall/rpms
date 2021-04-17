Name:      squashfs-tools-ng
Version:   1.1.0
Release:   1%{?dist}
Summary:   A new set of tools and libraries for working with SquashFS images
License:   GPL
URL:       https://infraroot.at/projects/squashfs-tools-ng
Source0:   https://infraroot.at/pub/squashfs/%{name}-%{version}.tar.gz

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: gcc
BuildRequires: libselinux-devel
BuildRequires: libtool
BuildRequires: libzstd-devel
BuildRequires: lzo-devel
BuildRequires: make
BuildRequires: xz-devel
BuildRequires: zlib-devel
Requires: libselinux
Requires: libzstd
Requires: lz4
Requires: lzo
Requires: xz
Requires: zlib

%description
A new set of tools and libraries for working with SquashFS images

%package devel
Summary:   A new set of tools and libraries for working with SquashFS images (development files)
%description devel
A new set of tools and libraries for working with SquashFS images (development files)

%prep
%autosetup

%build
./autogen.sh
%configure
%make_build

%install
%make_install

%files
%license licenses/*
%doc README.md
%{_bindir}/gensquashfs
%{_bindir}/rdsquashfs
%{_bindir}/sqfs2tar
%{_bindir}/sqfsdiff
%{_bindir}/tar2sqfs
%{_libdir}/libsquashfs.a
%{_libdir}/libsquashfs.la
%{_libdir}/libsquashfs.so
%{_libdir}/libsquashfs.so.1
%{_libdir}/libsquashfs.so.1.1.1
%{_libdir}/pkgconfig/libsquashfs1.pc
%{_mandir}/man1/gensquashfs.1.gz
%{_mandir}/man1/rdsquashfs.1.gz
%{_mandir}/man1/sqfs2tar.1.gz
%{_mandir}/man1/sqfsdiff.1.gz
%{_mandir}/man1/tar2sqfs.1.gz

%files devel
%{_includedir}/sqfs/block.h
%{_includedir}/sqfs/block_processor.h
%{_includedir}/sqfs/block_writer.h
%{_includedir}/sqfs/compressor.h
%{_includedir}/sqfs/data_reader.h
%{_includedir}/sqfs/dir.h
%{_includedir}/sqfs/dir_reader.h
%{_includedir}/sqfs/dir_writer.h
%{_includedir}/sqfs/error.h
%{_includedir}/sqfs/frag_table.h
%{_includedir}/sqfs/id_table.h
%{_includedir}/sqfs/inode.h
%{_includedir}/sqfs/io.h
%{_includedir}/sqfs/meta_reader.h
%{_includedir}/sqfs/meta_writer.h
%{_includedir}/sqfs/predef.h
%{_includedir}/sqfs/super.h
%{_includedir}/sqfs/table.h
%{_includedir}/sqfs/xattr.h
%{_includedir}/sqfs/xattr_reader.h
%{_includedir}/sqfs/xattr_writer.h
