%define plugin	epgsync

Summary:	VDR plugin: Import EPG of an other VDR
Name:		vdr-plugin-%plugin
Version:	0.0.4
Release:	3
Group:		Video
License:	GPL
URL:		https://vdr.schmirler.de/
Source:		http://vdr.schmirler.de/epgsync/vdr-%plugin-%{version}.tgz
BuildRequires:	vdr-devel >= 1.6.0
BuildRequires:	svdrpservice-devel
Requires:	vdr-abi = %vdr_abi
Requires:	vdr-plugin-svdrpservice

%description
With this plugin you can import the EPG of a remote VDR. It can
either use SVDRP or streamdev's VTP to download the EPG.

%prep
%setup -q -n %plugin-%{version}
%vdr_plugin_prep

perl -pi -e 's,"../svdrpservice/svdrpservice.h",<vdr/svdrpservice/svdrpservice.h>,' thread.h

%build
%vdr_plugin_build

%install
%vdr_plugin_install

%files -f %plugin.vdr
%doc README HISTORY


