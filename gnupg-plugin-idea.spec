Summary:	Additional module for GPG containing the IDEA cipher
Summary(pl):	Dodatkowy modu³ do GPG zawieraj±cy obs³ugê algorytmu IDEA
Name:		gnupg-plugin-idea
# gnupgext_version in idea.c
Version:	1.11
Release:	3
License:	BSD-like
Group:		Applications/File
Source0:	http://www.gnupg.dk/contrib-dk/idea.c.gz
# Source0-md5:	9dc3bc086824a8c7a331f35e09a3e57f
URL:		http://www.gnupg.org/
Requires:	gnupg
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	gnupg-i

%description
Additional module for GNU Privacy Guard containing the IDEA cipher.

%description -l pl
Dodatkowy modu³ do GNU Privacy Guard zawieraj±cy obs³ugê algorytmu
IDEA.

%prep
%setup -q -c -T
cp -f %{SOURCE0} .
gzip -d idea.c.gz

%build
%{__cc} -Wall %{rpmcflags} %{rpmldflags} -shared -fPIC -o idea idea.c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/gnupg

install idea $RPM_BUILD_ROOT%{_libdir}/gnupg

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gnupg/*
