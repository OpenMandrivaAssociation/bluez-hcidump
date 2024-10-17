%define name 	bluez-hcidump
%define version 2.5
%define release 11

Name: 		%{name}
Summary: 	Bluetooth HCI packet dump
Version: 	2.5
Release: 	1%{release}

Source0:	http://www.kernel.org/pub/linux/bluetooth/%{name}-%{version}.tar.gz
URL:		https://www.bluez.org
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
