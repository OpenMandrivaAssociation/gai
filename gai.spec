%define version 0.5.10
%define release %mkrel 7
%define name gai
%define lib_major 0
%define lib_name %mklibname %name %{lib_major}

Name:		%{name}
Version:	%{version}
Summary:    General Applet Interface Library
Release:	%{release}
License:	LGPL
Group:      Graphical desktop/Other
Url:		http://gai.sf.net
Source0:	http://prdownloads.sourceforge.net/gai/%{name}-%{version}.tar.bz2
Patch:		gai-0.5.10-X.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
Requires: 	gai-album, gai-bgswitcher, gai-blobs, gai-leds
Requires: 	gai-mailcounter, gai-pal, gai-visual-audio, gai-sun
BuildRequires:	libgnomeui2-devel >= 2.0
BuildRequires:	libglade2.0-devel >= 2.0
BuildRequires:	libgtkglext-devel
BuildRequires:  libpanel-applet-devel
BuildRequires:  rox
BuildRequires:  SDL-devel

%description
A collection of applets for panels, including the GNOME one.

%package -n %{lib_name}
Summary:    General Applet Interface Library
Group:      System/Libraries
Provides:   %{lib_name} = %{version}-%{release}
Provides:   lib%{name} = %{version}-%{release}

%description -n %{lib_name}
This library is intended to simplify the development and use of
dockapps and gnome panel applets. With this library the programmer
can focus on what the applet shall do, not on the interface.

%package -n %{lib_name}-devel
Summary:        Development files for gai
Group:          Development/C
Provides:       %{lib_name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Requires:       %{lib_name} = %{version}
Requires:  	libpanel-applet-devel


%description -n %{lib_name}-devel
This library is intended to simplify the development and use of
dockapps and gnome panel applets.
This package allows you to develop applications using gai.

%prep
%setup -q
%patch -p 1
autoconf
%build
export CFLAGS="%optflags -fPIC"
%configure2_5x
%make 

%install
rm -rf $RPM_BUILD_ROOT %name.lang
%makeinstall_std LOCALE_PREFIX=%buildroot%_datadir/locale
%find_lang %name
%if %mdkversion < 200900
%post -n %{lib_name} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{lib_name} -p /sbin/ldconfig
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %name.lang
%defattr(-,root,root,0755)
%doc AUTHORS BUGS ChangeLog README* THANKS TODO WINDOWMANAGERS 

%files -n %{lib_name}
%defattr(-,root,root,0755)
%{_libdir}/lib%{name}.so.*

%files -n %{lib_name}-devel
%defattr(-,root,root,0755)
%doc docs/*
%{_libdir}/pkgconfig/*
%{_libdir}/lib%{name}.so
%{_includedir}/*


