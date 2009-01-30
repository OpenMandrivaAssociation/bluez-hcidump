%define name 	bluez-hcidump
%define version 1.42
%define release %mkrel 2

Name: 		%{name}
Summary: 	Bluetooth HCI packet dump
Version: 	%{version}
Release: 	%{release}

Source0:	http://bluez.sourceforge.net/download/%{name}-%{version}.tar.gz
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
export CFLAGS="%{optflags} -fPIC"
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -fr %{buildroot}

%files
%defattr(-,root,root)
%doc README AUTHORS ChangeLog NEWS
%{_sbindir}/hcidump
%{_mandir}/*/*
