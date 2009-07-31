%define name    listen
%define version 0.6.3
%define rel     1
%define release %mkrel %rel

Name:       %name
Version:    %version
Release:    %release
Summary:    A music manager and player for GNOME
License:    GPLv2
Group:      Sound
URL:        http://www.listen-project.org/
Source:     http://download.listen-project.org/lastest/%name-%{version}.tar.gz
BuildRequires: python-devel
BuildRequires: python-sqlite2
BuildRequires: python-daap
BuildRequires: python-musicbrainz2
BuildRequires: python-tunepimp
BuildRequires: pyvorbis
BuildRequires: pyogg
BuildRequires: pymad
BuildRequires: pygtk2.0-devel
BuildRequires: gnome-python-extras
BuildRequires: python-webkitgtk
BuildRequires: dbus-python
BuildRequires: libgpod-devel
BuildRequires: gtk2-devel
BuildRequires: gstreamer0.10-python-devel
BuildRequires: intltool
BuildRequires: mutagen
BuildRequires: desktop-file-utils
BuildRequires: imagemagick
Requires:   python
Requires:   python-sqlite2
Requires:   python-daap
Requires:   python-musicbrainz2
requires:   python-tunepimp
Requires:   pyvorbis
Requires:   pyogg
Requires:   pymad
Requires:   gnome-python-gnomevfs
Requires:   gnome-python-extras
Requires:   gnome-python
Requires:   gnome-python-gtkhtml2
Requires:   gstreamer
Requires:   gstreamer0.10-python 
Requires:   gstreamer0.10-plugins-ugly
Requires:   gstreamer0.10-plugins-good
Requires:   gstreamer0.10-plugins-base
Requires:   mutagen
Requires:   python-webkitgtk
BuildRoot: %{_tmppath}/%{name}-%{version}

%description
Listen is a music manager and player for GNOME

With listen you can:
* Play your favorite songs
* Manage your library
* Manage your ipod
* Make playlists
* Automatically or manually download album covers
* Automatically synchronize album covers with iPod
* Easily burn an audio CD
* Directly get informations from wikipedia when you play a song
* See the lyrics of a song
* Have statistics about your favorite songs, albums or artists
* Listen to web radio
* Submit your songs to Audioscrobbler
* Quick access to last.fm related file

With listen you will be able to:
 * Listen And Rip Audio CDs
 * Browse and listen songs on a DAAP share
 * Share you library via a DAAP share
 * Fill metadata with musicbrainz
 * Make inteligent playlists

%prep
%setup -q 

for i in $( find src -name '*.py' ); do
     perl -pi -e 'print "# -*- coding: utf-8 -*-\n"  if $. == 1 ;' $i
done;

%build
make

%install
rm -rf %buildroot %name.lang
make install PREFIX=%buildroot/%_prefix/
%find_lang %name

# menu
desktop-file-install --vendor="" \
    --remove-category="Application" \
    --add-category="GTK" \
    --add-category="X-MandrivaLinux-Multimedia-Sound" \
    --dir %{buildroot}%{_datadir}/applications \
    %{buildroot}%{_datadir}/applications/*

install -d -m 755  %{buildroot}{%{_miconsdir},%{_liconsdir},%{_iconsdir}}
convert -geometry 16x16 data/img/%{name}.png %{buildroot}%{_miconsdir}/%{name}.png
convert -geometry 32x32 data/img/%{name}.png %{buildroot}%{_iconsdir}/%{name}.png
convert -geometry 48x48 data/img/%{name}.png %{buildroot}%{_liconsdir}/%{name}.png

%clean
rm -rf %buildroot

%files -f %name.lang
%defattr(-,root,root)
%doc INSTALL gpl.txt README TODO
%{_prefix}/lib/%name/
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_liconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_mandir}/man1/%{name}.1*
%{_datadir}/dbus-1/services/org.gnome.Listen.service

%if %mdkversion < 200900
%post 
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif


