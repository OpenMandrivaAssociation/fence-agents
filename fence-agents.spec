%define version 3.0.17

Name: fence-agents
Version: %{version}
Release: %mkrel 5
Summary: Fencing agents for cluster suite
Group: System/Kernel and hardware
URL: http://sources.redhat.com/cluster/wiki/
Source: https://fedorahosted.org/releases/c/l/cluster/fence-agents-%{version}.tar.gz
Patch0: fence-agents-remove-nonexistent-subdirs.patch
License: GPLv2
Conflicts: cman < 3.0.0
BuildRequires: cluster-devel >= %{version} nss-devel libvirt-devel openais-devel
BuildRequires: corosync-devel
BuildRequires: python-pexpect
BuildRequires: python-curl
BuildRequires: xsltproc
BuildRequires:	ccs-devel
BuildRequires:	pkgconfig(liblogthread) cman-devel
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
%config(noreplace) %{_sysconfdir}/cluster/fence_na.conf


%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 3.0.17-2mdv2011.0
+ Revision: 664299
- mass rebuild

* Wed Oct 13 2010 Buchan Milne <bgmilne@mandriva.org> 3.0.17-1mdv2011.0
+ Revision: 585515
- buildrequire python-curl
- update to new version 3.0.17

* Tue Sep 07 2010 Buchan Milne <bgmilne@mandriva.org> 3.0.16-1mdv2011.0
+ Revision: 576608
- update to new version 3.0.16
- Add fence_na.conf to files list

* Tue May 04 2010 Buchan Milne <bgmilne@mandriva.org> 3.0.11-1mdv2010.1
+ Revision: 542052
- New version 3.0.11

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuilt against nss-3.12.6

* Mon Jan 04 2010 Buchan Milne <bgmilne@mandriva.org> 3.0.6-1mdv2010.1
+ Revision: 486172
- update to new version 3.0.6
- update to new version 3.0.5
- buildrequire xsltproc
-buildrequire python-pexpect
- update to new version 3.0.4

* Wed Oct 14 2009 Buchan Milne <bgmilne@mandriva.org> 3.0.3-1mdv2010.0
+ Revision: 457374
- Buildrequire openais-devel and corosync-devel
- New version 3.0.3
- buildrequire the same version of cluster-devel
- import fence-agents


