Name:		powertabeditor
Version:	2.0.21	
Release:	2
Source0:	https://github.com/powertab/powertabeditor/archive/%{version}/%{name}-%{version}.tar.gz
Summary:  	Guitar tablature viewer and editor
URL:		https://github.com/powertabeditor/powertabeditor
License:	GPL-3.0
Group:		Utilites	
BuildRequires:  pkgconfig(alsa)
BuildRequires:	cmake
BuildRequires:  doctest-devel
BuildRequires:  %{_lib}boost-devel
BuildRequires:  pkgconfig(minizip)
BuildRequires:  pkgconfig(nlohmann_json)
BuildRequires:  pkgconfig(pugixml)
BuildRequires:	pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6QmlIntegration)
BuildRequires:	pkgconfig(Qt6PrintSupport)	
BuildRequires:  pkgconfig(Qt6Linguist)
BuildRequires:  pkgconfig(rtmidi)
BuildRequires:  %{_lib}unwind-devel
BuildSystem:	cmake
Suggests:       TiMidity++

%description
A powerful cross platform guitar tablature viewer and editor inspired by the no
longer developed Power Tab Editor. This poject is open-source and written from
scratch so that your favorite tabbing platform can continuously grow with your
needs.

%prep
%autosetup -p1

%files
%doc		README.md
%license	COPYING
%{_bindir}/powertabeditor
%{_datadir}/applications/powertabeditor.desktop
%{_datadir}/icons/hicolor/128x128/apps/powertabeditor.png
%{_datadir}/metainfo/powertabeditor.metainfo.xml
%{_datadir}/mime/packages/powertabeditor.xml
%{_datadir}/powertab/powertabeditor/translations/powertabeditor*.qm
%{_datadir}/powertab/powertabeditor/tunings.json


