Summary:	tfla-01 - a simple logic analyzer for the PC
Summary(pl):	tfla-01 - prosty analizatar stan�w logicznych dla PC
Name:		tfla-01
Version:	0.1.2
Release:	0.1
License:	GPL
Group:		Applications/Engineering
Source0:	http://download.berlios.de/tfla-01/%{name}-%{version}.tar.gz
# Source0-md5:	3f767d6258064cf7aec4375bd1406732
Source1:	%{name}.desktop
URL:		http://tfla-01.berlios.de/
BuildRequires:	libieee1284-devel
BuildRequires:	qmake
BuildRequires:	qt-devel >= 3.3.0
BuildRequires:	qt-linguist
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Simple logic analyzer for the PC's parallel port. The schematic which
needs to be attached on the parallel port is included in this
installation package.

%description -l pl
Prosty analizator stan�w logicznych dla portu r�wnoleg�ego PC. Schemat
urz�dzenia pod��czanego do portu r�wnoleg�ego znajduje si� razem z
programem.

%prep
%setup -q

%build
qmake
lrelease tfla-01.pro
%{__make} \
	QTDIR=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}
qmake PREFIX=$RPM_BUILD_ROOT%{_prefix}

%{__make} install \
	QTDIR=%{_prefix}
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}#
# FIXME: missing dir (move it to %doc or one level up)
#%{_docdir}/packages/tfla-01
%{_pixmapsdir}/*.png
%{_desktopdir}/*.desktop
