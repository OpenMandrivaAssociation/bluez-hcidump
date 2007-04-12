%define name 	bluez-hcidump
%define version 1.34
%define release %mkrel 1

Name: 		%{name}
Summary: 	Bluetooth HCI packet dump
Version: 	%{version}
Release: 	%{release}

Source:		%{name}-%{version}.tar.bz2
URL:		http://bluez.sourceforge.net/
License:	GPL
Group:		Communications
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	bluez-devel >= 2.23

%description
Bluetooth HCI packet dump.
 
%prep
%setup -q

%build
%configure2_5x
%make CFLAGS="$RPM_OPT_FLAGS"
										
%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README AUTHORS ChangeLog NEWS
%{_sbindir}/hcidump
%{_mandir}/*/*



