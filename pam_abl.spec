%define oname pam-abl

Summary:	Auto blacklisting of hosts and users
Name:		pam_abl
Version:	0.6.0
Release:	2
License:	GPLv2+
Group:		System/Libraries
Url:		http://sourceforge.net/projects/pam-abl/
Source0:	http://downloads.sourceforge.net/project/%{oname}/%{oname}/%{oname}-%{version}.tar.gz
Patch0:		pam_abl-0.6.0-whitelistroot.patch
BuildRequires:	cmake
BuildRequires:	db-devel
BuildRequires:	pam-devel

%description
A PAM module that provides auto blacklisting of hosts and users responsible
for repeated failed authentication attempts. Generally configured so that
blacklisted users still see normal login prompts but are guaranteed to fail
to authenticate.

%files
%doc README
/%{_lib}/security/*so*
%{_bindir}/%{name}
%config(noreplace) %{_sysconfdir}/security/pam_abl.conf
%dir %{_var}/lib/abl

#----------------------------------------------------------------------------

%prep
%setup -q -c
%patch0 -p1

%build
%cmake
%make

%install
%makeinstall_std -C build
install -d %{buildroot}/%{_lib}
mv %{buildroot}%{_prefix}/lib/security %{buildroot}/%{_lib}
install -d %{buildroot}%{_var}/lib/abl
install -D -m 644 conf/pam_abl.conf %{buildroot}%{_sysconfdir}/security/pam_abl.conf

