Summary:	A podcast receiver/catcher written in PyGTK
Summary(pl.UTF-8):	Czytnik podcastów napisany w PyGTK
Name:		gpodder
Version:	3.9.1
Release:	0.10
License:	GPL v2+
Group:		X11/Applications/Multimedia
Source0:	http://gpodder.org/src/%{name}-%{version}.tar.gz
# Source0-md5:	f257c2e887808e53a21787d394623764
URL:		http://gpodder.org/
BuildRequires:	ImageMagick
BuildRequires:	ImageMagick-coder-png
BuildRequires:	gettext-tools
BuildRequires:	help2man
BuildRequires:	intltool
BuildRequires:	python-devel
BuildRequires:	python-pygtk-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.596
Requires:	desktop-file-utils
Requires:	gtk-update-icon-cache
Requires:	hicolor-icon-theme
Requires:	lame
Requires:	mplayer
Requires:	python
Requires:	python-PyXML
Requires:	python-eyeD3
Requires:	python-mad
Requires:	python-modules
Requires:	python-pygtk-glade
Requires:	vorbis-tools
Requires:	wget
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GPodder is a podcast reveiver/catcher written in Python and using
PyGTK for GUI.

%description -l pl.UTF-8
GPodder jest czytnikiem podcastów napisanym w języku Python i
używającym PyGTK do obsługi interfejsu graficznego.

%prep
%setup -q

%build
%{__make} messages

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/gpodder/unittests.py*
%{__rm} -r $RPM_BUILD_ROOT%{py_sitedir}/gpodder/test

%py_postclean

# unknown icon sizes
%{__rm} -r $RPM_BUILD_ROOT%{_iconsdir}/hicolor/{26x26,40x40}

# unsupported locales
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/cs_CZ
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/es_ES
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/fa_IR
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/ko_KR


%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database
%update_icon_cache hicolor

%postun
%update_desktop_database
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/gpo
%attr(755,root,root) %{_bindir}/gpodder
%attr(755,root,root) %{_bindir}/gpodder-migrate2tres
%{_mandir}/man1/gpo.1*
%{_mandir}/man1/gpodder-migrate2tres.1*
%{_mandir}/man1/gpodder.1*
%{py_sitedir}/%{name}
%{py_sitedir}/%{name}-%{version}-py*.egg-info
%{_datadir}/%{name}
%{_desktopdir}/gpodder-url-handler.desktop
%{_desktopdir}/gpodder.desktop
%{_iconsdir}/*/*/*/%{name}.*
%{_datadir}/dbus-1/services/org.gpodder.service
