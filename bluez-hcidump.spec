%define name 	bluez-hcidump
%define version 2.4
%define release 1

Name: 		%{name}
Summary: 	Bluetooth HCI packet dump
Version: 	%{version}
Release: 	%{release}

Source0:	http://www.kernel.org/pub/linux/bluetooth/%{name}-%{version}.tar.gz
URL:		http://www.bluez.org
License:	GPL
Group:		Communications
BuildRequires:	bluez-devel >= 2.23

%description
Bluetooth HCI packet dump.
 
%prep
%setup -q

%build
export CFLAGS="%{optflags} -fPIC"
%configure2_5x
%make

%install
%makeinstall_std

%files
%doc README AUTHORS ChangeLog NEWS
%{_sbindir}/hcidump
%{_mandir}/*/*


%changelog
* Sat Apr 28 2012 Alexander Khrukin <akhrukin@mandriva.org> 2.4-1
+ Revision: 794250
- version update 2.4

* Fri Mar 09 2012 Götz Waschk <waschk@mandriva.org> 2.3-1
+ Revision: 783684
- update to new version 2.3

* Mon Jan 23 2012 Alexander Khrukin <akhrukin@mandriva.org> 2.2-1
+ Revision: 767393
- version update 2.2

* Tue Apr 26 2011 Funda Wang <fwang@mandriva.org> 2.0-1
+ Revision: 659082
- new version 2.0

* Tue Nov 30 2010 Oden Eriksson <oeriksson@mandriva.com> 1.42-5mdv2011.0
+ Revision: 603761
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 1.42-4mdv2010.1
+ Revision: 522228
- rebuilt for 2010.1

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 1.42-3mdv2010.0
+ Revision: 413177
- rebuild

* Fri Jan 30 2009 Guillaume Bedot <littletux@mandriva.org> 1.42-2mdv2009.1
+ Revision: 335468
- Rebuild for bluez 4

* Sun Jul 06 2008 Funda Wang <fwang@mandriva.org> 1.42-1mdv2009.0
+ Revision: 232198
- New version 1.42
- use -fPIC to solve x86_64 compile problem

* Mon Jun 16 2008 Thierry Vignaud <tv@mandriva.org> 1.41-2mdv2009.0
+ Revision: 220485
- rebuild

* Sun Feb 24 2008 Emmanuel Andry <eandry@mandriva.org> 1.41-1mdv2008.1
+ Revision: 174410
- New version

* Fri Jan 11 2008 Thierry Vignaud <tv@mandriva.org> 1.40-2mdv2008.1
+ Revision: 148985
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Mon Aug 27 2007 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.40-1mdv2008.0
+ Revision: 72118
- new release: 1.40

* Thu Aug 02 2007 Olivier Blin <blino@mandriva.org> 1.39-1mdv2008.0
+ Revision: 58069
- 1.39

