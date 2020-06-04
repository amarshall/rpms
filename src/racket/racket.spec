Name:           racket
Version:        7.7
Release:        1%{?dist}
Summary:        General purpose programming language

License:        GPLv3 and LGPLv3 and MIT
URL:            https://racket-lang.org
Source0:        https://mirror.racket-lang.org/installers/%{version}/%{name}-%{version}-src.tgz

# Remove SRFI library and docs with restrictive licensing.
# See: https://github.com/racket/srfi/issues/4 (open)
# Note: Upstream maintainers have confirmed this
#       is safe, since the removed components are 
#       extra elements which nothing else in the
#       package depends on.
# Note: SRFI 5 was replaced with a FOSS implementation.  Only
#       nonfree docs need to be removed by this patch now.
Patch0:         remove-nonfree.patch

# Issue Building for armv7hl in koji
ExcludeArch: %{arm} s390x

# To compile the program
BuildRequires: gcc

# To fix rpath issue with executables.
BuildRequires: chrpath

# Racket heavily utilizes the system ffi library.
BuildRequires: libffi-devel

# For the racket/gui library (via libffi)
# https://github.com/racket/gui/blob/master/gui-lib/mred/private/wx/gtk/gtk3.rkt
BuildRequires: gtk3

# For the racket/draw library (via libffi)
# https://github.com/racket/draw/blob/master/draw-lib/racket/draw/unsafe/cairo-lib.rkt
BuildRequires: cairo
# https://github.com/racket/draw/blob/master/draw-lib/racket/draw/unsafe/pango.rkt
BuildRequires: pango
# https://github.com/racket/draw/blob/master/draw-lib/racket/draw/unsafe/png.rkt
BuildRequires: libpng
# https://github.com/racket/draw/blob/master/draw-lib/racket/draw/unsafe/jpeg.rkt
BuildRequires: libjpeg-turbo
# https://github.com/racket/draw/blob/master/draw-lib/racket/draw/unsafe/glib.rkt
BuildRequires: glib2

# To validate desktop file
BuildRequires: desktop-file-utils

BuildRequires: git

# Require the subpackages
Requires:       racket-minimal%{?_isa} = %{version}-%{release}
Requires:       racket-pkgs = %{version}-%{release}
Recommends:     racket-doc = %{version}-%{release}

%description
Racket is a general-purpose programming language as well as 
the world's first ecosystem for developing and deploying new 
languages. Make your dream language, or use one of the dozens 
already available.

%prep

%autosetup -v -p2

# Remove bundled libffi
rm -r src/foreign/libffi
rm -r share/pkgs/srfi-doc-nonfree

%build
cd src

# Disable SSE on i686 until fixed upstream
# https://github.com/racket/racket/issues/2245
%ifarch %{ix86}
  %set_build_flags
  export CFLAGS=$(echo $CFLAGS | sed -e "s/-mfpmath=sse *//")
%endif

# do not use generations on architectures
# where it is broken
#  (this is currently a no-op, since arm and s390x are not enabled yet.
#   It is art of a fix that will land in a future release)
%configure \
%ifarch %{arm} s390x
        --disable-generations \
%endif
        --enable-pthread \
        --enable-shared \
        --enable-libffi \
        --disable-strip

%make_build

%install
cd src
%make_install

# Delete mred binaries and replace them with links.
rm -vf ${RPM_BUILD_ROOT}%{_bindir}/mred
rm -vf ${RPM_BUILD_ROOT}%{_bindir}/mred-text
ln -vs %{_bindir}/gracket ${RPM_BUILD_ROOT}%{_bindir}/mred
ln -vs %{_bindir}/gracket-text ${RPM_BUILD_ROOT}%{_bindir}/mred-text

# Delete static library. Apperently --disable-libs does not stop it.
rm -vf ${RPM_BUILD_ROOT}%{_libdir}/libracket3m.a

# Delete duplicate license files
rm -rf %{buildroot}%{_datadir}/racket/COPYING*txt

# Fix the rpath error.
chrpath --delete ${RPM_BUILD_ROOT}%{_bindir}/racket
chrpath --delete ${RPM_BUILD_ROOT}%{_libdir}/racket/gracket

# Remove the libtool files.
rm -f ${RPM_BUILD_ROOT}%{_libdir}/*.la

# Fix paths in the desktop files.
sed -i "s#${RPM_BUILD_ROOT}##g" \
       ${RPM_BUILD_ROOT}/%{_datadir}/applications/*.desktop

# Validate desktop files
desktop-file-validate %{buildroot}/%{_datadir}/applications/*.desktop

# Fix paths in html docs
DOCS_TO_FIX="
syntax/module-helpers.html
rackunit/api.html
reference/collects.html"
for i in $DOCS_TO_FIX; do
  sed -i "s#${RPM_BUILD_ROOT}##g" \
         ${RPM_BUILD_ROOT}/%{_datadir}/doc/racket/$i
done

# Remove the executable bit on legacy template file 
chmod -x ${RPM_BUILD_ROOT}%{_libdir}/racket/starter-sh

%ldconfig_scriptlets

# Equivalent to upstream's minimal-racket release
%package        minimal
Summary:        A minimal Racket installation
Requires:       racket-collects = %{version}-%{release}
%description    minimal
Racket's core runtime

%package        collects
Summary:        Racket's core collections libraries
BuildArch:      noarch
%description    collects
Libraries providing Racket's core functionality

# Arch independent source and bytecode files
%package        pkgs
Summary:        Racket package collections
# See BuildRequires section for details on dependencies
Requires:       gtk3
Requires:       cairo
Requires:       pango
Requires:       libpng
Requires:       glib2
Requires:       libjpeg-turbo
Requires:       racket-minimal = %{version}-%{release}
BuildArch:      noarch
%description    pkgs
Additional packages and libraries for Racket

# Development headers and links
%package        devel
Summary:        Development files for Racket
Requires:       racket-minimal%{?_isa} = %{version}-%{release}
%description    devel
Files needed to link against Racket.

# HTML documentation
%package        doc
Summary:        Documentation files for Racket
BuildArch:      noarch
%description    doc
A local installation of the Racket documentation system.

%files
%license src/COPYING.txt src/COPYING_LESSER.txt src/COPYING-libscheme.txt
%{_bindir}/drracket
%{_bindir}/gracket
%{_bindir}/gracket-text
%{_bindir}/mred-text
%{_bindir}/mred
%{_bindir}/mzc
%{_bindir}/mzpp
%{_bindir}/mzscheme
%{_bindir}/mztext
%{_bindir}/pdf-slatex
%{_bindir}/plt-games
%{_bindir}/plt-help
%{_bindir}/plt-r5rs
%{_bindir}/plt-r6rs
%{_bindir}/plt-web-server
%{_bindir}/scribble
%{_bindir}/setup-plt
%{_bindir}/slatex
%{_bindir}/slideshow
%{_bindir}/swindle
%{_datadir}/applications/

%files collects
%license src/COPYING.txt src/COPYING_LESSER.txt src/COPYING-libscheme.txt
%{_datadir}/racket/collects

%files minimal
%license src/COPYING.txt src/COPYING_LESSER.txt src/COPYING-libscheme.txt
%{_bindir}/racket
%{_bindir}/raco
%{_libdir}/racket
%{_libdir}/libracket3m-%{version}.so
%{_datadir}/racket/links.rktd
%{_datadir}/racket/pkgs/racket-lib
%{_datadir}/man/man1/racket*
%{_datadir}/man/man1/raco*
%dir %{_datadir}/racket
%dir %{_datadir}/doc/racket
%dir %{_sysconfdir}/racket/
%config %{_sysconfdir}/racket/config.rktd
%exclude %{_libdir}/libracket3m.so

%files pkgs
%license src/COPYING.txt src/COPYING_LESSER.txt src/COPYING-libscheme.txt
%{_datadir}/racket
%{_datadir}/man/man1/drracket*
%{_datadir}/man/man1/gracket*
%{_datadir}/man/man1/mred*
%{_datadir}/man/man1/mzc*
%{_datadir}/man/man1/mzscheme*
%{_datadir}/man/man1/plt-help*
%{_datadir}/man/man1/setup-plt*
%exclude %{_datadir}/racket/links.rktd
%exclude %dir %{_datadir}/racket/pkgs/racket-lib
%exclude %dir %{_datadir}/racket/collects

%files devel
%license src/COPYING.txt src/COPYING_LESSER.txt src/COPYING-libscheme.txt
%{_includedir}/racket
%{_libdir}/libracket3m.so

%files doc
%license src/COPYING.txt src/COPYING_LESSER.txt src/COPYING-libscheme.txt
%{_datadir}/doc/racket
