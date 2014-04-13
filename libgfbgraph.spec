Summary:	GObject library for Facebook Graph API
Name:		libgfbgraph
Version:	0.2.2
Release:	1
License:	GPL v3
Group:		Libraries
Source0:	https://download.gnome.org/sources/gfbgraph/0.2/gfbgraph-%{version}.tar.xz
# Source0-md5:	af796932cec99e6da8e21174caf28ee3
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gnome-online-accounts-devel
BuildRequires:	libsoup-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%package devel
Summary:	Header files for gfbgraph library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This is the package containing the header files for gfbgraph library.

%package apidocs
Summary:	API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
gfbgraph API documentation.

%prep
%setup -qn gfbgraph-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules	\
	--disable-static	\
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_prefix}/doc
%{__rm} -r $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %ghost %{_libdir}/libgfbgraph-*.so.0
%attr(755,root,root) %{_libdir}/libgfbgraph-*.so.*.*.*
%{_libdir}/girepository-1.0/GFBGraph-*.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgfbgraph-*.so
%{_includedir}/gfbgraph-*
%{_datadir}/gir-1.0/GFBGraph-*.gir
%{_pkgconfigdir}/libgfbgraph-0.2.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/gfbgraph

