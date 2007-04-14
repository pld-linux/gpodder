Summary:	A podcast  receiver/catcher written in PyGTK
Summary(pl):	Czytnik podcastów napisany w PyGTK
Name:		gpodder
Version:	0.9.1
Release:	0.1
License:	GPL v2+
Group:		Applications/Communications
Source0:	http://download.berlios.de/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	c600885be7b5212ed2c02f45a842ece2
URL:		http://gpodder.berlios.de/
BuildRequires:	ImageMagick
BuildRequires:	gettext-devel
BuildRequires:	help2man
BuildRequires:	intltool
BuildRequires:	python-devel
BuildRequires:	python-pygtk-devel
BuildRequires:	rpmbuild(macros) >= 1.177
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python
%pyrequires_eq	python-PyXML
%pyrequires_eq	python-eyeD3
%pyrequires_eq	python-mad
%pyrequires_eq	python-modules
%pyrequires_eq	python-pygtk-glade
Requires:	lame
Requires:	mplayer
Requires:	vorbis-tools
Requires:	wget
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GPodder is a podcast reveiver/catcher written in Python and using
PyGTK for GUI.

%description -l pl.UTF-8
GPodder jest czytnikiem podcastów napisanym w języku Python
i używającym PyGTK do obsługi interfejsu graficznego.

%prep
%setup -q

%build
%{__make} clean
%{__make} generators \
	CC="%{__cc}" \
	PREFIX=%{_prefix}
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	PREFIX=%{_prefix} \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_post

%postun
%update_desktop_database_postun

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README ChangeLog TODO
%attr(755,root,root) %{_bindir}/*
%{py_sitescriptdir}/%{name}
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
%{_iconsdir}/*/*/*/%{name}.*
%{_mandir}/man1/*
%{_pixmapsdir}/*.png