%define version 3.0.6

Name: fence-agents
Version: %{version}
Release: %mkrel 2
Summary: Fencing agents for cluster suite
Group: System/Kernel and hardware
URL: http://sources.redhat.com/cluster/wiki/
Source: ftp://sources.redhat.com/pub/cluster/releases/fence-agents-%{version}.tar.gz
Patch0: fence-agents-remove-nonexistent-subdirs.patch
License: GPLv2
Conflicts: cman < 3.0.0
BuildRequires: cluster-devel >= %{version} nss-devel libvirt-devel openais-devel
BuildRequires: corosync-devel
BuildRequires: python-pexpect
BuildRequires: xsltproc
BuildRoot: %{_tmppath}/%{name}-root

%description
This package contains fencing agents for use with the cman package from cluster
suite


%prep
%setup -q
%patch0 -p1

%build
./configure \
        --libdir=%{_libdir} \
        --mandir=%{_mandir} \
        --prefix=%{_prefix} \
        --sbindir=%{_sbindir} \
        --incdir=%{_includedir} \
        --without_kernel_modules \
        --disable_kernel_check \
        --nssincdir=%{_includedir}/nss \
        --nsprincdir=%{_includedir}/nspr4

%make -C fence

%install
rm -Rf %{buildroot}
%makeinstall_std -C fence

%clean
rm -Rf %{buildroot}

%files
%defattr(-,root,root)
%{_sbindir}/fence_*
%{_datadir}/fence
%{_mandir}/man8/fence_*.8.*
