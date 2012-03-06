Name:		netxen-firmware
Summary:	QLogic Linux Intelligent Ethernet (3000 and 3100 Series) Adapter Firmware
Version:	4.0.534
Release:	3.1%{?dist}
License:	Redistributable, no modification permitted
Group:		System Environment/Kernel
Source0:	ftp://ftp.qlogic.com/outgoing/linux/firmware/netxen_nic/phanfw.bin
Source1:	ftp://ftp.qlogic.com/outgoing/linux/firmware/netxen_nic/LICENCE.phanfw
URL:		ftp://ftp.qlogic.com/outgoing/linux/firmware/netxen_nic/
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch
Requires:	udev

%description
QLogic Linux Intelligent Ethernet (3000 and 3100 Series) Adapter Firmware.

%prep
%setup -n %{name} -c -T
cp %{SOURCE0} .
cp %{SOURCE1} .

%build
# Firmware, do nothing.

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/lib/firmware/
install -m0644 phanfw.bin %{buildroot}/lib/firmware/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc LICENCE.phanfw
/lib/firmware/phanfw.bin

%changelog
* Wed Jan 12 2011 John W. Linville <linville@redhat.com> - 4.0.534-3
- Related: rhbz#647036
- Quell old-fashioned rpmlint warnings

* Thu Dec 23 2010 Tom Callaway <spot@fedoraproject.org> - 4.0.534-3
- new LICENCE.phanfw
- add Requires: udev

* Mon Dec 13 2010 Tom Callaway <spot@fedoraproject.org> - 4.0.534-2
- update urls

* Mon Dec  6 2010 Tom Callaway <spot@fedoraproject.org> - 4.0.534-1
- initial package
