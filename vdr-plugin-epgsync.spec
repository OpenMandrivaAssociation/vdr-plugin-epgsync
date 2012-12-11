
%define plugin	epgsync
%define name	vdr-plugin-%plugin
%define version	0.0.4
%define rel	1

Summary:	VDR plugin: Import EPG of an other VDR
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://vdr.schmirler.de/
Source:		http://vdr.schmirler.de/epgsync/vdr-%plugin-%version.tgz
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


%changelog
* Tue Aug 17 2010 Anssi Hannula <anssi@mandriva.org> 0.0.4-1mdv2011.0
+ Revision: 570693
- new version

* Tue Jul 28 2009 Anssi Hannula <anssi@mandriva.org> 0.0.3-2mdv2011.0
+ Revision: 401088
- rebuild for new VDR

* Wed Jul 15 2009 Anssi Hannula <anssi@mandriva.org> 0.0.3-1mdv2010.0
+ Revision: 396137
- new version
- drop vdr 1.6 i18n patch, fixed upstream

* Fri Mar 20 2009 Anssi Hannula <anssi@mandriva.org> 0.0.2-9mdv2009.1
+ Revision: 359313
- rebuild for new vdr

* Mon Apr 28 2008 Anssi Hannula <anssi@mandriva.org> 0.0.2-8mdv2009.0
+ Revision: 197925
- rebuild for new vdr

* Sat Apr 26 2008 Anssi Hannula <anssi@mandriva.org> 0.0.2-7mdv2009.0
+ Revision: 197660
- add vdr_plugin_prep
- bump buildrequires on vdr-devel
- adapt to gettext i18n of VDR 1.6 (semi-automatic patch)

* Fri Jan 04 2008 Anssi Hannula <anssi@mandriva.org> 0.0.2-6mdv2008.1
+ Revision: 145087
- rebuild for new vdr

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 29 2007 Anssi Hannula <anssi@mandriva.org> 0.0.2-5mdv2008.1
+ Revision: 103090
- rebuild for new vdr

* Sun Jul 08 2007 Anssi Hannula <anssi@mandriva.org> 0.0.2-4mdv2008.0
+ Revision: 49996
- rebuild for new vdr
- rebuild for new vdr

* Sat May 05 2007 Anssi Hannula <anssi@mandriva.org> 0.0.2-2mdv2008.0
+ Revision: 22750
- rebuild for new vdr

* Tue May 01 2007 Anssi Hannula <anssi@mandriva.org> 0.0.2-1mdv2008.0
+ Revision: 19910
- Import vdr-plugin-epgsync

