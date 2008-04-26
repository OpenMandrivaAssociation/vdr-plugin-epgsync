
%define plugin	epgsync
%define name	vdr-plugin-%plugin
%define version	0.0.2
%define rel	7

Summary:	VDR plugin: Import EPG of an other VDR
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://vdr.schmirler.de/
Source:		http://vdr.schmirler.de/epgsync/vdr-%plugin-%version.tar.bz2
Patch0:		epgsync-0.0.2-i18n-1.6.patch
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.6.0
BuildRequires:	svdrpservice-devel
Requires:	vdr-abi = %vdr_abi
Requires:	vdr-plugin-svdrpservice

%description
With this plugin you can import the EPG of a remote VDR. It can
either use SVDRP or streamdev's VTP to download the EPG.

%prep
%setup -q -n %plugin-%version
%patch0 -p1
%vdr_plugin_prep

perl -pi -e 's,"../svdrpservice/svdrpservice.h",<vdr/svdrpservice/svdrpservice.h>,' thread.h

%build
%vdr_plugin_build

%install
rm -rf %{buildroot}
%vdr_plugin_install

%clean
rm -rf %{buildroot}

%post
%vdr_plugin_post %plugin

%postun
%vdr_plugin_postun %plugin

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY
