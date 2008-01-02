%define name 	pam_abl
%define version 0.2.3
%define release %mkrel 1

Summary:	Auto blacklisting of hosts and users
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License:	GPL
Group:		System/Libraries
URL: 		http://www.hexten.net/pam_abl/
BuildRequires:	pam-devel
Source0: 	http://www.padl.com/download/%{name}-%{version}.tar.bz2
Patch0:		pam_abl-destdir.patch.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-buildroot

%description
A PAM module that provides auto blacklisting of hosts and users
responsible for repeated failed authentication attempts. Generally
configured so that blacklisted users still see normal login prompts
but are guaranteed to fail to authenticate.

%prep
%setup -q -n %{name}
%patch0 -p1 -b .destdir
%build
%make

%install
rm -rf $RPM_BUILD_ROOT
install -d -m755 $RPM_BUILD_ROOT%{_bindir} $RPM_BUILD_ROOT/%{_lib}/security
%makeinstall_std PAMDIR=$RPM_BUILD_ROOT/%{_lib}/security

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS NEWS README THANKS doc/index.html doc/pam_abl.html doc/style.css
/%{_lib}/security/*so*
%{_bindir}/%{name}

