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
