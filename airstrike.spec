Summary:	Airstrike
Summary(pl):	Airstrike - Plastikowy Czerwony Baron
Name:		airstrike
Version:	pre6a
Release:	1
License:	GPL
Group:		Applications/Games
Source0:	http://icculus.org/airstrike/%{name}-%{version}-src.tar.gz
# Source0-md5:	af7367f9223309fbcf9759e04028394e
Patch0:		%{name}-pld.patch
URL:		http://icculus.org/airstrike/
BuildRequires:	SDL-devel => 1.2
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_image-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Airstrike is a 2d dogfight game in the tradition of the Intellivision
and Amiga games 'Biplanes' and 'BIP'. It features a robust physics
engine and several other extensions of the original games. It is
currently 0-2 player only, but will hopefully have network play and
some more advanced computer controlled enemies in the future. The
graphics have been created using the Povray raytracer, and should be
easy to extend and modify. Airstrike is being developed using GNU
tools and the excellent SDL library, and has been ported from the
original Linux version to both Windows and Mac OSX. The game is
released under the GPL.

%description -l pl
Airstrike jest dwuwymiarow± gr± polegaj±c± na wzajemnym ostrzeliwaniu
siê z plastikowych samolocików. A wszystko z ³adnie wykonan± za pomoc±
PovRaya grafik±.

%prep
%setup -q -n %{name}-%{version}-src
%patch0 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/games/airstrike,%{_mandir}/man6,%{_bindir}}
cp -rf  data $RPM_BUILD_ROOT%{_datadir}/games/airstrike
install doc/airstrike.6 $RPM_BUILD_ROOT%{_mandir}/man6
install airstrike $RPM_BUILD_ROOT%{_bindir}
install airstrikerc $RPM_BUILD_ROOT%{_datadir}/games/airstrike

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man6/*
%{_datadir}/games/airstrike/*
